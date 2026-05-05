from __future__ import annotations

import json
import sqlite3
from typing import Any

from binddrift.config import Config
from binddrift.db import connect, initialize, upsert_many
from binddrift.kernel import default_version_id


def canonical_node_id(node_type: str, label: str) -> str:
    return f"{node_type}:{label}"


def _node(node_type: str, label: str, properties: dict[str, Any] | None = None) -> dict[str, Any]:
    return {
        "node_id": canonical_node_id(node_type, label),
        "node_type": node_type,
        "label": label,
        "properties": json.dumps(properties or {}, sort_keys=True),
    }


def _edge(src: str, dst: str, edge_type: str, properties: dict[str, Any] | None = None) -> dict[str, Any]:
    return {"src": src, "dst": dst, "edge_type": edge_type, "properties": json.dumps(properties or {}, sort_keys=True)}


def build_graph(cfg: Config, version_id: str | None = None) -> dict[str, Any]:
    cfg.ensure_dirs()
    vid = version_id or default_version_id(cfg)
    conn = connect(cfg.database)
    initialize(conn)
    nodes: dict[str, dict[str, Any]] = {}
    edges: dict[tuple[str, str, str], dict[str, Any]] = {}

    def add_node(row: dict[str, Any]) -> str:
        row = {"version_id": vid, **row}
        nodes[row["node_id"]] = row
        return row["node_id"]

    def add_edge(row: dict[str, Any]) -> None:
        row = {"version_id": vid, **row}
        edges[(row["src"], row["dst"], row["edge_type"])] = row

    for row in conn.execute("SELECT DISTINCT c_symbol FROM c_functions WHERE version_id=?", (vid,)):
        add_node(_node("CFunction", row["c_symbol"]))
    for row in conn.execute("SELECT DISTINCT c_type FROM c_structs WHERE version_id=?", (vid,)):
        add_node(_node("CStruct", row["c_type"]))
    for row in conn.execute("SELECT DISTINCT name FROM c_macros WHERE version_id=?", (vid,)):
        add_node(_node("CMacro", row["name"]))
    for row in conn.execute("SELECT * FROM c_behavior_indicators WHERE version_id=?", (vid,)):
        c = add_node(_node("CFunction", row["c_symbol"]))
        indicator = add_node(
            _node(
                "CBehaviorIndicator",
                f"{row['c_symbol']}:{row['indicator_type']}:{row['evidence_file']}:{row['evidence_line']}",
                {
                    "indicator_type": row["indicator_type"],
                    "file": row["evidence_file"],
                    "line": row["evidence_line"],
                    "text": row["evidence_text"],
                    "confidence": row["confidence"],
                },
            )
        )
        add_edge(_edge(c, indicator, "HAS_C_INDICATOR"))
    for row in conn.execute("SELECT DISTINCT rust_symbol, c_symbol FROM binding_functions WHERE version_id=?", (vid,)):
        c = add_node(_node("CFunction", row["c_symbol"]))
        b = add_node(_node("RustBindingFunction", row["rust_symbol"]))
        add_edge(_edge(c, b, "GENERATED_FROM"))
    for row in conn.execute("SELECT DISTINCT rust_type, c_type FROM binding_structs WHERE version_id=?", (vid,)):
        c = add_node(_node("CStruct", row["c_type"]))
        b = add_node(_node("RustBindingStruct", row["rust_type"]))
        add_edge(_edge(c, b, "GENERATED_FROM"))
    for row in conn.execute("SELECT DISTINCT rust_name, c_name FROM binding_consts WHERE version_id=?", (vid,)):
        c = add_node(_node("CMacro", row["c_name"]))
        b = add_node(_node("RustBindingConst", row["rust_name"]))
        add_edge(_edge(c, b, "GENERATED_FROM"))
    for row in conn.execute("SELECT * FROM rust_binding_uses WHERE version_id=?", (vid,)):
        binding = add_node(_node("RustBindingFunction", row["binding_symbol"]))
        call_label = f"{row['rust_file']}:{row['line']}:{row['binding_symbol']}"
        call = add_node(
            _node(
                "RustUnsafeCall",
                call_label,
                {
                    "file": row["rust_file"],
                    "line": row["line"],
                    "unsafe": bool(row["enclosing_unsafe_block"]),
                    "function": row["enclosing_function"],
                    "impl": row["enclosing_impl"],
                },
            )
        )
        add_edge(_edge(binding, call, "CALLS_BINDING"))
        if row["enclosing_function"]:
            api = add_node(_node("RustSafeAPI", row["enclosing_function"]))
            add_edge(_edge(call, api, "EXPOSES_SAFE_API"))
    for row in conn.execute("SELECT * FROM rust_safety_comments WHERE version_id=? AND nearby_binding_symbol IS NOT NULL", (vid,)):
        comment = add_node(_node("RustSafetyComment", f"{row['rust_file']}:{row['line']}", {"text": row["text"]}))
        binding = add_node(_node("RustBindingFunction", row["nearby_binding_symbol"]))
        add_edge(_edge(binding, comment, "HAS_SAFETY_COMMENT"))
    for row in conn.execute("SELECT * FROM rust_error_mappings WHERE version_id=?", (vid,)):
        mapping = add_node(
            _node(
                "RustErrorMapping",
                f"{row['rust_file']}:{row['line']}:{row['mapping_type']}",
                {"mapping_type": row["mapping_type"], "text": row["text"], "api": row["nearby_api"]},
            )
        )
        if row["nearby_binding_symbol"]:
            binding = add_node(_node("RustBindingFunction", row["nearby_binding_symbol"]))
            add_edge(_edge(binding, mapping, "HAS_ERROR_MAPPING"))
        if row["nearby_api"]:
            api = add_node(_node("RustSafeAPI", row["nearby_api"]))
            add_edge(_edge(mapping, api, "EXPLAINS_SAFE_API"))
    for row in conn.execute("SELECT * FROM rust_lifetime_facts WHERE version_id=?", (vid,)):
        fact = add_node(
            _node(
                "RustLifetimeFact",
                f"{row['rust_file']}:{row['line']}:{row['fact_type']}",
                {"fact_type": row["fact_type"], "type": row["rust_type"], "text": row["evidence_text"]},
            )
        )
        if row["rust_type"]:
            rust_type = add_node(_node("RustType", row["rust_type"]))
            add_edge(_edge(rust_type, fact, "HAS_LIFETIME_FACT"))
        for symbol in json.loads(row["uses_bindings"]):
            binding = add_node(_node("RustBindingFunction", symbol))
            add_edge(_edge(binding, fact, "AFFECTS_LIFETIME"))

    upsert_many(conn, "graph_nodes", list(nodes.values()))
    upsert_many(conn, "graph_edges", list(edges.values()))
    return {"database": str(cfg.database), "version_id": vid, "nodes": len(nodes), "edges": len(edges)}


def query_graph(
    cfg: Config,
    symbol: str | None = None,
    api: str | None = None,
    version_id: str | None = None,
    fuzzy: bool = False,
) -> dict[str, Any]:
    vid = version_id or default_version_id(cfg)
    conn = connect(cfg.database)
    initialize(conn)
    target = symbol or api or ""
    if not target:
        return {"version_id": vid, "error": "provide --symbol or --api"}
    if fuzzy:
        like = f"%:{target}%"
        nodes = [
            dict(row)
            for row in conn.execute(
                "SELECT * FROM graph_nodes WHERE version_id=? AND (label=? OR node_id LIKE ?) LIMIT 100",
                (vid, target, like),
            )
        ]
    else:
        node_ids = [
            canonical_node_id("CFunction", target),
            canonical_node_id("RustBindingFunction", target),
            canonical_node_id("CStruct", target),
            canonical_node_id("RustBindingStruct", target),
            canonical_node_id("CMacro", target),
            canonical_node_id("RustBindingConst", target),
            canonical_node_id("RustSafeAPI", target),
        ]
        placeholders = ",".join("?" for _ in node_ids)
        nodes = [
            dict(row)
            for row in conn.execute(
                f"SELECT * FROM graph_nodes WHERE version_id=? AND node_id IN ({placeholders}) LIMIT 100",
                (vid, *node_ids),
            )
        ]
    node_ids = [row["node_id"] for row in nodes]
    edge_rows: list[sqlite3.Row] = []
    for node_id in node_ids:
        edge_rows.extend(conn.execute("SELECT * FROM graph_edges WHERE version_id=? AND (src=? OR dst=?) LIMIT 200", (vid, node_id, node_id)).fetchall())
    return {
        "version_id": vid,
        "query": target,
        "fuzzy": fuzzy,
        "nodes": nodes,
        "edges": [dict(row) for row in edge_rows],
    }


def evidence_chain(cfg: Config, symbol: str, version_id: str | None = None) -> dict[str, Any]:
    vid = version_id or default_version_id(cfg)
    conn = connect(cfg.database)
    initialize(conn)
    return {
        "version_id": vid,
        "symbol": symbol,
        "c_functions": [
            dict(row)
            for row in conn.execute("SELECT * FROM c_functions WHERE version_id=? AND c_symbol=? LIMIT 20", (vid, symbol))
        ],
        "c_indicators": [
            dict(row)
            for row in conn.execute(
                "SELECT * FROM c_behavior_indicators WHERE version_id=? AND c_symbol=? ORDER BY evidence_line LIMIT 50",
                (vid, symbol),
            )
        ],
        "rust_uses": [
            dict(row)
            for row in conn.execute(
                "SELECT * FROM rust_binding_uses WHERE version_id=? AND binding_symbol=? ORDER BY rust_file, line LIMIT 50",
                (vid, symbol),
            )
        ],
        "rust_error_mappings": [
            dict(row)
            for row in conn.execute(
                "SELECT * FROM rust_error_mappings WHERE version_id=? AND nearby_binding_symbol=? ORDER BY rust_file, line LIMIT 50",
                (vid, symbol),
            )
        ],
        "rust_safety_comments": [
            dict(row)
            for row in conn.execute(
                "SELECT * FROM rust_safety_comments WHERE version_id=? AND nearby_binding_symbol=? ORDER BY rust_file, line LIMIT 50",
                (vid, symbol),
            )
        ],
        "graph": query_graph(cfg, symbol=symbol, version_id=vid),
    }
