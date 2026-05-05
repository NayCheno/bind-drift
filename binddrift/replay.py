from __future__ import annotations

import json
import shutil
import time
from dataclasses import replace
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from binddrift.config import Config
from binddrift.dataset import extract_dataset
from binddrift.db import connect, initialize, upsert_many
from binddrift.detectors.tier1 import run_tier1, run_tier1_with_context
from binddrift.detectors.tier2 import run_tier2, run_tier2_with_context
from binddrift.environment import capture_environment, write_environment
from binddrift.evaluation.evaluator import generate_manual_review, run_evaluation
from binddrift.evaluation.protocol import write_default_evaluation_protocol
from binddrift.extractors.bindgen import extract_bindings
from binddrift.extractors.c_api import binding_closure_roots, extract_c_api
from binddrift.extractors.rust_usage import extract_rust_usage
from binddrift.graph.builder import build_graph
from binddrift.kernel import BINDING_BUILD_TARGETS
from binddrift.kernel import build_kernel_bindings, prepare_kernel_build
from binddrift.paper.cases import generate_case_studies
from binddrift.paper.tables import generate_paper_tables
from binddrift.ranking.scorer import rank_warnings
from binddrift.run_manifest import aggregate_pair_jsonl, write_run_manifest
from binddrift.toolchain_matrix import write_toolchain_matrix
from binddrift.versions import ensure_worktree, sanitize_ref, select_versions
from binddrift.warnings import read_warnings, split_main_and_single_version, write_jsonl


REPLAY_RUN_ID = "latest"


def run_pilot_replay(cfg: Config, commit_limit: int = 50, c_max_files: int = 50) -> dict[str, Any]:
    env = capture_environment(cfg)
    write_environment(cfg, env)
    results = {
        "env": {"linux_commit": env["linux_commit"], "bindgen_available": env["tools"]["bindgen"].get("available", False)},
        "commits": extract_dataset(cfg, limit=commit_limit),
        "kernel_prepare": prepare_kernel_build(cfg),
        "bindings": extract_bindings(cfg),
        "rust": extract_rust_usage(cfg),
        "c": extract_c_api(cfg, roots=["rust/helpers"], max_files=c_max_files),
        "graph": build_graph(cfg),
        "tier1": run_tier1(cfg),
    }
    results["tier2"] = run_tier2(cfg, append=True)
    results["ranking"] = rank_warnings(cfg)
    results["evaluation"] = run_evaluation(cfg)
    results["cases"] = generate_case_studies(cfg)
    results["tables"] = generate_paper_tables(cfg)
    return results


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _run_id() -> str:
    return REPLAY_RUN_ID


def _reset_replay_run_outputs(cfg: Config, run_id: str, run_dir: Path) -> None:
    if run_dir.exists():
        if run_dir.name != run_id or run_dir.parent.name != "replay":
            raise RuntimeError(f"refusing to clear unexpected replay directory: {run_dir}")
        shutil.rmtree(run_dir)
    run_dir.mkdir(parents=True, exist_ok=True)

    conn = connect(cfg.database)
    initialize(conn)
    for table in ("build_breakage_events", "drift_events", "replay_pairs", "replay_runs"):
        conn.execute(f"DELETE FROM {table} WHERE run_id=?", (run_id,))
    conn.commit()


class ReplayStageError(RuntimeError):
    def __init__(self, message: str, pair_status: str, build_status: str | None = None) -> None:
        super().__init__(message)
        self.pair_status = pair_status
        self.build_status = build_status


def _cfg_for_pair(cfg: Config, linux_tree: Path, pair_dir: Path) -> Config:
    return replace(
        cfg,
        linux_tree=linux_tree,
        data_dir=pair_dir,
        warnings_jsonl=pair_dir / "warnings.jsonl",
        drift_facts_jsonl=pair_dir / "drift_facts.jsonl",
        report_md=pair_dir / "warnings.md",
    )


def _cfg_for_replay_run(cfg: Config, run_dir: Path) -> Config:
    return replace(
        cfg,
        data_dir=run_dir,
        warnings_jsonl=run_dir / "warnings.jsonl",
        drift_facts_jsonl=run_dir / "drift_facts.jsonl",
        report_md=run_dir / "warnings.md",
    )


def _persist_run(cfg: Config, row: dict[str, Any]) -> None:
    conn = connect(cfg.database)
    initialize(conn)
    upsert_many(conn, "replay_runs", [row])


def _persist_pair(cfg: Config, row: dict[str, Any]) -> None:
    conn = connect(cfg.database)
    initialize(conn)
    upsert_many(conn, "replay_pairs", [row])


def mark_stale_replay_runs(cfg: Config) -> dict[str, int]:
    """Close replay rows left in `running` by an interrupted process."""

    conn = connect(cfg.database)
    initialize(conn)
    now = _now()
    run_count = conn.execute("SELECT COUNT(*) AS n FROM replay_runs WHERE status='running'").fetchone()["n"]
    pair_count = conn.execute("SELECT COUNT(*) AS n FROM replay_pairs WHERE status='running'").fetchone()["n"]
    conn.execute(
        """
        UPDATE replay_runs
        SET status='stale',
            completed_at=?,
            error=COALESCE(error, 'marked stale before a new replay run')
        WHERE status='running'
        """,
        (now,),
    )
    conn.execute(
        """
        UPDATE replay_pairs
        SET status='stale',
            completed_at=?,
            error=COALESCE(error, 'marked stale before a new replay run')
        WHERE status='running'
        """,
        (now,),
    )
    conn.commit()
    return {"runs": run_count, "pairs": pair_count}


def _version_ref(row: dict[str, Any], ref: str) -> dict[str, Any]:
    return {
        "ref": ref,
        "version_id": row["version_id"],
        "commit": row["git_commit"],
        "date": row.get("date"),
        "tag": row.get("tag"),
    }


def _failed_kernel_command(kernel: dict[str, Any]) -> dict[str, Any] | None:
    for command in kernel.get("commands", []):
        if command.get("returncode") not in (0, None):
            return command
    return None


def _kernel_failure_status(command: dict[str, Any]) -> tuple[str, str]:
    cmd = [str(part) for part in command.get("cmd", [])]
    if any(target in cmd for target in ("x86_64_defconfig", "defconfig", "rust.config", "olddefconfig")):
        return "failed_config", "config_failed"
    if cmd and cmd[0].endswith("scripts/config"):
        return "failed_config", "config_failed"
    if any(target in cmd for target in BINDING_BUILD_TARGETS):
        return "failed_build", "build_failed"
    return "failed_build", "build_failed"


def _extract_version(
    cfg: Config,
    version: dict[str, Any],
    roots: list[str] | None,
    max_files: int | None,
    build_bindings: bool,
    configure: bool,
    arch: str,
    toolchain_spec: dict[str, Any] | None,
) -> dict[str, Any]:
    worktree = ensure_worktree(cfg, version["ref"])
    if worktree.get("error"):
        raise RuntimeError(worktree["error"])
    tree = Path(worktree["path"])
    version_id = version["version_id"]
    tree_cfg = replace(cfg, linux_tree=tree)
    if build_bindings and toolchain_spec and toolchain_spec.get("missing"):
        raise ReplayStageError(
            f"toolchain missing for {version_id}: {', '.join(toolchain_spec['missing'])}. "
            "Run `uv run binddrift toolchain matrix` then `uv run binddrift toolchain bootstrap --install-matrix`.",
            "failed_toolchain",
            "toolchain_missing",
        )
    blocking_issues = [
        issue
        for issue in (toolchain_spec or {}).get("compatibility_issues", [])
        if issue.get("severity") == "blocking"
    ]
    if build_bindings and blocking_issues:
        details = "; ".join(issue.get("detail", issue.get("kind", "toolchain compatibility issue")) for issue in blocking_issues)
        raise ReplayStageError(
            f"toolchain incompatible for {version_id}: {details}",
            "failed_toolchain",
            "toolchain_incompatible",
        )
    if build_bindings:
        kernel = build_kernel_bindings(tree_cfg, version_id=version_id, configure=configure, arch=arch, toolchain=toolchain_spec)
        failed_command = _failed_kernel_command(kernel)
        if failed_command:
            pair_status, build_status = _kernel_failure_status(failed_command)
            raise ReplayStageError(
                f"kernel binding build failed for {version_id}: {failed_command.get('output', '')[-1000:]}",
                pair_status,
                build_status,
            )
    else:
        kernel = prepare_kernel_build(tree_cfg, version_id=version_id, configure=False, linux_tree=tree, arch=arch, toolchain=toolchain_spec)
    objtree = Path(kernel["objtree"])
    try:
        bindings = extract_bindings(tree_cfg, objtree=objtree, version_id=version_id)
        if build_bindings and bindings["missing_files"]:
            raise ReplayStageError(
                f"generated bindings missing for {version_id}: {bindings['missing_files']}",
                "failed_missing_bindings",
                "bindings_missing",
            )
        rust = extract_rust_usage(tree_cfg, version_id=version_id)
        selected_roots = roots or binding_closure_roots(tree_cfg)
        c_api = extract_c_api(tree_cfg, roots=selected_roots, version_id=version_id, max_files=max_files)
        graph = build_graph(tree_cfg, version_id=version_id)
    except ReplayStageError:
        raise
    except Exception as exc:
        raise ReplayStageError(f"extractor failed for {version_id}: {exc}", "failed_extract", "extract_failed") from exc
    _persist_version_metadata(cfg, version, kernel, arch, toolchain_spec)
    return {
        "worktree": worktree,
        "kernel": kernel,
        "bindings": bindings,
        "rust": rust,
        "c": c_api,
        "graph": graph,
        "toolchain": toolchain_spec or {},
    }


def _persist_version_metadata(
    cfg: Config,
    version: dict[str, Any],
    kernel: dict[str, Any],
    arch: str,
    toolchain_spec: dict[str, Any] | None,
) -> None:
    spec = toolchain_spec or {}
    resolved = spec.get("resolved", {})
    row = {
        "version_id": version["version_id"],
        "git_commit": version.get("commit") or kernel.get("linux_commit") or "",
        "tag": version.get("tag"),
        "date": version.get("date"),
        "arch": arch,
        "config_hash": kernel.get("config_hash"),
        "rustc_version": resolved.get("rustc_version_text"),
        "clang_version": resolved.get("clang_version_text"),
        "bindgen_version": resolved.get("bindgen_version_text") or spec.get("required", {}).get("bindgen"),
    }
    conn = connect(cfg.database)
    initialize(conn)
    upsert_many(conn, "versions", [row])


def _append_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, sort_keys=True) + "\n")


def run_version_replay(
    cfg: Config,
    start: str = "v6.1",
    include_head: bool = True,
    fetch_tags: bool = False,
    limit: int | None = None,
    build_bindings: bool = False,
    configure: bool = False,
    jobs: int = 1,
    roots: list[str] | None = None,
    max_files: int | None = None,
    arch: str = "x86_64",
    stop_on_error: bool = False,
    toolchain: str = "auto",
) -> dict[str, Any]:
    """Run adjacent-version replay into the fixed latest replay output.

    The implementation is intentionally sequential even though the public CLI
    records `jobs`: SQLite writes, Linux worktrees, and kernel object trees are
    easier to audit deterministically. The flag is kept in run metadata so a
    future parallel executor can preserve the same experiment interface.
    """

    cfg.ensure_dirs()
    stale = mark_stale_replay_runs(cfg)
    run_id = _run_id()
    run_dir = cfg.data_dir / "replay" / run_id
    _reset_replay_run_outputs(cfg, run_id, run_dir)
    refs_result = select_versions(cfg, start=start, include_head=include_head, fetch=fetch_tags, limit=limit)
    refs = refs_result["refs"]
    matrix = write_toolchain_matrix(cfg, refs, refs_result["version_rows"]) if toolchain == "auto" else None
    specs_by_version = {
        entry["version_id"]: entry for entry in (matrix or {}).get("entries", [])
    }
    versions = []
    for row, ref in zip(refs_result["version_rows"], refs, strict=True):
        version = _version_ref(row, ref)
        if toolchain == "auto":
            version["toolchain"] = specs_by_version.get(version["version_id"], {})
        versions.append(version)
    c_roots = roots
    run_row = {
        "run_id": run_id,
        "started_at": _now(),
        "completed_at": None,
        "status": "running",
        "start_ref": start,
        "include_head": int(include_head),
        "build_bindings": int(build_bindings),
        "configure": int(configure),
        "jobs": jobs,
        "arch": arch,
        "c_roots": json.dumps(c_roots if c_roots else ["<bindings-closure>"], sort_keys=True),
        "max_files": max_files,
        "refs": json.dumps(versions, sort_keys=True),
        "summary": "{}",
        "error": None,
    }
    _persist_run(cfg, run_row)

    processed: dict[str, dict[str, Any]] = {}
    pairs: list[dict[str, Any]] = []
    aggregate_warnings = run_dir / "warnings.jsonl"
    aggregate_promoted_warnings = run_dir / "promoted_warnings.jsonl"
    aggregate_drift_facts = run_dir / "drift_facts.jsonl"
    started = time.time()

    for index, (old_version, new_version) in enumerate(zip(versions, versions[1:], strict=False), start=1):
        pair_id = f"{run_id}-p{index:03d}-{sanitize_ref(old_version['version_id'])}-to-{sanitize_ref(new_version['version_id'])}"
        pair_dir = run_dir / pair_id
        pair_dir.mkdir(parents=True, exist_ok=True)
        pair_row = {
            "pair_id": pair_id,
            "run_id": run_id,
            "pair_index": index,
            "old_ref": old_version["ref"],
            "new_ref": new_version["ref"],
            "old_version": old_version["version_id"],
            "new_version": new_version["version_id"],
            "old_commit": old_version["commit"],
            "new_commit": new_version["commit"],
            "started_at": _now(),
            "completed_at": None,
            "status": "running",
            "warning_count": 0,
            "build_status": None,
            "extraction_summary": "{}",
            "evaluation_summary": "{}",
            "warnings_jsonl": str(pair_dir / "warnings.jsonl"),
            "report_md": str(pair_dir / "warnings.md"),
            "error": None,
        }
        _persist_pair(cfg, pair_row)
        try:
            for version in (old_version, new_version):
                if version["version_id"] not in processed:
                    processed[version["version_id"]] = _extract_version(
                        cfg,
                        version,
                        roots=c_roots,
                        max_files=max_files,
                        build_bindings=build_bindings,
                        configure=configure,
                        arch=arch,
                        toolchain_spec=version.get("toolchain") if toolchain == "auto" else None,
                    )
            pair_cfg = _cfg_for_pair(cfg, Path(processed[new_version["version_id"]]["worktree"]["path"]), pair_dir)
            tier1 = run_tier1_with_context(
                pair_cfg,
                old=old_version["version_id"],
                new=new_version["version_id"],
                run_id=run_id,
                pair_id=pair_id,
            )
            tier2 = run_tier2_with_context(
                pair_cfg,
                old=old_version["version_id"],
                new=new_version["version_id"],
                append=True,
                run_id=run_id,
                pair_id=pair_id,
            )
            ranking = rank_warnings(pair_cfg)
            evaluation = run_evaluation(pair_cfg, top_k=100, run_id=run_id, pair_id=pair_id)
            warnings = read_warnings(pair_cfg.warnings_jsonl)
            _append_jsonl(aggregate_warnings, warnings)
            pair_row.update(
                {
                    "completed_at": _now(),
                    "status": "completed",
                    "warning_count": len(warnings),
                    "build_status": "built" if build_bindings else "not_requested",
                    "extraction_summary": json.dumps(
                        {
                            "old": processed[old_version["version_id"]],
                            "new": processed[new_version["version_id"]],
                            "tier1": tier1,
                            "tier2": tier2,
                            "ranking": ranking,
                        },
                        sort_keys=True,
                    ),
                    "evaluation_summary": json.dumps(evaluation["summary"], sort_keys=True),
                }
            )
        except Exception as exc:  # pragma: no cover - exercised by real replay failures.
            status = exc.pair_status if isinstance(exc, ReplayStageError) else "failed"
            build_status = exc.build_status if isinstance(exc, ReplayStageError) else "failed"
            pair_row.update(
                {
                    "completed_at": _now(),
                    "status": status,
                    "build_status": build_status,
                    "error": str(exc)[-4000:],
                }
            )
            if stop_on_error:
                _persist_pair(cfg, pair_row)
                run_row.update(
                    {
                        "completed_at": _now(),
                        "status": "failed",
                        "summary": json.dumps(
                            {
                                "run_id": run_id,
                                "versions": len(versions),
                                "pairs": len(pairs) + 1,
                                "completed_pairs": sum(1 for pair in pairs if pair["status"] == "completed"),
                                "failed_pairs": sum(1 for pair in pairs if pair["status"] != "completed") + 1,
                                "run_dir": str(run_dir),
                                "stale_previous": stale,
                            },
                            sort_keys=True,
                        ),
                        "error": str(exc)[-4000:],
                    }
                )
                _persist_run(cfg, run_row)
                raise
        _persist_pair(cfg, pair_row)
        pairs.append(pair_row)

    completed = sum(1 for pair in pairs if pair["status"] == "completed")
    failed = sum(1 for pair in pairs if pair["status"] != "completed")
    drift_fact_count = aggregate_pair_jsonl(run_dir, "drift_facts.jsonl", aggregate_drift_facts)
    aggregate_ranking = rank_warnings(_cfg_for_replay_run(cfg, run_dir))
    main_warnings, single_version_targets = split_main_and_single_version(read_warnings(aggregate_warnings))
    write_jsonl(aggregate_promoted_warnings, main_warnings)
    write_jsonl(aggregate_warnings, main_warnings[:100])
    write_jsonl(run_dir / "single_version_review_targets.jsonl", single_version_targets)
    aggregate_review = generate_manual_review(
        _cfg_for_replay_run(cfg, run_dir),
        main_warnings[:100],
        top_k=100,
    )
    should_write_manifest = bool(completed and failed == 0 and aggregate_ranking["warnings"] > 0)
    summary = {
        "run_id": run_id,
        "versions": len(versions),
        "pairs": len(pairs),
        "completed_pairs": completed,
        "failed_pairs": failed,
        "warnings": min(len(main_warnings), 100),
        "promoted_replay_warnings": len(main_warnings),
        "aggregate_promoted_warnings": str(aggregate_promoted_warnings),
        "paper_topk": min(len(main_warnings), 100),
        "single_version_review_targets": len(single_version_targets),
        "ranking": aggregate_ranking,
        "duration_seconds": round(time.time() - started, 3),
        "aggregate_warnings": str(aggregate_warnings),
        "aggregate_drift_facts": str(aggregate_drift_facts),
        "drift_facts": drift_fact_count,
        "manual_review": str(aggregate_review),
        "run_dir": str(run_dir),
        "run_manifest": str(run_dir / "run_manifest.json") if should_write_manifest else None,
        "stale_previous": stale,
    }
    (run_dir / "summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    run_row.update(
        {
            "completed_at": _now(),
            "status": "completed" if failed == 0 else "completed_with_failures",
            "summary": json.dumps(summary, sort_keys=True),
        }
    )
    _persist_run(cfg, run_row)
    if should_write_manifest:
        write_default_evaluation_protocol(cfg, run_id=run_id)
        write_run_manifest(cfg, run_id=run_id)
    return summary
