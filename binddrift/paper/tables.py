from __future__ import annotations

import json
import csv
from pathlib import Path
from typing import Any

from binddrift.config import Config
from binddrift.db import connect, initialize
from binddrift.evaluation.protocol import FORBIDDEN_PRIMARY_SCORE_COMPONENTS, load_evaluation_protocol
from binddrift.evaluation.metrics import load_manual_labels, manual_review_agreement, warning_label_key
from binddrift.paper.audit import generate_extractor_audit, generate_strict_extractor_audit
from binddrift.ranking.oracle_blind_scorer import rank_primary_warnings_oracle_blind
from binddrift.run_manifest import canonical_run_dir, manifest_exists, repo_relative, resolve_manifest_path, sha256_file, validate_run_manifest
from binddrift.warnings import read_warnings


MAIN_REPLAY_STATUSES = {"completed", "completed_with_failures"}
MAIN_REPLAY_RUN_ID = "latest"


def generate_paper_tables(cfg: Config) -> dict[str, object]:
    tables_dir = cfg.repo_root / "paper/tables"
    tables_dir.mkdir(parents=True, exist_ok=True)
    manifest = None
    protocol = None
    if manifest_exists(cfg) or (canonical_run_dir(cfg) / "warnings.jsonl").exists():
        manifest = validate_run_manifest(cfg)
        protocol = load_evaluation_protocol(cfg)
    replay_summary = tables_dir / "replay_summary.json"
    fact_counts = tables_dir / "fact_counts.json"
    manual_review = tables_dir / "manual_review_summary.json"
    runtime = tables_dir / "runtime_scalability.json"
    _write_replay_summary(cfg, replay_summary)
    _write_fact_counts(cfg, fact_counts)
    _write_manual_review_summary(cfg, manual_review, manifest=manifest)
    _write_runtime_scalability(cfg, runtime, manifest=manifest)
    audit = generate_extractor_audit(cfg, manifest=manifest)
    strict_audit = generate_strict_extractor_audit(cfg, manifest=manifest)
    _validate_table_consistency(cfg, manifest)
    known = {
        "evaluation_summary": tables_dir / "evaluation_summary.json",
        "baselines_ablations": tables_dir / "baselines_ablations.json",
        "extractor_audit": Path(audit["extractor_audit"]),
        "strict_extractor_audit": Path(strict_audit["strict_extractor_audit"]),
        "replay_summary": replay_summary,
        "fact_counts": fact_counts,
        "manual_review_summary": manual_review,
        "runtime_scalability": runtime,
        "ranking_pooled_evaluation": tables_dir / "ranking_pooled_evaluation.json",
        "ranking_score_audit": tables_dir / "ranking_score_audit.json",
        "baseline_strict_comparison": tables_dir / "baseline_strict_comparison.json",
        "ablation_strict_comparison": tables_dir / "ablation_strict_comparison.json",
        "warning_volume_reduction": tables_dir / "warning_volume_reduction.json",
        "run_manifest": canonical_run_dir(cfg) / "run_manifest.json",
        "evaluation_protocol": Path(protocol["path"]) if protocol else canonical_run_dir(cfg) / "evaluation_protocol.json",
        "toolchain_matrix": cfg.data_dir / "toolchain_matrix.json",
    }
    index = {
        name: {"path": repo_relative(cfg, path), "available": path.exists()}
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
        json.dumps({"runs": runs, "pairs": pairs, "main_evidence_gate": _main_replay_gate(conn, cfg)}, indent=2, sort_keys=True) + "\n",
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
    gate = _main_replay_gate(conn, cfg)
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
    gate = _main_replay_gate(conn, cfg)
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
                    "single_version_review_targets": manifest.get("single_version_review_targets", 0),
                }
            )
        else:
            item["promoted_warnings"] = summary.get("warnings")
        rows.append(item)
    path.write_text(
        json.dumps({"runs": rows, "main_evidence_gate": _main_replay_gate(conn, cfg)}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def _validate_table_consistency(cfg: Config, manifest: dict[str, Any] | None) -> None:
    if not manifest:
        return
    tables_dir = cfg.repo_root / "paper/tables"
    evaluation_path = tables_dir / "evaluation_summary.json"
    evaluation = None
    expected_oracle_blind_uids: list[Any] | None = None
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
        if evaluation.get("protocol_version") != "ccfb-strict-v1":
            raise RuntimeError("evaluation_summary missing protocol_version ccfb-strict-v1")
        if evaluation.get("claim_boundary") != "evidence-backed warning prioritization":
            raise RuntimeError("evaluation_summary missing claim_boundary")
        if evaluation.get("primary_warning_set") != "oracle_blind_ranked_warnings":
            raise RuntimeError("evaluation_summary missing oracle-blind primary_warning_set")
        primary = evaluation.get("oracle_blind_primary_result") or {}
        if primary.get("oracle_blind") is not True:
            raise RuntimeError("evaluation_summary oracle_blind_primary_result is not oracle-blind")
        leaked_score_keys = sorted(FORBIDDEN_PRIMARY_SCORE_COMPONENTS & set(primary.get("score_component_keys") or []))
        if leaked_score_keys:
            raise RuntimeError("evaluation_summary oracle_blind_primary_result leaks oracle score components: " + ", ".join(leaked_score_keys))
        promoted = read_warnings(Path(manifest["resolved_paths"]["promoted_warnings"]))
        expected_oracle_blind_uids = [
            warning.get("warning_uid")
            for warning in rank_primary_warnings_oracle_blind(promoted)[: manifest["paper_topk"]]
        ]
        if primary.get("top_warning_uids") != expected_oracle_blind_uids:
            raise RuntimeError("evaluation_summary oracle_blind_primary_result does not match promoted oracle-blind top-k")
        if evaluation.get("manual_review") != primary.get("manual_review"):
            raise RuntimeError("evaluation_summary manual_review is not the oracle-blind primary result")
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
        main_variants = [row for row in baselines.get("variants", []) if row.get("kind") == "main"]
        if len(main_variants) != 1 or main_variants[0].get("oracle_blind") is not True:
            raise RuntimeError("baselines_ablations main variant must be oracle-blind")
        for variant in baselines.get("variants", []):
            if variant.get("kind") == "auxiliary":
                continue
            if variant.get("oracle_blind") is not True:
                raise RuntimeError(f"baselines_ablations {variant.get('variant')} variant must be oracle-blind")
            leaked_score_keys = sorted(FORBIDDEN_PRIMARY_SCORE_COMPONENTS & set(variant.get("score_component_keys") or []))
            if leaked_score_keys:
                raise RuntimeError(
                    f"baselines_ablations {variant.get('variant')} variant leaks oracle score components: "
                    + ", ".join(leaked_score_keys)
                )
        main = main_variants[0]
        if expected_oracle_blind_uids is None:
            promoted = read_warnings(Path(manifest["resolved_paths"]["promoted_warnings"]))
            expected_oracle_blind_uids = [
                warning.get("warning_uid")
                for warning in rank_primary_warnings_oracle_blind(promoted)[: manifest["paper_topk"]]
            ]
        if main.get("top_warning_uids") != expected_oracle_blind_uids:
            raise RuntimeError("baselines_ablations main variant does not match promoted oracle-blind top-k")
    ranking_path = tables_dir / "ranking_pooled_evaluation.json"
    if ranking_path.exists():
        ranking = json.loads(ranking_path.read_text(encoding="utf-8"))
        pool_path = _resolve_table_path(cfg, ranking.get("pool"))
        labels_path = _resolve_table_path(cfg, ranking.get("labels"))
        if not pool_path.exists() or not labels_path.exists():
            raise RuntimeError("ranking_pooled_evaluation points to missing pool or labels file")
        if ranking.get("pool_sha256") != sha256_file(pool_path):
            raise RuntimeError("ranking_pooled_evaluation pool_sha256 does not match current pool file")
        if ranking.get("labels_sha256") != sha256_file(labels_path):
            raise RuntimeError("ranking_pooled_evaluation labels_sha256 does not match current labels file")
        if manifest.get("resolved_paths", {}).get("pooled_review_set"):
            expected_pool = Path(manifest["resolved_paths"]["pooled_review_set"]).resolve()
            expected_labels = Path(manifest["resolved_paths"]["pooled_review_labels"]).resolve()
            if pool_path.resolve() != expected_pool:
                raise RuntimeError(f"ranking_pooled_evaluation pool {pool_path} != run_manifest pooled review set {expected_pool}")
            if labels_path.resolve() != expected_labels:
                raise RuntimeError(f"ranking_pooled_evaluation labels {labels_path} != run_manifest pooled review labels {expected_labels}")
        coverage = _strict_pooled_label_coverage(pool_path, labels_path)
        if coverage["coverage"] < 0.95:
            raise RuntimeError(f"ranking_pooled_evaluation label coverage below 95%: {coverage['coverage']}")
        reported = ranking.get("label_coverage") or {}
        if reported.get("coverage") != coverage["coverage"] or reported.get("labeled_rows") != coverage["labeled_rows"]:
            raise RuntimeError("ranking_pooled_evaluation label_coverage does not match current pool and labels")
        if (ranking.get("coverage_acceptance") or {}).get("passes") is not True:
            raise RuntimeError(f"ranking_pooled_evaluation label coverage below 95%: {coverage['coverage']}")
        for row in ranking.get("rankers", []):
            if row.get("evaluated_pool_rows") != coverage["pool_rows"]:
                raise RuntimeError(f"ranking_pooled_evaluation {row.get('ranker')} does not use the full pooled review set")
            if row.get("label_distribution") != coverage["label_distribution"]:
                raise RuntimeError(f"ranking_pooled_evaluation {row.get('ranker')} label distribution is not the pooled label distribution")


def _load_json(value: str | None, default: Any) -> Any:
    if not value:
        return default
    try:
        parsed = json.loads(value)
        return default if parsed is None else parsed
    except json.JSONDecodeError:
        return default


def _resolve_table_path(cfg: Config, value: Any) -> Path:
    if not value:
        return Path("__missing__")
    return resolve_manifest_path(cfg, str(value))


def _strict_pooled_label_coverage(pool_path: Path, labels_path: Path) -> dict[str, Any]:
    rows_by_uid: dict[str, dict[str, str]] = {}
    with labels_path.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            uid = row.get("warning_uid", "").strip()
            if uid:
                rows_by_uid[uid] = row
    pool_rows = read_warnings(pool_path)
    reviewed = 0
    excluded_conservative = 0
    label_distribution: dict[str, int] = {}
    for warning in pool_rows:
        row = rows_by_uid.get(str(warning.get("warning_uid"))) or {}
        label = row.get("adjudicated_label", "").strip()
        if label:
            label_distribution[label] = label_distribution.get(label, 0) + 1
        source = row.get("label_source", "")
        complete = bool(
            row.get("reviewer1_label", "").strip()
            and row.get("reviewer2_label", "").strip()
            and row.get("adjudicated_label", "").strip()
            and row.get("adjudication_notes", "").strip()
        )
        if "conservative" in source.lower():
            excluded_conservative += 1
            continue
        if complete:
            reviewed += 1
    return {
        "labeled_rows": reviewed,
        "pool_rows": len(pool_rows),
        "coverage": round(reviewed / len(pool_rows), 4) if pool_rows else 0.0,
        "excluded_conservative_backfill_rows": excluded_conservative,
        "label_distribution": label_distribution,
    }


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


def _main_replay_gate(conn, cfg: Config | None = None) -> dict[str, Any]:
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
        manifest = None
        if cfg is not None and run_id == MAIN_REPLAY_RUN_ID and manifest_exists(cfg):
            try:
                manifest = validate_run_manifest(cfg)
            except Exception as exc:
                reasons.append(f"invalid_run_manifest:{type(exc).__name__}")
        run_dir = summary.get("run_dir")
        if manifest:
            run_dir = str(canonical_run_dir(cfg))
        if not run_dir or not Path(run_dir).exists():
            reasons.append("missing_replay_dir")
        aggregate_warnings = (
            manifest.get("resolved_paths", {}).get("promoted_warnings")
            if manifest
            else summary.get("aggregate_promoted_warnings") or summary.get("aggregate_warnings")
        )
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
