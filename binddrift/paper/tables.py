from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from binddrift.config import Config
from binddrift.db import connect, initialize
from binddrift.evaluation.metrics import load_manual_labels, manual_review_agreement


MAIN_REPLAY_STATUSES = {"completed", "completed_with_failures"}


def generate_paper_tables(cfg: Config) -> dict[str, object]:
    tables_dir = cfg.repo_root / "paper/tables"
    tables_dir.mkdir(parents=True, exist_ok=True)
    replay_summary = tables_dir / "replay_summary.json"
    fact_counts = tables_dir / "fact_counts.json"
    manual_review = tables_dir / "manual_review_summary.json"
    runtime = tables_dir / "runtime_scalability.json"
    _write_replay_summary(cfg, replay_summary)
    _write_fact_counts(cfg, fact_counts)
    _write_manual_review_summary(cfg, manual_review)
    _write_runtime_scalability(cfg, runtime)
    known = {
        "evaluation_summary": tables_dir / "evaluation_summary.json",
        "baselines_ablations": tables_dir / "baselines_ablations.json",
        "replay_summary": replay_summary,
        "fact_counts": fact_counts,
        "manual_review_summary": manual_review,
        "runtime_scalability": runtime,
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


def _write_manual_review_summary(cfg: Config, path: Path) -> None:
    conn = connect(cfg.database)
    initialize(conn)
    source_run_id = None
    review_path = cfg.data_dir / "manual_review.csv"
    gate = _main_replay_gate(conn)
    for run_id in gate["eligible_run_ids"]:
        run = conn.execute("SELECT summary FROM replay_runs WHERE run_id=?", (run_id,)).fetchone()
        summary = _load_json(run["summary"] if run else None, {})
        candidate = Path(summary.get("run_dir", "")) / "manual_review.csv" if summary.get("run_dir") else None
        if candidate and candidate.exists():
            review_path = candidate
            source_run_id = run_id
            break
    labels = load_manual_labels(review_path)
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


def _write_runtime_scalability(cfg: Config, path: Path) -> None:
    conn = connect(cfg.database)
    initialize(conn)
    rows = []
    for row in conn.execute("SELECT run_id, status, summary FROM replay_runs ORDER BY started_at DESC LIMIT 20"):
        summary = json.loads(row["summary"] or "{}")
        rows.append(
            {
                "run_id": row["run_id"],
                "status": row["status"],
                "versions": summary.get("versions"),
                "pairs": summary.get("pairs"),
                "warnings": summary.get("warnings"),
                "duration_seconds": summary.get("duration_seconds"),
            }
        )
    path.write_text(
        json.dumps({"runs": rows, "main_evidence_gate": _main_replay_gate(conn)}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def _load_json(value: str | None, default: Any) -> Any:
    if not value:
        return default
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return default


def _main_replay_gate(conn) -> dict[str, Any]:
    """Identify replay outputs strong enough for main paper tables.

    Main-result rows must come from completed version replay pairs with
    generated bindings enabled. Pilot warnings, stale runs, single-version
    metadata, and versions with zero binding facts are kept visible but excluded
    from `main_by_version`.
    """

    eligible_run_ids: list[str] = []
    version_ids: set[str] = set()
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
        if aggregate_warnings and not Path(aggregate_warnings).exists():
            reasons.append("missing_aggregate_warnings")
        completed_pairs = [
            dict(row)
            for row in conn.execute(
                "SELECT old_version, new_version FROM replay_pairs WHERE run_id=? AND status='completed'",
                (run_id,),
            )
        ]
        if not completed_pairs:
            reasons.append("no_completed_pairs")
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
        eligible_run_ids.append(run_id)
        version_ids.update(candidate_versions)
    return {
        "usable": bool(eligible_run_ids),
        "eligible_run_ids": eligible_run_ids,
        "version_ids": sorted(version_ids),
        "excluded_runs": excluded_runs,
    }
