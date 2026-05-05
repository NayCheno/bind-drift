from __future__ import annotations

import json
import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .config import Config
from .gitutil import git_output


BINDING_TARGETS = [
    "rust/bindings/bindings_generated.rs",
    "rust/bindings/bindings_helpers_generated.rs",
]
BINDING_BUILD_TARGETS = ["rust/"]


def default_version_id(cfg: Config) -> str:
    return git_output(cfg.linux_tree, ["describe", "--always", "--dirty"], default="worktree")


def _run_make(
    linux_tree: Path,
    objtree: Path,
    targets: list[str],
    timeout: int = 1800,
    arch: str = "x86_64",
    make_vars: dict[str, str] | None = None,
    env_vars: dict[str, str] | None = None,
    log_file: Path | None = None,
) -> dict[str, Any]:
    make_vars = make_vars or {}
    cmd = ["make", f"O={objtree}"]
    if "LLVM" not in make_vars:
        cmd.append("LLVM=1")
    if arch != "x86_64":
        cmd.append(f"ARCH={arch}")
    for name, value in sorted(make_vars.items()):
        cmd.append(f"{name}={value}")
    cmd.extend(targets)
    try:
        proc = subprocess.run(
            cmd,
            cwd=linux_tree,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
            timeout=timeout,
            env=_build_env(env_vars),
        )
        if log_file:
            log_file.parent.mkdir(parents=True, exist_ok=True)
            log_file.write_text(proc.stdout, encoding="utf-8", errors="replace")
        return {
            "cmd": cmd,
            "returncode": proc.returncode,
            "output": proc.stdout[-16000:],
            "log_path": str(log_file) if log_file else None,
        }
    except subprocess.TimeoutExpired as exc:
        output = exc.stdout if isinstance(exc.stdout, str) else ""
        if log_file:
            log_file.parent.mkdir(parents=True, exist_ok=True)
            log_file.write_text(output, encoding="utf-8", errors="replace")
        return {
            "cmd": cmd,
            "returncode": 124,
            "output": output[-16000:],
            "timed_out": True,
            "log_path": str(log_file) if log_file else None,
        }


def _run_config_script(
    linux_tree: Path,
    objtree: Path,
    args: list[str],
    timeout: int = 120,
    env_vars: dict[str, str] | None = None,
    log_file: Path | None = None,
) -> dict[str, Any]:
    cmd = [str(linux_tree / "scripts/config"), "--file", str(objtree / ".config"), *args]
    try:
        proc = subprocess.run(
            cmd,
            cwd=linux_tree,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
            timeout=timeout,
            env=_build_env(env_vars),
        )
        if log_file:
            log_file.parent.mkdir(parents=True, exist_ok=True)
            log_file.write_text(proc.stdout, encoding="utf-8", errors="replace")
        return {
            "cmd": cmd,
            "returncode": proc.returncode,
            "output": proc.stdout[-8000:],
            "log_path": str(log_file) if log_file else None,
        }
    except subprocess.TimeoutExpired as exc:
        output = exc.stdout if isinstance(exc.stdout, str) else ""
        if log_file:
            log_file.parent.mkdir(parents=True, exist_ok=True)
            log_file.write_text(output, encoding="utf-8", errors="replace")
        return {
            "cmd": cmd,
            "returncode": 124,
            "output": output[-8000:],
            "timed_out": True,
            "log_path": str(log_file) if log_file else None,
        }


def _sha256(path: Path) -> str | None:
    if not path.exists():
        return None
    import hashlib

    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _build_env(env_vars: dict[str, str] | None) -> dict[str, str]:
    env = os.environ.copy()
    env.update(env_vars or {})
    return env


def binding_output_records(objtree: Path) -> list[dict[str, Any]]:
    outputs = []
    for target in BINDING_TARGETS:
        path = objtree / target
        outputs.append(
            {
                "path": str(path),
                "exists": path.exists(),
                "size": path.stat().st_size if path.exists() else 0,
                "sha256": _sha256(path),
            }
        )
    return outputs


def _safe_log_label(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "-", value).strip("-")[:80] or "command"


def _next_log_file(manifest: dict[str, Any], objtree: Path, label: str) -> Path:
    index = len(manifest["commands"]) + 1
    return objtree / "binddrift-logs" / f"{index:02d}-{_safe_log_label(label)}.log"


def _append_make(
    manifest: dict[str, Any],
    linux_tree: Path,
    objtree: Path,
    targets: list[str],
    timeout: int = 1800,
    arch: str = "x86_64",
    make_vars: dict[str, str] | None = None,
    env_vars: dict[str, str] | None = None,
) -> None:
    label = "-".join(targets)
    manifest["commands"].append(
        _run_make(
            linux_tree,
            objtree,
            targets,
            timeout=timeout,
            arch=arch,
            make_vars=make_vars,
            env_vars=env_vars,
            log_file=_next_log_file(manifest, objtree, label),
        )
    )


def _append_config_script(
    manifest: dict[str, Any],
    linux_tree: Path,
    objtree: Path,
    args: list[str],
    timeout: int = 120,
    env_vars: dict[str, str] | None = None,
) -> None:
    manifest["commands"].append(
        _run_config_script(
            linux_tree,
            objtree,
            args,
            timeout=timeout,
            env_vars=env_vars,
            log_file=_next_log_file(manifest, objtree, "scripts-config"),
        )
    )


def _manifest(
    cfg: Config,
    version_id: str,
    linux_tree: Path,
    objtree: Path,
    arch: str = "x86_64",
    toolchain: dict[str, Any] | None = None,
) -> dict[str, Any]:
    config_path = objtree / ".config"
    return {
        "version_id": version_id,
        "linux_tree": str(linux_tree),
        "linux_commit": git_output(linux_tree, ["rev-parse", "HEAD"], default=""),
        "objtree": str(objtree),
        "arch": arch,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "config": str(config_path),
        "config_hash": _sha256(config_path),
        "generated_bindings": [str(objtree / target) for target in BINDING_TARGETS],
        "toolchain": toolchain or {},
        "commands": [],
    }


def _write_manifest(objtree: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    manifest["config_hash"] = _sha256(Path(manifest["config"]))
    manifest["binding_outputs"] = binding_output_records(objtree)
    path = objtree / "binddrift-build.json"
    path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    manifest["manifest"] = str(path)
    return manifest


def _rustc_required(toolchain: dict[str, Any] | None) -> str | None:
    return ((toolchain or {}).get("required") or {}).get("rustc")


def _version_lt(left: str | None, right: str) -> bool:
    if not left:
        return False
    return tuple(int(part) for part in left.split(".")) < tuple(int(part) for part in right.split("."))


def _rust_config_normalization(toolchain: dict[str, Any] | None) -> list[str]:
    args: list[str] = ["-d", "WERROR"]
    if _version_lt(_rustc_required(toolchain), "1.81.0"):
        args.extend(["-d", "MITIGATION_CALL_DEPTH_TRACKING", "-d", "CALL_THUNKS", "-d", "CALL_PADDING"])
    args.extend(["-e", "RUST"])
    return args


def prepare_kernel_build(
    cfg: Config,
    version_id: str | None = None,
    run_make: bool = False,
    configure: bool = False,
    linux_tree: Path | None = None,
    arch: str = "x86_64",
    toolchain: dict[str, Any] | None = None,
) -> dict[str, Any]:
    cfg.ensure_dirs()
    tree = linux_tree or cfg.linux_tree
    vid = version_id or default_version_id(cfg)
    objtree = cfg.build_root / vid
    objtree.mkdir(parents=True, exist_ok=True)
    manifest = _manifest(cfg, vid, tree, objtree, arch=arch, toolchain=toolchain)
    make_vars = (toolchain or {}).get("make_vars") or None
    env_vars = (toolchain or {}).get("env_vars") or None
    if run_make:
        _append_make(manifest, tree, objtree, ["rustavailable"], timeout=180, arch=arch, make_vars=make_vars, env_vars=env_vars)
    if configure:
        defconfig = "x86_64_defconfig" if arch == "x86_64" else "defconfig"
        normalize_args = _rust_config_normalization(toolchain)
        _append_make(manifest, tree, objtree, [defconfig], timeout=600, arch=arch, make_vars=make_vars, env_vars=env_vars)
        _append_make(manifest, tree, objtree, ["rust.config"], timeout=600, arch=arch, make_vars=make_vars, env_vars=env_vars)
        if normalize_args:
            _append_config_script(manifest, tree, objtree, normalize_args, env_vars=env_vars)
        _append_make(manifest, tree, objtree, ["olddefconfig"], timeout=600, arch=arch, make_vars=make_vars, env_vars=env_vars)
    return _write_manifest(objtree, manifest)


def build_kernel_bindings(
    cfg: Config,
    version_id: str | None = None,
    configure: bool = False,
    linux_tree: Path | None = None,
    arch: str = "x86_64",
    toolchain: dict[str, Any] | None = None,
) -> dict[str, Any]:
    tree = linux_tree or cfg.linux_tree
    manifest = prepare_kernel_build(cfg, version_id=version_id, configure=configure, linux_tree=tree, arch=arch, toolchain=toolchain)
    objtree = Path(manifest["objtree"])
    make_vars = (toolchain or {}).get("make_vars") or None
    env_vars = (toolchain or {}).get("env_vars") or None
    _append_make(manifest, tree, objtree, BINDING_BUILD_TARGETS, timeout=1800, arch=arch, make_vars=make_vars, env_vars=env_vars)
    return _write_manifest(objtree, manifest)
