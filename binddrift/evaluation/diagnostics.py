from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path
from typing import Any

from binddrift.evaluation.metrics import FALSE_LABELS, TRUE_LABELS, warning_label_key
from binddrift.warnings import read_warnings


FALSE_REASON_VALUES = {
    "BINDING_ONLY",
    "NO_RUST_USE",
    "SUBSTRING_MISMATCH",
    "ADDED_SYMBOL_NO_OLD_EVIDENCE",
    "PLACEHOLDER_STRUCT_FIELDS",
    "NO_C_SOURCE_DIFF",
    "BENIGN_CONTRACT_CHANGE",
    "WEAK_INDICATOR",
}

CSV_FIELDS = ["warning_id", "symbol", "type", "pair_id", "label", "false_reason", "required_fix"]


def diagnose_false_positives(
    manual_review: Path,
    warnings_jsonl: Path,
    output_dir: Path,
    dev_ratio: float = 0.7,
) -> dict[str, Any]:
    warnings = read_warnings(warnings_jsonl)
    warnings_by_key = _warnings_by_key(warnings)
    hard_negatives: list[dict[str, str]] = []
    true_positives: list[dict[str, str]] = []

    for row in _manual_rows(manual_review):
        label = _label(row)
        if not label:
            continue
        warning = warnings_by_key.get(warning_label_key(row.get("warning_id"), row.get("pair_id") or None))
        if not warning:
            warning = warnings_by_key.get(str(row.get("warning_id")))
        if label in TRUE_LABELS:
            true_positives.append(_csv_row(row, warning, label, "", ""))
        elif label in FALSE_LABELS:
            reason = _false_reason(row, warning, label)
            hard_negatives.append(_csv_row(row, warning, label, reason, _required_fix(reason)))

    output_dir.mkdir(parents=True, exist_ok=True)
    hard_path = output_dir / "hard_negatives.csv"
    true_path = output_dir / "true_positives.csv"
    _write_csv(hard_path, hard_negatives)
    _write_csv(true_path, true_positives)
    split = _split_rows(hard_negatives + true_positives, dev_ratio)
    false_counts = dict(Counter(row["false_reason"] for row in hard_negatives if row["false_reason"]))
    return {
        "manual_review": str(manual_review),
        "warnings": str(warnings_jsonl),
        "hard_negatives": str(hard_path),
        "true_positives": str(true_path),
        "hard_negative_rows": len(hard_negatives),
        "true_positive_rows": len(true_positives),
        "false_positive_reasons": false_counts,
        "split": split,
        "recommended_gate_changes": _recommended_gate_changes(false_counts),
    }


def _manual_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as fh:
        return [dict(row) for row in csv.DictReader(fh)]


def _warnings_by_key(warnings: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for warning in warnings:
        warning_id = warning.get("warning_id")
        if not warning_id:
            continue
        pair_id = warning.get("pair_id")
        out[warning_label_key(warning_id, pair_id)] = warning
        out.setdefault(str(warning_id), warning)
    return out


def _label(row: dict[str, str]) -> str:
    return (row.get("adjudicated_label") or row.get("label") or "").strip()


def _csv_row(
    review_row: dict[str, str],
    warning: dict[str, Any] | None,
    label: str,
    false_reason: str,
    required_fix: str,
) -> dict[str, str]:
    c_side = (warning or {}).get("c_side", {})
    return {
        "warning_id": review_row.get("warning_id", ""),
        "symbol": str(c_side.get("symbol") or review_row.get("symbol", "")),
        "type": str((warning or {}).get("type") or review_row.get("type", "")),
        "pair_id": review_row.get("pair_id", ""),
        "label": label,
        "false_reason": false_reason,
        "required_fix": required_fix,
    }


def _false_reason(row: dict[str, str], warning: dict[str, Any] | None, label: str) -> str:
    explicit = (row.get("false_reason") or "").strip().upper()
    if explicit in FALSE_REASON_VALUES:
        return explicit
    notes = " ".join(
        row.get(key, "")
        for key in ("adjudication_notes", "reviewer_notes", "reviewer1_notes", "reviewer2_notes")
    ).lower()
    if "substring" in notes or "mismatch" in notes:
        return "SUBSTRING_MISMATCH"
    if "no rust" in notes or "not used" in notes:
        return "NO_RUST_USE"
    if "placeholder" in notes:
        return "PLACEHOLDER_STRUCT_FIELDS"
    if "weak" in notes or "indicator" in notes:
        return "WEAK_INDICATOR"
    if "benign" in notes or label == "BENIGN_DRIFT":
        return "BENIGN_CONTRACT_CHANGE"
    if not warning:
        return "NO_RUST_USE"
    c_side = warning.get("c_side", {})
    demotions = set(warning.get("demotion_reasons") or [])
    if c_side.get("old") == "absent" and c_side.get("new") == "added":
        return "ADDED_SYMBOL_NO_OLD_EVIDENCE"
    if warning.get("c_evidence_level") == "binding_only" or "generated_binding_only" in demotions:
        return "BINDING_ONLY"
    if warning.get("c_evidence_level") != "c_source_diff" and warning.get("type") == "SignatureDrift":
        return "NO_C_SOURCE_DIFF"
    rust_side = warning.get("rust_side", {})
    has_rust_use = bool(
        rust_side.get("uses")
        or rust_side.get("safe_apis")
        or rust_side.get("safety_comments")
        or rust_side.get("error_mappings")
        or rust_side.get("lifetime_facts")
        or rust_side.get("oracle_hits")
    )
    if not has_rust_use:
        return "NO_RUST_USE"
    if warning.get("indicator_based"):
        return "WEAK_INDICATOR"
    return "BENIGN_CONTRACT_CHANGE"


def _required_fix(reason: str) -> str:
    return {
        "BINDING_ONLY": "keep as drift fact unless oracle evidence exists",
        "NO_RUST_USE": "require direct Rust use, safe API, contract, or oracle evidence",
        "SUBSTRING_MISMATCH": "use exact canonical symbol matching",
        "ADDED_SYMBOL_NO_OLD_EVIDENCE": "require old C evidence or oracle before promotion",
        "PLACEHOLDER_STRUCT_FIELDS": "ignore placeholder-only layout changes without Rust layout dependency",
        "NO_C_SOURCE_DIFF": "require C source diff for signature drift promotion",
        "BENIGN_CONTRACT_CHANGE": "lower ranking unless contract evidence indicates stale Rust assumptions",
        "WEAK_INDICATOR": "require changed indicator with sufficient confidence and Rust contract evidence",
    }.get(reason, "inspect gate and ranking evidence")


def _write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def _split_rows(rows: list[dict[str, str]], dev_ratio: float) -> dict[str, Any]:
    pairs = sorted({row["pair_id"] for row in rows if row.get("pair_id")})
    if len(pairs) >= 2:
        dev_count = max(1, min(len(pairs) - 1, round(len(pairs) * dev_ratio)))
        dev_pairs = pairs[:dev_count]
        test_pairs = pairs[dev_count:]
        return {
            "strategy": "pair_holdout",
            "dev_pairs": dev_pairs,
            "test_pairs": test_pairs,
            "dev_rows": sum(1 for row in rows if row.get("pair_id") in dev_pairs),
            "test_rows": sum(1 for row in rows if row.get("pair_id") in test_pairs),
        }
    midpoint = round(len(rows) * dev_ratio)
    return {
        "strategy": "row_holdout",
        "dev_rows": midpoint,
        "test_rows": max(0, len(rows) - midpoint),
    }


def _recommended_gate_changes(false_counts: dict[str, int]) -> list[str]:
    return [
        _required_fix(reason)
        for reason, count in sorted(false_counts.items())
        if count > 0
    ]


def summary_json(summary: dict[str, Any]) -> str:
    return json.dumps(summary, indent=2, sort_keys=True)
