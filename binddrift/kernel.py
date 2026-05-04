from __future__ import annotations

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .config import Config
from .gitutil import git_output


def default_version_id(cfg: Config) -> str:
    return git_output(cfg.linux_tree, ["describe", "--always", "--dirty"], default="worktree")


def prepare_kernel_build(cfg: Config, version_id: str | None = None, run_make: bool = False) -> dict[str, Any]:
    cfg.ensure_dirs()
    vid = version_id or default_version_id(cfg)
    objtree = cfg.build_root / vid
    objtree.mkdir(parents=True, exist_ok=True)
    manifest = {
        "version_id": vid,
        "linux_tree": str(cfg.linux_tree),
        "objtree": str(objtree),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "generated_bindings": [
            str(objtree / "rust/bindings/bindings_generated.rs"),
            str(objtree / "rust/bindings/bindings_helpers_generated.rs"),
        ],
        "commands": [],
    }
    if run_make:
        cmd = ["make", f"O={objtree}", "LLVM=1", "rustavailable"]
        proc = subprocess.run(cmd, cwd=cfg.linux_tree, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        manifest["commands"].append({"cmd": cmd, "returncode": proc.returncode, "output": proc.stdout[-8000:]})
    path = objtree / "binddrift-build.json"
    path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    manifest["manifest"] = str(path)
    return manifest
