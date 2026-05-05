from pathlib import Path

from binddrift.config import Config
from binddrift.db import connect, initialize, upsert_many
from binddrift.evidence.impact import compute_rust_impact
from binddrift.graph.builder import build_graph, canonical_node_id, evidence_chain, query_graph


def test_graph_materializes_evidence_chain(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    conn = connect(cfg.database)
    initialize(conn)
    upsert_many(
        conn,
        "c_behavior_indicators",
        [
            {
                "version_id": "v-test",
                "c_symbol": "foo_get",
                "indicator_type": "ERR_PTR_RETURN",
                "evidence_file": "helpers.c",
                "evidence_line": 10,
                "evidence_text": "return ERR_PTR(-ENOMEM);",
                "confidence": 0.8,
            }
        ],
    )
    upsert_many(
        conn,
        "rust_binding_uses",
        [
            {
                "version_id": "v-test",
                "rust_file": "device.rs",
                "line": 20,
                "binding_symbol": "foo_get",
                "enclosing_unsafe_block": 1,
                "enclosing_function": "Device::get",
                "enclosing_impl": "Device",
                "enclosing_type": "Device",
            }
        ],
    )
    upsert_many(
        conn,
        "rust_error_mappings",
        [
            {
                "version_id": "v-test",
                "rust_file": "device.rs",
                "line": 21,
                "mapping_type": "ERR_PTR_MAPPING",
                "text": "from_err_ptr(ptr)",
                "nearby_binding_symbol": "foo_get",
                "nearby_api": "Device::get",
            }
        ],
    )

    summary = build_graph(cfg, version_id="v-test")
    chain = evidence_chain(cfg, "foo_get", version_id="v-test")

    assert summary["nodes"] >= 4
    assert chain["c_indicators"][0]["indicator_type"] == "ERR_PTR_RETURN"
    assert chain["rust_uses"][0]["enclosing_function"] == "Device::get"
    assert chain["rust_error_mappings"][0]["mapping_type"] == "ERR_PTR_MAPPING"


def test_no_substring_symbol_match_for_impact_or_graph_query(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    conn = connect(cfg.database)
    initialize(conn)
    upsert_many(
        conn,
        "c_functions",
        [
            {"version_id": "v-test", "c_symbol": "d_alloc", "return_type": "void", "params": "[]", "header_file": "d.h", "definition_file": "d.c", "line": 1},
        ],
    )
    upsert_many(
        conn,
        "rust_binding_uses",
        [
            {
                "version_id": "v-test",
                "rust_file": "alloc.rs",
                "line": 20,
                "binding_symbol": "dealloc",
                "enclosing_unsafe_block": 1,
                "enclosing_function": "Device::dealloc",
                "enclosing_impl": "Device",
                "enclosing_type": "Device",
            }
        ],
    )

    build_graph(cfg, version_id="v-test")
    impact = compute_rust_impact(conn, "v-test", "d_alloc", "SignatureDrift")
    exact = query_graph(cfg, symbol="d_alloc", version_id="v-test")
    fuzzy = query_graph(cfg, symbol="alloc", version_id="v-test", fuzzy=True)

    assert impact["eligible"] is False
    assert {node["node_id"] for node in exact["nodes"]} == {"CFunction:d_alloc"}
    assert "RustUnsafeCall:alloc.rs:20:dealloc" in {node["node_id"] for node in fuzzy["nodes"]}


def test_exact_graph_query_does_not_return_label_only_nodes(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    conn = connect(cfg.database)
    initialize(conn)
    upsert_many(
        conn,
        "c_functions",
        [
            {
                "version_id": "v-test",
                "c_symbol": "foo",
                "return_type": "void",
                "params": "[]",
                "header_file": "foo.h",
                "definition_file": "foo.c",
                "line": 1,
            },
        ],
    )
    build_graph(cfg, version_id="v-test")
    upsert_many(
        conn,
        "graph_nodes",
        [
            {
                "version_id": "v-test",
                "node_id": "RustSafeAPI:other",
                "node_type": "RustSafeAPI",
                "label": "foo",
                "properties": "{}",
            }
        ],
    )

    exact = query_graph(cfg, symbol="foo", version_id="v-test")
    fuzzy = query_graph(cfg, symbol="foo", version_id="v-test", fuzzy=True)

    assert canonical_node_id("CFunction", "foo") in {node["node_id"] for node in exact["nodes"]}
    assert "RustSafeAPI:other" not in {node["node_id"] for node in exact["nodes"]}
    assert "RustSafeAPI:other" in {node["node_id"] for node in fuzzy["nodes"]}
