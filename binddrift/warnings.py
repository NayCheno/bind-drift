from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .config import Config


def write_warnings(cfg: Config, warnings: list[dict[str, Any]]) -> Path:
    cfg.ensure_dirs()
    with cfg.warnings_jsonl.open("w", encoding="utf-8") as fh:
        for warning in warnings:
            fh.write(json.dumps(warning, sort_keys=True) + "\n")
    return cfg.warnings_jsonl


def read_warnings(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def warning_id(index: int) -> str:
    return f"W-{index:06d}"
