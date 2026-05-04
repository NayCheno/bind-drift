from __future__ import annotations

import json
from typing import Any

from binddrift.config import Config
from binddrift.db import connect, initialize, upsert_many
from binddrift.kernel import default_version_id
from binddrift.warnings import warning_id, write_warnings


def _available_versions(conn) -> list[str]:
    rows = conn.execute(
        """
        SELECT version_id FROM (
            SELECT version_id, COUNT(*) AS n FROM binding_functions GROUP BY version_id
            UNION
            SELECT version_id, COUNT(*) AS n FROM c_functions GROUP BY version_id
        ) GROUP BY version_id ORDER BY version_id
        """
    ).fetchall()
    return [row["version_id"] for row in rows]


def _rows_by(conn, table: str, version: str, key: str) -> dict[str, dict[str, Any]]:
    return {row[key]: dict(row) for row in conn.execute(f"SELECT * FROM {table} WHERE version_id=?", (version,))}


def _layout_by(conn, version: str) -> dict[str, dict[str, Any]]:
    rows: dict[str, dict[str, Any]] = {}
    for row in conn.execute("SELECT * FROM layout_facts WHERE version_id=?", (version,)):
        key = f"{row['rust_type']}::{row['field_name']}"
        rows[key] = dict(row)
    return rows


def _indicator_sets(conn, version: str) -> dict[str, set[str]]:
    out: dict[str, set[str]] = {}
    for row in conn.execute("SELECT c_symbol, indicator_type FROM c_behavior_indicators WHERE version_id=?", (version,)):
        out.setdefault(row["c_symbol"], set()).add(row["indicator_type"])
    return out


def _graph_exposure(conn, version: str, symbol: str) -> dict[str, Any]:
    edges = conn.execute(
        "SELECT * FROM graph_edges WHERE version_id=? AND (src LIKE ? OR dst LIKE ?) LIMIT 50",
        (version, f"%:{symbol}", f"%:{symbol}%"),
    ).fetchall()
    return {"edge_count": len(edges), "edges": [dict(row) for row in edges[:10]]}


def _make_warning(idx: int, drift_type: str, symbol: str, old: Any, new: Any, exposure: dict[str, Any]) -> dict[str, Any]:
    return {
        "warning_id": warning_id(idx),
        "type": drift_type,
        "risk": "Medium",
        "score": 0.0,
        "c_side": {"symbol": symbol, "old": old, "new": new},
        "rust_side": {"exposure": exposure},
        "evidence_chain": [],
        "explanation": f"{symbol} changed across the selected Linux versions.",
        "suggested_action": "Inspect the Rust safe abstraction and generated binding for stale assumptions.",
        "confidence": 0.85,
    }


def _event(warning: dict[str, Any], old_version: str | None, new_version: str) -> dict[str, Any]:
    return {
        "event_id": warning["warning_id"],
        "old_version": old_version,
        "new_version": new_version,
        "drift_type": warning["type"],
        "symbol": warning["c_side"]["symbol"],
        "old_value": json.dumps(warning["c_side"].get("old"), sort_keys=True),
        "new_value": json.dumps(warning["c_side"].get("new"), sort_keys=True),
        "evidence": json.dumps(warning.get("rust_side", {}), sort_keys=True),
    }


def _add_warning(
    warnings: list[dict[str, Any]],
    idx: int,
    drift_type: str,
    symbol: str,
    old: Any,
    new: Any,
    exposure: dict[str, Any],
) -> int:
    warnings.append(_make_warning(idx, drift_type, symbol, old, new, exposure))
    return idx + 1


def run_tier1(cfg: Config, old: str | None = None, new: str | None = None) -> dict[str, Any]:
    conn = connect(cfg.database)
    initialize(conn)
    versions = _available_versions(conn)
    selected_new = new or default_version_id(cfg)
    selected_old = old
    if not selected_old:
        prior = [version for version in versions if version != selected_new]
        selected_old = prior[-1] if prior else None
    if not selected_old:
        write_warnings(cfg, [])
        return {
            "warnings": 0,
            "warning_file": str(cfg.warnings_jsonl),
            "status": "need_two_versions",
            "available_versions": versions,
        }

    warnings: list[dict[str, Any]] = []
    idx = 1

    old_funcs = _rows_by(conn, "binding_functions", selected_old, "rust_symbol")
    new_funcs = _rows_by(conn, "binding_functions", selected_new, "rust_symbol")
    for symbol in sorted(set(old_funcs) | set(new_funcs)):
        old_row = old_funcs.get(symbol)
        new_row = new_funcs.get(symbol)
        if old_row and not new_row:
            idx = _add_warning(warnings, idx, "SignatureDrift", symbol, "present", "removed", _graph_exposure(conn, selected_new, symbol))
        elif new_row and not old_row:
            idx = _add_warning(warnings, idx, "SignatureDrift", symbol, "absent", "added", _graph_exposure(conn, selected_new, symbol))
        elif old_row and new_row and (old_row["params"], old_row["return_type"]) != (new_row["params"], new_row["return_type"]):
            idx = _add_warning(
                warnings,
                idx,
                "SignatureDrift",
                symbol,
                {"params": json.loads(old_row["params"]), "return_type": old_row["return_type"]},
                {"params": json.loads(new_row["params"]), "return_type": new_row["return_type"]},
                _graph_exposure(conn, selected_new, symbol),
            )

    old_structs = _rows_by(conn, "binding_structs", selected_old, "rust_type")
    new_structs = _rows_by(conn, "binding_structs", selected_new, "rust_type")
    for symbol in sorted(set(old_structs) & set(new_structs)):
        if old_structs[symbol]["fields"] != new_structs[symbol]["fields"]:
            warnings.append(
                _make_warning(
                    idx,
                    "FieldDrift",
                    symbol,
                    json.loads(old_structs[symbol]["fields"]),
                    json.loads(new_structs[symbol]["fields"]),
                    _graph_exposure(conn, selected_new, symbol),
                )
            )
            idx += 1

    old_layouts = _layout_by(conn, selected_old)
    new_layouts = _layout_by(conn, selected_new)
    for symbol in sorted(set(old_layouts) & set(new_layouts)):
        old_row = old_layouts[symbol]
        new_row = new_layouts[symbol]
        old_value = {key: old_row[key] for key in ("size", "align", "offset")}
        new_value = {key: new_row[key] for key in ("size", "align", "offset")}
        if old_value != new_value:
            idx = _add_warning(warnings, idx, "LayoutDrift", symbol, old_value, new_value, _graph_exposure(conn, selected_new, old_row["rust_type"]))

    old_consts = _rows_by(conn, "binding_consts", selected_old, "rust_name")
    new_consts = _rows_by(conn, "binding_consts", selected_new, "rust_name")
    for symbol in sorted(set(old_consts) & set(new_consts)):
        if old_consts[symbol]["value"] != new_consts[symbol]["value"]:
            idx = _add_warning(
                warnings,
                idx,
                "MacroConstDrift",
                symbol,
                old_consts[symbol]["value"],
                new_consts[symbol]["value"],
                _graph_exposure(conn, selected_new, symbol),
            )

    old_macros = _rows_by(conn, "c_macros", selected_old, "name")
    new_macros = _rows_by(conn, "c_macros", selected_new, "name")
    for symbol in sorted(set(old_macros) & set(new_macros)):
        if old_macros[symbol]["value"] != new_macros[symbol]["value"]:
            idx = _add_warning(
                warnings,
                idx,
                "MacroConstDrift",
                symbol,
                old_macros[symbol]["value"],
                new_macros[symbol]["value"],
                _graph_exposure(conn, selected_new, symbol),
            )

    old_c = _rows_by(conn, "c_functions", selected_old, "c_symbol")
    new_c = _rows_by(conn, "c_functions", selected_new, "c_symbol")
    for symbol in sorted(set(old_c) & set(new_c)):
        if old_c[symbol]["params"] != new_c[symbol]["params"] or old_c[symbol]["return_type"] != new_c[symbol]["return_type"]:
            warnings.append(
                _make_warning(
                    idx,
                    "SignatureDrift",
                    symbol,
                    {"params": json.loads(old_c[symbol]["params"]), "return_type": old_c[symbol]["return_type"]},
                    {"params": json.loads(new_c[symbol]["params"]), "return_type": new_c[symbol]["return_type"]},
                    _graph_exposure(conn, selected_new, symbol),
                )
            )
            idx += 1

    old_indicators = _indicator_sets(conn, selected_old)
    new_indicators = _indicator_sets(conn, selected_new)
    helper_symbols = {
        row["c_symbol"]
        for row in conn.execute(
            "SELECT DISTINCT c_symbol FROM c_functions WHERE version_id=? AND (header_file LIKE '%rust/helpers%' OR definition_file LIKE '%rust/helpers%')",
            (selected_new,),
        )
    }
    for symbol in sorted(helper_symbols & set(old_indicators) & set(new_indicators)):
        if old_indicators[symbol] != new_indicators[symbol]:
            idx = _add_warning(
                warnings,
                idx,
                "HelperDrift",
                symbol,
                sorted(old_indicators[symbol]),
                sorted(new_indicators[symbol]),
                _graph_exposure(conn, selected_new, symbol),
            )

    write_warnings(cfg, warnings)
    upsert_many(conn, "drift_events", [_event(warning, selected_old, selected_new) for warning in warnings])
    return {
        "warnings": len(warnings),
        "warning_file": str(cfg.warnings_jsonl),
        "old_version": selected_old,
        "new_version": selected_new,
    }
