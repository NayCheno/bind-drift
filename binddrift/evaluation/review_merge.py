from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path
from typing import Any

from binddrift.artifact_paths import sanitize_local_paths
from binddrift.config import Config
from binddrift.evaluation.metrics import TRUE_LABELS, labeled_summary, load_manual_labels, manual_review_agreement
from binddrift.evaluation.label_join import check_label_join
from binddrift.warnings import read_warnings


REVIEW_FIELDS = [
    "reviewer1_label",
    "reviewer1_notes",
    "reviewer2_label",
    "reviewer2_notes",
    "adjudicated_label",
    "adjudication_notes",
    "true_reason",
    "false_reason",
]
LEGACY_FIELDS = {"label", "reviewer_notes"}


TRUE_REASON_BY_LABEL = {
    "TRUE_BUILD_BREAKAGE": "BUILD_LOG_MATCH",
    "TRUE_WRAPPER_FIX": "WRAPPER_FIX_COMMIT_MATCH",
}


def merge_manual_review(
    run_dir: Path,
    warnings_jsonl: Path | None = None,
    aggregate_review: Path | None = None,
    override_jsonl: Path | None = None,
    cfg: Config | None = None,
) -> dict[str, Any]:
    """Merge pair-level review rows into the canonical replay review CSV."""

    run_dir = run_dir.resolve()
    warnings_jsonl = (warnings_jsonl or run_dir / "warnings.jsonl").resolve()
    aggregate_review = (aggregate_review or run_dir / "manual_review.csv").resolve()
    warnings = read_warnings(warnings_jsonl)
    warning_keys = {(warning.get("pair_id"), warning.get("warning_id")) for warning in warnings}
    pair_rows = _load_pair_review_rows(run_dir)
    override_rows = _load_override_rows(override_jsonl) if override_jsonl else {}
    fieldnames, aggregate_rows = _load_aggregate_rows(aggregate_review)

    updated = 0
    missing_sources: list[dict[str, str]] = []
    for row in aggregate_rows:
        key = (row.get("pair_id"), row.get("warning_id"))
        source = pair_rows.get(key)
        override = override_rows.get(key)
        if source is None and override is None:
            missing_sources.append({"pair_id": str(key[0]), "warning_id": str(key[1])})
            continue
        before = {field: row.get(field, "") for field in REVIEW_FIELDS}
        if source is not None:
            _copy_review_fields(row, source)
        if override is not None:
            _copy_review_fields(row, override)
        _fill_reason_codes(row, _warning_by_key(warnings).get(key))
        for field in LEGACY_FIELDS:
            row[field] = ""
        after = {field: row.get(field, "") for field in REVIEW_FIELDS}
        if after != before:
            updated += 1

    _write_csv(aggregate_review, fieldnames, aggregate_rows)
    labels = load_manual_labels(aggregate_review, uid_only=True)
    agreement = manual_review_agreement(aggregate_review)
    label_join = check_label_join(warnings_jsonl, aggregate_review)
    metrics = labeled_summary(warnings, labels)
    labels_only = [label for label in labels.values() if label]
    acceptance = _acceptance(metrics, agreement, len(warnings), labels_only)
    result = {
        "run_dir": str(run_dir),
        "warnings": len(warnings),
        "review_rows": len(aggregate_rows),
        "top_warning_rows": sum(1 for row in aggregate_rows if (row.get("pair_id"), row.get("warning_id")) in warning_keys),
        "updated_rows": updated,
        "missing_sources": missing_sources,
        "override_rows": len(override_rows),
        "label_distribution": dict(Counter(labels_only)),
        "true_labeled_warnings": metrics["true_labeled_warnings"],
        "agreement": agreement,
        "manual_review": metrics,
        "label_join": label_join,
        "acceptance": acceptance,
        "manual_review_csv": str(aggregate_review),
    }
    report = run_dir / "review_artifacts" / "aggregate_review_merge_summary.json"
    report.parent.mkdir(parents=True, exist_ok=True)
    artifact_result = sanitize_local_paths(result, cfg) if cfg else result
    report.write_text(json.dumps(artifact_result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


def _load_pair_review_rows(run_dir: Path) -> dict[tuple[str | None, str | None], dict[str, str]]:
    rows: dict[tuple[str | None, str | None], dict[str, str]] = {}
    for path in sorted(run_dir.glob("*/manual_review.csv")):
        with path.open(newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                key = (row.get("pair_id"), row.get("warning_id"))
                if key[0] and key[1]:
                    rows[key] = row
    return rows


def _load_override_rows(path: Path) -> dict[tuple[str | None, str | None], dict[str, str]]:
    rows: dict[tuple[str | None, str | None], dict[str, str]] = {}
    if not path.exists():
        return rows
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            raw = json.loads(line)
            row = {str(key): "" if value is None else str(value) for key, value in raw.items()}
            key = (row.get("pair_id"), row.get("warning_id"))
            if key[0] and key[1]:
                rows[key] = row
    return rows


def _load_aggregate_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)
    for field in REVIEW_FIELDS:
        if field not in fieldnames:
            fieldnames.append(field)
            for row in rows:
                row[field] = ""
    for field in LEGACY_FIELDS:
        if field not in fieldnames:
            fieldnames.append(field)
            for row in rows:
                row[field] = ""
    return fieldnames, rows


def _copy_review_fields(target: dict[str, str], source: dict[str, str]) -> None:
    for field in REVIEW_FIELDS:
        value = (source.get(field) or "").strip()
        if value:
            target[field] = value


def _warning_by_key(warnings: list[dict[str, Any]]) -> dict[tuple[Any, Any], dict[str, Any]]:
    return {(warning.get("pair_id"), warning.get("warning_id")): warning for warning in warnings}


def _fill_reason_codes(row: dict[str, str], warning: dict[str, Any] | None) -> None:
    label = (row.get("adjudicated_label") or "").strip()
    if not label:
        return
    if label in TRUE_LABELS:
        row["true_reason"] = _true_reason(label, warning)
        row["false_reason"] = ""
    else:
        row["false_reason"] = _false_reason(label, warning, row)
        row["true_reason"] = ""


def _true_reason(label: str, warning: dict[str, Any] | None) -> str:
    if label in TRUE_REASON_BY_LABEL:
        return TRUE_REASON_BY_LABEL[label]
    if not warning:
        return "CONTRACT_CHANGE_REACHES_SAFE_API"
    drift_type = str(warning.get("type") or "")
    rust_side = warning.get("rust_side") or {}
    if drift_type == "NullabilityDrift":
        return "NULLABILITY_MAPPING_STALE"
    if drift_type in {"OwnershipRefcountDrift", "AllocationFreePairingDrift"} or rust_side.get("lifetime_facts"):
        return "OWNERSHIP_LIFETIME_STALE"
    if drift_type == "SleepabilityDrift":
        return "SLEEPABILITY_CONTEXT_STALE"
    if drift_type == "ErrorDrift" or rust_side.get("error_mappings"):
        return "ERROR_MAPPING_STALE"
    return "CONTRACT_CHANGE_REACHES_SAFE_API"


def _false_reason(label: str, warning: dict[str, Any] | None, row: dict[str, str]) -> str:
    if label == "UNCLEAR":
        return "INSUFFICIENT_EVIDENCE"
    notes = " ".join(
        (row.get(field) or "").lower()
        for field in ("reviewer1_notes", "reviewer2_notes", "adjudication_notes")
    )
    if "mismatch" in notes or "wrong symbol" in notes:
        return "MISMATCHED_SYMBOL"
    if "parser" in notes or "artifact" in notes or "mismapped" in notes:
        return "EXTRACTOR_ERROR"
    if warning:
        if warning.get("old_version") is None or warning.get("pair_id") is None:
            return "NO_VERSION_CHANGE"
        rust_side = warning.get("rust_side") or {}
        if not any(
            rust_side.get(key)
            for key in ("uses", "safe_apis", "safety_comments", "error_mappings", "lifetime_facts", "oracle_hits")
        ):
            return "NO_RUST_IMPACT"
        if warning.get("c_evidence_level") == "binding_only":
            return "BINDING_ONLY"
        if warning.get("indicator_based"):
            return "WEAK_INDICATOR"
    if label == "BENIGN_DRIFT":
        return "BENIGN_CONTRACT_CHANGE"
    return "INSUFFICIENT_EVIDENCE"


def _acceptance(
    metrics: dict[str, Any],
    agreement: dict[str, Any],
    warning_count: int,
    labels: list[str],
) -> dict[str, Any]:
    unclear = sum(1 for label in labels if label == "UNCLEAR")
    unclear_rate = round(unclear / len(labels), 4) if labels else None
    checks = {
        "reviewed_warnings_ge_50": metrics["labeled_warnings"] >= 50,
        "double_labeled_ge_50": agreement["double_labeled"] >= 50,
        "agreement_rate_ge_075": (agreement["agreement_rate"] or 0) >= 0.75,
        "unclear_le_30pct": unclear_rate is not None and unclear_rate <= 0.30,
        "true_labeled_warnings_ge_5": metrics["true_labeled_warnings"] >= 5,
        "all_top_warnings_labeled": metrics["labeled_warnings"] == warning_count,
        "manual_precision_at_10_ge_030": (metrics["precision_at_k"].get("10") or 0) >= 0.30,
        "manual_precision_at_50_ge_015": (metrics["precision_at_k"].get("50") or 0) >= 0.15,
        "manual_precision_at_100_ge_010": (metrics["precision_at_k"].get("100") or 0) >= 0.10,
    }
    return {"passed": all(checks.values()), "checks": checks, "unclear_rate": unclear_rate}


def _write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})
