from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path
from typing import Any

from .config import Config
from .db import connect, initialize, upsert_many
from .gitutil import git_output, run_git


RELEASE_RE = re.compile(r"^v(?P<major>\d+)\.(?P<minor>\d+)$")


def release_key(ref: str) -> tuple[int, int]:
    match = RELEASE_RE.match(ref)
    if not match:
        return (-1, -1)
    return (int(match.group("major")), int(match.group("minor")))


def is_release_tag(ref: str, start: str = "v6.1") -> bool:
    key = release_key(ref)
    return key >= release_key(start)


def sanitize_ref(ref: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", ref).strip("_") or "ref"


def fetch_tags(cfg: Config) -> dict[str, Any]:
    proc = run_git(cfg.linux_tree, ["fetch", "--tags"], check=False)
    return {"returncode": proc.returncode, "stdout": proc.stdout[-4000:], "stderr": proc.stderr[-4000:]}


def select_versions(
    cfg: Config,
    start: str = "v6.1",
    include_head: bool = True,
    fetch: bool = False,
    limit: int | None = None,
) -> dict[str, Any]:
    cfg.ensure_dirs()
    fetch_result = fetch_tags(cfg) if fetch else None
    tags = git_output(cfg.linux_tree, ["tag", "--list", "v*"])
    refs = sorted((tag for tag in tags.splitlines() if is_release_tag(tag, start=start)), key=release_key)
    if limit and limit > 0:
        refs = refs[-limit:]
    if include_head:
        head = git_output(cfg.linux_tree, ["rev-parse", "--short=12", "HEAD"], default="HEAD")
        refs.append(f"HEAD:{head}")
    rows = [version_row(cfg.linux_tree, ref) for ref in refs]
    conn = connect(cfg.database)
    initialize(conn)
    upsert_many(conn, "versions", rows)
    path = cfg.data_dir / "versions.json"
    path.write_text(
        json.dumps({"start": start, "fetch": fetch_result, "versions": rows}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return {
        "database": str(cfg.database),
        "version_file": str(path),
        "versions": len(rows),
        "refs": refs,
        "fetch": fetch_result,
    }


def version_row(repo: Path, ref: str) -> dict[str, Any]:
    git_ref = ref.split(":", 1)[0] if ref.startswith("HEAD:") else ref
    commit = git_output(repo, ["rev-parse", git_ref], default=git_ref)
    date = git_output(repo, ["show", "-s", "--format=%cI", git_ref], default="")
    tag = ref if RELEASE_RE.match(ref) else None
    return {
        "version_id": sanitize_ref(ref),
        "git_commit": commit,
        "tag": tag,
        "date": date,
        "arch": "x86_64",
        "config_hash": None,
        "rustc_version": None,
        "clang_version": None,
        "bindgen_version": None,
    }


def ensure_worktree(cfg: Config, ref: str) -> dict[str, Any]:
    cfg.ensure_dirs()
    version_id = sanitize_ref(ref)
    path = cfg.worktree_root / version_id
    if path.exists() and (path / ".git").exists():
        commit = git_output(path, ["rev-parse", "HEAD"])
        return {"version_id": version_id, "ref": ref, "path": str(path), "commit": commit, "created": False}
    if path.exists():
        raise FileExistsError(f"worktree path exists but is not a git worktree: {path}")
    git_ref = ref.split(":", 1)[0] if ref.startswith("HEAD:") else ref
    proc = subprocess.run(
        ["git", "-C", str(cfg.linux_tree), "worktree", "add", "--detach", str(path), git_ref],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if proc.returncode != 0:
        return {"version_id": version_id, "ref": ref, "path": str(path), "created": False, "error": proc.stdout[-4000:]}
    commit = git_output(path, ["rev-parse", "HEAD"])
    return {"version_id": version_id, "ref": ref, "path": str(path), "commit": commit, "created": True}
