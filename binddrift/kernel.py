from __future__ import annotations

import json
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


def default_version_id(cfg: Config) -> str:
    return git_output(cfg.linux_tree, ["describe", "--always", "--dirty"], default="worktree")


def _run_make(linux_tree: Path, objtree: Path, targets: list[str], timeout: int = 1800) -> dict[str, Any]:
    cmd = ["make", f"O={objtree}", "LLVM=1", *targets]
    try:
        proc = subprocess.run(
            cmd,
            cwd=linux_tree,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
            timeout=timeout,
        )
        return {"cmd": cmd, "returncode": proc.returncode, "output": proc.stdout[-16000:]}
    except subprocess.TimeoutExpired as exc:
        output = exc.stdout if isinstance(exc.stdout, str) else ""
        return {"cmd": cmd, "returncode": 124, "output": output[-16000:], "timed_out": True}


def _sha256(path: Path) -> str | None:
    if not path.exists():
        return None
    import hashlib

    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _manifest(cfg: Config, version_id: str, linux_tree: Path, objtree: Path) -> dict[str, Any]:
    config_path = objtree / ".config"
    return {
        "version_id": version_id,
        "linux_tree": str(linux_tree),
        "linux_commit": git_output(linux_tree, ["rev-parse", "HEAD"], default=""),
        "objtree": str(objtree),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "config": str(config_path),
        "config_hash": _sha256(config_path),
        "generated_bindings": [str(objtree / target) for target in BINDING_TARGETS],
        "commands": [],
    }


def _write_manifest(objtree: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    manifest["config_hash"] = _sha256(Path(manifest["config"]))
    path = objtree / "binddrift-build.json"
    path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    manifest["manifest"] = str(path)
    return manifest


def prepare_kernel_build(
    cfg: Config,
    version_id: str | None = None,
    run_make: bool = False,
    configure: bool = False,
    linux_tree: Path | None = None,
) -> dict[str, Any]:
    cfg.ensure_dirs()
    tree = linux_tree or cfg.linux_tree
    vid = version_id or default_version_id(cfg)
    objtree = cfg.build_root / vid
    objtree.mkdir(parents=True, exist_ok=True)
    manifest = _manifest(cfg, vid, tree, objtree)
    if run_make:
        manifest["commands"].append(_run_make(tree, objtree, ["rustavailable"], timeout=180))
    if configure:
        manifest["commands"].extend(
            [
                _run_make(tree, objtree, ["x86_64_defconfig"], timeout=600),
                _run_make(tree, objtree, ["rust.config"], timeout=600),
                _run_make(tree, objtree, ["olddefconfig"], timeout=600),
            ]
        )
    return _write_manifest(objtree, manifest)


def build_kernel_bindings(
    cfg: Config,
    version_id: str | None = None,
    configure: bool = False,
    linux_tree: Path | None = None,
) -> dict[str, Any]:
    tree = linux_tree or cfg.linux_tree
    manifest = prepare_kernel_build(cfg, version_id=version_id, configure=configure, linux_tree=tree)
    objtree = Path(manifest["objtree"])
    manifest["commands"].append(_run_make(tree, objtree, BINDING_TARGETS, timeout=1800))
    outputs = []
    for target in BINDING_TARGETS:
        path = objtree / target
        outputs.append({"path": str(path), "exists": path.exists(), "size": path.stat().st_size if path.exists() else 0})
    manifest["binding_outputs"] = outputs
    return _write_manifest(objtree, manifest)
