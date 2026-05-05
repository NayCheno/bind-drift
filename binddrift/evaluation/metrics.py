from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from binddrift.warnings import make_warning_uid


TRUE_LABELS = {"TRUE_BUILD_BREAKAGE", "TRUE_WRAPPER_FIX", "TRUE_SEMANTIC_DRIFT"}
FALSE_LABELS = {"BENIGN_DRIFT", "FALSE_POSITIVE", "UNCLEAR"}


def warning_label_key(warning_id: object, pair_id: object | None = None) -> str:
    if pair_id:
        return f"{pair_id}:{warning_id}"
    return str(warning_id)


def warning_key(warning: dict[str, Any]) -> str:
    if warning.get("warning_uid"):
        return str(warning["warning_uid"])
    return warning_label_key(warning.get("warning_id"), warning.get("pair_id"))


def label_for_warning(labels: dict[str, str], warning: dict[str, Any]) -> str:
    uid = str(warning.get("warning_uid") or make_warning_uid(warning))
    if uid in labels:
        return labels[uid]
    pair_key = warning_label_key(warning.get("warning_id"), warning.get("pair_id"))
    if pair_key in labels:
        return labels[pair_key]
    return labels.get(str(warning.get("warning_id")), "")


def manual_review_row_key(row: dict[str, str], uid_only: bool = False) -> str | None:
    warning_uid = row.get("warning_uid", "").strip()
    if warning_uid:
        return warning_uid
    if uid_only:
        return None
    warning_id = row.get("warning_id")
    if not warning_id:
        return None
    return warning_label_key(warning_id, row.get("pair_id", "").strip() or None)


def load_manual_labels(path: Path, uid_only: bool = False) -> dict[str, str]:
    if not path.exists():
        return {}
    with path.open(newline="", encoding="utf-8") as fh:
        labels: dict[str, str] = {}
        for row in csv.DictReader(fh):
            key = manual_review_row_key(row, uid_only=uid_only)
            if not key:
                continue
            label = row.get("adjudicated_label", "").strip() or row.get("label", "").strip()
            labels[key] = label
        return labels


def manual_review_agreement(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"double_labeled": 0, "agreements": 0, "agreement_rate": None}
    double_labeled = 0
    agreements = 0
    with path.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            first = row.get("reviewer1_label", "").strip()
            second = row.get("reviewer2_label", "").strip()
            if not first or not second:
                continue
            double_labeled += 1
            agreements += int(first == second)
    return {
        "double_labeled": double_labeled,
        "agreements": agreements,
        "agreement_rate": round(agreements / double_labeled, 4) if double_labeled else None,
    }


def precision_at_k(warnings: list[dict[str, Any]], labels: dict[str, str], k: int) -> float | None:
    labeled = [warning for warning in warnings[:k] if label_for_warning(labels, warning)]
    if not labeled:
        return None
    true_count = sum(1 for warning in labeled if label_for_warning(labels, warning) in TRUE_LABELS)
    return round(true_count / len(labeled), 4)


def _warning_symbol(warning: dict[str, Any]) -> str | None:
    symbol = warning.get("c_side", {}).get("symbol")
    return str(symbol) if symbol else None


def _round(value: float | None) -> float | None:
    return round(value, 4) if value is not None else None


def labeled_summary(warnings: list[dict[str, Any]], labels: dict[str, str], ks: tuple[int, ...] = (10, 50, 100)) -> dict[str, Any]:
    warning_labels = [label_for_warning(labels, warning) for warning in warnings]
    labeled_count = sum(1 for label in warning_labels if label)
    true_count = sum(1 for label in warning_labels if label in TRUE_LABELS)
    per_type: dict[str, dict[str, Any]] = {}
    by_type: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for warning in warnings:
        by_type[str(warning.get("type", "Unknown"))].append(warning)
    for drift_type, rows in sorted(by_type.items()):
        type_labeled = [warning for warning in rows if label_for_warning(labels, warning)]
        type_true = [warning for warning in type_labeled if label_for_warning(labels, warning) in TRUE_LABELS]
        per_type[drift_type] = {
            "warnings": len(rows),
            "labeled_warnings": len(type_labeled),
            "true_labeled_warnings": len(type_true),
            "precision": _round(len(type_true) / len(type_labeled)) if type_labeled else None,
        }
    return {
        "labeled_warnings": labeled_count,
        "true_labeled_warnings": true_count,
        "precision": round(true_count / labeled_count, 4) if labeled_count else None,
        "precision_at_k": {str(k): precision_at_k(warnings, labels, k) for k in ks},
        "label_distribution": dict(Counter(label for label in warning_labels if label)),
        "per_type": per_type,
        "unclear_warnings": sum(1 for label in warning_labels if label == "UNCLEAR"),
    }


def oracle_summary(warnings: list[dict[str, Any]], oracle_symbols: set[str], ks: tuple[int, ...] = (10, 50, 100)) -> dict[str, Any]:
    """Measure ranked warnings against a symbol-level oracle.

    The replay oracles available to BindDrift are usually mined at symbol
    granularity: a build log mentions `bindings::foo`, or a wrapper-fix commit
    touches `bindings::foo`. This helper reports ranking quality while keeping
    the denominator explicit.
    """

    ranked = [warning for warning in warnings if _warning_symbol(warning)]
    if not oracle_symbols:
        return {
            "oracle_symbols": 0,
            "matched_symbols": 0,
            "precision": None,
            "recall": None,
            "f1": None,
            "precision_at_k": {str(k): None for k in ks},
            "mrr": None,
        }

    true_indices = {
        index
        for index, warning in enumerate(ranked)
        if (_warning_symbol(warning) or "") in oracle_symbols
    }
    precision = len(true_indices) / len(ranked) if ranked else None
    matched_symbols = {
        _warning_symbol(warning)
        for warning in ranked
        if (_warning_symbol(warning) or "") in oracle_symbols
    }
    recall = len(matched_symbols) / len(oracle_symbols)
    f1 = (2 * precision * recall / (precision + recall)) if precision is not None and precision + recall > 0 else None
    p_at_k: dict[str, float | None] = {}
    for k in ks:
        top = ranked[:k]
        p_at_k[str(k)] = _round(sum(1 for warning in top if (_warning_symbol(warning) or "") in oracle_symbols) / len(top)) if top else None

    reciprocal_ranks: list[float] = []
    for symbol in sorted(oracle_symbols):
        for rank, warning in enumerate(ranked, start=1):
            if _warning_symbol(warning) == symbol:
                reciprocal_ranks.append(1 / rank)
                break
        else:
            reciprocal_ranks.append(0.0)

    return {
        "oracle_symbols": len(oracle_symbols),
        "matched_symbols": len(matched_symbols),
        "precision": _round(precision),
        "recall": _round(recall),
        "f1": _round(f1),
        "precision_at_k": p_at_k,
        "mrr": _round(sum(reciprocal_ranks) / len(reciprocal_ranks)),
    }
