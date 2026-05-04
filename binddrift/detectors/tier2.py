from __future__ import annotations

from collections import defaultdict
from typing import Any

from binddrift.config import Config
from binddrift.db import connect, initialize
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
    rows = conn.execute(
        """
        SELECT rust_file, line, text, nearby_api
        FROM rust_safety_comments
        WHERE version_id=? AND nearby_binding_symbol=?
        LIMIT 10
        """,
        (version, symbol),
    ).fetchall()
    return [dict(row) for row in rows]


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


def run_tier2(cfg: Config, old: str | None = None, new: str | None = None, append: bool = False) -> dict[str, Any]:
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
        changed = indicators - old_ind.get(symbol, set()) if selected_old else indicators
        exposure = _rust_exposure(conn, selected_new, symbol)
        if not exposure:
            continue
        for indicator in sorted(changed):
            drift_type = TYPE_MAP.get(indicator)
            if not drift_type:
                continue
            c_evidence = _evidence(conn, selected_new, symbol, indicator)
            rust_evidence = _rust_mapping(conn, selected_new, symbol)
            warnings.append(
                {
                    "warning_id": warning_id(idx),
                    "type": drift_type,
                    "risk": RISK_MAP[drift_type],
                    "score": 0.0,
                    "c_side": {
                        "symbol": symbol,
                        "indicator": indicator,
                        "old_version": selected_old,
                        "new_version": selected_new,
                        "evidence": c_evidence,
                    },
                    "rust_side": {
                        "binding": f"bindings::{symbol}",
                        "uses": exposure,
                        "safety_comments": rust_evidence,
                    },
                    "explanation": f"{symbol} has {indicator} C-side evidence and is used across a Rust unsafe boundary.",
                    "suggested_action": "Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.",
                    "confidence": max([item["confidence"] for item in c_evidence], default=0.5),
                    "indicator_based": True,
                    "not_a_bug_claim": True,
                }
            )
            idx += 1

    write_warnings(cfg, warnings)
    return {
        "warnings": len(warnings),
        "new_warnings": len(warnings) - len(existing),
        "warning_file": str(cfg.warnings_jsonl),
        "old_version": selected_old,
        "new_version": selected_new,
    }
