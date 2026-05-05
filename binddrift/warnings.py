from __future__ import annotations

import json
import hashlib
from pathlib import Path
from typing import Any

from .config import Config


def write_warnings(cfg: Config, warnings: list[dict[str, Any]]) -> Path:
    cfg.ensure_dirs()
    with cfg.warnings_jsonl.open("w", encoding="utf-8") as fh:
        for warning in warnings:
            row = dict(warning)
            ensure_warning_uid(row)
            fh.write(json.dumps(row, sort_keys=True) + "\n")
    return cfg.warnings_jsonl


def write_drift_facts(cfg: Config, facts: list[dict[str, Any]]) -> Path:
    cfg.ensure_dirs()
    with cfg.drift_facts_jsonl.open("w", encoding="utf-8") as fh:
        for fact in facts:
            fh.write(json.dumps(fact, sort_keys=True) + "\n")
    return cfg.drift_facts_jsonl


def read_warnings(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def warning_id(index: int) -> str:
    return f"W-{index:06d}"


def fact_id(index: int) -> str:
    return f"F-{index:06d}"


def _stable_value(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (dict, list, tuple)):
        return json.dumps(value, sort_keys=True, separators=(",", ":"))
    return str(value)


def make_warning_uid(warning: dict[str, Any]) -> str:
    c_side = warning.get("c_side") or {}
    parts = [
        warning.get("run_id"),
        warning.get("pair_id"),
        warning.get("old_version") or c_side.get("old_version"),
        warning.get("new_version") or c_side.get("new_version"),
        warning.get("type"),
        c_side.get("symbol"),
        c_side.get("indicator"),
        c_side.get("old", c_side.get("old_indicators")),
        c_side.get("new", c_side.get("new_indicators")),
    ]
    payload = "|".join(_stable_value(part) for part in parts)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def ensure_warning_uid(warning: dict[str, Any]) -> str:
    uid = str(warning.get("warning_uid") or make_warning_uid(warning))
    warning["warning_uid"] = uid
    return uid
