from __future__ import annotations

import json
import sqlite3
from typing import Any

from binddrift.config import Config
from binddrift.db import connect, initialize, upsert_many
from binddrift.kernel import default_version_id


def _node(node_type: str, label: str, properties: dict[str, Any] | None = None) -> dict[str, Any]:
    return {
        "node_id": f"{node_type}:{label}",
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
    for row in conn.execute("SELECT DISTINCT name FROM c_macros WHERE version_id=?", (vid,)):
        add_node(_node("CMacro", row["name"]))
    for row in conn.execute("SELECT DISTINCT rust_symbol, c_symbol FROM binding_functions WHERE version_id=?", (vid,)):
        c = add_node(_node("CFunction", row["c_symbol"]))
        b = add_node(_node("RustBindingFunction", row["rust_symbol"]))
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

    upsert_many(conn, "graph_nodes", list(nodes.values()))
    upsert_many(conn, "graph_edges", list(edges.values()))
    return {"database": str(cfg.database), "version_id": vid, "nodes": len(nodes), "edges": len(edges)}


def query_graph(cfg: Config, symbol: str | None = None, api: str | None = None, version_id: str | None = None) -> dict[str, Any]:
    vid = version_id or default_version_id(cfg)
    conn = connect(cfg.database)
    initialize(conn)
    target = symbol or api or ""
    if not target:
        return {"version_id": vid, "error": "provide --symbol or --api"}
    like = f"%:{target}%"
    nodes = [dict(row) for row in conn.execute("SELECT * FROM graph_nodes WHERE version_id=? AND (label=? OR node_id LIKE ?) LIMIT 100", (vid, target, like))]
    node_ids = [row["node_id"] for row in nodes]
    edge_rows: list[sqlite3.Row] = []
    for node_id in node_ids:
        edge_rows.extend(conn.execute("SELECT * FROM graph_edges WHERE version_id=? AND (src=? OR dst=?) LIMIT 200", (vid, node_id, node_id)).fetchall())
    return {
        "version_id": vid,
        "query": target,
        "nodes": nodes,
        "edges": [dict(row) for row in edge_rows],
    }
