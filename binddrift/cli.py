from __future__ import annotations

import argparse
import json
from typing import Callable

from . import __version__
from .config import Config
from .dataset import extract_dataset
from .environment import capture_environment, write_environment


Command = Callable[[argparse.Namespace, Config], int]


def _config(args: argparse.Namespace) -> Config:
    return Config.from_args(
        repo_root=args.repo_root,
        linux_tree=args.linux_tree,
        state_dir=args.state_dir,
        data_dir=args.data_dir,
    )


def _not_implemented(name: str) -> Command:
    def command(args: argparse.Namespace, cfg: Config) -> int:
        cfg.ensure_dirs()
        print(json.dumps({"command": name, "status": "not_implemented"}, indent=2))
        return 0

    return command


def cmd_env_check(args: argparse.Namespace, cfg: Config) -> int:
    metadata = capture_environment(cfg)
    path = write_environment(cfg, metadata)
    metadata["written_to"] = str(path)
    print(json.dumps(metadata, indent=2, sort_keys=True))
    return 0


def cmd_extract_commits(args: argparse.Namespace, cfg: Config) -> int:
    summary = extract_dataset(cfg, limit=args.limit, fetch=args.fetch_tags)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


def _add_common(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--repo-root", default=".", help="Repository root that owns the BindDrift artifact.")
    parser.add_argument("--linux-tree", default="vendor/linux", help="Linux source tree relative to repo root.")
    parser.add_argument("--state-dir", default=".binddrift", help="Mutable BindDrift state directory.")
    parser.add_argument("--data-dir", default="data", help="Artifact data output directory.")


def _set(parser: argparse.ArgumentParser, func: Command) -> None:
    parser.set_defaults(func=func)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="binddrift", description="BindDrift research artifact CLI.")
    parser.add_argument("--version", action="version", version=f"binddrift {__version__}")
    _add_common(parser)
    sub = parser.add_subparsers(dest="command", required=True)

    env = sub.add_parser("env", help="Environment commands.")
    env_sub = env.add_subparsers(dest="env_command", required=True)
    _set(env_sub.add_parser("check", help="Capture reproducible environment metadata."), cmd_env_check)

    kernel = sub.add_parser("kernel", help="Linux preparation commands.")
    kernel_sub = kernel.add_subparsers(dest="kernel_command", required=True)
    _set(kernel_sub.add_parser("prepare", help="Prepare an out-of-tree kernel build directory."), _not_implemented("kernel prepare"))

    extract = sub.add_parser("extract", help="Extractor commands.")
    extract_sub = extract.add_subparsers(dest="extract_command", required=True)
    for name in ("bindings", "rust", "c"):
        _set(extract_sub.add_parser(name, help=f"Extract {name} facts."), _not_implemented(f"extract {name}"))
    commits = extract_sub.add_parser("commits", help="Extract version and commit metadata.")
    commits.add_argument("--limit", type=int, default=200, help="Number of commits to import from the selected ref.")
    commits.add_argument("--fetch-tags", action="store_true", help="Fetch tags in the Linux source tree before extraction.")
    _set(commits, cmd_extract_commits)

    graph = sub.add_parser("graph", help="Dependency graph commands.")
    graph_sub = graph.add_subparsers(dest="graph_command", required=True)
    _set(graph_sub.add_parser("build", help="Build the C-to-Rust graph."), _not_implemented("graph build"))
    query = graph_sub.add_parser("query", help="Query the dependency graph.")
    query.add_argument("--symbol", help="C or binding symbol to query.")
    query.add_argument("--api", help="Rust safe API to query.")
    _set(query, _not_implemented("graph query"))

    detect = sub.add_parser("detect", help="Drift detector commands.")
    detect_sub = detect.add_subparsers(dest="detect_command", required=True)
    for name in ("tier1", "tier2", "all"):
        _set(detect_sub.add_parser(name, help=f"Run {name} detectors."), _not_implemented(f"detect {name}"))

    _set(sub.add_parser("rank", help="Rank warnings."), _not_implemented("rank"))
    _set(sub.add_parser("replay", help="Run a pilot replay."), _not_implemented("replay"))
    _set(sub.add_parser("eval", help="Generate evaluation tables."), _not_implemented("eval"))

    paper = sub.add_parser("paper", help="Paper artifact commands.")
    paper_sub = paper.add_subparsers(dest="paper_command", required=True)
    _set(paper_sub.add_parser("tables", help="Generate paper tables."), _not_implemented("paper tables"))
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    cfg = _config(args)
    func: Command = args.func
    return func(args, cfg)
