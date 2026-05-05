from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path
from typing import Any

from binddrift.evaluation.metrics import manual_review_row_key, warning_label_key
from binddrift.warnings import make_warning_uid, read_warnings


def _warning_keys(warning: dict[str, Any]) -> tuple[str, str, str]:
    uid = str(warning.get("warning_uid") or make_warning_uid(warning))
    pair_key = warning_label_key(warning.get("warning_id"), warning.get("pair_id"))
    legacy_key = str(warning.get("warning_id"))
    return uid, pair_key, legacy_key


def check_label_join(warnings_jsonl: Path, manual_review: Path) -> dict[str, Any]:
    warnings = read_warnings(warnings_jsonl)
    warning_keys_by_uid = {_warning_keys(warning)[0]: _warning_keys(warning) for warning in warnings}
    all_warning_keys = {key for keys in warning_keys_by_uid.values() for key in keys if key}
    review_rows: list[dict[str, str]] = []
    if manual_review.exists():
        with manual_review.open(newline="", encoding="utf-8") as fh:
            review_rows = list(csv.DictReader(fh))

    review_keys: set[str] = set()
    orphan_rows: list[dict[str, str]] = []
    label_distribution: Counter[str] = Counter()
    matched_review_rows = 0
    for index, row in enumerate(review_rows, start=1):
        key = manual_review_row_key(row)
        label = row.get("adjudicated_label", "").strip() or row.get("label", "").strip()
        if label:
            label_distribution[label] += 1
        if not key:
            orphan_rows.append({"row": str(index), "warning_id": row.get("warning_id", ""), "reason": "missing_join_key"})
            continue
        review_keys.add(key)
        if key in all_warning_keys:
            matched_review_rows += 1
        else:
            orphan_rows.append({"row": str(index), "join_key": key, "warning_id": row.get("warning_id", "")})

    unmatched = []
    for warning in warnings:
        keys = _warning_keys(warning)
        if not any(key in review_keys for key in keys):
            unmatched.append(
                {
                    "warning_uid": keys[0],
                    "pair_id": warning.get("pair_id"),
                    "warning_id": warning.get("warning_id"),
                    "type": warning.get("type"),
                    "symbol": (warning.get("c_side") or {}).get("symbol"),
                }
            )

    return {
        "warnings": len(warnings),
        "review_rows": len(review_rows),
        "matched_review_rows": matched_review_rows,
        "unmatched_warnings": unmatched,
        "orphan_review_rows": orphan_rows,
        "label_distribution": dict(sorted(label_distribution.items())),
    }
