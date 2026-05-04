from pathlib import Path

from binddrift import kernel as kernel_module
from binddrift.config import Config
from binddrift.kernel import BINDING_BUILD_TARGETS, BINDING_TARGETS, build_kernel_bindings, prepare_kernel_build


def test_binding_targets_are_generated_rust_files():
    assert BINDING_TARGETS == [
        "rust/bindings/bindings_generated.rs",
        "rust/bindings/bindings_helpers_generated.rs",
    ]
    assert BINDING_BUILD_TARGETS == ["rust/"]


def test_prepare_kernel_build_writes_manifest(tmp_path: Path):
    linux = tmp_path / "vendor/linux"
    linux.mkdir(parents=True)
    cfg = Config.from_args(repo_root=tmp_path)
    toolchain = {"required": {"rustc": "1.78.0", "bindgen": "0.65.1"}, "make_vars": {"RUSTC": "rustup run 1.78.0 rustc"}}
    manifest = prepare_kernel_build(cfg, version_id="test-version", linux_tree=linux, toolchain=toolchain)

    assert Path(manifest["manifest"]).exists()
    assert manifest["version_id"] == "test-version"
    assert manifest["toolchain"]["required"]["rustc"] == "1.78.0"
    assert manifest["generated_bindings"][0].endswith("rust/bindings/bindings_generated.rs")


def test_build_kernel_bindings_restats_generated_outputs(monkeypatch, tmp_path: Path):
    linux = tmp_path / "vendor/linux"
    linux.mkdir(parents=True)
    cfg = Config.from_args(repo_root=tmp_path)

    seen_env_vars = []

    def fake_run_make(linux_tree, objtree, targets, timeout=1800, arch="x86_64", make_vars=None, env_vars=None, log_file=None):
        seen_env_vars.append(env_vars or {})
        for target in BINDING_TARGETS:
            path = objtree / target
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("pub const BINDDRIFT_TEST: u32 = 1;\n", encoding="utf-8")
        if log_file:
            log_file.parent.mkdir(parents=True, exist_ok=True)
            log_file.write_text("full build log\n", encoding="utf-8")
        return {"cmd": ["make", *targets], "returncode": 0, "output": "ok", "log_path": str(log_file) if log_file else None}

    monkeypatch.setattr(kernel_module, "_run_make", fake_run_make)

    manifest = build_kernel_bindings(
        cfg,
        version_id="test-version",
        linux_tree=linux,
        toolchain={"env_vars": {"LIBCLANG_PATH": "/usr/lib/llvm-18/lib"}},
    )

    assert all(output["exists"] for output in manifest["binding_outputs"])
    assert all(output["sha256"] for output in manifest["binding_outputs"])
    assert Path(manifest["commands"][-1]["log_path"]).read_text(encoding="utf-8") == "full build log\n"
    assert seen_env_vars[-1] == {"LIBCLANG_PATH": "/usr/lib/llvm-18/lib"}


def test_prepare_kernel_build_disables_werror_when_configuring(monkeypatch, tmp_path: Path):
    linux = tmp_path / "vendor/linux"
    (linux / "scripts").mkdir(parents=True)
    (linux / "scripts/config").write_text("#!/bin/sh\n", encoding="utf-8")
    cfg = Config.from_args(repo_root=tmp_path)
    config_args = []

    def fake_append_make(manifest, linux_tree, objtree, targets, timeout=1800, arch="x86_64", make_vars=None, env_vars=None):
        manifest["commands"].append({"cmd": ["make", *targets], "returncode": 0, "output": ""})

    def fake_append_config_script(manifest, linux_tree, objtree, args, timeout=120, env_vars=None):
        config_args.extend(args)
        manifest["commands"].append({"cmd": ["scripts/config", *args], "returncode": 0, "output": ""})

    monkeypatch.setattr(kernel_module, "_append_make", fake_append_make)
    monkeypatch.setattr(kernel_module, "_append_config_script", fake_append_config_script)

    prepare_kernel_build(
        cfg,
        version_id="test-version",
        linux_tree=linux,
        configure=True,
        toolchain={"required": {"rustc": "1.78.0"}},
    )

    assert ["-d", "WERROR"] == config_args[:2]
    assert "MITIGATION_CALL_DEPTH_TRACKING" in config_args
    assert config_args[-2:] == ["-e", "RUST"]
