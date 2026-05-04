from __future__ import annotations

import json
from typing import Any

from binddrift.config import Config
from binddrift.db import connect, initialize
from binddrift.warnings import read_warnings
from .metrics import labeled_summary, load_manual_labels, oracle_summary


BASELINES = ["BindgenOnly", "CSignatureDiff", "BuildOnly", "GrepUsage", "NoRanking", "Tier1Only"]
ABLATIONS = ["NoGraph", "NoTier2", "NoRanking", "NoSafetyComment", "NoCommitText", "NoBehaviorIndicator"]
TIER1_TYPES = {"SignatureDrift", "LayoutDrift", "FieldDrift", "MacroConstDrift", "HelperDrift"}
TIER2_TYPES = {"NullabilityDrift", "ErrorDrift", "OwnershipRefcountDrift", "AllocationFreePairingDrift", "SleepabilityDrift"}


def generate_baselines(cfg: Config) -> dict[str, Any]:
    conn = connect(cfg.database)
    initialize(conn)
    warnings = read_warnings(cfg.warnings_jsonl)
    labels = load_manual_labels(cfg.data_dir / "manual_review.csv")
    build_symbols = _build_symbols(conn, warnings)
    wrapper_symbols: set[str] = set()
    for row in conn.execute("SELECT matched_symbols FROM wrapper_fix_events WHERE likely_wrapper_fix=1"):
        wrapper_symbols.update(str(symbol) for symbol in json.loads(row["matched_symbols"]) if symbol)
    counts = {
        "binding_functions": conn.execute("SELECT COUNT(*) AS n FROM binding_functions").fetchone()["n"],
        "c_functions": conn.execute("SELECT COUNT(*) AS n FROM c_functions").fetchone()["n"],
        "rust_binding_uses": conn.execute("SELECT COUNT(*) AS n FROM rust_binding_uses").fetchone()["n"],
        "graph_edges": conn.execute("SELECT COUNT(*) AS n FROM graph_edges").fetchone()["n"],
        "build_breakage_events": conn.execute("SELECT COUNT(*) AS n FROM build_breakage_events").fetchone()["n"],
        "warnings": len(warnings),
    }
    rows = []
    for name in BASELINES:
        candidates = _variant_warnings(name, warnings, build_symbols)
        rows.append(
            {
                "variant": name,
                "kind": "baseline",
                "candidate_count": _candidate_count(name, counts),
                "warning_count": len(candidates),
                "manual_review": labeled_summary(candidates, labels),
                "build_breakage_prediction": oracle_summary(candidates, build_symbols),
                "wrapper_fix_prediction": oracle_summary(candidates, wrapper_symbols),
                "note": "Metrics are computed over the variant's filtered or re-ranked warning list.",
            }
        )
    for name in ABLATIONS:
        candidates = _variant_warnings(name, warnings, build_symbols)
        rows.append(
            {
                "variant": name,
                "kind": "ablation",
                "candidate_count": _candidate_count(name, counts),
                "warning_count": len(candidates),
                "manual_review": labeled_summary(candidates, labels),
                "build_breakage_prediction": oracle_summary(candidates, build_symbols),
                "wrapper_fix_prediction": oracle_summary(candidates, wrapper_symbols),
                "note": "Metrics are computed over the variant's filtered or re-ranked warning list.",
            }
        )
    path = cfg.repo_root / "paper/tables/baselines_ablations.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"counts": counts, "variants": rows}, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return {"baseline_table": str(path), "variants": len(rows), "counts": counts}


def _candidate_count(name: str, counts: dict[str, int]) -> int:
    if name == "BindgenOnly":
        return counts["binding_functions"]
    if name == "CSignatureDiff":
        return counts["c_functions"]
    if name == "BuildOnly":
        return counts["build_breakage_events"]
    if name == "GrepUsage":
        return counts["rust_binding_uses"]
    if name == "Tier1Only":
        return counts["warnings"]
    if name == "NoGraph":
        return counts["c_functions"]
    return counts["warnings"]


def _symbol(warning: dict[str, Any]) -> str | None:
    symbol = warning.get("c_side", {}).get("symbol")
    return str(symbol) if symbol else None


def _build_symbols(conn, warnings: list[dict[str, Any]]) -> set[str]:
    pair_ids = {warning.get("pair_id") for warning in warnings if warning.get("pair_id")}
    run_ids = {warning.get("run_id") for warning in warnings if warning.get("run_id")}
    if len(pair_ids) == 1:
        return {
            str(row["symbol"])
            for row in conn.execute("SELECT DISTINCT symbol FROM build_breakage_events WHERE pair_id=? AND symbol IS NOT NULL", (next(iter(pair_ids)),))
        }
    if len(run_ids) == 1:
        return {
            str(row["symbol"])
            for row in conn.execute("SELECT DISTINCT symbol FROM build_breakage_events WHERE run_id=? AND symbol IS NOT NULL", (next(iter(run_ids)),))
        }
    return {
        str(row["symbol"])
        for row in conn.execute("SELECT DISTINCT symbol FROM build_breakage_events WHERE symbol IS NOT NULL")
    }


def _variant_warnings(name: str, warnings: list[dict[str, Any]], build_symbols: set[str]) -> list[dict[str, Any]]:
    if name == "BindgenOnly":
        return [warning for warning in warnings if warning.get("type") in {"SignatureDrift", "LayoutDrift", "FieldDrift", "MacroConstDrift"}]
    if name == "CSignatureDiff":
        return [warning for warning in warnings if warning.get("type") == "SignatureDrift"]
    if name == "BuildOnly":
        return [warning for warning in warnings if (_symbol(warning) or "") in build_symbols]
    if name == "GrepUsage":
        return [warning for warning in warnings if warning.get("rust_side", {}).get("uses") or warning.get("rust_side", {}).get("exposure", {}).get("edge_count")]
    if name in {"Tier1Only", "NoTier2", "NoBehaviorIndicator"}:
        return [warning for warning in warnings if warning.get("type") in TIER1_TYPES]
    if name == "NoGraph":
        return sorted(warnings, key=lambda warning: (_symbol(warning) or "", str(warning.get("warning_id"))))
    if name == "NoRanking":
        return sorted(warnings, key=lambda warning: str(warning.get("warning_id")))
    if name == "NoSafetyComment":
        return [
            {**warning, "rust_side": {**warning.get("rust_side", {}), "safety_comments": []}}
            for warning in warnings
        ]
    if name == "NoCommitText":
        return [
            warning
            for warning in warnings
            if warning.get("type") in TIER1_TYPES or warning.get("type") in TIER2_TYPES
        ]
    return warnings
