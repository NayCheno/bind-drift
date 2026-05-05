from pathlib import Path

from binddrift.config import Config
from binddrift.db import connect, initialize, upsert_many
from binddrift.detectors.tier2 import run_tier2
from binddrift.extractors.c_api import _parse_file as _parse_c_file
from binddrift.extractors.bindgen import _parse_file
from binddrift.extractors.rust_usage import _parse_file as _parse_rust_file
from binddrift.ranking.scorer import _markdown, rank_warnings, score_breakdown, score_warning
from binddrift.warnings import read_warnings, write_warnings


def test_config_defaults(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    assert cfg.linux_tree == tmp_path / "vendor/linux"
    assert cfg.database.name == "binddrift.sqlite3"


def test_score_contract_warning():
    warning = {
        "type": "NullabilityDrift",
        "confidence": 0.8,
        "promotion_status": "promoted",
        "c_evidence_level": "c_behavior_indicator",
        "rust_side": {
            "uses": [{"enclosing_unsafe_block": 1}, {"enclosing_unsafe_block": 0}],
            "safe_apis": [{"api_name": "Device::get"}],
            "safety_comments": [{"text": "SAFETY: checked"}],
        },
    }
    assert score_warning(warning) >= 12
    assert score_breakdown(warning)["safe_api_exposure"] == 4.0


def test_rank_warnings_filters_unpromoted_and_keeps_score_breakdown(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    write_warnings(
        cfg,
        [
            {
                "warning_id": "W-000001",
                "type": "SignatureDrift",
                "promotion_status": "unpromoted",
                "promotion_reasons": ["direct_binding_use"],
                "c_evidence_level": "binding_only",
                "c_side": {"symbol": "generated_only", "old": "absent", "new": "added"},
                "rust_side": {"exposure": {"edge_count": 50}},
            },
            {
                "warning_id": "W-000002",
                "type": "NullabilityDrift",
                "promotion_status": "promoted",
                "c_evidence_level": "c_behavior_indicator",
                "confidence": 0.8,
                "c_side": {"symbol": "foo_get", "old_indicators": ["NULL_RETURN"], "new_indicators": ["ERR_PTR_RETURN"]},
                "rust_side": {
                    "uses": [{"rust_file": "device.rs", "line": 2, "enclosing_function": "Device::get", "enclosing_unsafe_block": 1}],
                    "safe_apis": [{"api_name": "Device::get"}],
                    "error_mappings": [{"mapping_type": "ERR_PTR_MAPPING"}],
                },
                "evidence_chain": [{"evidence_file": "foo.c", "evidence_line": 1, "evidence_text": "return ERR_PTR(-ENOMEM);"}],
            },
        ],
    )

    result = rank_warnings(cfg)
    ranked = read_warnings(cfg.warnings_jsonl)

    assert result["dropped_unpromoted"] == 1
    assert [warning["warning_id"] for warning in ranked] == ["W-000002"]
    assert ranked[0]["score_breakdown"]["direct_rust_use"] == 4.0
    assert ranked[0]["score_breakdown"].get("binding_only_penalty") == -0.0


def test_rank_warnings_scores_tier2_error_mappings_as_contract(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    conn = connect(cfg.database)
    initialize(conn)
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
                "mapping_type": "ERR_PTR_MAPPING",
                "text": "from_err_ptr(ptr)",
                "nearby_binding_symbol": "foo_get",
                "nearby_api": "Device::get",
            }
        ],
    )

    run_tier2(cfg, old="old", new="new")
    rank_warnings(cfg)
    ranked = read_warnings(cfg.warnings_jsonl)

    assert ranked[0]["score_breakdown"]["contract_mapping"] == 3.0
    assert ranked[0]["score_breakdown"]["c_source_diff_strength"] == 3.0
    assert ranked[0]["risk"] == "Medium"
    assert ranked[0]["score"] >= 10.0
    assert ranked[0]["c_evidence_level"] == "c_behavior_indicator"
    assert ranked[0]["rust_side"]["error_mappings"][0]["mapping_type"] == "ERR_PTR_MAPPING"
    assert "ERR_PTR_MAPPING" in cfg.report_md.read_text(encoding="utf-8")


def test_markdown_report_includes_evidence_sections():
    report = _markdown(
        [
            {
                "warning_id": "W-000001",
                "type": "NullabilityDrift",
                "risk": "High",
                "score": 11,
                "score_breakdown": {"direct_rust_use": 4.0, "safe_api_exposure": 4.0},
                "c_side": {"symbol": "foo_get", "evidence": [{"evidence_file": "foo.c", "evidence_line": 1, "evidence_text": "return ERR_PTR(-ENOMEM);"}]},
                "rust_side": {
                    "uses": [{"rust_file": "device.rs", "line": 2, "enclosing_function": "Device::get", "enclosing_unsafe_block": 1}],
                    "safe_apis": [{"api_name": "Device::get"}],
                    "error_mappings": [{"rust_file": "device.rs", "line": 3, "mapping_type": "ERR_PTR_MAPPING"}],
                    "weak_lifetime_facts": [{"rust_file": "device.rs", "line": 4, "fact_type": "LIFETIME_NAMING_PATTERN"}],
                },
                "explanation": "Changed.",
                "suggested_action": "Review.",
            }
        ]
    )
    assert "### C Evidence" in report
    assert "### Score Breakdown" in report
    assert "### Rust Evidence" in report
    assert "foo.c:1" in report
    assert "safe API `Device::get`" in report
    assert "ERR_PTR_MAPPING" in report
    assert "weak lifetime name" in report


def test_bindgen_parser_handles_multiline_generated_items(tmp_path: Path):
    generated = tmp_path / "bindings_generated.rs"
    generated.write_text(
        """
extern "C" {
    pub fn foo_device_get(
        dev: *mut device,
        cb: ::core::option::Option<unsafe extern "C" fn(arg: *mut ::core::ffi::c_void)>,
    ) -> *mut device;
}
pub const DMA_ATTR_NO_WARN: u32 =
    8;
#[repr(C)]
pub struct device {
    pub kobj: kobject,
    pub parent: *mut device,
}
const _: () = {
    assert_eq!(::core::mem::size_of::<device>(), 64usize);
    assert_eq!(::core::mem::align_of::<device>(), 8usize);
};
""",
        encoding="utf-8",
    )

    facts = _parse_file(generated, "v-test")

    assert facts.functions[0]["rust_symbol"] == "foo_device_get"
    assert "Option<unsafe extern" in facts.functions[0]["params"]
    assert facts.consts[0]["value"] == "8"
    assert facts.structs[0]["rust_type"] == "device"
    assert len(facts.structs[0]["fields"]) > 0
    assert len(facts.layouts) == 2


def test_rust_usage_parser_finds_lifetime_and_error_mapping(tmp_path: Path):
    rust = tmp_path / "device.rs"
    rust.write_text(
        """
pub struct Device;
impl Drop for Device {
    fn drop(&mut self) {
        unsafe { bindings::put_device(self.as_ptr()) };
    }
}
impl Device {
    pub fn get(&self) -> Result<Option<Self>> {
        // SAFETY: C returns NULL on failure.
        let ptr = unsafe { bindings::get_device(self.as_ptr()) };
        NonNull::new(ptr).map(|_| Device).ok_or(EINVAL)
    }
}
""",
        encoding="utf-8",
    )

    uses, apis, comments, lifetime_facts, error_mappings = _parse_rust_file(rust, "v-test")

    assert {use["binding_symbol"] for use in uses} == {"put_device", "get_device"}
    assert all(use["enclosing_unsafe_block"] == 1 for use in uses)
    assert any(api["api_name"] == "Device::get" for api in apis)
    assert any(fact["fact_type"] == "IMPL_DROP" for fact in lifetime_facts)
    assert any(mapping["mapping_type"] == "NONNULL_MAPPING" for mapping in error_mappings)
    assert comments[0]["nearby_binding_symbol"] == "get_device"


def test_c_parser_handles_multiline_function_and_indicators(tmp_path: Path):
    source = tmp_path / "helpers.c"
    source.write_text(
        """
#define FOO_FLAG 8
struct foo {
    int count;
    void *ptr;
};
static inline struct foo *
foo_get(struct foo *foo,
        int flags)
{
    if (!foo)
        return ERR_PTR(-ENOMEM);
    kref_get(&foo->count);
    might_sleep();
    return foo;
}
""",
        encoding="utf-8",
    )

    functions, structs, macros, indicators = _parse_c_file(source, "v-test")

    assert functions[0]["c_symbol"] == "foo_get"
    assert "int flags" in functions[0]["params"]
    assert structs[0]["c_type"] == "foo"
    assert macros[0]["name"] == "FOO_FLAG"
    indicator_types = {item["indicator_type"] for item in indicators if item["c_symbol"] == "foo_get"}
    assert {"ERR_PTR_RETURN", "ERROR_CODE", "REFCOUNT_GET", "MAY_SLEEP"} <= indicator_types
