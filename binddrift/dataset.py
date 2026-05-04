from __future__ import annotations

import json
import subprocess
from datetime import datetime, timezone
from typing import Any

from .config import Config
from .db import connect, initialize, upsert_many
from .environment import capture_environment
from .gitutil import git_output, run_git


RUST_PATH_PREFIXES = ("rust/",)
C_API_EXTENSIONS = (".h", ".c")
C_API_PREFIXES = ("include/", "drivers/", "fs/", "kernel/", "mm/", "net/", "block/", "ipc/", "security/")


def _is_rust_related(files: list[str]) -> bool:
    return any(path.startswith(RUST_PATH_PREFIXES) or path.endswith(".rs") for path in files)


def _is_c_api_related(files: list[str]) -> bool:
    return any(path.endswith(C_API_EXTENSIONS) and path.startswith(C_API_PREFIXES) for path in files)


def current_version_row(cfg: Config) -> dict[str, Any]:
    env = capture_environment(cfg)
    return {
        "version_id": env["linux_describe"] or env["linux_commit"][:12],
        "git_commit": env["linux_commit"],
        "tag": env["linux_describe"] if env["linux_describe"].startswith("v") else None,
        "date": datetime.now(timezone.utc).isoformat(),
        "arch": env["arch"],
        "config_hash": env["config_hash"],
        "rustc_version": env["tools"]["rustc"].get("version") if env["tools"]["rustc"].get("available") else None,
        "clang_version": env["tools"]["clang"].get("version") if env["tools"]["clang"].get("available") else None,
        "bindgen_version": env["tools"]["bindgen"].get("version") if env["tools"]["bindgen"].get("available") else None,
    }


def _commit_files(cfg: Config, commit: str) -> list[str]:
    out = git_output(cfg.linux_tree, ["show", "--name-only", "--format=", commit])
    return [line for line in out.splitlines() if line.strip()]


def collect_commits(cfg: Config, limit: int = 200, ref: str = "HEAD") -> list[dict[str, Any]]:
    fmt = "%H%x1f%P%x1f%aI%x1f%an%x1f%s%x1e%B%x1d"
    proc = run_git(cfg.linux_tree, ["log", f"--max-count={limit}", f"--format={fmt}", ref])
    rows: list[dict[str, Any]] = []
    for record in proc.stdout.split("\x1d"):
        record = record.strip()
        if not record:
            continue
        head, _, body = record.partition("\x1e")
        parts = head.split("\x1f")
        if len(parts) < 5:
            continue
        commit_id, parents, date, author, subject = parts[:5]
        files = _commit_files(cfg, commit_id)
        rows.append(
            {
                "commit_id": commit_id,
                "parent_id": parents.split()[0] if parents else None,
                "date": date,
                "author": author,
                "subject": subject,
                "message": body.strip(),
                "changed_files": json.dumps(files, sort_keys=True),
                "is_rust_related": int(_is_rust_related(files)),
                "is_c_api_related": int(_is_c_api_related(files)),
            }
        )
    return rows


def fetch_tags(cfg: Config) -> None:
    subprocess.run(["git", "-C", str(cfg.linux_tree), "fetch", "--tags"], check=True)


def extract_dataset(cfg: Config, limit: int = 200, fetch: bool = False) -> dict[str, Any]:
    cfg.ensure_dirs()
    if fetch:
        fetch_tags(cfg)
    conn = connect(cfg.database)
    initialize(conn)
    version = current_version_row(cfg)
    commits = collect_commits(cfg, limit=limit)
    upsert_many(conn, "versions", [version])
    upsert_many(conn, "commits", commits)
    return {
        "database": str(cfg.database),
        "versions": 1,
        "commits": len(commits),
        "rust_related_commits": sum(row["is_rust_related"] for row in commits),
        "c_api_related_commits": sum(row["is_c_api_related"] for row in commits),
    }
