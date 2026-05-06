from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

from binddrift.artifact_paths import LOCAL_PATH_MARKERS, repo_relative, sanitize_local_paths
from binddrift.config import Config
from binddrift.db import connect, initialize
from binddrift.evaluation.metrics import TRUE_LABELS, label_for_warning, load_manual_labels, manual_review_row_key, warning_key
from binddrift.ranking.oracle_blind_scorer import generated_binding_only
from binddrift.run_manifest import canonical_run_dir, manifest_exists, validate_run_manifest
from binddrift.warnings import eligible_for_main_warning, read_warnings


POSITIVE_TARGET = 8
NEGATIVE_TARGET = 2
FALSE_POSITIVE_NEGATIVE_TARGET = 1
CASE_TARGET_TYPES = [
    "NullabilityDrift",
    "OwnershipRefcountDrift",
    "AllocationFreeDrift",
    "SleepabilityContextDrift",
    "LayoutFieldDrift",
]
CASE_TEMPLATE_HEADINGS = [
    "## Summary",
    "## Old Version Evidence",
    "## New Version Evidence",
    "## C-Side Diff",
    "## Rust-Side Dependency",
    "## Safe API / Contract Assumption",
    "## Manual Review Label",
    "## Why This Is Not Generated-Binding-Only",
    "## Why Compiler Alone Does Not Catch It",
    "## Alternative Explanation Considered",
    "## Maintainer Review Implication",
    "## Reproduction Pointers",
]


def generate_case_studies(cfg: Config, *, main_paper_mode: bool | None = None) -> dict[str, object]:
    manifest = validate_run_manifest(cfg) if manifest_exists(cfg) else None
    main_mode = bool(manifest) if main_paper_mode is None else main_paper_mode
    warning_source = _case_warning_source(cfg, manifest)
    warnings = read_warnings(warning_source)
    review_sources = _case_review_sources(cfg, warning_source, manifest)
    review_rows = _load_review_rows(review_sources)
    labels = {key: row.get("adjudicated_label", "") or row.get("label", "") for key, row in review_rows.items()}
    for key, label in (_load_adjudicated_labels(review_sources[-1]) if review_sources else {}).items():
        labels.setdefault(key, label)
    semantic_targets = _semantic_target_rows(cfg, warnings)
    candidates = semantic_targets or warnings
    candidates = [sanitize_local_paths(row, cfg) for row in candidates]

    positive_cases = _select_positive_cases(candidates, labels, review_rows)
    negative_cases = _select_negative_cases(candidates, labels, review_rows, positive_cases=positive_cases)
    if main_mode and len(positive_cases) < POSITIVE_TARGET:
        raise RuntimeError(f"Fewer than {POSITIVE_TARGET} adjudicated positive case studies available: {len(positive_cases)}")

    cases_dir = cfg.repo_root / "paper/cases"
    cases_dir.mkdir(parents=True, exist_ok=True)
    for stale in cases_dir.glob("case-*.md"):
        stale.unlink()

    created: list[str] = []
    for idx, warning in enumerate(positive_cases + negative_cases, start=1):
        label = label_for_warning(labels, warning)
        review = _review_for_warning(warning, review_rows)
        case_kind = "positive" if label in TRUE_LABELS else "negative"
        case_type = _case_drift_type(warning)
        symbol = _symbol(warning)
        path = cases_dir / f"case-{idx:02d}-{_slug(case_type)}-{_slug(symbol)}.md"
        text = _case_template(case_type, warning, label, review, case_kind=case_kind)
        path.write_text(text, encoding="utf-8")
        created.append(str(path))

    summary = _case_summary_table(positive_cases, negative_cases, labels, cfg)
    summary_path = cfg.repo_root / "paper/tables/case_study_summary.json"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    missing_path = cfg.repo_root / "paper/analysis/missing_case_types.md"
    missing_path.parent.mkdir(parents=True, exist_ok=True)
    missing_path.write_text(_missing_case_types(summary), encoding="utf-8")
    return {
        "cases": len(positive_cases),
        "positive_cases": len(positive_cases),
        "negative_cases": len(negative_cases),
        "files": created,
        "warning_source": repo_relative(cfg, warning_source),
        "manual_review": repo_relative(cfg, review_sources[-1]) if review_sources else "",
        "case_study_summary": repo_relative(cfg, summary_path),
        "missing_case_types": repo_relative(cfg, missing_path),
        "main_paper_mode": main_mode,
        "acceptance": summary["acceptance"],
        "note": "positive cases use only adjudicated true positives; negative cases are counted separately",
    }


def _case_warning_source(cfg: Config, manifest: dict | None = None) -> Path:
    if manifest:
        return Path(manifest["resolved_paths"].get("promoted_warnings") or manifest["resolved_paths"]["warnings"])
    canonical = canonical_run_dir(cfg) / "promoted_warnings.jsonl"
    if canonical.exists():
        return canonical
    canonical = canonical_run_dir(cfg) / "warnings.jsonl"
    if canonical.exists():
        return canonical
    conn = connect(cfg.database)
    initialize(conn)
    for row in conn.execute("SELECT summary FROM replay_runs WHERE status IN ('completed', 'completed_with_failures') ORDER BY started_at DESC"):
        try:
            aggregate = json.loads(row["summary"] or "{}").get("aggregate_warnings")
        except json.JSONDecodeError:
            aggregate = None
        if aggregate and Path(aggregate).exists():
            return Path(aggregate)
    return cfg.warnings_jsonl


def _case_review_sources(cfg: Config, warning_source: Path, manifest: dict | None = None) -> list[Path]:
    candidates: list[Path] = []
    if manifest:
        pooled = manifest["resolved_paths"].get("pooled_review_labels")
        if pooled:
            candidates.append(Path(pooled))
        semantic = canonical_run_dir(cfg) / "semantic_target_review.csv"
        if semantic.exists():
            candidates.append(semantic)
        candidates.append(Path(manifest["resolved_paths"]["manual_review"]))
    else:
        for name in ("semantic_target_review.csv", "pooled_review_labels.csv", "manual_review.csv"):
            adjacent = warning_source.parent / name
            if adjacent.exists():
                candidates.append(adjacent)
        fallback = cfg.data_dir / "manual_review.csv"
        if fallback.exists():
            candidates.append(fallback)
    seen: set[Path] = set()
    out: list[Path] = []
    for path in candidates:
        resolved = path.resolve()
        if resolved not in seen and path.exists():
            seen.add(resolved)
            out.append(path)
    return out


def _semantic_target_rows(cfg: Config, warnings: list[dict[str, Any]]) -> list[dict[str, Any]]:
    path = canonical_run_dir(cfg) / "semantic_target_review_set.jsonl"
    if not path.exists():
        return []
    target_rows = read_warnings(path)
    by_uid = {str(warning.get("warning_uid")): warning for warning in warnings if warning.get("warning_uid")}
    merged: list[dict[str, Any]] = []
    for target in target_rows:
        base = dict(by_uid.get(str(target.get("warning_uid")), {}))
        base.update(target)
        merged.append(base)
    return merged


def _select_positive_cases(
    warnings: list[dict[str, Any]],
    labels: dict[str, str],
    review_rows: dict[str, dict[str, str]],
) -> list[dict[str, Any]]:
    valid = [warning for warning in warnings if _case_is_valid(warning, label_for_warning(labels, warning), review_rows)]
    selected: list[dict[str, Any]] = []
    used: set[str] = set()

    def add_first(predicate) -> None:
        for warning in valid:
            key = warning_key(warning)
            if key in used or not predicate(warning):
                continue
            selected.append(warning)
            used.add(key)
            return

    for case_type in CASE_TARGET_TYPES:
        add_first(lambda warning, case_type=case_type: label_for_warning(labels, warning) == "TRUE_SEMANTIC_DRIFT" and _case_drift_type(warning) == case_type)

    for case_type in CASE_TARGET_TYPES:
        if sum(1 for warning in selected if label_for_warning(labels, warning) == "TRUE_WRAPPER_FIX") >= POSITIVE_TARGET // 2:
            break
        add_first(lambda warning, case_type=case_type: _case_drift_type(warning) == case_type and label_for_warning(labels, warning) == "TRUE_WRAPPER_FIX")

    add_first(lambda warning: label_for_warning(labels, warning) == "TRUE_BUILD_BREAKAGE")

    for warning in valid:
        if len(selected) >= POSITIVE_TARGET:
            break
        key = warning_key(warning)
        if label_for_warning(labels, warning) == "TRUE_WRAPPER_FIX" and sum(1 for item in selected if label_for_warning(labels, item) == "TRUE_WRAPPER_FIX") >= POSITIVE_TARGET // 2:
            continue
        if key not in used:
            selected.append(warning)
            used.add(key)
    return selected[:POSITIVE_TARGET]


def _select_negative_cases(
    warnings: list[dict[str, Any]],
    labels: dict[str, str],
    review_rows: dict[str, dict[str, str]],
    *,
    positive_cases: list[dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    selected: list[dict[str, Any]] = []
    used: set[str] = set()
    covered_types = {_case_drift_type(warning) for warning in positive_cases or []}
    preferred_case_types = [case_type for case_type in CASE_TARGET_TYPES if case_type not in covered_types]

    def try_add(warning: dict[str, Any]) -> bool:
        key = warning_key(warning)
        if key in used:
            return False
        if not eligible_for_main_warning(warning):
            return False
        if not _review_has_adjudication(warning, review_rows):
            return False
        if not _has_case_evidence_chain(warning):
            return False
        selected.append(warning)
        used.add(key)
        return True

    for case_type in preferred_case_types:
        for preferred in ("FALSE_POSITIVE", "BENIGN_DRIFT", "UNCLEAR"):
            for warning in warnings:
                if len(selected) >= NEGATIVE_TARGET:
                    return selected
                if _case_drift_type(warning) != case_type:
                    continue
                if label_for_warning(labels, warning) == preferred and try_add(warning):
                    break
            if len(selected) >= NEGATIVE_TARGET or any(_case_drift_type(warning) == case_type for warning in selected):
                break

    for preferred in ("FALSE_POSITIVE", "BENIGN_DRIFT", "UNCLEAR"):
        for warning in warnings:
            if len(selected) >= NEGATIVE_TARGET:
                return selected
            label = label_for_warning(labels, warning)
            if label != preferred:
                continue
            key = warning_key(warning)
            if key in used:
                continue
            raw_type = str(warning.get("type") or "Unknown")
            if any(str(item.get("type") or "Unknown") == raw_type for item in selected):
                continue
            try_add(warning)
    for preferred in ("FALSE_POSITIVE", "BENIGN_DRIFT", "UNCLEAR"):
        for warning in warnings:
            if len(selected) >= NEGATIVE_TARGET:
                return selected
            label = label_for_warning(labels, warning)
            key = warning_key(warning)
            if label != preferred or key in used:
                continue
            try_add(warning)
    return selected


def _case_is_valid(warning: dict[str, Any], label: str | None, review_rows: dict[str, dict[str, str]]) -> bool:
    return bool(
        label in TRUE_LABELS
        and eligible_for_main_warning(warning)
        and warning.get("old_version")
        and warning.get("new_version")
        and warning.get("pair_id")
        and not generated_binding_only(warning)
        and _has_c_evidence(warning)
        and _has_rust_impact(warning)
        and _has_case_evidence_chain(warning)
        and _review_has_adjudication(warning, review_rows)
    )


def _load_adjudicated_labels(path: Path) -> dict[str, str]:
    return load_manual_labels(path)


def _load_review_rows(paths: list[Path]) -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    for path in paths:
        if not path.exists():
            continue
        with path.open(newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                key = manual_review_row_key(row)
                if not key:
                    continue
                label = row.get("adjudicated_label", "").strip() or row.get("label", "").strip()
                if not label:
                    continue
                clean = {field: str(value or "") for field, value in row.items()}
                clean["adjudicated_label"] = label
                rows.setdefault(key, clean)
                uid_key = row.get("warning_uid", "").strip()
                if uid_key:
                    rows.setdefault(uid_key, clean)
    return rows


def _review_has_adjudication(warning: dict[str, Any], review_rows: dict[str, dict[str, str]]) -> bool:
    row = _review_for_warning(warning, review_rows)
    return bool(row.get("adjudicated_label") and row.get("adjudication_notes", "") is not None)


def _review_for_warning(warning: dict[str, Any], review_rows: dict[str, dict[str, str]]) -> dict[str, str]:
    keys = [
        warning_key(warning),
        str(warning.get("warning_uid") or ""),
        str(warning.get("warning_id") or ""),
    ]
    pair_id = warning.get("pair_id")
    if pair_id and warning.get("warning_id"):
        keys.append(f"{pair_id}:{warning.get('warning_id')}")
    for key in keys:
        if key and key in review_rows:
            return review_rows[key]
    return {}


def _has_c_evidence(warning: dict[str, Any]) -> bool:
    c_side = warning.get("c_side", {})
    structured_diff = c_side.get("old") is not None and c_side.get("new") is not None
    return bool(
        c_side.get("evidence")
        or c_side.get("old_indicators")
        or c_side.get("new_indicators")
        or structured_diff
        or warning.get("c_evidence_level") in {"c_source_diff", "c_behavior_indicator", "binding_only", "build_oracle", "wrapper_fix"}
    )


def _has_rust_impact(warning: dict[str, Any]) -> bool:
    rust_side = warning.get("rust_side", {})
    return bool(
        rust_side.get("uses")
        or rust_side.get("safe_apis")
        or rust_side.get("safety_comments")
        or rust_side.get("error_mappings")
        or rust_side.get("lifetime_facts")
        or rust_side.get("oracle_hits")
        or warning.get("rust_impact_level") in {"direct_unsafe_call", "safe_api", "contract_mapping", "oracle_confirmed"}
    )


def _has_wrapper_oracle(warning: dict[str, Any]) -> bool:
    rust_side = warning.get("rust_side", {})
    evidence = list(warning.get("evidence_chain") or []) + list(rust_side.get("oracle_hits") or [])
    return any(isinstance(item, dict) and item.get("oracle_type") == "wrapper_fix" for item in evidence)


def _exposure_edges(warning: dict[str, Any]) -> list[dict[str, Any]]:
    edges = ((warning.get("rust_side") or {}).get("exposure") or {}).get("edges") or []
    return [edge for edge in edges if isinstance(edge, dict)]


def _has_binding_or_helper_evidence(warning: dict[str, Any]) -> bool:
    fact_source = str(warning.get("fact_source") or "")
    if fact_source in {"binding_diff", "layout_diff", "macro_diff", "c_api_diff"}:
        return True
    return any(edge.get("edge_type") == "GENERATED_FROM" for edge in _exposure_edges(warning))


def _has_unsafe_or_binding_use(warning: dict[str, Any]) -> bool:
    rust_side = warning.get("rust_side", {})
    for use in rust_side.get("uses") or []:
        if isinstance(use, dict) and bool(use.get("enclosing_unsafe_block")):
            return True
    return False


def _has_contract_mapping_evidence(warning: dict[str, Any]) -> bool:
    rust_side = warning.get("rust_side", {})
    return bool(
        rust_side.get("safe_apis")
        or rust_side.get("safety_comments")
        or rust_side.get("error_mappings")
        or rust_side.get("lifetime_facts")
        or rust_side.get("oracle_hits")
        or warning.get("rust_impact_level") in {"safe_api", "contract_mapping", "oracle_confirmed"}
    )


def _has_case_evidence_chain(warning: dict[str, Any]) -> bool:
    return bool(
        _has_c_evidence(warning)
        and _has_binding_or_helper_evidence(warning)
        and _has_unsafe_or_binding_use(warning)
        and _has_contract_mapping_evidence(warning)
    )


def _case_summary_table(
    positive_cases: list[dict[str, Any]],
    negative_cases: list[dict[str, Any]],
    labels: dict[str, str],
    cfg: Config,
) -> dict[str, Any]:
    positive_labels = [label_for_warning(labels, warning) for warning in positive_cases]
    negative_labels = [label_for_warning(labels, warning) for warning in negative_cases]
    all_cases = positive_cases + negative_cases
    all_types = sorted({_case_drift_type(warning) for warning in all_cases})
    positive_types = sorted({_case_drift_type(warning) for warning in positive_cases})
    raw_warning_types = sorted({str(warning.get("type") or "Unknown") for warning in all_cases})
    missing_evidence_chain = [
        {
            "warning_uid": warning.get("warning_uid"),
            "warning_id": warning.get("warning_id"),
            "pair_id": warning.get("pair_id"),
            "symbol": _symbol(warning),
            "case_kind": "positive" if warning in positive_cases else "negative",
        }
        for warning in all_cases
        if not _has_case_evidence_chain(warning)
    ]
    case_paths = sorted((cfg.repo_root / "paper/cases").glob("case-*.md"))
    absolute_paths = _count_absolute_local_paths(case_paths)
    semantic_true_cases = sum(1 for label in positive_labels if label == "TRUE_SEMANTIC_DRIFT")
    non_wrapper_semantic_cases = sum(1 for warning, label in zip(positive_cases, positive_labels) if label == "TRUE_SEMANTIC_DRIFT" and not _has_wrapper_oracle(warning))
    wrapper_cases = sum(1 for label in positive_labels if label == "TRUE_WRAPPER_FIX")
    summary = {
        "case_studies": len(positive_cases),
        "positive_case_studies": len(positive_cases),
        "negative_case_studies": len(negative_cases),
        "case_drift_types": all_types,
        "drift_type_count": len(all_types),
        "positive_case_drift_types": positive_types,
        "positive_drift_type_count": len(positive_types),
        "raw_warning_types": raw_warning_types,
        "raw_warning_type_count": len(raw_warning_types),
        "semantic_true_cases": semantic_true_cases,
        "non_wrapper_semantic_cases": non_wrapper_semantic_cases,
        "wrapper_fix_backed_cases": wrapper_cases,
        "build_breakage_cases": sum(1 for label in positive_labels if label == "TRUE_BUILD_BREAKAGE"),
        "false_positive_cases": sum(1 for label in positive_labels if label == "FALSE_POSITIVE"),
        "false_positive_negative_cases": sum(1 for label in negative_labels if label == "FALSE_POSITIVE"),
        "benign_drift_cases": sum(1 for label in positive_labels if label == "BENIGN_DRIFT"),
        "unlabeled_cases": sum(1 for label in positive_labels if not label),
        "absolute_local_paths": absolute_paths,
        "case_evidence_chain_missing": missing_evidence_chain,
        "case_evidence_chain_missing_count": len(missing_evidence_chain),
        "positive_label_distribution": dict(Counter(positive_labels)),
        "negative_label_distribution": dict(Counter(negative_labels)),
    }
    summary["acceptance"] = {
        "case_studies_minimum": summary["case_studies"] >= 8,
        "negative_case_studies_minimum": summary["negative_case_studies"] >= 2,
        "negative_false_positive_case": summary["false_positive_negative_cases"] >= FALSE_POSITIVE_NEGATIVE_TARGET,
        "positive_labels_all_true": all(label in TRUE_LABELS for label in positive_labels),
        "drift_type_count_minimum": summary["drift_type_count"] >= 4,
        "raw_warning_type_count_minimum": summary["raw_warning_type_count"] >= 3,
        "semantic_true_cases_minimum": summary["semantic_true_cases"] >= 3,
        "non_wrapper_semantic_cases_minimum": summary["non_wrapper_semantic_cases"] >= 2,
        "wrapper_fix_backed_cases_limit": summary["wrapper_fix_backed_cases"] <= max(0, summary["case_studies"] // 2),
        "evidence_chain_complete": summary["case_evidence_chain_missing_count"] == 0,
        "positive_labels_clean": summary["false_positive_cases"] == 0 and summary["benign_drift_cases"] == 0 and summary["unlabeled_cases"] == 0,
        "absolute_local_paths_clean": summary["absolute_local_paths"] == 0,
    }
    summary["acceptance"]["minimum_passes"] = all(summary["acceptance"].values())
    return summary


def _count_absolute_local_paths(paths: list[Path]) -> int:
    count = 0
    for path in paths:
        text = path.read_text(encoding="utf-8")
        count += sum(text.count(marker) for marker in LOCAL_PATH_MARKERS)
    return count


def _case_template(case_type: str, warning: dict[str, Any], label: str, review: dict[str, str], *, case_kind: str) -> str:
    c_side = warning.get("c_side", {})
    rust_side = warning.get("rust_side", {})
    symbol = _symbol(warning)
    warning_id = warning.get("warning_id", "unknown")
    title_prefix = "Positive" if case_kind == "positive" else "Failure Analysis"
    return f"""# {title_prefix}: {case_type} for `{symbol}`

## Summary

{_case_summary(symbol, warning_id, label, case_kind)}

## Old Version Evidence

- Version: `{_old_version(warning)}`
- Old value or indicators: `{c_side.get('old', c_side.get('old_indicators', []))}`

## New Version Evidence

- Version: `{_new_version(warning)}`
- New value or indicators: `{c_side.get('new', c_side.get('new_indicators', []))}`

## C-Side Diff

{_format_c_evidence(c_side)}

## Rust-Side Dependency

{_format_rust_evidence(rust_side)}

## Safe API / Contract Assumption

{_contract_assumption(warning)}

## Manual Review Label

- Adjudicated label: `{label or "UNLABELED"}`
- Reviewer 1: `{review.get('reviewer1_label', '')}` -- {review.get('reviewer1_notes', '')}
- Reviewer 2: `{review.get('reviewer2_label', '')}` -- {review.get('reviewer2_notes', '')}
- Adjudication: {review.get('adjudication_notes', '')}

## Why This Is Not Generated-Binding-Only

{_not_binding_only_explanation(warning)}

## Why Compiler Alone Does Not Catch It

The compiler checks the current Rust/C binding shape. This case is about whether a Rust abstraction, helper, or safety invariant remains synchronized with an evolving C-side contract across versions.

## Alternative Explanation Considered

{_alternative_explanation(label)}

## Maintainer Review Implication

{_maintainer_implication(label)}

## Reproduction Pointers

- Warning: `{warning_id}`
- Warning UID: `{warning.get('warning_uid', 'n/a')}`
- Replay pair: `{warning.get('pair_id') or 'n/a'}`
- Drift type: `{case_type}`
- C symbol: `{symbol}`
- Risk: `{warning.get('risk', 'Unknown')}`
- Score: `{warning.get('score', 0)}`
"""


def _old_version(warning: dict[str, Any]) -> str:
    return str(warning.get("old_version") or warning.get("c_side", {}).get("old_version") or "unknown")


def _new_version(warning: dict[str, Any]) -> str:
    return str(warning.get("new_version") or warning.get("c_side", {}).get("new_version") or "unknown")


def _symbol(warning: dict[str, Any]) -> str:
    return str((warning.get("c_side") or {}).get("symbol") or "unknown")


def _case_drift_type(warning: dict[str, Any]) -> str:
    return str(warning.get("semantic_target_type") or warning.get("type") or "Warning")


def _slug(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9_]+", "_", value.strip().lower()).strip("_")
    return slug or "unknown"


def _not_binding_only_explanation(warning: dict[str, Any]) -> str:
    rust_side = warning.get("rust_side", {})
    if warning.get("c_evidence_level") == "binding_only":
        return "The case has Rust reachability or contract/oracle evidence beyond a generated binding delta; generated-binding-only rows are excluded from positive case selection."
    if rust_side.get("uses") or rust_side.get("safe_apis") or rust_side.get("error_mappings") or rust_side.get("safety_comments"):
        return "The case includes C-side source or indicator evidence plus Rust-side dependency evidence."
    return "The case is retained because review evidence connects the warning to a Rust-impact path rather than a standalone generated binding change."


def _case_summary(symbol: str, warning_id: str, label: str, case_kind: str) -> str:
    if case_kind == "negative":
        return f"`{symbol}` produced `{warning_id}` and is included as a negative/failure-analysis case with adjudicated label `{label}`."
    return f"`{symbol}` produced `{warning_id}` and is included as an adjudicated positive review target with label `{label}`."


def _format_c_evidence(c_side: dict[str, Any]) -> str:
    lines = [
        f"- Old indicators/value: `{c_side.get('old', c_side.get('old_indicators', []))}`",
        f"- New indicators/value: `{c_side.get('new', c_side.get('new_indicators', []))}`",
    ]
    for item in (c_side.get("evidence") or [])[:5]:
        if isinstance(item, dict):
            lines.append(f"- `{item.get('evidence_file')}:{item.get('evidence_line')}`: `{item.get('evidence_text', '')}`")
    return "\n".join(lines)


def _format_rust_evidence(rust_side: dict[str, Any]) -> str:
    lines: list[str] = []
    for edge in ((rust_side.get("exposure") or {}).get("edges") or [])[:5]:
        if isinstance(edge, dict):
            lines.append(f"- exposure `{edge.get('edge_type')}`: `{edge.get('src')}` -> `{edge.get('dst')}`")
    uses = sorted(
        [use for use in (rust_side.get("uses") or []) if isinstance(use, dict)],
        key=lambda use: (not bool(use.get("enclosing_unsafe_block")), str(use.get("rust_file") or ""), int(use.get("line") or 0)),
    )
    for use in uses[:5]:
        if isinstance(use, dict):
            context = use.get("enclosing_function") or use.get("enclosing_impl") or use.get("enclosing_type") or "binding or module scope"
            unsafe_note = " (unsafe block)" if bool(use.get("enclosing_unsafe_block")) else ""
            lines.append(f"- `{use.get('rust_file')}:{use.get('line')}` in `{context}`{unsafe_note}")
    for item in (rust_side.get("safe_apis") or [])[:3]:
        if isinstance(item, dict):
            lines.append(f"- safe API `{item.get('api_name')}`")
    for item in (rust_side.get("safety_comments") or [])[:3]:
        if isinstance(item, dict):
            lines.append(f"- `{item.get('rust_file')}:{item.get('line')}`: `{item.get('text', '')}`")
    for item in (rust_side.get("error_mappings") or [])[:3]:
        if isinstance(item, dict):
            lines.append(f"- `{item.get('rust_file')}:{item.get('line')}` error mapping `{item.get('mapping_type')}`")
    for item in (rust_side.get("lifetime_facts") or [])[:3]:
        if isinstance(item, dict):
            lines.append(f"- `{item.get('rust_file')}:{item.get('line')}` lifetime fact `{item.get('fact_type')}`")
    for item in (rust_side.get("oracle_hits") or [])[:3]:
        if isinstance(item, dict):
            lines.append(f"- {item.get('oracle_type')}: `{item.get('symbol', item.get('commit_id', 'oracle'))}`")
    return "\n".join(lines) if lines else "- No Rust-side evidence was attached to this warning."


def _contract_assumption(warning: dict[str, Any]) -> str:
    rust_side = warning.get("rust_side", {})
    if rust_side.get("safe_apis"):
        return "The warning reaches a public safe Rust API, so the maintainer review question is whether that API's documented contract remains synchronized with the C-side behavior."
    if rust_side.get("error_mappings"):
        return "The warning reaches Rust error-mapping code, so the review question is whether the C return convention still matches Rust Result/Error handling."
    if rust_side.get("lifetime_facts"):
        return "The warning reaches Rust ownership or lifetime evidence, so the review question is whether object lifetime assumptions changed."
    if rust_side.get("oracle_hits"):
        return "The warning is connected to later Rust wrapper/helper evidence and is reported separately from semantic-only drift."
    return "The warning reaches Rust code and should be reviewed as an evidence-backed target, not as an automatically confirmed defect."


def _alternative_explanation(label: str) -> str:
    if label == "TRUE_SEMANTIC_DRIFT":
        return "Review considered whether this was only signature churn or generated binding noise; adjudication kept it because C-side drift, Rust exposure, and contract dependence were all present."
    if label == "TRUE_WRAPPER_FIX":
        return "Review considered whether this was semantic drift; adjudication classifies it as wrapper-fix-backed validation instead of standalone semantic evidence."
    if label == "TRUE_BUILD_BREAKAGE":
        return "Review considered whether this was a soft contract warning; adjudication uses build evidence as the stronger label."
    return "Review considered whether the warning should be promoted, but adjudication found the evidence benign, unsupported, or incomplete."


def _maintainer_implication(label: str) -> str:
    if label in TRUE_LABELS:
        return "A maintainer should inspect the Rust wrapper or safe abstraction path when carrying this C-side change across versions."
    return "This case documents why similar high-scoring warnings need manual review before being counted as true positives."


def _missing_case_types(summary: dict[str, Any]) -> str:
    present = set(summary.get("case_drift_types") or [])
    missing = [case_type for case_type in CASE_TARGET_TYPES if case_type not in present]
    lines = [
        "# Missing Case Types",
        "",
        f"Selected case-study drift types: {', '.join(summary.get('case_drift_types') or []) or 'none'}.",
        f"Selected positive drift types: {', '.join(summary.get('positive_case_drift_types') or []) or 'none'}.",
        "",
    ]
    if not missing:
        lines.append("No target drift type is missing from the case-study suite.")
    else:
        lines.append("The following target drift types were not represented by an adjudicated case study:")
        lines.extend(f"- `{case_type}`" for case_type in missing)
    if summary.get("semantic_true_cases", 0) < 2:
        lines.append("")
        lines.append("Semantic true-positive case coverage is below the two-case gate, so semantic claims must remain exploratory.")
    return "\n".join(lines).rstrip() + "\n"
