from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from binddrift.artifact_paths import sanitize_local_paths
from binddrift.config import Config
from binddrift.evaluation.metrics import TRUE_LABELS, label_for_warning, load_manual_labels, manual_review_row_key
from binddrift.ranking.oracle_blind_scorer import rank_warnings_oracle_blind
from binddrift.run_manifest import canonical_run_dir, repo_relative, sha256_file, validate_run_manifest
from binddrift.warnings import read_warnings, write_jsonl


SEMANTIC_REVIEW_QUOTAS = {
    "NullabilityDrift": 20,
    "OwnershipRefcountDrift": 20,
    "AllocationFreeDrift": 20,
    "SleepabilityContextDrift": 20,
    "LayoutFieldDrift": 20,
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
    output_set = output_set or run_dir / "semantic_target_review_set.jsonl"
    output_review = output_review or run_dir / "semantic_target_review.csv"
    output_summary = output_summary or cfg.repo_root / "paper/tables/semantic_drift_review_summary.json"

    warnings = read_warnings(warnings_path)
    review_rows = _load_review_rows(
        [
            Path(manifest["resolved_paths"].get("pooled_review_labels", "")),
            Path(manifest["resolved_paths"]["manual_review"]),
        ]
    )
    labels = {key: row.get("adjudicated_label", "") for key, row in review_rows.items()}
    selected, shortages = select_semantic_targets(warnings, review_rows)
    selected = [sanitize_local_paths(row, cfg) for row in selected]

    output_set.parent.mkdir(parents=True, exist_ok=True)
    write_jsonl(output_set, selected)
    output_review.parent.mkdir(parents=True, exist_ok=True)
    _write_review_csv(output_review, selected, review_rows)

    summary = build_semantic_review_summary(
        selected,
        labels,
        shortages=shortages,
        warnings_source=repo_relative(cfg, warnings_path),
        review_sources=[repo_relative(cfg, path) for path in _existing_review_paths(manifest)],
        target_set=repo_relative(cfg, output_set),
        target_review=repo_relative(cfg, output_review),
        warnings_sha256=sha256_file(warnings_path),
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
    review_rows: dict[str, dict[str, str]],
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
        category = semantic_target_type(warning)
        if not category:
            continue
        key = str(warning.get("warning_uid") or "")
        if key not in review_rows:
            continue
        by_category[category].append(warning)

    for category, quota in quotas.items():
        candidates = by_category.get(category, [])
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
            shortages[category] = f"only {category_count} adjudicated labeled candidates available for quota {quota}"

    return selected, shortages


def build_semantic_review_summary(
    selected: list[dict[str, Any]],
    labels: dict[str, str],
    *,
    shortages: dict[str, str] | None = None,
    warnings_source: str | None = None,
    review_sources: list[str] | None = None,
    target_set: str | None = None,
    target_review: str | None = None,
    warnings_sha256: str | None = None,
) -> dict[str, Any]:
    warning_labels = [label_for_warning(labels, warning) for warning in selected]
    type_distribution = Counter(str(warning.get("semantic_target_type") or warning.get("type")) for warning in selected)
    true_semantic = [warning for warning in selected if label_for_warning(labels, warning) == "TRUE_SEMANTIC_DRIFT"]
    true_wrapper = [warning for warning in selected if label_for_warning(labels, warning) == "TRUE_WRAPPER_FIX"]
    false_labels = [label for label in warning_labels if label and label not in TRUE_LABELS]
    non_wrapper_semantic = [
        warning
        for warning in true_semantic
        if not _has_wrapper_oracle(warning)
    ]
    false_taxonomy = Counter(_false_positive_taxonomy(warning, label_for_warning(labels, warning)) for warning in selected if label_for_warning(labels, warning) in {"FALSE_POSITIVE", "BENIGN_DRIFT", "UNCLEAR"})
    acceptance = {
        "minimum_true_semantic_drift": 8,
        "minimum_non_wrapper_semantic_true_positives": 5,
        "minimum_semantic_drift_types": 3,
        "true_semantic_drift_passes": len(true_semantic) >= 8,
        "non_wrapper_semantic_passes": len(non_wrapper_semantic) >= 5,
        "semantic_drift_type_passes": len({warning.get("semantic_target_type") for warning in true_semantic}) >= 3,
    }
    acceptance["minimum_passes"] = bool(
        acceptance["true_semantic_drift_passes"]
        and acceptance["non_wrapper_semantic_passes"]
        and acceptance["semantic_drift_type_passes"]
    )
    return {
        "warnings_source": warnings_source,
        "warnings_sha256": warnings_sha256,
        "review_sources": review_sources or [],
        "target_set": target_set,
        "target_review": target_review,
        "review_method": "adjudicated double-review labels reused from pooled/manual review artifacts; missing labels are not counted as reviewed",
        "candidates_reviewed": len(selected),
        "quota": dict(SEMANTIC_REVIEW_QUOTAS),
        "quota_shortages": shortages or {},
        "label_distribution": dict(Counter(label for label in warning_labels if label)),
        "type_distribution": dict(type_distribution),
        "true_semantic_drift_count": len(true_semantic),
        "true_wrapper_fix_count": len(true_wrapper),
        "non_wrapper_semantic_true_positives": len(non_wrapper_semantic),
        "semantic_drift_types": sorted({str(warning.get("semantic_target_type")) for warning in true_semantic}),
        "semantic_drift_type_count": len({str(warning.get("semantic_target_type")) for warning in true_semantic}),
        "false_positive_taxonomy": dict(false_taxonomy),
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
    if warning_type in {"FieldDrift", "LayoutDrift", "LayoutFieldDrift"} or fact_source == "layout_diff" or '"fields"' in c_side_payload:
        return "LayoutFieldDrift"
    if any(token in symbol for token in ("err", "null", "ptr", "is_err")) or rust_side.get("error_mappings"):
        return "NullabilityDrift"
    if any(token in symbol for token in ("ref", "kref", "get", "put", "device", "drop")) or rust_side.get("lifetime_facts"):
        return "OwnershipRefcountDrift"
    if any(token in symbol for token in ("alloc", "free", "release", "request", "devm", "kfree")):
        return "AllocationFreeDrift"
    if any(token in symbol for token in ("sleep", "gfp", "lock", "mutex", "queue", "work", "atomic")):
        return "SleepabilityContextDrift"
    return ""


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
                rows[key] = {field: str(row.get(field, "") or "") for field in set(REVIEW_FIELDS) | set(row)}
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
    if label == "UNCLEAR":
        return "missing_evidence"
    if label == "BENIGN_DRIFT":
        return "real_drift_without_rust_contract_impact"
    if warning.get("c_evidence_level") == "binding_only":
        return "binding_only_or_generated_surface"
    return "unsupported_or_mismapped_contract"


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
