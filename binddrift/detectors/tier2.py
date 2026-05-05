from __future__ import annotations

from collections import defaultdict
from typing import Any

from binddrift.config import Config
from binddrift.db import connect, initialize, upsert_many
from binddrift.evidence.impact import compute_rust_impact
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
    if not selected_old:
        existing = read_warnings(cfg.warnings_jsonl) if append else []
        write_warnings(cfg, existing)
        return {
            "warnings": len(existing),
            "new_warnings": 0,
            "warning_file": str(cfg.warnings_jsonl),
            "old_version": selected_old,
            "new_version": selected_new,
            "status": "need_old_version",
        }
    old_ind = _indicators(conn, selected_old) if selected_old else {}
    new_ind = _indicators(conn, selected_new)
    existing = read_warnings(cfg.warnings_jsonl) if append else []
    warnings = list(existing)
    idx = len(warnings) + 1

    for symbol, indicators in sorted(new_ind.items()):
        if symbol == "<file>":
            continue
        if selected_old and symbol not in old_ind:
            continue
        old_set = old_ind.get(symbol, set())
        changed = indicators - old_set if selected_old else indicators
        for indicator in sorted(changed):
            drift_type = _drift_type(indicator, old_set, indicators)
            if not drift_type:
                continue
            impact = compute_rust_impact(conn, selected_new, symbol, drift_type, pair_id=pair_id)
            if not impact["eligible"]:
                continue
            c_evidence = _evidence(conn, selected_new, symbol, indicator)
            rust_evidence = impact["safety_comments"] + impact["error_mappings"]
            lifetime_evidence = impact["lifetime_facts"]
            weak_lifetime_evidence = impact["weak_lifetime_facts"]
            if drift_type in {"NullabilityDrift", "ErrorDrift"} and not (
                rust_evidence or impact["direct_uses"] or impact["safe_apis"] or impact["oracle_hits"]
            ):
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
                        "uses": impact["direct_uses"],
                        "safe_apis": impact["safe_apis"],
                        "safety_comments": rust_evidence,
                        "lifetime_facts": lifetime_evidence,
                        "weak_lifetime_facts": weak_lifetime_evidence,
                        "oracle_hits": impact["oracle_hits"],
                    },
                    "evidence_chain": c_evidence + rust_evidence + lifetime_evidence + impact["oracle_hits"],
                    "explanation": f"{symbol} has {indicator} C-side evidence and is used across a Rust unsafe boundary.",
                    "suggested_action": "Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.",
                    "confidence": max([item["confidence"] for item in c_evidence], default=0.5),
                    "indicator_based": True,
                    "not_a_bug_claim": True,
                    "record_kind": "warning",
                    "promotion_status": "promoted",
                    "rust_impact_level": impact["impact_level"],
                    "promotion_reasons": impact["reasons"],
                    "demotion_reasons": [],
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
