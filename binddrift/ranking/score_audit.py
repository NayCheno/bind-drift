from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path
from typing import Any

from binddrift.config import Config
from binddrift.evaluation.metrics import label_for_warning, load_manual_labels
from binddrift.ranking.oracle_blind_scorer import (
    generated_binding_only,
    oracle_dependent_binding_only,
    oracle_only_promotion,
    primary_oracle_blind_eligible,
    rank_primary_warnings_oracle_blind,
    rank_warnings_oracle_blind,
    strict_top50_eligible,
)
from binddrift.run_manifest import canonical_run_dir, repo_relative, sha256_file, validate_run_manifest
from binddrift.warnings import read_warnings


TOP20_ANALYSIS = Path("paper/analysis/top20_false_positive_analysis.md")


def generate_ranking_score_audit(
    cfg: Config,
    *,
    warnings_path: Path | None = None,
    labels_path: Path | None = None,
    ranking_eval_path: Path | None = None,
    output: Path | None = None,
    analysis_output: Path | None = None,
) -> dict[str, Any]:
    manifest = validate_run_manifest(cfg)
    run_dir = canonical_run_dir(cfg)
    warnings_path = warnings_path or Path(manifest["resolved_paths"]["promoted_warnings"])
    labels_path = labels_path or (
        Path(manifest["resolved_paths"].get("pooled_review_labels"))
        if manifest["resolved_paths"].get("pooled_review_labels")
        else Path(manifest["resolved_paths"]["manual_review"])
    )
    ranking_eval_path = ranking_eval_path or cfg.repo_root / "paper/tables/ranking_pooled_evaluation.json"
    output = output or cfg.repo_root / "paper/tables/ranking_score_audit.json"
    analysis_output = analysis_output or cfg.repo_root / TOP20_ANALYSIS
    warnings = read_warnings(warnings_path)
    labels = load_manual_labels(labels_path, uid_only=True)
    ranking_eval = json.loads(ranking_eval_path.read_text(encoding="utf-8")) if ranking_eval_path.exists() else {}
    audit = build_ranking_score_audit(
        warnings,
        labels,
        ranking_eval=ranking_eval,
        warnings_source=repo_relative(cfg, warnings_path),
        labels_source=repo_relative(cfg, labels_path),
        warnings_sha256=sha256_file(warnings_path),
        labels_sha256=sha256_file(labels_path),
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_top20_false_positive_analysis(audit, analysis_output)
    return {"ranking_score_audit": str(output), "top20_false_positive_analysis": str(analysis_output)}


def build_ranking_score_audit(
    warnings: list[dict[str, Any]],
    labels: dict[str, str],
    *,
    ranking_eval: dict[str, Any] | None = None,
    warnings_source: str | None = None,
    labels_source: str | None = None,
    warnings_sha256: str | None = None,
    labels_sha256: str | None = None,
) -> dict[str, Any]:
    full_ranked = rank_warnings_oracle_blind(warnings)
    primary_ranked = rank_primary_warnings_oracle_blind(warnings)
    full_top50 = full_ranked[:50]
    strict_window = [warning for warning in primary_ranked if strict_top50_eligible(warning)][:50]
    primary_metrics = _primary_metrics(ranking_eval or {})
    top20 = primary_ranked[:20]
    top20_false_positives = [warning for warning in top20 if label_for_warning(labels, warning) == "FALSE_POSITIVE"]
    return {
        "ranker": "binddrift_oracle_blind",
        "oracle_blind": True,
        "warnings_source": warnings_source,
        "warnings_sha256": warnings_sha256,
        "labels_source": labels_source,
        "labels_sha256": labels_sha256,
        "warning_count": len(warnings),
        "primary_candidate_count": len(primary_ranked),
        "strict_top50_target": 50,
        "strict_top50_window_size": len(strict_window),
        "strict_top50_shortfall": max(0, 50 - len(strict_window)),
        "strict_top50_shortfall_reason": (
            "candidate pool contains fewer than 50 oracle-blind scored warnings with C/binding evidence plus Rust reachability"
            if len(strict_window) < 50
            else ""
        ),
        "strict_top50_checks": _window_checks(strict_window),
        "full_rank_top50_checks": _window_checks(full_top50),
        "strict_top50": [_warning_row(warning, labels, rank=idx) for idx, warning in enumerate(strict_window, start=1)],
        "full_rank_top50": [_warning_row(warning, labels, rank=idx) for idx, warning in enumerate(full_top50, start=1)],
        "top20_label_distribution": dict(Counter(label_for_warning(labels, warning) or "UNLABELED" for warning in top20)),
        "top20_false_positive_count": len(top20_false_positives),
        "top20_false_positives": [_failure_row(warning, labels, rank=idx) for idx, warning in enumerate(top20, start=1) if label_for_warning(labels, warning) == "FALSE_POSITIVE"],
        "primary_metrics": primary_metrics,
        "claim_recommendation": _claim_recommendation(primary_metrics),
    }


def _primary_metrics(ranking_eval: dict[str, Any]) -> dict[str, Any]:
    primary = next((row for row in ranking_eval.get("rankers", []) if row.get("ranker") == "binddrift_oracle_blind"), {})
    return {
        "p_at_10": primary.get("p_at_10"),
        "p_at_20": primary.get("p_at_20"),
        "p_at_50": primary.get("p_at_50"),
        "p_at_100": primary.get("p_at_100"),
        "ndcg_at_20": primary.get("ndcg_at_20"),
        "minimum_topk_passes": bool(
            (primary.get("p_at_10") or 0.0) >= 0.50
            and (primary.get("p_at_20") or 0.0) >= 0.45
            and (primary.get("p_at_50") or 0.0) >= 0.42
            and (primary.get("p_at_100") or 0.0) >= 0.40
            and (primary.get("ndcg_at_20") or 0.0) >= 0.55
        ),
    }


def _claim_recommendation(metrics: dict[str, Any]) -> str:
    if metrics.get("minimum_topk_passes"):
        return "ranking improvement claim may be considered only if baseline lift gate also passes"
    return "evidence gate claim only; ranking improvement not supported"


def _window_checks(warnings: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "warnings": len(warnings),
        "tier_d_warnings": sum(1 for warning in warnings if warning.get("eligibility_tier") == "D"),
        "generated_binding_only_warnings": sum(1 for warning in warnings if generated_binding_only(warning)),
        "missing_score_components": sum(1 for warning in warnings if not warning.get("score_components")),
        "missing_score_explanations": sum(1 for warning in warnings if not warning.get("score_explanation")),
        "unsupported_c_evidence_warnings": sum(1 for warning in warnings if not _has_c_or_binding_evidence(warning)),
        "unsupported_rust_reachability_warnings": sum(1 for warning in warnings if not _has_rust_reachability(warning)),
        "binding_only_c_evidence_warnings": sum(1 for warning in warnings if warning.get("c_evidence_level") == "binding_only"),
        "oracle_only_promotion_warnings": sum(1 for warning in warnings if oracle_only_promotion(warning)),
        "oracle_dependent_binding_only_warnings": sum(1 for warning in warnings if oracle_dependent_binding_only(warning)),
        "non_primary_oracle_blind_candidates": sum(1 for warning in warnings if not primary_oracle_blind_eligible(warning)),
        "tier_distribution": dict(Counter(str(warning.get("eligibility_tier")) for warning in warnings)),
    }


def _warning_row(warning: dict[str, Any], labels: dict[str, str], *, rank: int) -> dict[str, Any]:
    components = warning.get("score_components") or {}
    return {
        "rank": rank,
        "warning_uid": warning.get("warning_uid"),
        "warning_id": warning.get("warning_id"),
        "pair_id": warning.get("pair_id"),
        "type": warning.get("type"),
        "symbol": (warning.get("c_side") or {}).get("symbol"),
        "label": label_for_warning(labels, warning),
        "oracle_blind": warning.get("oracle_blind") is True,
        "eligibility_tier": warning.get("eligibility_tier"),
        "strict_top50_eligible": warning.get("strict_top50_eligible") is True,
        "primary_oracle_blind_eligible": warning.get("primary_oracle_blind_eligible") is True,
        "oracle_only_promotion": warning.get("oracle_only_promotion") is True,
        "oracle_dependent_binding_only": warning.get("oracle_dependent_binding_only") is True,
        "generated_binding_only": warning.get("generated_binding_only") is True,
        "c_evidence_level": warning.get("c_evidence_level"),
        "rust_reachability": _rust_reachability_kind(warning),
        "oracle_blind_score": warning.get("oracle_blind_score"),
        "score_components": components,
        "dominant_score_components": _dominant_components(components),
    }


def _failure_row(warning: dict[str, Any], labels: dict[str, str], *, rank: int) -> dict[str, Any]:
    row = _warning_row(warning, labels, rank=rank)
    row["failure_taxonomy"] = _failure_taxonomy(warning)
    return row


def _dominant_components(components: dict[str, Any], limit: int = 3) -> list[dict[str, Any]]:
    numeric = [(key, float(value)) for key, value in components.items() if isinstance(value, (int, float)) and value > 0]
    numeric.sort(key=lambda item: (-item[1], item[0]))
    return [{"component": key, "value": value} for key, value in numeric[:limit]]


def _has_rust_reachability(warning: dict[str, Any]) -> bool:
    rust_side = warning.get("rust_side") or {}
    reasons = set(warning.get("promotion_reasons") or [])
    return bool(rust_side.get("uses") or rust_side.get("safe_apis") or "direct_binding_use" in reasons or "exposes_safe_api" in reasons)


def _has_c_or_binding_evidence(warning: dict[str, Any]) -> bool:
    return warning.get("c_evidence_level") in {"c_source_diff", "c_behavior_indicator", "binding_only"} or warning.get("fact_source") in {"binding_diff", "layout_diff"}


def _rust_reachability_kind(warning: dict[str, Any]) -> str:
    rust_side = warning.get("rust_side") or {}
    reasons = set(warning.get("promotion_reasons") or [])
    kinds: list[str] = []
    if rust_side.get("uses") or "direct_binding_use" in reasons:
        kinds.append("direct_rust_use")
    if rust_side.get("safe_apis") or "exposes_safe_api" in reasons:
        kinds.append("safe_api_exposure")
    return ",".join(kinds) if kinds else "none"


def _failure_taxonomy(warning: dict[str, Any]) -> str:
    symbol = str((warning.get("c_side") or {}).get("symbol") or "").lower()
    if warning.get("type") == "SignatureDrift" and symbol.isupper():
        return "macro_or_constant_rendered_as_signature"
    if symbol in {"ptr_err", "err_ptr"}:
        return "generic_error_pointer_helper_overprioritized"
    if warning.get("type") == "SignatureDrift":
        return "signature_change_without_supported_rust_contract_impact"
    if warning.get("c_evidence_level") == "binding_only":
        return "binding_only_or_generated_surface"
    return "weak_contract_mapping_or_scope_mismatch"


def write_top20_false_positive_analysis(audit: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Top-20 False Positive Analysis",
        "",
        "This analysis covers false positives in the oracle-blind top-20 ranking. Warnings remain review targets, not confirmed bugs.",
        "",
        f"- Primary P@10: {audit['primary_metrics'].get('p_at_10')}",
        f"- Ranking claim: {audit['claim_recommendation']}",
        f"- Top-20 false positives: {audit['top20_false_positive_count']}",
        "",
    ]
    if not audit["top20_false_positives"]:
        lines.append("No `FALSE_POSITIVE` labels appear in the top-20.")
    for item in audit["top20_false_positives"]:
        lines.extend(
            [
                f"## Rank {item['rank']}: {item['symbol']} ({item['type']})",
                "",
                f"- Warning: `{item['warning_id']}`",
                f"- Pair: `{item['pair_id']}`",
                f"- Score: `{item['oracle_blind_score']}`",
                f"- Tier: `{item['eligibility_tier']}`",
                f"- Failure taxonomy: `{item['failure_taxonomy']}`",
                f"- Dominant components: {_format_components(item['dominant_score_components'])}",
                "- Audit note: high C/Rust reachability evidence was not sufficient to establish supported Rust contract impact under adjudication.",
                "",
            ]
        )
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def _format_components(components: list[dict[str, Any]]) -> str:
    return ", ".join(f"`{item['component']}={item['value']}`" for item in components) if components else "`none`"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate BindDrift oracle-blind ranking score audit artifacts.")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--warnings")
    parser.add_argument("--labels")
    parser.add_argument("--ranking-eval")
    parser.add_argument("--output")
    parser.add_argument("--analysis-output")
    args = parser.parse_args(argv)
    cfg = Config.from_args(repo_root=args.repo_root)
    result = generate_ranking_score_audit(
        cfg,
        warnings_path=Path(args.warnings).resolve() if args.warnings else None,
        labels_path=Path(args.labels).resolve() if args.labels else None,
        ranking_eval_path=Path(args.ranking_eval).resolve() if args.ranking_eval else None,
        output=Path(args.output).resolve() if args.output else None,
        analysis_output=Path(args.analysis_output).resolve() if args.analysis_output else None,
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
