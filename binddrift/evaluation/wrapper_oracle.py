from __future__ import annotations

import json
from datetime import datetime
from typing import Any

from .metrics import _round


FIX_KINDS = {
    "error_mapping",
    "nullability",
    "ownership",
    "layout",
    "signature",
    "allocation",
    "sleepability",
}

COMPATIBLE_WARNING_TYPES = {
    "SignatureDrift": {"signature", "error_mapping", "nullability", "ownership", "allocation", "sleepability"},
    "FieldDrift": {"layout", "signature", "ownership", "allocation"},
    "LayoutDrift": {"layout", "ownership", "allocation"},
    "MacroConstDrift": {"signature", "layout"},
    "ErrorDrift": {"error_mapping", "signature"},
    "NullabilityDrift": {"nullability", "error_mapping", "signature"},
    "OwnershipRefcountDrift": {"ownership"},
    "AllocationFreePairingDrift": {"allocation", "ownership"},
    "SleepabilityDrift": {"sleepability"},
}


def wrapper_fix_events_from_db(conn) -> list[dict[str, Any]]:
    return [
        {
            "commit": row["commit_id"],
            "date": row["date"],
            "subject": row["subject"],
            "changed_files": _json_list(row["changed_files"]),
            "matched_symbols": _json_list(row["matched_symbols"]),
            "likely_wrapper_fix": bool(row["likely_wrapper_fix"]),
        }
        for row in conn.execute(
            """
            SELECT commit_id, date, subject, changed_files, matched_symbols, likely_wrapper_fix
            FROM wrapper_fix_events
            WHERE likely_wrapper_fix=1
            """
        )
    ]


def wrapper_fix_events_from_warnings(warnings: list[dict[str, Any]]) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str]] = set()
    for warning in warnings:
        for hit in (warning.get("rust_side") or {}).get("oracle_hits") or []:
            if not isinstance(hit, dict) or hit.get("oracle_type") != "wrapper_fix":
                continue
            commit = str(hit.get("commit_id") or hit.get("commit") or "")
            subject = str(hit.get("subject") or "")
            key = (commit, subject, str(hit.get("matched_symbols") or ""))
            if key in seen:
                continue
            seen.add(key)
            events.append(
                {
                    "commit": commit,
                    "date": hit.get("date"),
                    "subject": subject,
                    "changed_files": _coerce_list(hit.get("changed_files")),
                    "matched_symbols": _coerce_list(hit.get("matched_symbols")),
                    "likely_wrapper_fix": True,
                }
            )
    return events


def version_dates_from_db(conn) -> dict[str, str]:
    return {
        str(row["version_id"]): str(row["date"])
        for row in conn.execute("SELECT version_id, date FROM versions WHERE date IS NOT NULL")
    }


def max_version_date(version_dates: dict[str, str]) -> str | None:
    return _max_date(version_dates.values())


def replay_head_date(warnings: list[dict[str, Any]], version_dates: dict[str, str]) -> str | None:
    new_versions = {str(warning.get("new_version")) for warning in warnings if warning.get("new_version")}
    head_versions = {version for version in new_versions if version.startswith("HEAD_")}
    scoped_versions = head_versions or new_versions
    return _max_date(version_dates[version] for version in scoped_versions if version in version_dates)


def typed_wrapper_oracle_rows(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str]] = set()
    for event in events:
        if not event.get("likely_wrapper_fix", True):
            continue
        commit = str(event.get("commit") or event.get("commit_id") or "")
        symbols = [str(symbol) for symbol in _coerce_list(event.get("matched_symbols")) if symbol]
        if not commit or not symbols:
            continue
        changed_files = [str(path) for path in _coerce_list(event.get("changed_files")) if path]
        fix_kinds = classify_fix_kinds(str(event.get("subject") or ""), changed_files, symbols)
        for symbol in symbols:
            for fix_kind in sorted(fix_kinds):
                key = (commit, symbol, fix_kind)
                if key in seen:
                    continue
                seen.add(key)
                rows.append(
                    {
                        "oracle_type": "wrapper_fix",
                        "commit": commit,
                        "date": event.get("date"),
                        "subject": event.get("subject"),
                        "symbol": symbol,
                        "fix_kind": fix_kind,
                        "rust_file": _first_rust_file(changed_files),
                        "diff_hunk": "",
                        "evidence_strength": evidence_strength(fix_kind, changed_files),
                        "changed_files": changed_files,
                        "oracle_id": f"{commit}:{symbol}:{fix_kind}",
                    }
                )
    return rows


def classify_fix_kinds(subject: str, changed_files: list[str], symbols: list[str]) -> set[str]:
    text = " ".join([subject, *changed_files, *symbols]).lower()
    kinds: set[str] = set()
    if any(needle in text for needle in ("error", "err_ptr", "errno", "errname", "result", "ptr_err", "is_err")):
        kinds.add("error_mapping")
    if any(needle in text for needle in ("null", "non-null", "nonnull", "option")):
        kinds.add("nullability")
    if any(needle in text for needle in ("refcount", "lifetime", "borrow", "own", "arc", "get_device", "put", "release")):
        kinds.add("ownership")
    if any(needle in text for needle in ("struct", "field", "layout", "queue_limits", "device context", "context")):
        kinds.add("layout")
    if any(needle in text for needle in ("alloc", "free", "dma", "kvec")):
        kinds.add("allocation")
    if any(needle in text for needle in ("sleep", "atomic", "blocking", "workqueue", "queue_work")):
        kinds.add("sleepability")
    if any(needle in text for needle in ("api", "binding", "bindings", "wrapper", "helper", "add", "convert", "remove", "signature", "args", "unified")):
        kinds.add("signature")
    return kinds or {"signature"}


def typed_wrapper_oracle_summary(
    warnings: list[dict[str, Any]],
    events: list[dict[str, Any]],
    version_dates: dict[str, str] | None = None,
    head_date: str | None = None,
    ks: tuple[int, ...] = (10, 50, 100),
    enforce_time: bool = True,
    time_window: str | None = None,
) -> dict[str, Any]:
    window = time_window or ("old_to_head" if enforce_time else "compatibility")
    typed_rows = typed_wrapper_oracle_rows(events)
    warning_symbols = {_warning_symbol(warning) for warning in warnings if _warning_symbol(warning)}
    candidate_rows = [row for row in typed_rows if row["symbol"] in warning_symbols]
    dates = version_dates or {}
    upper_bound = head_date or _max_date(dates.values())
    matched_warning_hits = [
        _typed_hits_for_warning(warning, candidate_rows, dates, upper_bound, window)
        for warning in warnings
    ]
    matched_indices = {index for index, hits in enumerate(matched_warning_hits) if hits}
    matched_oracle_ids = {
        hit["oracle_id"]
        for hits in matched_warning_hits
        for hit in hits
    }
    candidate_ids = {row["oracle_id"] for row in candidate_rows}
    precision = len(matched_indices) / len(warnings) if warnings else None
    recall = len(matched_oracle_ids) / len(candidate_ids) if candidate_ids else None
    f1 = (2 * precision * recall / (precision + recall)) if precision is not None and recall is not None and precision + recall > 0 else None
    p_at_k: dict[str, float | None] = {}
    for k in ks:
        top = matched_warning_hits[:k]
        p_at_k[str(k)] = _round(sum(1 for hits in top if hits) / len(top)) if top else None

    reciprocal_ranks: list[float] = []
    for oracle_id in sorted(candidate_ids):
        for rank, hits in enumerate(matched_warning_hits, start=1):
            if any(hit["oracle_id"] == oracle_id for hit in hits):
                reciprocal_ranks.append(1 / rank)
                break
        else:
            reciprocal_ranks.append(0.0)

    all_hits = [hit for hits in matched_warning_hits for hit in hits]
    return {
        "oracle_rows": len(candidate_ids),
        "global_oracle_rows": len({row["oracle_id"] for row in typed_rows}),
        "matched_oracle_rows": len(matched_oracle_ids),
        "matched_warnings": len(matched_indices),
        "precision": _round(precision),
        "recall": _round(recall),
        "f1": _round(f1),
        "precision_at_k": p_at_k,
        "mrr": _round(sum(reciprocal_ranks) / len(reciprocal_ranks)) if reciprocal_ranks else None,
        "enforce_time": window != "compatibility",
        "time_window": window,
        "head_date": upper_bound,
        "fix_kind_distribution": _count(row["fix_kind"] for row in candidate_rows),
        "matched_fix_kind_distribution": _count(hit["fix_kind"] for hit in all_hits),
        "time_relation_distribution": _count(hit["time_relation"] for hit in all_hits),
        "note": (
            "Typed wrapper oracle requires symbol and warning-type/fix-kind compatibility. "
            "The old_to_head time window accepts wrapper fixes after the warning old-version date "
            "and no later than the replay head date; compatibility mode is an auxiliary upper-bound."
        ),
    }


def _typed_hits_for_warning(
    warning: dict[str, Any],
    rows: list[dict[str, Any]],
    version_dates: dict[str, str],
    head_date: str | None,
    time_window: str,
) -> list[dict[str, Any]]:
    symbol = _warning_symbol(warning)
    drift_type = str(warning.get("type") or "")
    if not symbol:
        return []
    hits: list[dict[str, Any]] = []
    for row in rows:
        if row["symbol"] != symbol or not compatible_fix_kind(drift_type, row["fix_kind"]):
            continue
        time_relation = _time_relation(row.get("date"), warning, version_dates)
        if not _within_time_window(row.get("date"), warning, version_dates, head_date, time_window):
            continue
        hits.append({**row, "matched_warning_type": drift_type, "time_relation": time_relation})
    return hits


def compatible_fix_kind(warning_type: str, fix_kind: str) -> bool:
    return fix_kind in COMPATIBLE_WARNING_TYPES.get(warning_type, set())


def evidence_strength(fix_kind: str, changed_files: list[str]) -> str:
    rust_paths = [path for path in changed_files if path.startswith(("rust/kernel", "rust/helpers", "rust/bindings"))]
    if fix_kind in {"error_mapping", "nullability", "ownership", "allocation", "sleepability"} and rust_paths:
        return "strong"
    return "weak" if not rust_paths else "strong"


def wrapper_fix_in_time_window(
    commit_date: Any,
    warning: dict[str, Any],
    version_dates: dict[str, str],
    head_date: str | None = None,
    time_window: str = "old_to_head",
) -> bool:
    return _within_time_window(commit_date, warning, version_dates, head_date, time_window)


def _time_relation(commit_date: Any, warning: dict[str, Any], version_dates: dict[str, str]) -> str:
    date = _parse_date(commit_date)
    old_date = _parse_date(version_dates.get(str(warning.get("old_version"))))
    new_date = _parse_date(version_dates.get(str(warning.get("new_version"))))
    if not date or not old_date:
        return "unknown"
    if date <= old_date:
        return "before_drift"
    if new_date and date <= new_date:
        return "same_pair"
    return "after_drift"


def _within_time_window(
    commit_date: Any,
    warning: dict[str, Any],
    version_dates: dict[str, str],
    head_date: str | None,
    time_window: str,
) -> bool:
    if time_window == "compatibility":
        return True
    date = _parse_date(commit_date)
    old_date = _parse_date(version_dates.get(str(warning.get("old_version"))))
    if not date or not old_date or date <= old_date:
        return False
    if time_window == "old_to_new":
        upper = _parse_date(version_dates.get(str(warning.get("new_version")))) or _parse_date(head_date)
        return date <= upper if upper else True
    if time_window == "old_to_head":
        upper = _parse_date(head_date)
        if upper and upper > old_date:
            return date <= upper
        return True
    raise ValueError(f"unknown typed wrapper oracle time_window: {time_window}")


def _warning_symbol(warning: dict[str, Any]) -> str | None:
    symbol = (warning.get("c_side") or {}).get("symbol")
    return str(symbol) if symbol else None


def _json_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    try:
        decoded = json.loads(str(value))
    except json.JSONDecodeError:
        return []
    return decoded if isinstance(decoded, list) else []


def _coerce_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    return _json_list(value)


def _parse_date(value: Any) -> datetime | None:
    if value is None:
        return None
    text = str(value)
    if not text:
        return None
    try:
        return datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        return None


def _max_date(values) -> str | None:
    best_text: str | None = None
    best_date: datetime | None = None
    for value in values:
        parsed = _parse_date(value)
        if parsed is not None and (best_date is None or parsed > best_date):
            best_date = parsed
            best_text = str(value)
    return best_text


def _first_rust_file(changed_files: list[str]) -> str:
    for path in changed_files:
        if path.startswith(("rust/kernel", "rust/helpers", "rust/bindings")):
            return path
    return changed_files[0] if changed_files else ""


def _count(values) -> dict[str, int]:
    counts: dict[str, int] = {}
    for value in values:
        key = str(value)
        counts[key] = counts.get(key, 0) + 1
    return dict(sorted(counts.items()))
