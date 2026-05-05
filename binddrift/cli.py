from __future__ import annotations

import argparse
import json
from dataclasses import replace
from pathlib import Path
from typing import Callable

from . import __version__
from .config import Config
from .dataset import extract_dataset
from .detectors.tier1 import run_tier1, run_tier1_with_context
from .detectors.tier2 import run_tier2, run_tier2_with_context
from .environment import capture_environment, write_environment
from .evaluation.evaluator import run_evaluation
from .evaluation.evaluator import generate_manual_review
from .evaluation.diagnostics import diagnose_false_positives
from .extractors.bindgen import extract_bindings
from .extractors.c_api import extract_c_api
from .extractors.rust_usage import extract_rust_usage
from .kernel import build_kernel_bindings, prepare_kernel_build
from .graph.builder import build_graph, evidence_chain, query_graph
from .ranking.scorer import rank_warnings
from .paper.cases import generate_case_studies
from .paper.tables import generate_paper_tables
from .replay import run_pilot_replay, run_version_replay
from .run_manifest import aggregate_pair_jsonl, canonical_run_dir, write_run_manifest
from .warnings import read_warnings
from .toolchain import bootstrap_toolchain, check_toolchain
from .toolchain_matrix import write_toolchain_matrix
from .versions import ensure_worktree, select_versions


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


def cmd_toolchain_check(args: argparse.Namespace, cfg: Config) -> int:
    result = check_toolchain(cfg, run_rustavailable=args.run_rustavailable)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


def cmd_toolchain_bootstrap(args: argparse.Namespace, cfg: Config) -> int:
    result = bootstrap_toolchain(
        cfg,
        install_bindgen=args.install_bindgen,
        install_rust_src=args.install_rust_src,
        install_matrix=args.install_matrix,
        matrix_file=Path(args.matrix_file).resolve() if args.matrix_file else None,
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


def cmd_toolchain_matrix(args: argparse.Namespace, cfg: Config) -> int:
    refs_result = select_versions(cfg, start=args.start, include_head=not args.no_head, fetch=args.fetch_tags, limit=args.limit)
    result = write_toolchain_matrix(cfg, refs_result["refs"], refs_result["version_rows"])
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


def cmd_extract_commits(args: argparse.Namespace, cfg: Config) -> int:
    summary = extract_dataset(cfg, limit=args.limit, fetch=args.fetch_tags)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


def cmd_dataset_versions(args: argparse.Namespace, cfg: Config) -> int:
    result = select_versions(cfg, start=args.start, include_head=not args.no_head, fetch=args.fetch_tags, limit=args.limit)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


def cmd_dataset_worktree(args: argparse.Namespace, cfg: Config) -> int:
    result = ensure_worktree(cfg, args.ref)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


def cmd_kernel_prepare(args: argparse.Namespace, cfg: Config) -> int:
    manifest = prepare_kernel_build(cfg, version_id=args.version_id, run_make=args.run_make, configure=args.configure, arch=args.arch)
    print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


def cmd_kernel_build_bindings(args: argparse.Namespace, cfg: Config) -> int:
    manifest = build_kernel_bindings(cfg, version_id=args.version_id, configure=args.configure, arch=args.arch)
    print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


def cmd_extract_bindings(args: argparse.Namespace, cfg: Config) -> int:
    summary = extract_bindings(
        cfg,
        objtree=Path(args.objtree).resolve() if args.objtree else None,
        version_id=args.version_id,
    )
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


def cmd_extract_rust(args: argparse.Namespace, cfg: Config) -> int:
    summary = extract_rust_usage(cfg, version_id=args.version_id)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


def cmd_extract_c(args: argparse.Namespace, cfg: Config) -> int:
    summary = extract_c_api(cfg, roots=args.root or None, version_id=args.version_id, max_files=args.max_files)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


def cmd_extract_all(args: argparse.Namespace, cfg: Config) -> int:
    result = {
        "bindings": extract_bindings(cfg, version_id=args.version_id),
        "rust": extract_rust_usage(cfg, version_id=args.version_id),
        "c": extract_c_api(cfg, roots=args.root, version_id=args.version_id, max_files=args.max_files),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


def cmd_graph_build(args: argparse.Namespace, cfg: Config) -> int:
    summary = build_graph(cfg, version_id=args.version_id)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


def cmd_graph_query(args: argparse.Namespace, cfg: Config) -> int:
    result = query_graph(cfg, symbol=args.symbol, api=args.api, version_id=args.version_id, fuzzy=args.fuzzy)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


def cmd_graph_evidence(args: argparse.Namespace, cfg: Config) -> int:
    result = evidence_chain(cfg, symbol=args.symbol, version_id=args.version_id)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


def cmd_detect_tier1(args: argparse.Namespace, cfg: Config) -> int:
    result = run_tier1_with_context(cfg, old=args.old, new=args.new, run_id=args.run_id, pair_id=args.pair_id)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


def cmd_detect_tier2(args: argparse.Namespace, cfg: Config) -> int:
    result = run_tier2_with_context(cfg, old=args.old, new=args.new, append=args.append, run_id=args.run_id, pair_id=args.pair_id)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


def cmd_detect_all(args: argparse.Namespace, cfg: Config) -> int:
    tier1 = run_tier1_with_context(cfg, old=args.old, new=args.new, run_id=args.run_id, pair_id=args.pair_id)
    tier2 = run_tier2_with_context(cfg, old=args.old, new=args.new, append=True, run_id=args.run_id, pair_id=args.pair_id)
    print(json.dumps({"tier1": tier1, "tier2": tier2}, indent=2, sort_keys=True))
    return 0


def cmd_rank(args: argparse.Namespace, cfg: Config) -> int:
    result = rank_warnings(cfg)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


def cmd_eval(args: argparse.Namespace, cfg: Config) -> int:
    result = run_evaluation(
        cfg,
        build_log=Path(args.build_log).resolve() if args.build_log else None,
        top_k=args.top_k,
        run_id=args.run_id,
        pair_id=args.pair_id,
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


def cmd_eval_manifest(args: argparse.Namespace, cfg: Config) -> int:
    run_dir = canonical_run_dir(cfg, args.run_id)
    run_cfg = replace(
        cfg,
        data_dir=run_dir,
        warnings_jsonl=run_dir / "warnings.jsonl",
        drift_facts_jsonl=run_dir / "drift_facts.jsonl",
        report_md=run_dir / "warnings.md",
    )
    drift_facts = run_dir / "drift_facts.jsonl"
    if args.refresh or not drift_facts.exists():
        aggregate_pair_jsonl(run_dir, "drift_facts.jsonl", drift_facts)
    review = run_dir / "manual_review.csv"
    if args.refresh_review or not review.exists():
        generate_manual_review(run_cfg, read_warnings(run_cfg.warnings_jsonl), top_k=args.top_k)
    manifest = write_run_manifest(cfg, run_id=args.run_id)
    print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


def cmd_eval_diagnose_false_positives(args: argparse.Namespace, cfg: Config) -> int:
    output_dir = Path(args.output_dir).resolve() if args.output_dir else cfg.data_dir / "manual"
    result = diagnose_false_positives(
        manual_review=Path(args.manual_review).resolve(),
        warnings_jsonl=Path(args.warnings).resolve(),
        output_dir=output_dir,
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


def cmd_replay(args: argparse.Namespace, cfg: Config) -> int:
    if args.replay_command == "versions":
        result = run_version_replay(
            cfg,
            start=args.start,
            include_head=args.include_head,
            fetch_tags=args.fetch_tags,
            limit=args.limit,
            build_bindings=args.build_bindings,
            configure=args.configure,
            jobs=args.jobs,
            roots=args.root,
            max_files=args.max_files,
            arch=args.arch,
            stop_on_error=args.stop_on_error,
            toolchain=args.toolchain,
        )
    else:
        result = run_pilot_replay(cfg, commit_limit=args.commit_limit, c_max_files=args.c_max_files)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


def cmd_paper_cases(args: argparse.Namespace, cfg: Config) -> int:
    result = generate_case_studies(cfg)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


def cmd_paper_tables(args: argparse.Namespace, cfg: Config) -> int:
    result = generate_paper_tables(cfg)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


def cmd_paper_build(args: argparse.Namespace, cfg: Config) -> int:
    result = {"cases": generate_case_studies(cfg), "tables": generate_paper_tables(cfg)}
    print(json.dumps(result, indent=2, sort_keys=True))
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

    toolchain = sub.add_parser("toolchain", help="Rust-for-Linux toolchain commands.")
    toolchain_sub = toolchain.add_subparsers(dest="toolchain_command", required=True)
    toolchain_check = toolchain_sub.add_parser("check", help="Check Rust-for-Linux build requirements.")
    toolchain_check.add_argument("--run-rustavailable", action="store_true", help="Run `make LLVM=1 rustavailable` in the Linux tree.")
    _set(toolchain_check, cmd_toolchain_check)
    bootstrap = toolchain_sub.add_parser("bootstrap", help="Install supported missing user-space tools.")
    bootstrap.add_argument("--install-bindgen", action="store_true", help="Install bindgen-cli through Cargo when bindgen is missing.")
    bootstrap.add_argument("--install-rust-src", action="store_true", help="Install rust-src through rustup.")
    bootstrap.add_argument("--install-matrix", action="store_true", help="Install Rust and bindgen versions from data/toolchain_matrix.json.")
    bootstrap.add_argument("--matrix-file", help="Toolchain matrix JSON file to bootstrap; defaults to data/toolchain_matrix.json.")
    _set(bootstrap, cmd_toolchain_bootstrap)
    matrix = toolchain_sub.add_parser("matrix", help="Generate the per-kernel Rust-for-Linux toolchain matrix.")
    matrix.add_argument("--start", default="v6.1", help="First release tag to include.")
    matrix.add_argument("--limit", type=int, help="Keep only the last N selected refs.")
    matrix.add_argument("--fetch-tags", action="store_true", help="Fetch tags in the Linux source tree before selection.")
    matrix.add_argument("--no-head", action="store_true", help="Do not append the current HEAD pseudo-version.")
    _set(matrix, cmd_toolchain_matrix)

    dataset = sub.add_parser("dataset", help="Linux version dataset commands.")
    dataset_sub = dataset.add_subparsers(dest="dataset_command", required=True)
    versions = dataset_sub.add_parser("versions", help="Select Rust-era Linux release versions for replay.")
    versions.add_argument("--start", default="v6.1", help="First release tag to include.")
    versions.add_argument("--limit", type=int, help="Keep only the last N release tags before HEAD.")
    versions.add_argument("--fetch-tags", action="store_true", help="Fetch tags in the Linux source tree before selection.")
    versions.add_argument("--no-head", action="store_true", help="Do not append the current HEAD pseudo-version.")
    _set(versions, cmd_dataset_versions)
    worktree = dataset_sub.add_parser("worktree", help="Create or reuse a managed replay worktree for a ref.")
    worktree.add_argument("ref", help="Git tag, commit, branch, or HEAD:<short> pseudo-ref.")
    _set(worktree, cmd_dataset_worktree)

    kernel = sub.add_parser("kernel", help="Linux preparation commands.")
    kernel_sub = kernel.add_subparsers(dest="kernel_command", required=True)
    prepare = kernel_sub.add_parser("prepare", help="Prepare an out-of-tree kernel build directory.")
    prepare.add_argument("--version-id", help="Version id for the object tree; defaults to git describe.")
    prepare.add_argument("--run-make", action="store_true", help="Run `make O=<objtree> LLVM=1 rustavailable` after creating the object tree.")
    prepare.add_argument("--configure", action="store_true", help="Generate an x86_64 Rust-enabled kernel config in the object tree.")
    prepare.add_argument("--arch", default="x86_64", help="Kernel ARCH value for configuration and build commands.")
    _set(prepare, cmd_kernel_prepare)
    build_bindings = kernel_sub.add_parser("build-bindings", help="Build generated Rust binding snapshots in the object tree.")
    build_bindings.add_argument("--version-id", help="Version id for the object tree; defaults to git describe.")
    build_bindings.add_argument("--configure", action="store_true", help="Generate config before building binding outputs.")
    build_bindings.add_argument("--arch", default="x86_64", help="Kernel ARCH value for configuration and build commands.")
    _set(build_bindings, cmd_kernel_build_bindings)

    extract = sub.add_parser("extract", help="Extractor commands.")
    extract_sub = extract.add_subparsers(dest="extract_command", required=True)
    bindings = extract_sub.add_parser("bindings", help="Extract bindgen-generated Rust facts.")
    bindings.add_argument("--objtree", help="Kernel object tree that contains rust/bindings/*_generated.rs.")
    bindings.add_argument("--version-id", help="Version id for extracted facts.")
    _set(bindings, cmd_extract_bindings)
    rust = extract_sub.add_parser("rust", help="Extract Rust wrapper usage facts.")
    rust.add_argument("--version-id", help="Version id for extracted facts.")
    _set(rust, cmd_extract_rust)
    c_api = extract_sub.add_parser("c", help="Extract C API facts and behavior indicators.")
    c_api.add_argument("--root", action="append", help="Linux-relative path to scan; may be repeated.")
    c_api.add_argument("--version-id", help="Version id for extracted facts.")
    c_api.add_argument("--max-files", type=int, help="Limit scanned files for fast pilot runs.")
    _set(c_api, cmd_extract_c)
    extract_all = extract_sub.add_parser("all", help="Run binding, Rust, and C extractors.")
    extract_all.add_argument("--version-id", help="Version id for extracted facts.")
    extract_all.add_argument("--root", action="append", help="Linux-relative C path to scan; may be repeated.")
    extract_all.add_argument("--max-files", type=int, help="Limit scanned C files for fast pilot runs.")
    _set(extract_all, cmd_extract_all)
    commits = extract_sub.add_parser("commits", help="Extract version and commit metadata.")
    commits.add_argument("--limit", type=int, default=200, help="Number of commits to import from the selected ref.")
    commits.add_argument("--fetch-tags", action="store_true", help="Fetch tags in the Linux source tree before extraction.")
    _set(commits, cmd_extract_commits)

    graph = sub.add_parser("graph", help="Dependency graph commands.")
    graph_sub = graph.add_subparsers(dest="graph_command", required=True)
    graph_build = graph_sub.add_parser("build", help="Build the C-to-Rust graph.")
    graph_build.add_argument("--version-id", help="Version id to graph.")
    _set(graph_build, cmd_graph_build)
    query = graph_sub.add_parser("query", help="Query the dependency graph.")
    query.add_argument("--symbol", help="C or binding symbol to query.")
    query.add_argument("--api", help="Rust safe API to query.")
    query.add_argument("--version-id", help="Version id to query.")
    query.add_argument("--fuzzy", action="store_true", help="Allow substring node-id search for manual exploration only.")
    _set(query, cmd_graph_query)
    evidence = graph_sub.add_parser("evidence", help="Materialize a C-to-Rust evidence chain for a symbol.")
    evidence.add_argument("symbol", help="C or binding symbol to explain.")
    evidence.add_argument("--version-id", help="Version id to query.")
    _set(evidence, cmd_graph_evidence)

    detect = sub.add_parser("detect", help="Drift detector commands.")
    detect_sub = detect.add_subparsers(dest="detect_command", required=True)
    tier1 = detect_sub.add_parser("tier1", help="Run Tier 1 objective drift detectors.")
    tier1.add_argument("--old", help="Old version id.")
    tier1.add_argument("--new", help="New version id.")
    tier1.add_argument("--run-id", help="Replay run id to attach to emitted warnings.")
    tier1.add_argument("--pair-id", help="Replay pair id to attach to emitted warnings.")
    _set(tier1, cmd_detect_tier1)
    tier2 = detect_sub.add_parser("tier2", help="Run Tier 2 indicator-based contract detectors.")
    tier2.add_argument("--old", help="Old version id.")
    tier2.add_argument("--new", help="New version id.")
    tier2.add_argument("--append", action="store_true", help="Append to existing warnings instead of replacing them.")
    tier2.add_argument("--run-id", help="Replay run id to attach to emitted warnings.")
    tier2.add_argument("--pair-id", help="Replay pair id to attach to emitted warnings.")
    _set(tier2, cmd_detect_tier2)
    all_detectors = detect_sub.add_parser("all", help="Run all detectors.")
    all_detectors.add_argument("--old", help="Old version id.")
    all_detectors.add_argument("--new", help="New version id.")
    all_detectors.add_argument("--run-id", help="Replay run id to attach to emitted warnings.")
    all_detectors.add_argument("--pair-id", help="Replay pair id to attach to emitted warnings.")
    _set(all_detectors, cmd_detect_all)

    _set(sub.add_parser("rank", help="Rank warnings."), cmd_rank)
    replay = sub.add_parser("replay", help="Run a pilot replay.")
    replay.add_argument("replay_command", nargs="?", choices=["run", "versions"], default="run", help="Replay mode: `run` for the pilot or `versions` for adjacent-version replay.")
    replay.add_argument("--commit-limit", type=int, default=50, help="Number of commits to import.")
    replay.add_argument("--c-max-files", type=int, default=50, help="Number of C files to scan in the pilot.")
    replay.add_argument("--start", default="v6.1", help="First release tag to include for `replay versions`.")
    replay.add_argument("--limit", type=int, help="Keep only the last N selected refs before replay.")
    replay.add_argument("--include-head", action=argparse.BooleanOptionalAction, default=True, help="Include the current HEAD pseudo-version.")
    replay.add_argument("--fetch-tags", action="store_true", help="Fetch tags in the Linux source tree before version selection.")
    replay.add_argument("--build-bindings", action="store_true", help="Build generated Rust bindings for every replayed version.")
    replay.add_argument("--configure", action="store_true", help="Generate a Rust-enabled kernel config before binding builds.")
    replay.add_argument("--jobs", type=int, default=1, help="Requested replay parallelism recorded in metadata; execution is currently deterministic and sequential.")
    replay.add_argument("--root", action="append", help="Linux-relative C path to scan during version replay; may be repeated.")
    replay.add_argument("--max-files", type=int, help="Limit scanned C files during version replay.")
    replay.add_argument("--arch", default="x86_64", help="Kernel ARCH for binding generation and extraction metadata.")
    replay.add_argument("--stop-on-error", action="store_true", help="Stop at the first failed version pair instead of recording and continuing.")
    replay.add_argument("--toolchain", choices=["auto", "off"], default="auto", help="Use the per-version Rust-for-Linux toolchain matrix during version replay.")
    _set(replay, cmd_replay)
    eval_parser = sub.add_parser("eval", help="Generate evaluation tables.")
    eval_sub = eval_parser.add_subparsers(dest="eval_command")
    eval_parser.add_argument("--build-log", help="Optional Rust-enabled build log to parse.")
    eval_parser.add_argument("--top-k", type=int, default=100, help="Number of top warnings to include before stratified manual review sampling.")
    eval_parser.add_argument("--run-id", help="Replay run id associated with the evaluation oracle rows.")
    eval_parser.add_argument("--pair-id", help="Replay pair id associated with the evaluation oracle rows.")
    _set(eval_parser, cmd_eval)
    eval_all = eval_sub.add_parser("all", help="Generate all evaluation tables.")
    eval_all.add_argument("--build-log", help="Optional Rust-enabled build log to parse.")
    eval_all.add_argument("--top-k", type=int, default=100, help="Number of top warnings to include before stratified manual review sampling.")
    eval_all.add_argument("--run-id", help="Replay run id associated with the evaluation oracle rows.")
    eval_all.add_argument("--pair-id", help="Replay pair id associated with the evaluation oracle rows.")
    _set(eval_all, cmd_eval)
    manifest = eval_sub.add_parser("manifest", help="Generate the canonical replay run manifest.")
    manifest.add_argument("--run-id", default="latest", help="Replay run id to manifest.")
    manifest.add_argument("--top-k", type=int, default=100, help="Top warnings to include in a generated review skeleton.")
    manifest.add_argument("--refresh", action="store_true", help="Rebuild aggregate drift_facts.jsonl before writing the manifest.")
    manifest.add_argument("--refresh-review", action="store_true", help="Regenerate the canonical manual_review.csv skeleton.")
    _set(manifest, cmd_eval_manifest)
    diagnose = eval_sub.add_parser("diagnose-false-positives", help="Convert manual labels into hard negatives and diagnosis counts.")
    diagnose.add_argument("--manual-review", required=True, help="Manual review CSV with labels.")
    diagnose.add_argument("--warnings", required=True, help="Warnings JSONL used by the manual review CSV.")
    diagnose.add_argument("--output-dir", help="Directory for hard_negatives.csv and true_positives.csv; defaults to data/manual.")
    _set(diagnose, cmd_eval_diagnose_false_positives)

    paper = sub.add_parser("paper", help="Paper artifact commands.")
    paper_sub = paper.add_subparsers(dest="paper_command", required=True)
    _set(paper_sub.add_parser("tables", help="Generate paper tables."), cmd_paper_tables)
    _set(paper_sub.add_parser("cases", help="Generate case study skeletons."), cmd_paper_cases)
    _set(paper_sub.add_parser("build", help="Generate paper cases and table index."), cmd_paper_build)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    cfg = _config(args)
    func: Command = args.func
    return func(args, cfg)
