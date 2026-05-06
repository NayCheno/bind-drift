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


def sanitize_local_path_text(text: str, cfg: Config) -> str:
    return _sanitize_string(text, cfg)


def sanitize_local_path_file(path: Path, cfg: Config) -> bool:
    text = path.read_text(encoding="utf-8", errors="ignore")
    sanitized = sanitize_local_path_text(text, cfg)
    if sanitized == text:
        return False
    path.write_text(sanitized, encoding="utf-8")
    return True


def sanitize_local_path_tree(
    root: Path,
    cfg: Config,
    *,
    suffixes: set[str] | None = None,
) -> list[str]:
    suffixes = suffixes or {".json", ".jsonl", ".csv", ".md"}
    changed: list[str] = []
    if not root.exists():
        return changed
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix not in suffixes:
            continue
        if sanitize_local_path_file(path, cfg):
            changed.append(repo_relative(cfg, path))
    return changed


def _sanitize_string(value: str, cfg: Config) -> str:
    replacements = {
        str(cfg.repo_root): ".",
        str(cfg.state_dir): ".binddrift",
        str(cfg.data_dir): "data",
        str(cfg.database): ".binddrift/binddrift.sqlite3",
        str(cfg.linux_tree): "vendor/linux",
        str(Path.home()): "$HOME",
        "/tmp/": "$TMPDIR/",
    }
    out = value
    for old, new in sorted(replacements.items(), key=lambda item: len(item[0]), reverse=True):
        out = out.replace(old, new)
    return out
