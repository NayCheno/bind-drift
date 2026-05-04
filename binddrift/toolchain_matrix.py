from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .config import Config
from .gitutil import git_output


TOOL_CASE_RE = re.compile(
    r"(?P<tool>rustc|bindgen)\)\s*\n\s*echo\s+(?P<version>[0-9]+(?:\.[0-9]+){1,2})",
    re.MULTILINE,
)


def parse_min_tool_versions(script_text: str) -> dict[str, str]:
    """Extract Rust-for-Linux tool versions from scripts/min-tool-version.sh."""

    return {match.group("tool"): match.group("version") for match in TOOL_CASE_RE.finditer(script_text)}


def _git_ref(ref: str) -> str:
    return ref.split(":", 1)[0] if ref.startswith("HEAD:") else ref


def required_versions_for_ref(repo: Path, ref: str) -> dict[str, str]:
    script = git_output(repo, ["show", f"{_git_ref(ref)}:scripts/min-tool-version.sh"], default="")
    return parse_min_tool_versions(script)


def _run_text(command: list[str], env: dict[str, str] | None = None) -> str | None:
    try:
        proc = subprocess.run(
            command,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
            timeout=30,
            env=env,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if proc.returncode != 0:
        return None
    return proc.stdout.strip()


def _rust_lib_src(rustc_version: str) -> str:
    sysroot = _run_text(["rustup", "run", rustc_version, "rustc", "--print", "sysroot"])
    if sysroot:
        return str(Path(sysroot) / "lib/rustlib/src/rust/library")
    host = _run_text(["rustc", "-vV"])
    host_triple = "x86_64-unknown-linux-gnu"
    if host:
        for line in host.splitlines():
            if line.startswith("host: "):
                host_triple = line.split(":", 1)[1].strip()
                break
    return str(Path.home() / ".rustup/toolchains" / f"{rustc_version}-{host_triple}" / "lib/rustlib/src/rust/library")


def _rust_wrapper_root(cfg: Config, rustc_version: str) -> Path:
    return cfg.state_dir / "toolchains" / f"rust-{rustc_version}" / "bin"


def _ensure_rustup_wrappers(cfg: Config, rustc_version: str) -> dict[str, str]:
    root = _rust_wrapper_root(cfg, rustc_version)
    root.mkdir(parents=True, exist_ok=True)
    wrappers = {}
    for tool in ("rustc", "rustdoc", "rustfmt", "clippy-driver"):
        path = root / tool
        path.write_text(
            f"#!/usr/bin/env sh\nexec rustup run {rustc_version} {tool} \"$@\"\n",
            encoding="utf-8",
        )
        path.chmod(0o755)
        wrappers[tool] = str(path)
    return wrappers


def _bindgen_root(cfg: Config, bindgen_version: str) -> Path:
    return cfg.state_dir / "toolchains" / f"bindgen-{bindgen_version}"


def _command_available(command: str) -> bool:
    first = command.split()[0]
    return shutil.which(first) is not None


def _clang_major() -> str | None:
    output = _run_text(["clang", "--version"])
    if not output:
        return None
    match = re.search(r"clang version\s+([0-9]+)", output)
    return match.group(1) if match else None


def _llvm_config_command() -> str:
    major = _clang_major()
    if major:
        versioned = f"llvm-config-{major}"
        if shutil.which(versioned):
            return versioned
    return "llvm-config"


def _llvm_env() -> tuple[dict[str, str], dict[str, Any], list[str]]:
    missing: list[str] = []
    resolved: dict[str, Any] = {}
    env_vars: dict[str, str] = {}

    llvm_config = _llvm_config_command()
    llvm_config_path = shutil.which(llvm_config)
    llvm_libdir = _run_text([llvm_config, "--libdir"]) if llvm_config_path else None
    llvm_version = _run_text([llvm_config, "--version"]) if llvm_config_path else None
    clang_path = shutil.which("clang")
    clang_version = _run_text(["clang", "--version"]) if clang_path else None

    if llvm_config_path:
        env_vars["LLVM_CONFIG_PATH"] = llvm_config_path
    else:
        missing.append("llvm-config")
    if llvm_libdir:
        env_vars["LIBCLANG_PATH"] = llvm_libdir
    else:
        missing.append("libclang")

    resolved.update(
        {
            "clang_path": clang_path,
            "clang_version_text": clang_version,
            "llvm_config": llvm_config,
            "llvm_config_path": llvm_config_path,
            "llvm_config_version_text": llvm_version,
            "llvm_libdir": llvm_libdir,
            "libclang_path": env_vars.get("LIBCLANG_PATH"),
        }
    )
    return env_vars, resolved, missing


def _major_version(value: str | None) -> int | None:
    if not value:
        return None
    match = re.search(r"([0-9]+)", value)
    return int(match.group(1)) if match else None


def _compatibility_issues(bindgen_version: str | None, resolved: dict[str, Any]) -> list[dict[str, str]]:
    libclang_major = _major_version(resolved.get("llvm_config_version_text"))
    if bindgen_version and _version_key(bindgen_version) < (0, 62, 0) and libclang_major and libclang_major >= 16:
        return [
            {
                "kind": "bindgen_0_56_llvm16_anonymous_ident",
                "severity": "blocking",
                "detail": (
                    f"bindgen {bindgen_version} is known to fail with LLVM/libclang {libclang_major}+ "
                    "on Linux Rust bindings that contain anonymous C items; use libclang <=15 or exclude this tag from binding-built replay."
                ),
            }
        ]
    return []


def make_toolchain_spec(cfg: Config, ref: str, version_row: dict[str, Any]) -> dict[str, Any]:
    required = required_versions_for_ref(cfg.linux_tree, ref)
    rustc_version = required.get("rustc")
    bindgen_version = required.get("bindgen")
    make_vars: dict[str, str] = {}
    missing: list[str] = []
    resolved: dict[str, Any] = {}
    env_vars, llvm_resolved, llvm_missing = _llvm_env()
    resolved.update(llvm_resolved)
    missing.extend(llvm_missing)

    if rustc_version:
        wrappers = _ensure_rustup_wrappers(cfg, rustc_version)
        rust_commands = {
            "RUSTC": wrappers["rustc"],
            "HOSTRUSTC": wrappers["rustc"],
            "RUSTDOC": wrappers["rustdoc"],
            "RUSTFMT": wrappers["rustfmt"],
            "CLIPPY_DRIVER": wrappers["clippy-driver"],
            "RUST_LIB_SRC": _rust_lib_src(rustc_version),
        }
        make_vars.update(rust_commands)
        installed = _run_text(["rustup", "run", rustc_version, "rustc", "--version"]) is not None
        if not installed:
            missing.append(f"rustup toolchain {rustc_version}")
        resolved["rustc_version_text"] = _run_text([rust_commands["RUSTC"], "--version"])
        resolved["rust_lib_src_exists"] = Path(rust_commands["RUST_LIB_SRC"]).exists()
        resolved["rust_wrappers"] = wrappers

    if bindgen_version:
        bindgen_bin = _bindgen_root(cfg, bindgen_version) / "bin" / "bindgen"
        make_vars["BINDGEN"] = str(bindgen_bin)
        if not bindgen_bin.exists():
            missing.append(f"bindgen {bindgen_version}")
        resolved["bindgen_version_text"] = _run_text([str(bindgen_bin), "--version"], env=env_vars) if bindgen_bin.exists() else None
        resolved["bindgen_bin_exists"] = bindgen_bin.exists()
        probe = cfg.linux_tree / "scripts/rust_is_available_bindgen_libclang.h"
        resolved["bindgen_libclang_probe_text"] = _run_text([str(bindgen_bin), str(probe)], env=env_vars) if bindgen_bin.exists() and probe.exists() else None
    if not _command_available("rustup"):
        missing.append("rustup")
    if not _command_available("cargo"):
        missing.append("cargo")
    compatibility_issues = _compatibility_issues(bindgen_version, resolved)

    return {
        "version_id": version_row["version_id"],
        "ref": ref,
        "git_commit": version_row.get("git_commit"),
        "tag": version_row.get("tag"),
        "date": version_row.get("date"),
        "required": {"rustc": rustc_version, "bindgen": bindgen_version},
        "make_vars": make_vars,
        "env_vars": env_vars,
        "resolved": resolved,
        "compatibility_issues": compatibility_issues,
        "missing": sorted(set(missing)),
    }


def bootstrap_commands(cfg: Config, entries: list[dict[str, Any]]) -> list[list[str]]:
    rust_versions = sorted({entry["required"].get("rustc") for entry in entries if entry["required"].get("rustc")}, key=_version_key)
    commands: list[list[str]] = [
        ["rustup", "toolchain", "install", version, "--profile", "minimal", "--component", "rust-src", "--component", "rustfmt", "--component", "clippy"]
        for version in rust_versions
    ]
    bindgen_to_rust: dict[str, str] = {}
    for entry in entries:
        bindgen = entry["required"].get("bindgen")
        rustc = entry["required"].get("rustc")
        if bindgen and rustc and bindgen not in bindgen_to_rust:
            bindgen_to_rust[bindgen] = rustc
    for bindgen, rustc in sorted(bindgen_to_rust.items(), key=lambda item: _version_key(item[0])):
        commands.append(
            [
                "cargo",
                f"+{rustc}",
                "install",
                "--locked",
                "--version",
                bindgen,
                _bindgen_crate_name(bindgen),
                "--root",
                str(_bindgen_root(cfg, bindgen)),
            ]
        )
    return commands


def write_toolchain_matrix(cfg: Config, refs: list[str], version_rows: list[dict[str, Any]]) -> dict[str, Any]:
    cfg.ensure_dirs()
    entries = [make_toolchain_spec(cfg, ref, row) for ref, row in zip(refs, version_rows, strict=True)]
    matrix = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "linux_tree": str(cfg.linux_tree),
        "entries": entries,
        "bootstrap_commands": bootstrap_commands(cfg, entries),
        "missing": sorted({item for entry in entries for item in entry["missing"]}),
        "official_sources": [
            "https://docs.kernel.org/rust/quick-start.html",
            "https://docs.kernel.org/process/changes.html",
            "https://rust-for-linux.com/rust-version-policy",
        ],
    }
    path = cfg.data_dir / "toolchain_matrix.json"
    path.write_text(json.dumps(matrix, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    matrix["written_to"] = str(path)
    return matrix


def load_toolchain_matrix(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def execute_bootstrap_commands(commands: list[list[str]]) -> list[dict[str, Any]]:
    actions: list[dict[str, Any]] = []
    env = os.environ.copy()
    for command in commands:
        if reason := _skip_reason(command):
            actions.append({"command": command, "returncode": 0, "output": reason, "skipped": True})
            continue
        action = _execute_bootstrap_command(command, env)
        actions.append(action)
        if _needs_modern_cargo_fallback(command, action):
            fallback = ["cargo", *command[2:]]
            fallback_action = _execute_bootstrap_command(fallback, env)
            fallback_action["fallback_for"] = command
            actions.append(fallback_action)
            action = fallback_action
        if _needs_old_bindgen_package_fallback(command, action):
            fallback = [*command]
            fallback[fallback.index("bindgen-cli")] = "bindgen"
            fallback_action = _execute_bootstrap_command(fallback, env)
            fallback_action["fallback_for"] = command
            actions.append(fallback_action)
    return actions


def _skip_reason(command: list[str]) -> str | None:
    if command[:3] == ["rustup", "toolchain", "install"] and len(command) >= 4:
        version = command[3]
        if _run_text(["rustup", "run", version, "rustc", "--version"]):
            return f"rustup toolchain {version} already installed"
    if command and command[0] == "cargo" and "--root" in command and "--version" in command:
        root = Path(command[command.index("--root") + 1])
        version = command[command.index("--version") + 1]
        bindgen = root / "bin" / "bindgen"
        output = _run_text([str(bindgen), "--version"]) if bindgen.exists() else None
        if output and output.strip() == f"bindgen {version}":
            return f"bindgen-cli {version} already installed at {root}"
    return None


def _execute_bootstrap_command(command: list[str], env: dict[str, str]) -> dict[str, Any]:
    try:
        proc = subprocess.run(
            command,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
            timeout=3600,
            env=env,
        )
        return {"command": command, "returncode": proc.returncode, "output": proc.stdout[-12000:]}
    except subprocess.TimeoutExpired as exc:
        output = exc.stdout if isinstance(exc.stdout, str) else ""
        return {"command": command, "returncode": 124, "output": output[-12000:], "timed_out": True}


def _needs_modern_cargo_fallback(command: list[str], action: dict[str, Any]) -> bool:
    return (
        len(command) > 1
        and command[0] == "cargo"
        and command[1].startswith("+")
        and action.get("returncode") != 0
        and "HTTP-based registries requires" in str(action.get("output", ""))
    )


def _needs_old_bindgen_package_fallback(command: list[str], action: dict[str, Any]) -> bool:
    return (
        command
        and command[0] == "cargo"
        and "bindgen-cli" in command
        and action.get("returncode") != 0
        and "could not find `bindgen-cli`" in str(action.get("output", ""))
    )


def _bindgen_crate_name(version: str) -> str:
    return "bindgen" if _version_key(version) < (0, 60, 0) else "bindgen-cli"


def _version_key(value: str | None) -> tuple[int, ...]:
    if not value:
        return ()
    return tuple(int(part) for part in value.split("."))
