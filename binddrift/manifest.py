from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Any

from binddrift.config import Config
from binddrift.gitutil import git_output


def write_manifest(cfg: Config, verification: dict[str, Any]) -> dict[str, Any]:
    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "repo_commit": git_output(cfg.repo_root, ["rev-parse", "HEAD"]),
        "linux_commit": git_output(cfg.linux_tree, ["rev-parse", "HEAD"]),
        "step_commits": git_output(cfg.repo_root, ["log", "--oneline", "--grep=^step "]).splitlines(),
        "commands": verification,
        "known_limitations": [
            "Generated Rust bindings require a Rust-enabled kernel object tree.",
            "Tier 2 detectors are indicator-based warnings, not proof of bugs.",
            "Pilot evaluation has no precision/recall until manual labels are filled.",
        ],
    }
    path = cfg.data_dir / "artifact_manifest.json"
    cfg.data_dir.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    manifest["path"] = str(path)
    return manifest
