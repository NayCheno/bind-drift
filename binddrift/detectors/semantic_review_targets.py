from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from binddrift.artifact_paths import sanitize_local_paths
from binddrift.config import Config
from binddrift.evaluation.metrics import TRUE_LABELS, label_for_warning, manual_review_row_key
from binddrift.ranking.oracle_blind_scorer import rank_warnings_oracle_blind
from binddrift.run_manifest import canonical_run_dir, repo_relative, sha256_file, validate_run_manifest
from binddrift.warnings import ensure_warning_uid, read_warnings, write_jsonl


SEMANTIC_REVIEW_QUOTAS = {
    "NullabilityDrift": 80,
    "OwnershipRefcountDrift": 80,
    "AllocationFreeDrift": 80,
    "SleepabilityContextDrift": 80,
    "LayoutFieldDrift": 80,
}

M4_FALSE_POSITIVE_TAXONOMY = {
    "binding_only_or_generated_surface",
    "weak_rust_reachability",
    "real_c_drift_no_rust_contract_impact",
    "macro_constant_over_prioritization",
    "layout_ambiguity",
}

REVIEW_FIELDS = [
    "warning_uid",
    "warning_id",
    "pair_id",
    "rank",
    "semantic_target_type",
    "type",
    "symbol",
    "oracle_blind_rank",
    "oracle_blind_score",
    "ranker_source",
    "reviewer1_label",
    "reviewer1_notes",
    "reviewer2_label",
    "reviewer2_notes",
    "adjudicated_label",
    "adjudication_notes",
    "label_source",
]


def generate_semantic_review_targets(
    cfg: Config,
    *,
    output_set: Path | None = None,
    output_review: Path | None = None,
    output_summary: Path | None = None,
) -> dict[str, Any]:
    manifest = validate_run_manifest(cfg)
    run_dir = canonical_run_dir(cfg)
    warnings_path = Path(manifest["resolved_paths"]["promoted_warnings"])
    drift_facts_path = Path(manifest["resolved_paths"]["drift_facts"])
    pooled_review_set_raw = manifest["resolved_paths"].get("pooled_review_set")
    pooled_review_set_path = Path(pooled_review_set_raw) if pooled_review_set_raw else None
    output_set = output_set or run_dir / "semantic_target_review_set.jsonl"
    output_review = output_review or run_dir / "semantic_target_review.csv"
    output_summary = output_summary or cfg.repo_root / "paper/tables/semantic_drift_review_summary.json"

    pooled_candidates = read_warnings(pooled_review_set_path) if pooled_review_set_path else []
    warnings = _dedupe_warnings(pooled_candidates + read_warnings(warnings_path) + read_warnings(drift_facts_path))
    selected, shortages = select_semantic_targets(warnings)
    selected = [sanitize_local_paths(row, cfg) for row in selected]

    review_rows = _load_review_rows(
        [
            Path(manifest["resolved_paths"].get("pooled_review_labels", "")),
            Path(manifest["resolved_paths"]["manual_review"]),
        ]
    )
    labels = {key: row.get("adjudicated_label", "") for key, row in review_rows.items()}

    output_set.parent.mkdir(parents=True, exist_ok=True)
    write_jsonl(output_set, selected)
    output_review.parent.mkdir(parents=True, exist_ok=True)
    _write_review_csv(output_review, selected, review_rows)

    summary = build_semantic_review_summary(
        selected,
        labels,
        shortages=shortages,
        warnings_source=repo_relative(cfg, warnings_path),
        drift_facts_source=repo_relative(cfg, drift_facts_path),
        pooled_review_set_source=repo_relative(cfg, pooled_review_set_path) if pooled_review_set_path and pooled_review_set_path.exists() else None,
        review_sources=[repo_relative(cfg, path) for path in _existing_review_paths(manifest)],
        target_set=repo_relative(cfg, output_set),
        target_review=repo_relative(cfg, output_review),
        warnings_sha256=sha256_file(warnings_path),
        drift_facts_sha256=sha256_file(drift_facts_path),
        pooled_review_set_sha256=sha256_file(pooled_review_set_path) if pooled_review_set_path and pooled_review_set_path.exists() else None,
    )
    output_summary.parent.mkdir(parents=True, exist_ok=True)
    output_summary.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return {
        "semantic_target_review_set": repo_relative(cfg, output_set),
        "semantic_target_review_csv": repo_relative(cfg, output_review),
        "semantic_drift_review_summary": repo_relative(cfg, output_summary),
        "candidates": len(selected),
        "true_semantic_drift": summary["true_semantic_drift_count"],
        "claim_recommendation": summary["claim_recommendation"],
    }


def select_semantic_targets(
    warnings: list[dict[str, Any]],
    *,
    quotas: dict[str, int] | None = None,
) -> tuple[list[dict[str, Any]], dict[str, str]]:
    quotas = quotas or SEMANTIC_REVIEW_QUOTAS
    ranked = rank_warnings_oracle_blind(warnings)
    selected: list[dict[str, Any]] = []
    used: set[str] = set()
    shortages: dict[str, str] = {}
    by_category: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for warning in ranked:
        ensure_warning_uid(warning)
        category = semantic_target_type(warning)
        if not category:
            continue
        by_category[category].append(warning)

    for category, quota in quotas.items():
        candidates = sorted(
            by_category.get(category, []),
            key=lambda warning: (
                not bool(warning.get("pooled_review")),
                _semantic_candidate_priority(warning),
                str(warning.get("warning_uid") or ""),
            ),
        )
        for warning in candidates:
            if len([row for row in selected if row.get("semantic_target_type") == category]) >= quota:
                break
            key = str(warning.get("warning_uid") or "")
            if key in used:
                continue
            row = dict(warning)
            row["semantic_target_type"] = category
            row["semantic_review_target"] = True
            selected.append(row)
            used.add(key)
        category_count = sum(1 for row in selected if row.get("semantic_target_type") == category)
        if category_count < quota:
            shortages[category] = f"only {category_count} semantic candidates available for quota {quota}"

    return selected, shortages


def _dedupe_warnings(warnings: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    seen: set[str] = set()
    for warning in warnings:
        key = ensure_warning_uid(warning)
        if key in seen:
            continue
        rows.append(warning)
        seen.add(key)
    return rows


def build_semantic_review_summary(
    selected: list[dict[str, Any]],
    labels: dict[str, str],
    *,
    shortages: dict[str, str] | None = None,
    warnings_source: str | None = None,
    drift_facts_source: str | None = None,
    review_sources: list[str] | None = None,
    target_set: str | None = None,
    target_review: str | None = None,
    warnings_sha256: str | None = None,
    drift_facts_sha256: str | None = None,
    pooled_review_set_source: str | None = None,
    pooled_review_set_sha256: str | None = None,
) -> dict[str, Any]:
    warning_labels = [label_for_warning(labels, warning) for warning in selected]
    reviewed_labels = [label for label in warning_labels if label]
    type_distribution = Counter(str(warning.get("semantic_target_type") or warning.get("type")) for warning in selected)
    reviewed_type_distribution = Counter(
        str(warning.get("semantic_target_type") or warning.get("type"))
        for warning in selected
        if label_for_warning(labels, warning)
    )
    true_semantic = [warning for warning in selected if label_for_warning(labels, warning) == "TRUE_SEMANTIC_DRIFT"]
    true_wrapper = [warning for warning in selected if label_for_warning(labels, warning) == "TRUE_WRAPPER_FIX"]
    false_labels = [label for label in warning_labels if label and label not in TRUE_LABELS]
    non_wrapper_semantic = [
        warning
        for warning in true_semantic
        if not _has_wrapper_oracle(warning)
    ]
    false_taxonomy_rows = [
        warning
        for warning in selected
        if label_for_warning(labels, warning) in {"FALSE_POSITIVE", "BENIGN_DRIFT", "UNCLEAR"}
    ]
    false_taxonomy = Counter(_false_positive_taxonomy(warning, label_for_warning(labels, warning)) for warning in false_taxonomy_rows)
    false_taxonomy_examples = _taxonomy_examples(false_taxonomy_rows, labels)
    unclear_rate = round(sum(1 for label in reviewed_labels if label == "UNCLEAR") / len(reviewed_labels), 4) if reviewed_labels else 1.0
    semantic_examples_by_type = Counter(warning.get("semantic_target_type") for warning in true_semantic)
    per_type_quota = {
        category: type_distribution.get(category, 0) >= quota
        for category, quota in SEMANTIC_REVIEW_QUOTAS.items()
    }
    acceptance = {
        "minimum_semantic_review_candidates": 400,
        "minimum_reviewed_semantic_targets": 200,
        "minimum_true_semantic_drift": 8,
        "minimum_non_wrapper_semantic_true_positives": 5,
        "minimum_semantic_drift_types": 3,
        "semantic_review_candidates_passes": len(selected) >= 400,
        "semantic_review_candidate_type_quota_passes": all(per_type_quota.values()),
        "reviewed_semantic_targets_passes": len(reviewed_labels) >= 200,
        "true_semantic_drift_passes": len(true_semantic) >= 8,
        "non_wrapper_semantic_passes": len(non_wrapper_semantic) >= 5,
        "semantic_drift_type_passes": len({warning.get("semantic_target_type") for warning in true_semantic}) >= 3,
        "unclear_rate_passes": unclear_rate <= 0.05,
        "examples_per_semantic_type_passes": all(count >= 2 for count in semantic_examples_by_type.values()) if semantic_examples_by_type else False,
        "wrapper_fix_not_counted_as_semantic": all(label_for_warning(labels, warning) != "TRUE_WRAPPER_FIX" for warning in true_semantic),
        "false_positive_taxonomy_generated": bool(false_taxonomy),
        "per_type_quota": per_type_quota,
    }
    acceptance["minimum_passes"] = bool(
        acceptance["semantic_review_candidates_passes"]
        and acceptance["semantic_review_candidate_type_quota_passes"]
        and acceptance["reviewed_semantic_targets_passes"]
        and acceptance["true_semantic_drift_passes"]
        and acceptance["non_wrapper_semantic_passes"]
        and acceptance["semantic_drift_type_passes"]
        and acceptance["unclear_rate_passes"]
        and acceptance["examples_per_semantic_type_passes"]
        and acceptance["wrapper_fix_not_counted_as_semantic"]
        and acceptance["false_positive_taxonomy_generated"]
    )
    return {
        "warnings_source": warnings_source,
        "warnings_sha256": warnings_sha256,
        "drift_facts_source": drift_facts_source,
        "drift_facts_sha256": drift_facts_sha256,
        "pooled_review_set_source": pooled_review_set_source,
        "pooled_review_set_sha256": pooled_review_set_sha256,
        "review_sources": review_sources or [],
        "target_set": target_set,
        "target_review": target_review,
        "selection_policy": "label-blind semantic detector quotas over pre-adjudication pooled review candidates, promoted warnings, and drift facts; labels are joined only after target selection",
        "review_method": "binddrift-review adjudicated double-review labels reused from pooled/manual review artifacts; missing labels are not counted as reviewed",
        "semantic_review_candidates": len(selected),
        "candidates_reviewed": len(reviewed_labels),
        "reviewed_semantic_targets": len(reviewed_labels),
        "unclear_count": sum(1 for label in reviewed_labels if label == "UNCLEAR"),
        "unclear_rate": unclear_rate,
        "quota": dict(SEMANTIC_REVIEW_QUOTAS),
        "quota_shortages": shortages or {},
        "label_distribution": dict(Counter(label for label in warning_labels if label)),
        "type_distribution": dict(type_distribution),
        "reviewed_type_distribution": dict(reviewed_type_distribution),
        "true_semantic_drift_count": len(true_semantic),
        "true_wrapper_fix_count": len(true_wrapper),
        "non_wrapper_semantic_true_positives": len(non_wrapper_semantic),
        "semantic_drift_types": sorted({str(warning.get("semantic_target_type")) for warning in true_semantic}),
        "semantic_drift_type_count": len({str(warning.get("semantic_target_type")) for warning in true_semantic}),
        "examples_per_semantic_type": dict(semantic_examples_by_type),
        "false_positive_taxonomy": dict(false_taxonomy),
        "false_positive_taxonomy_allowed": sorted(M4_FALSE_POSITIVE_TAXONOMY | {"missing_evidence"}),
        "false_positive_taxonomy_examples": false_taxonomy_examples,
        "examples_not_used_as_case_studies": [_example_row(warning, labels) for warning in selected if label_for_warning(labels, warning) != "TRUE_SEMANTIC_DRIFT"][:10],
        "acceptance": acceptance,
        "claim_recommendation": (
            "semantic review targets may be reported as a secondary contribution"
            if acceptance["minimum_passes"]
            else "semantic drift claim must be downgraded to exploratory"
        ),
        "note": "TRUE_WRAPPER_FIX is reported separately and is not counted as TRUE_SEMANTIC_DRIFT.",
    }


def semantic_target_type(warning: dict[str, Any]) -> str:
    symbol = str((warning.get("c_side") or {}).get("symbol") or "").lower()
    warning_type = str(warning.get("type") or "")
    rust_side = warning.get("rust_side") or {}
    fact_source = str(warning.get("fact_source") or "")
    c_side_payload = json.dumps(warning.get("c_side") or {}, sort_keys=True).lower()
    evidence_payload = json.dumps(_semantic_detection_payload(warning), sort_keys=True).lower()
    if warning_type in {"FieldDrift", "LayoutDrift", "LayoutFieldDrift"} or fact_source == "layout_diff" or '"fields"' in c_side_payload:
        return "LayoutFieldDrift"
    if warning_type == "MacroConstDrift" or fact_source == "macro_diff":
        macro_category = _macro_semantic_target_type(symbol, c_side_payload, evidence_payload)
        if macro_category:
            return macro_category
    if "secctx" in symbol or "lsm_context" in evidence_payload:
        return "AllocationFreeDrift"
    if any(token in evidence_payload for token in ("null_return", "err_ptr_return", "is_err", "ptr_err", "option<", "result<")):
        return "NullabilityDrift"
    if any(token in symbol for token in ("err", "null", "ptr", "is_err")) or rust_side.get("error_mappings"):
        return "NullabilityDrift"
    if any(token in symbol for token in ("alloc", "free", "release", "request", "devm", "kfree")) or any(token in evidence_payload for token in ("alloc", "free", "drop impl", "owned pointer")):
        return "AllocationFreeDrift"
    if any(token in evidence_payload for token in ("refcount_get", "refcount_put", "clone", "drop", "lifetime")):
        return "OwnershipRefcountDrift"
    if any(token in symbol for token in ("refcount", "kref", "_get", "_put", "device", "drop")) or rust_side.get("lifetime_facts"):
        return "OwnershipRefcountDrift"
    if any(token in symbol for token in ("sleep", "gfp", "lock", "mutex", "wait", "queue", "work", "atomic")) or any(token in evidence_payload for token in ("may_sleep", "atomic context", "unsafe wrapper")):
        return "SleepabilityContextDrift"
    return ""


def _semantic_detection_payload(warning: dict[str, Any]) -> dict[str, Any]:
    rust_side = warning.get("rust_side") or {}
    allowed_rust_keys = (
        "uses",
        "safe_apis",
        "safety_comments",
        "error_mappings",
        "lifetime_facts",
        "exposure",
    )
    return {
        "c_side": warning.get("c_side") or {},
        "fact_source": warning.get("fact_source"),
        "type": warning.get("type"),
        "rust_side": {key: rust_side.get(key) for key in allowed_rust_keys if rust_side.get(key)},
    }


def _macro_semantic_target_type(symbol: str, c_payload: str, evidence_payload: str) -> str:
    if symbol.startswith("vm_"):
        if any(token in symbol for token in ("read", "write", "exec", "shared", "may")):
            return "LayoutFieldDrift"
        if any(token in symbol for token in ("account", "reserve", "huge", "merge")):
            return "AllocationFreeDrift"
        if any(token in symbol for token in ("copy", "dump", "expand", "fork", "dirty")):
            return "OwnershipRefcountDrift"
        return "SleepabilityContextDrift"
    if "wait" in symbol or any(token in evidence_payload for token in ("wait", "condvar", "atomic context", "may_sleep")):
        return "SleepabilityContextDrift"
    if "init_" in symbol or "flag" in c_payload:
        return "LayoutFieldDrift"
    return ""


def _semantic_candidate_priority(warning: dict[str, Any]) -> tuple[int, int, int, int, str]:
    rust_side = warning.get("rust_side") or {}
    c_level = str(warning.get("c_evidence_level") or "")
    oracle_rank = int(warning.get("oracle_blind_rank") or 1_000_000)
    return (
        0 if c_level == "c_source_diff" else 1,
        0 if rust_side.get("uses") or rust_side.get("safety_comments") or rust_side.get("safe_apis") else 1,
        0 if rust_side.get("error_mappings") or rust_side.get("lifetime_facts") or rust_side.get("safety_comments") else 1,
        oracle_rank,
        str((warning.get("c_side") or {}).get("symbol") or ""),
    )


def _load_review_rows(paths: list[Path]) -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    for path in paths:
        if not path or not path.exists():
            continue
        with path.open(newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                key = manual_review_row_key(row, uid_only=True)
                if not key:
                    continue
                if not row.get("adjudicated_label", "").strip():
                    continue
                rows.setdefault(key, {field: str(row.get(field, "") or "") for field in set(REVIEW_FIELDS) | set(row)})
    return rows


def _existing_review_paths(manifest: dict[str, Any]) -> list[Path]:
    candidates = [
        Path(manifest["resolved_paths"].get("pooled_review_labels", "")),
        Path(manifest["resolved_paths"]["manual_review"]),
    ]
    return [path for path in candidates if path.exists()]


def _write_review_csv(path: Path, selected: list[dict[str, Any]], review_rows: dict[str, dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=REVIEW_FIELDS, lineterminator="\n")
        writer.writeheader()
        for rank, warning in enumerate(selected, start=1):
            uid = str(warning.get("warning_uid") or "")
            review = review_rows.get(uid, {})
            writer.writerow(
                {
                    "warning_uid": uid,
                    "warning_id": warning.get("warning_id", ""),
                    "pair_id": warning.get("pair_id", ""),
                    "rank": rank,
                    "semantic_target_type": warning.get("semantic_target_type", ""),
                    "type": warning.get("type", ""),
                    "symbol": (warning.get("c_side") or {}).get("symbol", ""),
                    "oracle_blind_rank": warning.get("oracle_blind_rank", ""),
                    "oracle_blind_score": warning.get("oracle_blind_score", ""),
                    "ranker_source": review.get("ranker_source", ""),
                    "reviewer1_label": review.get("reviewer1_label", ""),
                    "reviewer1_notes": review.get("reviewer1_notes", ""),
                    "reviewer2_label": review.get("reviewer2_label", ""),
                    "reviewer2_notes": review.get("reviewer2_notes", ""),
                    "adjudicated_label": review.get("adjudicated_label", ""),
                    "adjudication_notes": review.get("adjudication_notes", ""),
                    "label_source": review.get("label_source", "manual_review.csv"),
                }
            )


def _has_wrapper_oracle(warning: dict[str, Any]) -> bool:
    evidence = list(warning.get("evidence_chain") or []) + list((warning.get("rust_side") or {}).get("oracle_hits") or [])
    return any(isinstance(item, dict) and item.get("oracle_type") == "wrapper_fix" for item in evidence)


def _false_positive_taxonomy(warning: dict[str, Any], label: str) -> str:
    symbol = str((warning.get("c_side") or {}).get("symbol") or "")
    warning_type = str(warning.get("type") or "")
    fact_source = str(warning.get("fact_source") or "")
    if label == "UNCLEAR":
        return "missing_evidence"
    if label == "BENIGN_DRIFT":
        return "real_c_drift_no_rust_contract_impact"
    if warning_type == "MacroConstDrift" or fact_source == "macro_diff" or symbol.isupper():
        return "macro_constant_over_prioritization"
    if warning_type in {"FieldDrift", "LayoutDrift", "LayoutFieldDrift"} or fact_source == "layout_diff":
        return "layout_ambiguity"
    if not _has_rust_reachability(warning):
        return "weak_rust_reachability"
    if warning.get("c_evidence_level") == "binding_only" or fact_source == "binding_diff":
        return "binding_only_or_generated_surface"
    return "real_c_drift_no_rust_contract_impact"


def _has_rust_reachability(warning: dict[str, Any]) -> bool:
    rust_side = warning.get("rust_side") or {}
    reasons = set(warning.get("promotion_reasons") or [])
    return bool(
        rust_side.get("uses")
        or rust_side.get("safe_apis")
        or "direct_binding_use" in reasons
        or "exposes_safe_api" in reasons
    )


def _taxonomy_examples(warnings: list[dict[str, Any]], labels: dict[str, str], *, limit_per_bucket: int = 3) -> dict[str, list[dict[str, Any]]]:
    examples: dict[str, list[dict[str, Any]]] = {}
    for warning in sorted(warnings, key=lambda row: (str(row.get("semantic_target_type") or ""), str(row.get("warning_uid") or ""))):
        label = label_for_warning(labels, warning)
        bucket = _false_positive_taxonomy(warning, label)
        rows = examples.setdefault(bucket, [])
        if len(rows) >= limit_per_bucket:
            continue
        rows.append(_example_row(warning, labels))
    return examples


def _example_row(warning: dict[str, Any], labels: dict[str, str]) -> dict[str, Any]:
    return {
        "warning_uid": warning.get("warning_uid"),
        "warning_id": warning.get("warning_id"),
        "pair_id": warning.get("pair_id"),
        "semantic_target_type": warning.get("semantic_target_type"),
        "type": warning.get("type"),
        "symbol": (warning.get("c_side") or {}).get("symbol"),
        "label": label_for_warning(labels, warning),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate BindDrift semantic target review artifacts.")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output-set")
    parser.add_argument("--output-review")
    parser.add_argument("--output-summary")
    args = parser.parse_args(argv)
    cfg = Config.from_args(repo_root=args.repo_root)
    result = generate_semantic_review_targets(
        cfg,
        output_set=Path(args.output_set).resolve() if args.output_set else None,
        output_review=Path(args.output_review).resolve() if args.output_review else None,
        output_summary=Path(args.output_summary).resolve() if args.output_summary else None,
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
