from pathlib import Path

from binddrift.config import Config
from binddrift.db import connect, initialize, upsert_many
from binddrift.graph.builder import build_graph, evidence_chain


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
