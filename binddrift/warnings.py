from __future__ import annotations

import json
import hashlib
from pathlib import Path
from typing import Any

from .config import Config


def write_warnings(cfg: Config, warnings: list[dict[str, Any]]) -> Path:
    cfg.ensure_dirs()
    return write_jsonl(cfg.warnings_jsonl, warnings)


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


def eligible_for_main_warning(warning: dict[str, Any]) -> bool:
    old_version = warning.get("old_version") or (warning.get("c_side") or {}).get("old_version")
    new_version = warning.get("new_version") or (warning.get("c_side") or {}).get("new_version")
    return bool(
        old_version
        and new_version
        and old_version != new_version
        and warning.get("pair_id")
        and warning.get("promotion_status") == "promoted"
    )


def split_main_and_single_version(warnings: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    main: list[dict[str, Any]] = []
    single_version: list[dict[str, Any]] = []
    for warning in warnings:
        if eligible_for_main_warning(warning):
            main.append(warning)
        else:
            old_version = warning.get("old_version") or (warning.get("c_side") or {}).get("old_version")
            pair_id = warning.get("pair_id")
            if old_version is None or not pair_id:
                single_version.append(warning)
    return main, single_version


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for row in rows:
            item = dict(row)
            ensure_warning_uid(item)
            fh.write(json.dumps(item, sort_keys=True) + "\n")
    return path


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
