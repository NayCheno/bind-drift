from __future__ import annotations

from pathlib import Path
from typing import Any

from binddrift.config import Config


LOCAL_PATH_MARKERS = ("/home/", "/Users/", "/tmp/")


def repo_relative(cfg: Config, path: Path) -> str:
    try:
        return str(path.resolve().relative_to(cfg.repo_root))
    except ValueError:
        return str(path.resolve())


def sanitize_local_paths(value: Any, cfg: Config) -> Any:
    if isinstance(value, dict):
        return {key: sanitize_local_paths(item, cfg) for key, item in value.items()}
    if isinstance(value, list):
        return [sanitize_local_paths(item, cfg) for item in value]
    if isinstance(value, str):
        return _sanitize_string(value, cfg)
    return value


def _sanitize_string(value: str, cfg: Config) -> str:
    replacements = {
        str(cfg.repo_root): ".",
        str(cfg.state_dir): ".binddrift",
        str(cfg.data_dir): "data",
        str(cfg.database): ".binddrift/binddrift.sqlite3",
        str(cfg.linux_tree): "vendor/linux",
    }
    out = value
    for old, new in sorted(replacements.items(), key=lambda item: len(item[0]), reverse=True):
        out = out.replace(old, new)
    return out
