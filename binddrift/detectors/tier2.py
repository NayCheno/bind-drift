from __future__ import annotations

from collections import defaultdict
from typing import Any

from binddrift.config import Config
from binddrift.db import connect, initialize, upsert_many
from binddrift.kernel import default_version_id
from binddrift.warnings import read_warnings, warning_id, write_warnings


TYPE_MAP = {
    "NULL_RETURN": "NullabilityDrift",
    "ERR_PTR_RETURN": "NullabilityDrift",
    "ERROR_CODE": "ErrorDrift",
    "REFCOUNT_GET": "OwnershipRefcountDrift",
    "REFCOUNT_PUT": "OwnershipRefcountDrift",
    "ALLOC": "AllocationFreePairingDrift",
    "FREE": "AllocationFreePairingDrift",
    "MAY_SLEEP": "SleepabilityDrift",
}


RISK_MAP = {
    "NullabilityDrift": "High",
    "ErrorDrift": "Medium",
    "OwnershipRefcountDrift": "High",
    "AllocationFreePairingDrift": "High",
    "SleepabilityDrift": "Medium",
}


def _rust_exposure(conn, version: str, symbol: str) -> list[dict[str, Any]]:
    rows = conn.execute(
        """
        SELECT rust_file, line, enclosing_function, enclosing_impl, enclosing_unsafe_block
        FROM rust_binding_uses
        WHERE version_id=? AND binding_symbol=?
        LIMIT 20
        """,
        (version, symbol),
    ).fetchall()
    return [dict(row) for row in rows]


def _rust_mapping(conn, version: str, symbol: str) -> list[dict[str, Any]]:
    comments = conn.execute(
        """
        SELECT rust_file, line, text, nearby_api
        FROM rust_safety_comments
        WHERE version_id=? AND nearby_binding_symbol=?
        LIMIT 10
        """,
        (version, symbol),
    ).fetchall()
    mappings = conn.execute(
        """
        SELECT rust_file, line, mapping_type AS text, nearby_api
        FROM rust_error_mappings
        WHERE version_id=? AND nearby_binding_symbol=?
        LIMIT 20
        """,
        (version, symbol),
    ).fetchall()
    return [dict(row) for row in comments] + [dict(row) for row in mappings]


def _rust_lifetime(conn, version: str, symbol: str) -> list[dict[str, Any]]:
    rows = conn.execute(
        """
        SELECT rust_file, line, fact_type, rust_type, evidence_text
        FROM rust_lifetime_facts
        WHERE version_id=? AND uses_bindings LIKE ?
        LIMIT 20
        """,
        (version, f'%"{symbol}"%'),
    ).fetchall()
    facts = [dict(row) for row in rows]
    if facts:
        return facts
    use_rows = conn.execute(
        """
        SELECT rust_file, line, enclosing_function, enclosing_impl
        FROM rust_binding_uses
        WHERE version_id=? AND binding_symbol=?
        LIMIT 20
        """,
        (version, symbol),
    ).fetchall()
    for row in use_rows:
        function = (row["enclosing_function"] or "").lower()
        if any(needle in function for needle in ("drop", "clone", "inc_ref", "dec_ref", "get", "put", "new", "free", "release")):
            facts.append(
                {
                    "rust_file": row["rust_file"],
                    "line": row["line"],
                    "fact_type": "LIFETIME_NAMING_PATTERN",
                    "rust_type": row["enclosing_impl"],
                    "evidence_text": row["enclosing_function"],
                }
            )
    return facts


def _indicators(conn, version: str) -> dict[str, set[str]]:
    out: dict[str, set[str]] = defaultdict(set)
    for row in conn.execute("SELECT c_symbol, indicator_type FROM c_behavior_indicators WHERE version_id=?", (version,)):
        out[row["c_symbol"]].add(row["indicator_type"])
    return out


def _evidence(conn, version: str, symbol: str, indicator_type: str) -> list[dict[str, Any]]:
    rows = conn.execute(
        """
        SELECT evidence_file, evidence_line, evidence_text, confidence
        FROM c_behavior_indicators
        WHERE version_id=? AND c_symbol=? AND indicator_type=?
        LIMIT 5
        """,
        (version, symbol, indicator_type),
    ).fetchall()
    return [dict(row) for row in rows]


def _drift_type(indicator: str, old_set: set[str], new_set: set[str]) -> str | None:
    if indicator in {"NULL_RETURN", "ERR_PTR_RETURN"}:
        return "NullabilityDrift"
    if indicator == "ERROR_CODE":
        return "ErrorDrift"
    if indicator in {"REFCOUNT_GET", "REFCOUNT_PUT"}:
        return "OwnershipRefcountDrift"
    if indicator in {"ALLOC", "FREE"}:
        return "AllocationFreePairingDrift"
    if indicator == "MAY_SLEEP":
        return "SleepabilityDrift"
    return TYPE_MAP.get(indicator)


def _event(warning: dict[str, Any]) -> dict[str, Any]:
    return {
        "event_id": f"{warning.get('pair_id')}:{warning['warning_id']}" if warning.get("pair_id") else warning["warning_id"],
        "run_id": warning.get("run_id"),
        "pair_id": warning.get("pair_id"),
        "old_version": warning["c_side"].get("old_version"),
        "new_version": warning["c_side"]["new_version"],
        "drift_type": warning["type"],
        "symbol": warning["c_side"]["symbol"],
        "old_value": ",".join(warning["c_side"].get("old_indicators", [])),
        "new_value": ",".join(warning["c_side"].get("new_indicators", [])),
        "evidence": str(warning.get("evidence_chain", [])),
    }


def run_tier2(cfg: Config, old: str | None = None, new: str | None = None, append: bool = False) -> dict[str, Any]:
    return run_tier2_with_context(cfg, old=old, new=new, append=append)


def run_tier2_with_context(
    cfg: Config,
    old: str | None = None,
    new: str | None = None,
    append: bool = False,
    run_id: str | None = None,
    pair_id: str | None = None,
) -> dict[str, Any]:
    conn = connect(cfg.database)
    initialize(conn)
    selected_new = new or default_version_id(cfg)
    selected_old = old
    old_ind = _indicators(conn, selected_old) if selected_old else {}
    new_ind = _indicators(conn, selected_new)
    existing = read_warnings(cfg.warnings_jsonl) if append else []
    warnings = list(existing)
    idx = len(warnings) + 1

    for symbol, indicators in sorted(new_ind.items()):
        if symbol == "<file>":
            continue
        old_set = old_ind.get(symbol, set())
        changed = indicators - old_set if selected_old else indicators
        exposure = _rust_exposure(conn, selected_new, symbol)
        if not exposure:
            continue
        for indicator in sorted(changed):
            drift_type = _drift_type(indicator, old_set, indicators)
            if not drift_type:
                continue
            c_evidence = _evidence(conn, selected_new, symbol, indicator)
            rust_evidence = _rust_mapping(conn, selected_new, symbol)
            lifetime_evidence = _rust_lifetime(conn, selected_new, symbol)
            if drift_type in {"NullabilityDrift", "ErrorDrift"} and not rust_evidence:
                continue
            if drift_type in {"OwnershipRefcountDrift", "AllocationFreePairingDrift"} and not lifetime_evidence:
                continue
            warnings.append(
                {
                    "warning_id": warning_id(idx),
                    "run_id": run_id,
                    "pair_id": pair_id,
                    "old_version": selected_old,
                    "new_version": selected_new,
                    "type": drift_type,
                    "risk": RISK_MAP[drift_type],
                    "score": 0.0,
                    "c_side": {
                        "symbol": symbol,
                        "indicator": indicator,
                        "old_indicators": sorted(old_set),
                        "new_indicators": sorted(indicators),
                        "old_version": selected_old,
                        "new_version": selected_new,
                        "evidence": c_evidence,
                    },
                    "rust_side": {
                        "binding": f"bindings::{symbol}",
                        "uses": exposure,
                        "safety_comments": rust_evidence,
                        "lifetime_facts": lifetime_evidence,
                    },
                    "evidence_chain": c_evidence + rust_evidence + lifetime_evidence,
                    "explanation": f"{symbol} has {indicator} C-side evidence and is used across a Rust unsafe boundary.",
                    "suggested_action": "Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.",
                    "confidence": max([item["confidence"] for item in c_evidence], default=0.5),
                    "indicator_based": True,
                    "not_a_bug_claim": True,
                }
            )
            idx += 1

    write_warnings(cfg, warnings)
    new_warning_slice = warnings[len(existing) :]
    upsert_many(conn, "drift_events", [_event(warning) for warning in new_warning_slice])
    return {
        "warnings": len(warnings),
        "new_warnings": len(warnings) - len(existing),
        "warning_file": str(cfg.warnings_jsonl),
        "old_version": selected_old,
        "new_version": selected_new,
    }
