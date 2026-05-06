from __future__ import annotations

from typing import Any

from binddrift.config import Config
from binddrift.artifact_paths import repo_relative, sanitize_local_paths
from binddrift.db import connect, initialize
from binddrift.evaluation.wrapper_oracle import classify_fix_kinds, compatible_fix_kind, replay_head_date, version_dates_from_db, wrapper_fix_in_time_window
from binddrift.warnings import read_warnings, write_warnings


def _has_any(items: Any) -> bool:
    return bool(items) if isinstance(items, list) else False


def _has_evidence_chain(warning: dict[str, Any]) -> bool:
    rust_side = warning.get("rust_side", {})
    return bool(
        rust_side.get("uses")
        or rust_side.get("safe_apis")
        or rust_side.get("safety_comments")
        or rust_side.get("error_mappings")
        or rust_side.get("lifetime_facts")
        or rust_side.get("oracle_hits")
    )


def score_breakdown(
    warning: dict[str, Any],
    version_dates: dict[str, str] | None = None,
    head_date: str | None = None,
) -> dict[str, float]:
    rust_side = warning.get("rust_side", {})
    uses = rust_side.get("uses") or []
    safety_comments = rust_side.get("safety_comments") or []
    error_mappings = rust_side.get("error_mappings") or []
    lifetime_facts = rust_side.get("lifetime_facts") or []
    safe_apis = rust_side.get("safe_apis") or []
    oracle_hits = rust_side.get("oracle_hits") or []
    c_side = warning.get("c_side", {})
    old_value = c_side.get("old", c_side.get("old_indicators"))
    new_value = c_side.get("new", c_side.get("new_indicators"))
    promotion_reasons = set(warning.get("promotion_reasons") or [])
    evidence_chain = warning.get("evidence_chain") or []

    c_source_evidence = 1.0 if warning.get("c_evidence_level") in {"c_source_diff", "c_behavior_indicator", "build_oracle", "wrapper_fix"} else 0.0
    direct_use = 1.0 if _has_any(uses) or "direct_binding_use" in promotion_reasons else 0.0
    safe_api = 1.0 if _has_any(safe_apis) or "exposes_safe_api" in promotion_reasons else 0.0
    contract_mapping = 1.0 if _has_any(error_mappings) or _has_any(lifetime_facts) else 0.0
    safety_comment = 1.0 if _has_any(safety_comments) else 0.0
    build_oracle = 1.0 if any(hit.get("oracle_type") == "build_breakage" for hit in oracle_hits if isinstance(hit, dict)) else 0.0
    wrapper_oracle = 1.0 if _has_typed_wrapper_oracle(warning, version_dates, head_date) else 0.0
    multi_version_consistency = 1.0 if len(warning.get("observed_pairs") or []) > 1 else 0.0
    indicator_confidence = max(0.0, min(float(warning.get("confidence", 0.0)), 1.0)) if warning.get("indicator_based") else 0.0

    binding_only = 1.0 if warning.get("c_evidence_level") == "binding_only" else 0.0
    added_without_old = 1.0 if old_value == "absent" and new_value == "added" and not c_source_evidence else 0.0
    weak_name_match = 1.0 if _has_any(rust_side.get("weak_lifetime_facts") or []) and not (contract_mapping or safety_comment or build_oracle or wrapper_oracle) else 0.0
    no_evidence_chain = 1.0 if not evidence_chain and not (direct_use or safe_api or build_oracle or wrapper_oracle) else 0.0

    return {
        "direct_rust_use": 4.0 * direct_use,
        "safe_api_exposure": 4.0 * safe_api,
        "contract_mapping": 3.0 * contract_mapping,
        "safety_comment": 3.0 * safety_comment,
        "c_source_diff_strength": 3.0 * c_source_evidence,
        "build_oracle_hit": 5.0 * build_oracle,
        "wrapper_fix_hit": 4.0 * wrapper_oracle,
        "multi_version_consistency": 2.0 * multi_version_consistency,
        "indicator_confidence": round(indicator_confidence, 3),
        "binding_only_penalty": -5.0 * binding_only,
        "added_symbol_without_old_c_evidence_penalty": -3.0 * added_without_old,
        "weak_name_match_penalty": -3.0 * weak_name_match,
        "no_evidence_chain_penalty": -2.0 * no_evidence_chain,
    }


def score_warning(warning: dict[str, Any]) -> float:
    return round(sum(score_breakdown(warning).values()), 3)


def _has_typed_wrapper_oracle(
    warning: dict[str, Any],
    version_dates: dict[str, str] | None,
    head_date: str | None,
) -> bool:
    rust_side = warning.get("rust_side", {})
    oracle_hits = rust_side.get("oracle_hits") or []
    wrapper_hits = [hit for hit in oracle_hits if isinstance(hit, dict) and hit.get("oracle_type") == "wrapper_fix"]
    if not wrapper_hits:
        return False
    if version_dates is None:
        return True
    symbol = warning.get("c_side", {}).get("symbol")
    drift_type = str(warning.get("type") or "")
    if not symbol:
        return False
    for hit in wrapper_hits:
        changed_files = hit.get("changed_files") if isinstance(hit.get("changed_files"), list) else []
        fix_kinds = classify_fix_kinds(str(hit.get("subject") or ""), changed_files, [str(symbol)])
        if not any(compatible_fix_kind(drift_type, fix_kind) for fix_kind in fix_kinds):
            continue
        if wrapper_fix_in_time_window(hit.get("date"), warning, version_dates, head_date):
            return True
    return False


def _is_promoted(warning: dict[str, Any]) -> bool:
    if warning.get("promotion_status") != "promoted":
        return False
    if not _has_evidence_chain(warning):
        return False
    return True


def _warning_consistency_key(warning: dict[str, Any]) -> tuple[str, str] | None:
    symbol = warning.get("c_side", {}).get("symbol")
    drift_type = warning.get("type")
    if not symbol or not drift_type:
        return None
    return str(drift_type), str(symbol)


def _annotate_observed_pairs(warnings: list[dict[str, Any]]) -> None:
    pairs_by_key: dict[tuple[str, str], set[str]] = {}
    for warning in warnings:
        key = _warning_consistency_key(warning)
        pair_id = warning.get("pair_id")
        if key and pair_id:
            pairs_by_key.setdefault(key, set()).add(str(pair_id))
    for warning in warnings:
        key = _warning_consistency_key(warning)
        if not key:
            continue
        observed = sorted(pairs_by_key.get(key, set()))
        if len(observed) > 1:
            warning["observed_pairs"] = observed


def rank_warnings(cfg: Config) -> dict[str, Any]:
    input_warnings = read_warnings(cfg.warnings_jsonl)
    warnings = [warning for warning in input_warnings if _is_promoted(warning)]
    _annotate_observed_pairs(warnings)
    conn = connect(cfg.database)
    initialize(conn)
    version_dates = version_dates_from_db(conn)
    head_date = replay_head_date(warnings, version_dates)
    for warning in warnings:
        warning.setdefault("evidence_chain", [])
        breakdown = score_breakdown(warning, version_dates=version_dates, head_date=head_date)
        warning["score_breakdown"] = breakdown
        warning["score"] = round(sum(breakdown.values()), 3)
        rust_side = warning.get("rust_side", {})
        has_high_evidence = bool(
            rust_side.get("safe_apis")
            or rust_side.get("error_mappings")
            or rust_side.get("lifetime_facts")
            or rust_side.get("oracle_hits")
        )
        if warning.get("score", 0) >= 12 and has_high_evidence:
            warning["risk"] = "High"
        elif warning.get("score", 0) >= 8 and (rust_side.get("uses") or has_high_evidence):
            warning["risk"] = "Medium"
        else:
            warning["risk"] = "Low"
    warnings.sort(key=lambda item: item.get("score", 0), reverse=True)
    for idx, warning in enumerate(warnings, start=1):
        warning["rank"] = idx
    write_warnings(cfg, warnings)
    cfg.report_md.write_text(sanitize_local_paths(_markdown(warnings), cfg), encoding="utf-8")
    return {
        "warnings": len(warnings),
        "input_warnings": len(input_warnings),
        "dropped_unpromoted": len(input_warnings) - len(warnings),
        "warning_file": repo_relative(cfg, cfg.warnings_jsonl),
        "report": repo_relative(cfg, cfg.report_md),
    }


def _markdown(warnings: list[dict[str, Any]]) -> str:
    lines = ["# BindDrift Ranked Warnings", ""]
    if not warnings:
        lines.append("No warnings were generated for the current pilot inputs.")
        lines.append("")
        return "\n".join(lines)
    for warning in warnings:
        lines.extend(
            [
                f"## {warning['warning_id']} {warning.get('type', 'Warning')}",
                "",
                f"- Risk: {warning.get('risk', 'Unknown')}",
                f"- Score: {warning.get('score', 0)}",
                f"- Symbol: {warning.get('c_side', {}).get('symbol', 'unknown')}",
                f"- Explanation: {warning.get('explanation', '')}",
                f"- Suggested action: {warning.get('suggested_action', '')}",
                "",
                "### C Evidence",
                "",
                _format_c_side(warning),
                "",
                "### Score Breakdown",
                "",
                _format_score_breakdown(warning),
                "",
                "### Rust Evidence",
                "",
                _format_rust_side(warning),
                "",
            ]
        )
    return "\n".join(lines)


def _format_c_side(warning: dict[str, Any]) -> str:
    c_side = warning.get("c_side", {})
    evidence = c_side.get("evidence") or []
    lines = [
        f"- Old: `{c_side.get('old', c_side.get('old_indicators', 'n/a'))}`",
        f"- New: `{c_side.get('new', c_side.get('new_indicators', 'n/a'))}`",
    ]
    for item in evidence[:5]:
        if isinstance(item, dict):
            lines.append(f"- {item.get('evidence_file')}:{item.get('evidence_line')} `{item.get('evidence_text', '')}`")
    return "\n".join(lines)


def _format_rust_side(warning: dict[str, Any]) -> str:
    rust_side = warning.get("rust_side", {})
    uses = rust_side.get("uses") or []
    lines: list[str] = []
    for use in uses[:5]:
        if isinstance(use, dict):
            lines.append(
                f"- {use.get('rust_file')}:{use.get('line')} `{use.get('enclosing_function')}` "
                f"unsafe={use.get('enclosing_unsafe_block')}"
            )
    for item in (rust_side.get("safe_apis") or [])[:3]:
        if isinstance(item, dict):
            lines.append(f"- safe API `{item.get('api_name')}`")
    for item in (rust_side.get("safety_comments") or [])[:3]:
        if isinstance(item, dict):
            lines.append(f"- {item.get('rust_file')}:{item.get('line')} `{item.get('text', '')}`")
    for item in (rust_side.get("error_mappings") or [])[:3]:
        if isinstance(item, dict):
            lines.append(f"- {item.get('rust_file')}:{item.get('line')} `{item.get('mapping_type')}`")
    for item in (rust_side.get("lifetime_facts") or [])[:3]:
        if isinstance(item, dict):
            lines.append(f"- {item.get('rust_file')}:{item.get('line')} `{item.get('fact_type')}`")
    for item in (rust_side.get("weak_lifetime_facts") or [])[:3]:
        if isinstance(item, dict):
            lines.append(f"- weak lifetime name {item.get('rust_file')}:{item.get('line')} `{item.get('fact_type')}`")
    for item in (rust_side.get("oracle_hits") or [])[:3]:
        if isinstance(item, dict):
            lines.append(f"- {item.get('oracle_type')}: `{item.get('symbol', item.get('commit_id', 'oracle'))}`")
    return "\n".join(lines) if lines else "- No Rust exposure evidence recorded."


def _format_score_breakdown(warning: dict[str, Any]) -> str:
    breakdown = warning.get("score_breakdown") or {}
    if not breakdown:
        return "- No score breakdown recorded."
    return "\n".join(f"- {key}: `{value}`" for key, value in breakdown.items() if value)
