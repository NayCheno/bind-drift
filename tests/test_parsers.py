from pathlib import Path

from binddrift.config import Config
from binddrift.extractors.bindgen import _parse_file
from binddrift.extractors.rust_usage import _parse_file as _parse_rust_file
from binddrift.ranking.scorer import score_warning


def test_config_defaults(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    assert cfg.linux_tree == tmp_path / "vendor/linux"
    assert cfg.database.name == "binddrift.sqlite3"


def test_score_contract_warning():
    warning = {
        "type": "NullabilityDrift",
        "confidence": 0.8,
        "rust_side": {"uses": [{"enclosing_unsafe_block": 1}, {"enclosing_unsafe_block": 0}]},
    }
    assert score_warning(warning) > 10


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
