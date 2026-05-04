from pathlib import Path

from binddrift.config import Config
from binddrift.kernel import BINDING_TARGETS, prepare_kernel_build


def test_binding_targets_are_generated_rust_files():
    assert BINDING_TARGETS == [
        "rust/bindings/bindings_generated.rs",
        "rust/bindings/bindings_helpers_generated.rs",
    ]


def test_prepare_kernel_build_writes_manifest(tmp_path: Path):
    linux = tmp_path / "vendor/linux"
    linux.mkdir(parents=True)
    cfg = Config.from_args(repo_root=tmp_path)
    manifest = prepare_kernel_build(cfg, version_id="test-version", linux_tree=linux)

    assert Path(manifest["manifest"]).exists()
    assert manifest["version_id"] == "test-version"
    assert manifest["generated_bindings"][0].endswith("rust/bindings/bindings_generated.rs")
