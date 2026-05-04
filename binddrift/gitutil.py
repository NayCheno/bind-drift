from __future__ import annotations

import subprocess
from pathlib import Path


def run_git(repo: Path, args: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        check=check,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def git_output(repo: Path, args: list[str], default: str = "") -> str:
    proc = run_git(repo, args, check=False)
    if proc.returncode != 0:
        return default
    return proc.stdout.strip()


def is_git_repo(repo: Path) -> bool:
    return (repo / ".git").exists() or bool(git_output(repo, ["rev-parse", "--git-dir"]))
