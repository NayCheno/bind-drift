from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from binddrift.config import Config
from binddrift.db import connect, initialize
from binddrift.evaluation.metrics import load_manual_labels, manual_review_agreement, warning_label_key
from binddrift.run_manifest import canonical_run_dir, manifest_exists, validate_run_manifest


MAIN_REPLAY_STATUSES = {"completed", "completed_with_failures"}
MAIN_REPLAY_RUN_ID = "latest"


def generate_paper_tables(cfg: Config) -> dict[str, object]:
    tables_dir = cfg.repo_root / "paper/tables"
    tables_dir.mkdir(parents=True, exist_ok=True)
    manifest = None
    if manifest_exists(cfg) or (canonical_run_dir(cfg) / "warnings.jsonl").exists():
        manifest = validate_run_manifest(cfg)
    replay_summary = tables_dir / "replay_summary.json"
    fact_counts = tables_dir / "fact_counts.json"
    manual_review = tables_dir / "manual_review_summary.json"
    runtime = tables_dir / "runtime_scalability.json"
    _write_replay_summary(cfg, replay_summary)
    _write_fact_counts(cfg, fact_counts)
    _write_manual_review_summary(cfg, manual_review, manifest=manifest)
    _write_runtime_scalability(cfg, runtime, manifest=manifest)
    _validate_table_consistency(cfg, manifest)
    known = {
        "evaluation_summary": tables_dir / "evaluation_summary.json",
        "baselines_ablations": tables_dir / "baselines_ablations.json",
        "replay_summary": replay_summary,
        "fact_counts": fact_counts,
        "manual_review_summary": manual_review,
        "runtime_scalability": runtime,
        "run_manifest": canonical_run_dir(cfg) / "run_manifest.json",
        "toolchain_matrix": cfg.data_dir / "toolchain_matrix.json",
    }
    index = {
        name: {"path": str(path), "available": path.exists()}
        for name, path in known.items()
    }
    out = tables_dir / "table_index.json"
    out.write_text(json.dumps(index, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return {"table_index": str(out), "tables": index}


def _write_replay_summary(cfg: Config, path: Path) -> None:
    conn = connect(cfg.database)
    initialize(conn)
    runs = [dict(row) for row in conn.execute("SELECT * FROM replay_runs ORDER BY started_at DESC LIMIT 20")]
    pairs = [
        dict(row)
        for row in conn.execute(
            """
            SELECT run_id, status, COUNT(*) AS pairs, SUM(warning_count) AS warnings
            FROM replay_pairs
            GROUP BY run_id, status
            ORDER BY run_id DESC, status
            """
        )
    ]
    path.write_text(
        json.dumps({"runs": runs, "pairs": pairs, "main_evidence_gate": _main_replay_gate(conn)}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def _write_fact_counts(cfg: Config, path: Path) -> None:
    conn = connect(cfg.database)
    initialize(conn)
    tables = [
        "versions",
        "binding_functions",
        "binding_structs",
        "binding_consts",
        "layout_facts",
        "c_functions",
        "c_structs",
        "c_macros",
        "c_behavior_indicators",
        "rust_binding_uses",
        "rust_safe_apis",
        "rust_safety_comments",
        "rust_lifetime_facts",
        "rust_error_mappings",
        "graph_edges",
        "drift_events",
        "build_breakage_events",
        "wrapper_fix_events",
    ]
    counts = {table: conn.execute(f"SELECT COUNT(*) AS n FROM {table}").fetchone()["n"] for table in tables}
    by_version = [
        dict(row)
        for row in conn.execute(
            """
            SELECT version_id,
                   (SELECT COUNT(*) FROM binding_functions WHERE binding_functions.version_id=versions.version_id) AS binding_functions,
                   (SELECT COUNT(*) FROM rust_binding_uses WHERE rust_binding_uses.version_id=versions.version_id) AS rust_binding_uses,
                   (SELECT COUNT(*) FROM c_functions WHERE c_functions.version_id=versions.version_id) AS c_functions,
                   (SELECT COUNT(*) FROM graph_edges WHERE graph_edges.version_id=versions.version_id) AS graph_edges
            FROM versions
            ORDER BY date, version_id
            """
        )
    ]
    gate = _main_replay_gate(conn)
    main_versions = set(gate["version_ids"])
    main_by_version = [row for row in by_version if row["version_id"] in main_versions]
    path.write_text(
        json.dumps(
            {"counts": counts, "by_version": by_version, "main_by_version": main_by_version, "main_evidence_gate": gate},
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )


def _write_manual_review_summary(cfg: Config, path: Path, manifest: dict[str, Any] | None = None) -> None:
    conn = connect(cfg.database)
    initialize(conn)
    source_run_id = None
    review_path = cfg.data_dir / "manual_review.csv"
    gate = _main_replay_gate(conn)
    if manifest:
        review_path = Path(manifest["resolved_paths"]["manual_review"])
        source_run_id = str(manifest["run_id"])
    else:
        for run_id in gate["eligible_run_ids"]:
            run = conn.execute("SELECT summary FROM replay_runs WHERE run_id=?", (run_id,)).fetchone()
            summary = _load_json(run["summary"] if run else None, {})
            candidate = Path(summary.get("run_dir", "")) / "manual_review.csv" if summary.get("run_dir") else None
            if candidate and candidate.exists():
                review_path = candidate
                source_run_id = run_id
                break
    labels = load_manual_labels(review_path, uid_only=bool(manifest))
    labeled = [label for label in labels.values() if label]
    all_unclear = bool(labeled) and set(labeled) == {"UNCLEAR"}
    agreement = manual_review_agreement(review_path)
    path.write_text(
        json.dumps(
            {
                "manual_review_csv": str(review_path),
                "source_run_id": source_run_id,
                "labeled_warnings": len(labeled),
                "true_labeled_warnings": sum(1 for label in labels.values() if label.startswith("TRUE_")),
                "agreement": agreement,
                "all_labels_unclear": all_unclear,
                "usable_for_main": bool(labeled) and not all_unclear,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )


def _write_runtime_scalability(cfg: Config, path: Path, manifest: dict[str, Any] | None = None) -> None:
    conn = connect(cfg.database)
    initialize(conn)
    rows = []
    for row in conn.execute("SELECT run_id, status, summary FROM replay_runs ORDER BY started_at DESC LIMIT 20"):
        summary = json.loads(row["summary"] or "{}")
        item = {
            "run_id": row["run_id"],
            "status": row["status"],
            "versions": summary.get("versions"),
            "pairs": summary.get("pairs"),
            "duration_seconds": summary.get("duration_seconds"),
        }
        if manifest and row["run_id"] == manifest["run_id"]:
            item.update(
                {
                    "drift_facts": manifest["drift_fact_count"],
                    "promoted_warnings": manifest["promoted_warning_count"],
                    "paper_topk": manifest["paper_topk"],
                }
            )
        else:
            item["promoted_warnings"] = summary.get("warnings")
        rows.append(item)
    path.write_text(
        json.dumps({"runs": rows, "main_evidence_gate": _main_replay_gate(conn)}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def _validate_table_consistency(cfg: Config, manifest: dict[str, Any] | None) -> None:
    if not manifest:
        return
    tables_dir = cfg.repo_root / "paper/tables"
    evaluation_path = tables_dir / "evaluation_summary.json"
    evaluation = None
    if evaluation_path.exists():
        evaluation = json.loads(evaluation_path.read_text(encoding="utf-8"))
        if evaluation.get("warnings") != manifest["warning_count"]:
            raise RuntimeError(
                f"evaluation_summary warnings {evaluation.get('warnings')} != run_manifest warning_count {manifest['warning_count']}"
            )
        expected_manifest = canonical_run_dir(cfg) / "run_manifest.json"
        evaluation_manifest = evaluation.get("run_manifest")
        if not evaluation_manifest or Path(evaluation_manifest).resolve() != expected_manifest.resolve():
            raise RuntimeError(
                f"evaluation_summary run_manifest {evaluation_manifest} != {expected_manifest}"
            )
    manual_path = tables_dir / "manual_review_summary.json"
    manual = None
    if manual_path.exists():
        manual = json.loads(manual_path.read_text(encoding="utf-8"))
        if manual.get("source_run_id") != manifest["run_id"]:
            raise RuntimeError(
                f"manual_review_summary source_run_id {manual.get('source_run_id')} != run_manifest run_id {manifest['run_id']}"
            )
    if evaluation and manual:
        evaluation_manual = evaluation.get("manual_review") or {}
        if (
            evaluation_manual.get("labeled_warnings") != manual.get("labeled_warnings")
            and "filtered_labeled_warnings" not in evaluation_manual
        ):
            raise RuntimeError(
                "evaluation_summary manual_review.labeled_warnings "
                f"{evaluation_manual.get('labeled_warnings')} != manual_review_summary labeled_warnings {manual.get('labeled_warnings')}"
            )
    baselines_path = tables_dir / "baselines_ablations.json"
    if baselines_path.exists():
        baselines = json.loads(baselines_path.read_text(encoding="utf-8"))
        baseline_warnings = (baselines.get("counts") or {}).get("warnings")
        if baseline_warnings != manifest["warning_count"]:
            raise RuntimeError(
                f"baselines_ablations counts.warnings {baseline_warnings} != run_manifest warning_count {manifest['warning_count']}"
            )
        source = baselines.get("source") or {}
        expected_manifest = canonical_run_dir(cfg) / "run_manifest.json"
        source_manifest = source.get("run_manifest")
        if not source_manifest or Path(source_manifest).resolve() != expected_manifest.resolve():
            raise RuntimeError(
                f"baselines_ablations source.run_manifest {source_manifest} != {expected_manifest}"
            )
        expected_warnings = Path(manifest["resolved_paths"]["warnings"]).resolve()
        source_warnings = source.get("warnings")
        if not source_warnings or Path(source_warnings).resolve() != expected_warnings:
            raise RuntimeError(
                f"baselines_ablations source.warnings {source_warnings} != {expected_warnings}"
            )
        expected_review = Path(manifest["resolved_paths"]["manual_review"]).resolve()
        source_review = source.get("manual_review")
        if not source_review or Path(source_review).resolve() != expected_review:
            raise RuntimeError(
                f"baselines_ablations source.manual_review {source_review} != {expected_review}"
            )


def _load_json(value: str | None, default: Any) -> Any:
    if not value:
        return default
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return default


def _read_warning_ids(path: Path) -> tuple[int, set[str], set[str]]:
    ids: set[str] = set()
    keys: set[str] = set()
    count = 0
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            count += 1
            row = json.loads(line)
            warning_id = row.get("warning_id")
            if warning_id:
                ids.add(str(warning_id))
                keys.add(warning_label_key(warning_id, row.get("pair_id")))
            if row.get("warning_uid"):
                keys.add(str(row["warning_uid"]))
    return count, ids, keys


def _manual_review_warning_ids(path: Path) -> set[str]:
    labels = load_manual_labels(path)
    return set(labels)


def _main_replay_gate(conn) -> dict[str, Any]:
    """Identify replay outputs strong enough for main paper tables.

    Main-result rows must come from completed version replay pairs with
    generated bindings enabled. Pilot warnings, stale runs, single-version
    metadata, and versions with zero binding facts are kept visible but excluded
    from `main_by_version`.
    """

    eligible_runs: list[dict[str, Any]] = []
    excluded_runs: list[dict[str, Any]] = []
    for run in conn.execute("SELECT * FROM replay_runs ORDER BY started_at DESC"):
        reasons: list[str] = []
        run_id = run["run_id"]
        refs = _load_json(run["refs"], [])
        if run["status"] not in MAIN_REPLAY_STATUSES:
            reasons.append(f"status:{run['status']}")
        if not run["build_bindings"]:
            reasons.append("bindings_not_built")
        if len(refs) < 2:
            reasons.append("single_version")
        summary = _load_json(run["summary"], {})
        run_dir = summary.get("run_dir")
        if not run_dir or not Path(run_dir).exists():
            reasons.append("missing_replay_dir")
        aggregate_warnings = summary.get("aggregate_warnings")
        aggregate_warning_count = None
        aggregate_warning_ids: set[str] | None = None
        aggregate_warning_keys: set[str] | None = None
        if aggregate_warnings:
            aggregate_path = Path(aggregate_warnings)
            if not aggregate_path.exists():
                reasons.append("missing_aggregate_warnings")
            else:
                try:
                    aggregate_warning_count, aggregate_warning_ids, aggregate_warning_keys = _read_warning_ids(aggregate_path)
                except (OSError, json.JSONDecodeError) as exc:
                    reasons.append(f"invalid_aggregate_warnings:{type(exc).__name__}")
        completed_pairs = [
            dict(row)
            for row in conn.execute(
                "SELECT old_version, new_version, warning_count FROM replay_pairs WHERE run_id=? AND status='completed'",
                (run_id,),
            )
        ]
        if not completed_pairs:
            reasons.append("no_completed_pairs")
        db_warning_count = sum(int(row["warning_count"] or 0) for row in completed_pairs)
        if aggregate_warning_count is not None and aggregate_warning_count != db_warning_count:
            reasons.append(f"aggregate_warning_count_mismatch:{aggregate_warning_count}!={db_warning_count}")
        if run_dir:
            review_path = Path(run_dir) / "manual_review.csv"
            if review_path.exists() and aggregate_warning_ids is not None and aggregate_warning_keys is not None:
                review_ids = _manual_review_warning_ids(review_path)
                missing_review_ids = {
                    warning_id
                    for warning_id in review_ids
                    if warning_id not in aggregate_warning_ids and warning_id not in aggregate_warning_keys
                }
                if missing_review_ids:
                    reasons.append(f"manual_review_ids_not_in_warnings:{len(missing_review_ids)}")
        candidate_versions = sorted({row["old_version"] for row in completed_pairs} | {row["new_version"] for row in completed_pairs})
        zero_binding_versions = [
            version_id
            for version_id in candidate_versions
            if conn.execute("SELECT COUNT(*) AS n FROM binding_functions WHERE version_id=?", (version_id,)).fetchone()["n"] == 0
        ]
        if zero_binding_versions:
            reasons.append("zero_binding_facts:" + ",".join(zero_binding_versions))
        if reasons:
            excluded_runs.append({"run_id": run_id, "reasons": reasons})
            continue
        eligible_runs.append({"run_id": run_id, "version_ids": candidate_versions})
    selected_runs = _select_main_replay_runs(eligible_runs, excluded_runs)
    version_ids = {version_id for run in selected_runs for version_id in run["version_ids"]}
    return {
        "usable": bool(selected_runs),
        "canonical_run_id": selected_runs[0]["run_id"] if selected_runs else None,
        "eligible_run_ids": [run["run_id"] for run in selected_runs],
        "candidate_run_ids": [run["run_id"] for run in eligible_runs],
        "version_ids": sorted(version_ids),
        "excluded_runs": excluded_runs,
    }


def _select_main_replay_runs(eligible_runs: list[dict[str, Any]], excluded_runs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    if not eligible_runs:
        return []
    selected = next((run for run in eligible_runs if run["run_id"] == MAIN_REPLAY_RUN_ID), eligible_runs[0])
    for run in eligible_runs:
        if run["run_id"] != selected["run_id"]:
            excluded_runs.append({"run_id": run["run_id"], "reasons": [f"superseded_by:{selected['run_id']}"]})
    return [selected]
