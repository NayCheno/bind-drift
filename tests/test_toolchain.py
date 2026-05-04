import subprocess
from pathlib import Path

from binddrift.config import Config
from binddrift.toolchain import recommendations, rustavailable_recommendations
from binddrift import toolchain_matrix
from binddrift.toolchain_matrix import bootstrap_commands, execute_bootstrap_commands, parse_min_tool_versions, write_toolchain_matrix


def test_recommendations_include_bindgen_install():
    recs = recommendations(["bindgen"])
    assert any("cargo install --locked bindgen-cli" in item for item in recs)


def test_recommendations_are_empty_when_complete():
    assert recommendations([]) == []


def test_rustavailable_recommends_rust_src():
    recs = rustavailable_recommendations("Source code for the 'core' standard library could not be found")
    assert any("rustup component add rust-src" in item for item in recs)


def _git(repo: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(repo), *args], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


def test_parse_min_tool_versions_extracts_kernel_requirements():
    script = """
case "$1" in
rustc)
	echo 1.78.0
	;;
bindgen)
	echo 0.65.1
	;;
esac
"""

    assert parse_min_tool_versions(script) == {"rustc": "1.78.0", "bindgen": "0.65.1"}


def test_toolchain_matrix_generates_bootstrap_commands(monkeypatch, tmp_path: Path):
    monkeypatch.setattr(
        toolchain_matrix,
        "_llvm_env",
        lambda: (
            {"LIBCLANG_PATH": "/usr/lib/llvm-18/lib", "LLVM_CONFIG_PATH": "/usr/bin/llvm-config-18"},
            {"libclang_path": "/usr/lib/llvm-18/lib", "llvm_config_version_text": "18.1.3"},
            [],
        ),
    )
    repo = tmp_path / "vendor/linux"
    repo.mkdir(parents=True)
    (repo / "scripts").mkdir()
    (repo / "scripts/min-tool-version.sh").write_text(
        """
case "$1" in
rustc)
	echo 1.78.0
	;;
bindgen)
	echo 0.65.1
	;;
esac
""",
        encoding="utf-8",
    )
    subprocess.run(["git", "-C", str(repo), "init"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    _git(repo, "config", "user.email", "binddrift@example.com")
    _git(repo, "config", "user.name", "BindDrift Test")
    _git(repo, "add", ".")
    _git(repo, "commit", "-m", "fixture")
    _git(repo, "tag", "v6.10")
    cfg = Config.from_args(repo_root=tmp_path)
    rows = [
        {
            "version_id": "v6.10",
            "git_commit": subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip(),
            "tag": "v6.10",
            "date": "",
        }
    ]

    matrix = write_toolchain_matrix(cfg, ["v6.10"], rows)
    commands = bootstrap_commands(cfg, matrix["entries"])

    assert Path(matrix["written_to"]).exists()
    assert matrix["entries"][0]["required"] == {"rustc": "1.78.0", "bindgen": "0.65.1"}
    assert "LIBCLANG_PATH" in matrix["entries"][0]["env_vars"]
    assert "LLVM_CONFIG_PATH" in matrix["entries"][0]["env_vars"]
    assert matrix["entries"][0]["resolved"]["libclang_path"] == matrix["entries"][0]["env_vars"]["LIBCLANG_PATH"]
    assert ["rustup", "toolchain", "install", "1.78.0", "--profile", "minimal", "--component", "rust-src", "--component", "rustfmt", "--component", "clippy"] in commands
    assert any(command[:6] == ["cargo", "+1.78.0", "install", "--locked", "--version", "0.65.1"] for command in commands)


def test_toolchain_matrix_preserves_kernel_tag_requirements(monkeypatch, tmp_path: Path):
    monkeypatch.setattr(
        toolchain_matrix,
        "_llvm_env",
        lambda: (
            {"LIBCLANG_PATH": "/usr/lib/llvm-18/lib", "LLVM_CONFIG_PATH": "/usr/bin/llvm-config-18"},
            {"libclang_path": "/usr/lib/llvm-18/lib", "llvm_config_version_text": "18.1.3"},
            [],
        ),
    )
    repo = tmp_path / "vendor/linux"
    repo.mkdir(parents=True)
    (repo / "scripts").mkdir()
    subprocess.run(["git", "-C", str(repo), "init"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    _git(repo, "config", "user.email", "binddrift@example.com")
    _git(repo, "config", "user.name", "BindDrift Test")
    for tag, rustc, bindgen in [
        ("v6.1", "1.62.0", "0.56.0"),
        ("v6.5", "1.68.2", "0.56.0"),
        ("v6.10", "1.78.0", "0.65.1"),
    ]:
        (repo / "scripts/min-tool-version.sh").write_text(
            f"""
case "$1" in
rustc)
\techo {rustc}
\t;;
bindgen)
\techo {bindgen}
\t;;
esac
""",
            encoding="utf-8",
        )
        _git(repo, "add", ".")
        _git(repo, "commit", "-m", f"{tag} toolchain")
        _git(repo, "tag", tag)
    cfg = Config.from_args(repo_root=tmp_path)
    rows = [
        {"version_id": tag, "git_commit": subprocess.check_output(["git", "-C", str(repo), "rev-parse", tag], text=True).strip(), "tag": tag, "date": ""}
        for tag in ("v6.1", "v6.5", "v6.10")
    ]

    matrix = write_toolchain_matrix(cfg, ["v6.1", "v6.5", "v6.10"], rows)

    assert [entry["required"] for entry in matrix["entries"]] == [
        {"rustc": "1.62.0", "bindgen": "0.56.0"},
        {"rustc": "1.68.2", "bindgen": "0.56.0"},
        {"rustc": "1.78.0", "bindgen": "0.65.1"},
    ]
    assert matrix["entries"][0]["compatibility_issues"][0]["kind"] == "bindgen_0_56_llvm16_anonymous_ident"
    assert matrix["entries"][1]["compatibility_issues"][0]["kind"] == "bindgen_0_56_llvm16_anonymous_ident"
    assert matrix["entries"][2]["compatibility_issues"] == []


def test_bootstrap_commands_use_legacy_bindgen_crate_name(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    entries = [
        {"required": {"rustc": "1.62.0", "bindgen": "0.56.0"}},
        {"required": {"rustc": "1.78.0", "bindgen": "0.65.1"}},
    ]

    commands = bootstrap_commands(cfg, entries)

    assert any(command[:7] == ["cargo", "+1.62.0", "install", "--locked", "--version", "0.56.0", "bindgen"] for command in commands)
    assert any(command[:7] == ["cargo", "+1.78.0", "install", "--locked", "--version", "0.65.1", "bindgen-cli"] for command in commands)


def test_bootstrap_retries_old_cargo_http_registry_failure(monkeypatch):
    calls = []

    def fake_execute(command, env):
        calls.append(command)
        if command[0] == "cargo" and command[1].startswith("+"):
            return {"command": command, "returncode": 101, "output": "HTTP-based registries requires `-Z http-registry`"}
        return {"command": command, "returncode": 0, "output": "installed"}

    monkeypatch.setattr(toolchain_matrix, "_execute_bootstrap_command", fake_execute)

    actions = execute_bootstrap_commands([["cargo", "+1.62.0", "install", "--locked", "--version", "0.56.0", "bindgen-cli"]])

    assert calls == [
        ["cargo", "+1.62.0", "install", "--locked", "--version", "0.56.0", "bindgen-cli"],
        ["cargo", "install", "--locked", "--version", "0.56.0", "bindgen-cli"],
    ]
    assert actions[-1]["returncode"] == 0


def test_bootstrap_retries_old_bindgen_package_name(monkeypatch):
    calls = []

    def fake_execute(command, env):
        calls.append(command)
        if "bindgen-cli" in command:
            return {"command": command, "returncode": 101, "output": "could not find `bindgen-cli` in registry"}
        return {"command": command, "returncode": 0, "output": "installed"}

    monkeypatch.setattr(toolchain_matrix, "_execute_bootstrap_command", fake_execute)

    actions = execute_bootstrap_commands([["cargo", "install", "--locked", "--version", "0.56.0", "bindgen-cli", "--root", "/tmp/root"]])

    assert calls == [
        ["cargo", "install", "--locked", "--version", "0.56.0", "bindgen-cli", "--root", "/tmp/root"],
        ["cargo", "install", "--locked", "--version", "0.56.0", "bindgen", "--root", "/tmp/root"],
    ]
    assert actions[-1]["returncode"] == 0
