from __future__ import annotations

import csv
from pathlib import Path
from typing import Any


TRUE_LABELS = {"TRUE_BUILD_BREAKAGE", "TRUE_WRAPPER_FIX", "TRUE_SEMANTIC_DRIFT"}


def load_manual_labels(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    with path.open(newline="", encoding="utf-8") as fh:
        return {row["warning_id"]: row.get("label", "").strip() for row in csv.DictReader(fh) if row.get("warning_id")}


def precision_at_k(warnings: list[dict[str, Any]], labels: dict[str, str], k: int) -> float | None:
    labeled = [warning for warning in warnings[:k] if labels.get(str(warning.get("warning_id")))]
    if not labeled:
        return None
    true_count = sum(1 for warning in labeled if labels.get(str(warning.get("warning_id"))) in TRUE_LABELS)
    return round(true_count / len(labeled), 4)


def labeled_summary(warnings: list[dict[str, Any]], labels: dict[str, str], ks: tuple[int, ...] = (10, 50, 100)) -> dict[str, Any]:
    labeled_count = sum(1 for warning in warnings if labels.get(str(warning.get("warning_id"))))
    true_count = sum(1 for warning in warnings if labels.get(str(warning.get("warning_id"))) in TRUE_LABELS)
    return {
        "labeled_warnings": labeled_count,
        "true_labeled_warnings": true_count,
        "precision": round(true_count / labeled_count, 4) if labeled_count else None,
        "precision_at_k": {str(k): precision_at_k(warnings, labels, k) for k in ks},
    }
