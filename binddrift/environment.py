from __future__ import annotations

import hashlib
import json
import platform
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .config import Config
from .gitutil import git_output


def _tool_version(command: list[str]) -> dict[str, Any]:
    exe = shutil.which(command[0])
    if not exe:
        return {"available": False, "command": command[0]}
    proc = subprocess.run(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
    first_line = proc.stdout.splitlines()[0] if proc.stdout else ""
    return {
        "available": proc.returncode == 0,
        "command": command[0],
        "path": exe,
        "version": first_line,
        "returncode": proc.returncode,
    }


def _sha256(path: Path) -> str | None:
    if not path.exists():
        return None
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def capture_environment(cfg: Config) -> dict[str, Any]:
    linux = cfg.linux_tree
    commit = git_output(linux, ["rev-parse", "HEAD"])
    describe = git_output(linux, ["describe", "--always", "--dirty"], default=commit)
    branch = git_output(linux, ["rev-parse", "--abbrev-ref", "HEAD"])
    status = git_output(linux, ["status", "--short"])
    config_path = linux / ".config"
    return {
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "repo_root": str(cfg.repo_root),
        "linux_tree": str(linux),
        "linux_commit": commit,
        "linux_describe": describe,
        "linux_branch": branch,
        "linux_dirty": bool(status.strip()),
        "arch": platform.machine(),
        "platform": platform.platform(),
        "config_path": str(config_path),
        "config_hash": _sha256(config_path),
        "generated_bindings_note": "Rust-for-Linux generated bindings are expected under OBJTREE/rust/bindings, not the source tree.",
        "tools": {
            "make": _tool_version(["make", "--version"]),
            "clang": _tool_version(["clang", "--version"]),
            "rustc": _tool_version(["rustc", "--version"]),
            "rustfmt": _tool_version(["rustfmt", "--version"]),
            "bindgen": _tool_version(["bindgen", "--version"]),
            "python": {
                "available": True,
                "command": "python",
                "version": platform.python_version(),
            },
        },
    }


def write_environment(cfg: Config, metadata: dict[str, Any]) -> Path:
    cfg.ensure_dirs()
    path = cfg.data_dir / "environment.json"
    path.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path
