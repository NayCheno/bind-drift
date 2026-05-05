import json
from pathlib import Path

from binddrift.config import Config
from binddrift.db import connect, initialize, upsert_many
from binddrift.detectors.tier1 import run_tier1
from binddrift.detectors.tier2 import run_tier2
from binddrift.warnings import read_warnings


def test_tier1_detects_signature_layout_const_and_helper(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    conn = connect(cfg.database)
    initialize(conn)
    upsert_many(
        conn,
        "binding_functions",
        [
            {
                "version_id": "old",
                "rust_symbol": "foo_get",
                "c_symbol": "foo_get",
                "params": json.dumps([{"name": "x", "type": "i32"}]),
                "return_type": "i32",
                "is_unsafe": 1,
                "source_file": "old.rs",
                "line": 1,
            },
            {
                "version_id": "new",
                "rust_symbol": "foo_get",
                "c_symbol": "foo_get",
                "params": json.dumps([{"name": "x", "type": "u32"}]),
                "return_type": "i32",
                "is_unsafe": 1,
                "source_file": "new.rs",
                "line": 1,
            },
        ],
    )
    upsert_many(
        conn,
        "layout_facts",
        [
            {"version_id": "old", "rust_type": "foo", "field_name": "", "size": 8, "align": 4, "offset": None, "source_file": "old.rs", "line": 2},
            {"version_id": "new", "rust_type": "foo", "field_name": "", "size": 16, "align": 4, "offset": None, "source_file": "new.rs", "line": 2},
        ],
    )
    upsert_many(
        conn,
        "c_macros",
        [
            {"version_id": "old", "name": "FOO_FLAG", "value": "1", "source_file": "old.h", "line": 1},
            {"version_id": "new", "name": "FOO_FLAG", "value": "2", "source_file": "new.h", "line": 1},
        ],
    )
    upsert_many(
        conn,
        "c_functions",
        [
            {"version_id": "old", "c_symbol": "rust_helper_foo", "return_type": "void", "params": "[]", "header_file": "", "definition_file": "rust/helpers/foo.c", "line": 1},
            {"version_id": "new", "c_symbol": "rust_helper_foo", "return_type": "void", "params": "[]", "header_file": "", "definition_file": "rust/helpers/foo.c", "line": 1},
        ],
    )
    upsert_many(
        conn,
        "c_behavior_indicators",
        [
            {"version_id": "old", "c_symbol": "rust_helper_foo", "indicator_type": "NULL_RETURN", "evidence_file": "foo.c", "evidence_line": 1, "evidence_text": "return NULL;", "confidence": 0.7},
            {"version_id": "new", "c_symbol": "rust_helper_foo", "indicator_type": "ERR_PTR_RETURN", "evidence_file": "foo.c", "evidence_line": 1, "evidence_text": "return ERR_PTR(-ENOMEM);", "confidence": 0.7},
        ],
    )

    result = run_tier1(cfg, old="old", new="new")
    warnings = read_warnings(cfg.warnings_jsonl)
    facts = read_warnings(cfg.drift_facts_jsonl)
    warning_types = {warning["type"] for warning in warnings}
    fact_types = {fact["type"] for fact in facts}
    binding_only_facts = [fact for fact in facts if "generated_binding_only" in fact.get("demotion_reasons", [])]

    assert result["facts"] >= 4
    assert {"SignatureDrift", "LayoutDrift", "MacroConstDrift", "HelperDrift"} <= fact_types
    assert {"MacroConstDrift", "HelperDrift"} <= warning_types
    assert binding_only_facts
    assert all(fact["promotion_status"] == "unpromoted" for fact in binding_only_facts)
    assert not any(
        warning["type"] == "SignatureDrift" and warning["c_side"]["symbol"] == "foo_get"
        for warning in warnings
    )


def test_tier2_requires_rust_contract_evidence(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    conn = connect(cfg.database)
    initialize(conn)
    upsert_many(
        conn,
        "c_behavior_indicators",
        [
            {"version_id": "old", "c_symbol": "foo_get", "indicator_type": "NULL_RETURN", "evidence_file": "foo.c", "evidence_line": 1, "evidence_text": "return NULL;", "confidence": 0.7},
            {"version_id": "new", "c_symbol": "foo_get", "indicator_type": "ERR_PTR_RETURN", "evidence_file": "foo.c", "evidence_line": 1, "evidence_text": "return ERR_PTR(-ENOMEM);", "confidence": 0.8},
        ],
    )
    upsert_many(
        conn,
        "rust_binding_uses",
        [
            {
                "version_id": "new",
                "rust_file": "device.rs",
                "line": 10,
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
                "version_id": "new",
                "rust_file": "device.rs",
                "line": 11,
                "mapping_type": "NONNULL_MAPPING",
                "text": "NonNull::new(ptr)",
                "nearby_binding_symbol": "foo_get",
                "nearby_api": "Device::get",
            }
        ],
    )

    result = run_tier2(cfg, old="old", new="new")
    warnings = read_warnings(cfg.warnings_jsonl)

    assert result["new_warnings"] == 1
    assert warnings[0]["type"] == "NullabilityDrift"
    assert warnings[0]["indicator_based"] is True
    assert warnings[0]["evidence_chain"]


def test_tier1_tier2_append_keeps_warning_ids_unique_after_demoted_facts(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    conn = connect(cfg.database)
    initialize(conn)
    upsert_many(
        conn,
        "binding_functions",
        [
            {
                "version_id": "old",
                "rust_symbol": "generated_only",
                "c_symbol": "generated_only",
                "params": "[]",
                "return_type": "void",
                "is_unsafe": 1,
                "source_file": "old.rs",
                "line": 1,
            },
            {
                "version_id": "new",
                "rust_symbol": "generated_only",
                "c_symbol": "generated_only",
                "params": json.dumps([{"name": "x", "type": "i32"}]),
                "return_type": "void",
                "is_unsafe": 1,
                "source_file": "new.rs",
                "line": 1,
            },
        ],
    )
    upsert_many(
        conn,
        "c_macros",
        [
            {"version_id": "old", "name": "FOO_FLAG", "value": "1", "source_file": "old.h", "line": 1},
            {"version_id": "new", "name": "FOO_FLAG", "value": "2", "source_file": "new.h", "line": 1},
        ],
    )
    upsert_many(
        conn,
        "c_behavior_indicators",
        [
            {"version_id": "old", "c_symbol": "foo_get", "indicator_type": "NULL_RETURN", "evidence_file": "foo.c", "evidence_line": 1, "evidence_text": "return NULL;", "confidence": 0.7},
            {"version_id": "new", "c_symbol": "foo_get", "indicator_type": "ERR_PTR_RETURN", "evidence_file": "foo.c", "evidence_line": 2, "evidence_text": "return ERR_PTR(-ENOMEM);", "confidence": 0.8},
        ],
    )
    upsert_many(
        conn,
        "rust_binding_uses",
        [
            {
                "version_id": "new",
                "rust_file": "device.rs",
                "line": 10,
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
                "version_id": "new",
                "rust_file": "device.rs",
                "line": 11,
                "mapping_type": "NONNULL_MAPPING",
                "text": "NonNull::new(ptr)",
                "nearby_binding_symbol": "foo_get",
                "nearby_api": "Device::get",
            }
        ],
    )

    run_tier1(cfg, old="old", new="new")
    run_tier2(cfg, old="old", new="new", append=True)

    warning_ids = [warning["warning_id"] for warning in read_warnings(cfg.warnings_jsonl)]
    assert warning_ids == ["W-000001", "W-000002"]
