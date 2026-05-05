from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Config:
    repo_root: Path
    linux_tree: Path
    state_dir: Path
    build_root: Path
    worktree_root: Path
    data_dir: Path
    database: Path
    drift_facts_jsonl: Path
    warnings_jsonl: Path
    report_md: Path

    @classmethod
    def from_args(
        cls,
        repo_root: str | Path = ".",
        linux_tree: str | Path = "vendor/linux",
        state_dir: str | Path = ".binddrift",
        data_dir: str | Path = "data",
    ) -> "Config":
        root = Path(repo_root).resolve()
        linux = (root / linux_tree).resolve()
        state = (root / state_dir).resolve()
        data = (root / data_dir).resolve()
        return cls(
            repo_root=root,
            linux_tree=linux,
            state_dir=state,
            build_root=state / "build",
            worktree_root=state / "worktrees",
            data_dir=data,
            database=state / "binddrift.sqlite3",
            drift_facts_jsonl=data / "drift_facts.jsonl",
            warnings_jsonl=data / "warnings.jsonl",
            report_md=data / "warnings.md",
        )

    def ensure_dirs(self) -> None:
        for path in (self.state_dir, self.build_root, self.worktree_root, self.data_dir):
            path.mkdir(parents=True, exist_ok=True)
