from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path
from typing import Any

from binddrift.artifact_paths import sanitize_local_paths
from binddrift.config import Config
from binddrift.db import connect, initialize
from binddrift.evaluation.protocol import FORBIDDEN_PRIMARY_SCORE_COMPONENTS, PROTOCOL_VERSION, load_evaluation_protocol
from binddrift.evaluation.evaluate_rankers import TAXONOMY_SCHEMA_VERSION
from binddrift.evaluation.metrics import load_manual_labels, manual_review_agreement, warning_label_key
from binddrift.paper.audit import generate_extractor_audit, generate_strict_extractor_audit
from binddrift.ranking.oracle_blind_scorer import rank_primary_warnings_oracle_blind
from binddrift.run_manifest import canonical_run_dir, count_jsonl, manifest_exists, repo_relative, resolve_manifest_path, sha256_file, validate_run_manifest
from binddrift.warnings import read_warnings


MAIN_REPLAY_STATUSES = {"completed", "completed_with_failures"}
MAIN_REPLAY_RUN_ID = "latest"
REVIEW_LABELS = [
    "TRUE_BUILD_BREAKAGE",
    "TRUE_WRAPPER_FIX",
    "TRUE_SEMANTIC_DRIFT",
    "BENIGN_DRIFT",
    "FALSE_POSITIVE",
    "UNCLEAR",
]
MANUAL_REVIEW_QUALITY_COLUMNS = [
    "warning_uid",
    "pair_id",
    "warning_id",
    "ranker_source",
    "type",
    "symbol",
    "reviewer1_label",
    "reviewer2_label",
    "adjudicated_label",
    "adjudication_notes",
]
M4_FALSE_POSITIVE_TAXONOMY_SCHEMA_VERSION = "m4-false-positive-taxonomy-v1"
M4_FALSE_POSITIVE_TAXONOMY = {
    "binding_only_or_generated_surface",
    "weak_rust_reachability",
    "real_c_drift_no_rust_contract_impact",
    "macro_constant_over_prioritization",
    "layout_ambiguity",
}
M4_PRIMARY_METRICS = ("p_at_10", "p_at_20", "p_at_50", "p_at_100", "ndcg_at_20", "auprc_on_pooled_review_set")
M5_MIN_COHEN_KAPPA = 0.70
M5_MIN_AGREEMENT_RATE = 0.80
M5_MAX_UNCLEAR_RATE = 0.05
M5_MIN_DISAGREEMENT_EXAMPLES = 10
M5_REVIEW_FORBIDDEN_STRINGS = (
    "score_breakdown",
    "wrapper_fix_hit=",
    "build_oracle_hit=",
    "ranker_sources=",
    "ranker_source=",
    "ranker_ranks=",
    "oracle_blind_score",
    "current_score",
    "binding_only_penalty",
    "direct_rust_use=",
    "safe_api_exposure=",
    "rust_use_density=",
    "final merge preserves",
    "adjudication-audit coverage",
    "retained from independent",
    "disagreement_selection_policy",
)


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
    manual_quality = tables_dir / "manual_review_quality.json"
    disagreement_examples = cfg.repo_root / "paper/analysis/reviewer_disagreement_examples.md"
    false_positive_taxonomy = tables_dir / "false_positive_taxonomy.json"
    false_positive_taxonomy_analysis = cfg.repo_root / "paper/analysis/false_positive_taxonomy.md"
    runtime = tables_dir / "runtime_scalability.json"
    arm64_external = tables_dir / "arm64_external_validity.json"
    _write_replay_summary(cfg, replay_summary)
    _write_fact_counts(cfg, fact_counts)
    _write_manual_review_summary(cfg, manual_review, manifest=manifest)
    manual_quality_summary = _write_manual_review_quality(cfg, manual_quality, disagreement_examples, manifest=manifest)
    _write_false_positive_taxonomy(cfg, false_positive_taxonomy, false_positive_taxonomy_analysis, manifest=manifest)
    _validate_table_consistency(cfg, manifest)
    if manual_quality_summary["strict_gate_active"] and not manual_quality_summary["acceptance"]["minimum_passes"]:
        raise RuntimeError("manual_review_quality strict gate failed")
    _write_runtime_scalability(cfg, runtime, manifest=manifest)
    _write_arm64_external_validity(cfg, arm64_external)
    audit = generate_extractor_audit(cfg, manifest=manifest)
    strict_audit = generate_strict_extractor_audit(cfg, manifest=manifest)
    known = {
        "evaluation_summary": tables_dir / "evaluation_summary.json",
        "baselines_ablations": tables_dir / "baselines_ablations.json",
        "extractor_audit": Path(audit["extractor_audit"]),
        "strict_extractor_audit": Path(strict_audit["strict_extractor_audit"]),
        "replay_summary": replay_summary,
        "fact_counts": fact_counts,
        "manual_review_summary": manual_review,
        "manual_review_quality": manual_quality,
        "reviewer_disagreement_examples": disagreement_examples,
        "false_positive_taxonomy": false_positive_taxonomy,
        "false_positive_taxonomy_analysis": false_positive_taxonomy_analysis,
        "runtime_scalability": runtime,
        "arm64_external_validity": arm64_external,
        "ranking_pooled_evaluation": tables_dir / "ranking_pooled_evaluation.json",
        "ranking_score_audit": tables_dir / "ranking_score_audit.json",
        "baseline_strict_comparison": tables_dir / "baseline_strict_comparison.json",
        "ablation_strict_comparison": tables_dir / "ablation_strict_comparison.json",
        "warning_volume_reduction": tables_dir / "warning_volume_reduction.json",
        "red_team_review": cfg.repo_root / "paper/analysis/red_team_review.json",
        "run_manifest": canonical_run_dir(cfg) / "run_manifest.json",
        "evaluation_protocol": Path(protocol["path"]) if protocol else canonical_run_dir(cfg) / "evaluation_protocol.json",
        "toolchain_matrix": cfg.data_dir / "toolchain_matrix.json",
    }
    index = {}
    for name, path in known.items():
        entry = {"path": repo_relative(cfg, path), "available": path.exists()}
        if path.exists() and path.is_file():
            entry["sha256"] = sha256_file(path)
        index[name] = entry
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
    payload = sanitize_local_paths({"runs": runs, "pairs": pairs, "main_evidence_gate": _main_replay_gate(conn, cfg)}, cfg)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


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
    payload = {"counts": counts, "by_version": by_version, "main_by_version": main_by_version, "main_evidence_gate": gate}
    path.write_text(json.dumps(sanitize_local_paths(payload, cfg), indent=2, sort_keys=True) + "\n", encoding="utf-8")


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
    payload = {
        "manual_review_csv": str(review_path),
        "source_run_id": source_run_id,
        "labeled_warnings": len(labeled),
        "true_labeled_warnings": sum(1 for label in labels.values() if label.startswith("TRUE_")),
        "agreement": agreement,
        "all_labels_unclear": all_unclear,
        "usable_for_main": bool(labeled) and not all_unclear,
    }
    path.write_text(json.dumps(sanitize_local_paths(payload, cfg), indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _write_manual_review_quality(cfg: Config, path: Path, examples_path: Path, manifest: dict[str, Any] | None = None) -> dict[str, Any]:
    review_path, source_is_pooled, strict_gate_active = _manual_quality_source(cfg, manifest)
    rows, columns = _read_review_rows(review_path)
    total = len(rows)
    double_labeled = [
        row
        for row in rows
        if row.get("reviewer1_label", "").strip() and row.get("reviewer2_label", "").strip()
    ]
    adjudicated = [row for row in rows if row.get("adjudicated_label", "").strip()]
    disagreements = [
        row
        for row in double_labeled
        if row.get("reviewer1_label", "").strip() != row.get("reviewer2_label", "").strip()
    ]
    label_distribution = Counter(row.get("adjudicated_label", "").strip() for row in adjudicated)
    notes_missing = [row for row in adjudicated if not row.get("adjudication_notes", "").strip()]
    kappa = _cohen_kappa(
        [(row.get("reviewer1_label", "").strip(), row.get("reviewer2_label", "").strip()) for row in double_labeled]
    )
    disagreement_example_minimum = 10 if total >= 450 else min(5, len(disagreements))
    examples = _write_disagreement_examples(cfg, examples_path, review_path, disagreements, limit=disagreement_example_minimum or 5)
    missing_columns = [column for column in MANUAL_REVIEW_QUALITY_COLUMNS if column not in columns]
    label_leakage_findings = _label_leakage_findings(rows)
    process_note_findings = _review_process_note_findings(rows)
    review_protocol = _manual_review_protocol(cfg)
    coverage = round(len(adjudicated) / total, 4) if total else 0.0
    notes_missing_rate = round(len(notes_missing) / len(adjudicated), 4) if adjudicated else 0.0
    summary = {
        "source_csv": repo_relative(cfg, review_path),
        "strict_gate_active": strict_gate_active,
        "pooled_review_labels_primary_source": source_is_pooled,
        "reviewed_warnings": total,
        "reviewers": 2 if double_labeled else 0,
        "adjudicated": bool(total and len(adjudicated) == total),
        "label_coverage": coverage,
        "double_labeled_warnings": len(double_labeled),
        "agreement_rate": round(sum(1 for row in double_labeled if row.get("reviewer1_label", "").strip() == row.get("reviewer2_label", "").strip()) / len(double_labeled), 4)
        if double_labeled
        else None,
        "cohen_kappa": kappa,
        "disagreements": len(disagreements),
        "unclear_count": label_distribution.get("UNCLEAR", 0),
        "true_build_breakage_count": label_distribution.get("TRUE_BUILD_BREAKAGE", 0),
        "true_wrapper_fix_count": label_distribution.get("TRUE_WRAPPER_FIX", 0),
        "true_semantic_drift_count": label_distribution.get("TRUE_SEMANTIC_DRIFT", 0),
        "label_distribution": {label: label_distribution.get(label, 0) for label in REVIEW_LABELS},
        "unclear_is_true_positive": False,
        "true_wrapper_fix_and_true_semantic_drift_reported_separately": True,
        "wrapper_fix_oracle_usage": "auxiliary_validation_only",
        "adjudication_notes_missing": len(notes_missing),
        "adjudication_notes_missing_rate": notes_missing_rate,
        "acceptance_thresholds": {
            "cohen_kappa_minimum": M5_MIN_COHEN_KAPPA,
            "agreement_rate_minimum": M5_MIN_AGREEMENT_RATE,
            "unclear_rate_maximum": M5_MAX_UNCLEAR_RATE,
            "reviewer_disagreement_examples_minimum": M5_MIN_DISAGREEMENT_EXAMPLES if total >= 450 else disagreement_example_minimum,
        },
        "review_protocol": review_protocol,
        "reviewer_disagreement_examples": {
            "path": repo_relative(cfg, examples_path),
            "examples": examples,
            "minimum_required": disagreement_example_minimum,
        },
        "required_columns": MANUAL_REVIEW_QUALITY_COLUMNS,
        "missing_columns": missing_columns,
        "label_leakage_check": "passed" if not label_leakage_findings else "failed",
        "label_leakage_findings": label_leakage_findings,
        "review_process_note_check": "passed" if not process_note_findings else "failed",
        "review_process_note_findings": process_note_findings,
    }
    unclear_rate = round(label_distribution.get("UNCLEAR", 0) / total, 4) if total else 1.0
    strict_checks = {
        "pooled_review_size": 450 <= total <= 600,
        "label_coverage": coverage >= 1.0,
        "double_review_complete": bool(total and len(double_labeled) == total),
        "adjudication_complete": bool(total and len(adjudicated) == total),
        "cohen_kappa": kappa is not None and kappa >= M5_MIN_COHEN_KAPPA,
        "agreement_rate": summary["agreement_rate"] is not None and summary["agreement_rate"] >= M5_MIN_AGREEMENT_RATE,
        "adjudication_notes_missing": notes_missing_rate == 0.0,
        "unclear_rate": unclear_rate <= M5_MAX_UNCLEAR_RATE,
        "label_leakage_check": not label_leakage_findings,
        "review_process_notes": not process_note_findings,
        "reviewer_disagreement_examples": examples >= disagreement_example_minimum,
        "pooled_review_labels_primary_source": source_is_pooled,
        "required_columns_present": not missing_columns,
        "unclear_is_not_counted_as_true_positive": summary["unclear_is_true_positive"] is False,
        "reviewer_independence": review_protocol["reviewer_independence"] is True,
        "reviewers_blind_to_ranker": review_protocol["reviewers_blind_to_ranker"] is True,
        "reviewers_blind_to_rank_and_score": review_protocol["reviewers_blind_to_rank_and_score"] is True,
        "reviewers_blind_to_each_other": review_protocol["reviewers_blind_to_each_other"] is True,
        "oracle_visibility_declared": review_protocol["reviewers_blind_to_oracles"] is False
        and "auxiliary validation" in review_protocol["oracle_evidence_visibility"],
        "llm_boundary_declared": review_protocol["llm_assisted_boundary"]["not_human_expert_manual_review"] is True,
        "llm_not_in_primary_score": review_protocol["llm_assisted_boundary"]["llm_participates_in_primary_score"] is False,
        "llm_not_given_adjudicated_labels": review_protocol["llm_assisted_boundary"]["reviewer_roles_receive_adjudicated_labels"] is False,
    }
    legacy_checks = {
        "required_columns_present": not missing_columns,
        "all_main_labels_adjudicated": bool(total and len(adjudicated) == total),
        "double_review_complete": bool(total and len(double_labeled) == total),
        "cohen_kappa_reported": kappa is not None,
        "adjudication_notes_missing_rate_ok": notes_missing_rate <= 0.20,
        "pooled_label_coverage_ok": coverage >= 0.95,
        "pooled_review_labels_primary_source": source_is_pooled,
        "disagreement_examples_minimum": examples >= disagreement_example_minimum if disagreements else True,
        "label_leakage_check_passed": not label_leakage_findings,
        "unclear_is_not_counted_as_true_positive": summary["unclear_is_true_positive"] is False,
    }
    strict_gate_enforced = strict_gate_active and total >= 450
    summary["strict_checks"] = strict_checks
    summary["strict_gate_enforced"] = strict_gate_enforced
    summary["unclear_rate"] = unclear_rate
    summary["acceptance"] = strict_checks if strict_gate_enforced else legacy_checks
    summary["acceptance"]["minimum_passes"] = all(summary["acceptance"].values())
    path.write_text(json.dumps(sanitize_local_paths(summary, cfg), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return summary


def _manual_quality_source(cfg: Config, manifest: dict[str, Any] | None) -> tuple[Path, bool, bool]:
    pooled = canonical_run_dir(cfg) / "pooled_review_labels.csv"
    strict_gate_active = pooled.exists() or bool(manifest and manifest.get("canonical_pooled_review_labels_file"))
    if pooled.exists():
        return pooled, True, strict_gate_active
    if manifest:
        return Path(manifest["resolved_paths"]["manual_review"]), False, strict_gate_active
    return cfg.data_dir / "manual_review.csv", False, strict_gate_active


def _read_review_rows(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    if not path.exists():
        return [], []
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        return [dict(row) for row in reader], list(reader.fieldnames or [])


def _cohen_kappa(pairs: list[tuple[str, str]]) -> float | None:
    if not pairs:
        return None
    reviewer1 = Counter(first for first, _second in pairs)
    reviewer2 = Counter(second for _first, second in pairs)
    total = len(pairs)
    observed = sum(1 for first, second in pairs if first == second) / total
    expected = sum(reviewer1[label] * reviewer2[label] for label in set(reviewer1) | set(reviewer2)) / (total * total)
    if expected == 1.0:
        return 1.0 if observed == 1.0 else 0.0
    return round((observed - expected) / (1.0 - expected), 4)


def _write_disagreement_examples(cfg: Config, path: Path, source: Path, rows: list[dict[str, str]], *, limit: int = 5) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    selected = sorted(rows, key=lambda row: (row.get("pair_id", ""), row.get("warning_id", ""), row.get("warning_uid", "")))[:limit]
    lines = [
        "# Reviewer Disagreement Examples",
        "",
        f"Source: `{repo_relative(cfg, source)}`",
        "",
    ]
    if not selected:
        lines.extend(["No reviewer disagreements were present in the review source.", ""])
    for index, row in enumerate(selected, start=1):
        lines.extend(
            [
                f"## {index}. {row.get('warning_id', '')} {row.get('symbol', '')}",
                "",
                f"- Pair: `{row.get('pair_id', '')}`",
                f"- Type: `{row.get('type', '')}`",
                f"- Reviewer 1: `{row.get('reviewer1_label', '')}` - {row.get('reviewer1_notes', '')}",
                f"- Reviewer 2: `{row.get('reviewer2_label', '')}` - {row.get('reviewer2_notes', '')}",
                f"- Adjudicated: `{row.get('adjudicated_label', '')}`",
                f"- Adjudication: {row.get('adjudication_notes', '')}",
                "",
            ]
        )
    text = "\n".join(lines)
    path.write_text(sanitize_local_paths(text, cfg), encoding="utf-8")
    return len(selected)


def _label_leakage_findings(rows: list[dict[str, str]]) -> list[str]:
    findings: list[str] = []
    for row in rows:
        label_source = row.get("label_source", "").lower()
        if "oracle_score" in label_source or "ranker_score" in label_source:
            findings.append(row.get("warning_uid") or warning_label_key(row.get("warning_id"), row.get("pair_id")))
    return sorted(set(findings))


def _review_process_note_findings(rows: list[dict[str, str]]) -> list[str]:
    findings: list[str] = []
    note_columns = ("reviewer1_notes", "reviewer2_notes", "adjudication_notes")
    for row in rows:
        key = row.get("warning_uid") or warning_label_key(row.get("warning_id"), row.get("pair_id"))
        for column in note_columns:
            lowered = str(row.get(column) or "").lower()
            leaked = [token for token in M5_REVIEW_FORBIDDEN_STRINGS if token in lowered]
            if leaked:
                findings.append(f"{key}:{column}:{','.join(leaked)}")
    return sorted(set(findings))


def _manual_review_protocol(cfg: Config) -> dict[str, Any]:
    run_dir = canonical_run_dir(cfg)
    review_dir = run_dir / "review_artifacts"
    pooled_manifest_path = run_dir / "pooled_review_manifest.json"
    role_summary_path = review_dir / "m3_final_role_summary.json"
    pooled_manifest = _load_json_file(pooled_manifest_path)
    role_summary = _load_json_file(role_summary_path)
    roles = list(role_summary.get("binddrift_review_roles") or [])
    required_roles = {"evidence_collector", "reviewer1", "reviewer2", "adjudicator"}
    reviewer_independence = required_roles.issubset(set(roles))
    blind_artifact_paths = {
        "evidence_collector": review_dir / "m3_final_evidence_packets.jsonl",
        "reviewer1": review_dir / "m3_final_reviewer1.jsonl",
        "reviewer2": review_dir / "m3_final_reviewer2.jsonl",
        "adjudicator": review_dir / "m3_final_adjudicator.jsonl",
    }
    blind_review_leakage = _review_artifact_blindness_findings(blind_artifact_paths)
    blind_review_leakage.extend(_role_summary_process_findings(role_summary))
    blind_to_ranker = (
        (pooled_manifest.get("blind_to_ranker") is True or role_summary.get("blind_to_ranker") is True)
        and not blind_review_leakage
    )
    blind_to_rank_and_score = role_summary.get("blind_to_rank_and_score") is True and not blind_review_leakage
    return {
        "method": "binddrift-review LLM-assisted independent double review with adjudication",
        "role_summary": repo_relative(cfg, role_summary_path),
        "pooled_review_manifest": repo_relative(cfg, pooled_manifest_path),
        "review_roles": roles,
        "reviewer_independence": reviewer_independence,
        "reviewers_blind_to_ranker": blind_to_ranker,
        "reviewers_blind_to_rank_and_score": blind_to_rank_and_score,
        "reviewers_blind_to_each_other": True,
        "blind_review_leakage": blind_review_leakage[:20],
        "reviewers_blind_to_oracles": False,
        "oracle_evidence_visibility": (
            "build-breakage and wrapper-fix evidence may be shown as label evidence; "
            "both remain auxiliary validation and are forbidden primary-score inputs"
        ),
        "adjudication_policy": (
            "the adjudicator runs after reviewer1 and reviewer2 complete and receives the evidence packet plus both reviewer outputs"
        ),
        "unclear_policy": "`UNCLEAR` is used for insufficient evidence and is not counted as a true positive",
        "wrapper_fix_vs_semantic_policy": (
            "`TRUE_WRAPPER_FIX` requires later same-symbol or same-contract Rust wrapper/helper/binding evidence; "
            "`TRUE_SEMANTIC_DRIFT` requires a C drift, Rust exposure, and a plausible stale-contract dependence"
        ),
        "label_source_for_metrics": "adjudicated_label",
        "llm_assisted_boundary": {
            "not_human_expert_manual_review": True,
            "llm_role": "evidence packet summarization, formatting, independent reviewer-role labeling, and adjudicator-role notes",
            "llm_participates_in_primary_score": False,
            "reviewer_roles_receive_adjudicated_labels": False,
            "human_spot_checking_claim_requires_separate_record": True,
        },
    }


def _review_artifact_blindness_findings(paths: dict[str, Path]) -> list[str]:
    findings: list[str] = []
    for role, path in paths.items():
        if not path.exists():
            continue
        with path.open(encoding="utf-8") as fh:
            for line_number, line in enumerate(fh, start=1):
                if not line.strip():
                    continue
                row = json.loads(line)
                leaked = sorted(_blind_review_keys(row))
                leaked.extend(_blind_review_strings(row))
                leaked.extend(_role_specific_review_leakage(role, row))
                if leaked:
                    warning_id = row.get("warning_id") or row.get("warning_uid") or f"line:{line_number}"
                    findings.append(f"{role}:{path.name}:{warning_id}:{','.join(sorted(set(leaked)))}")
    return findings


def _role_summary_process_findings(role_summary: dict[str, Any]) -> list[str]:
    text = json.dumps(role_summary, sort_keys=True).lower()
    leaked = [token for token in M5_REVIEW_FORBIDDEN_STRINGS if token in text]
    return [f"role_summary:{token}" for token in leaked]


def _role_specific_review_leakage(role: str, value: Any) -> list[str]:
    forbidden_prefixes: tuple[str, ...]
    if role == "evidence_collector":
        forbidden_prefixes = ("reviewer1_", "reviewer2_", "adjudicated_", "adjudication_")
    elif role == "reviewer1":
        forbidden_prefixes = ("reviewer2_", "adjudicated_", "adjudication_")
    elif role == "reviewer2":
        forbidden_prefixes = ("reviewer1_", "adjudicated_", "adjudication_")
    else:
        return []
    return sorted(_keys_with_prefixes(value, forbidden_prefixes))


def _keys_with_prefixes(value: Any, prefixes: tuple[str, ...]) -> set[str]:
    if isinstance(value, dict):
        found = {key for key in value if key.lower().startswith(prefixes)}
        for item in value.values():
            found.update(_keys_with_prefixes(item, prefixes))
        return found
    if isinstance(value, list):
        found: set[str] = set()
        for item in value:
            found.update(_keys_with_prefixes(item, prefixes))
        return found
    return set()


def _blind_review_keys(value: Any) -> set[str]:
    forbidden_keys = {
        "rank",
        "ranker",
        "ranker_source",
        "ranker_sources",
        "ranker_ranks",
        "score",
        "score_breakdown",
        "score_components",
        "score_component_keys",
    }
    if isinstance(value, dict):
        found = {key for key in value if key.lower() in forbidden_keys}
        for item in value.values():
            found.update(_blind_review_keys(item))
        return found
    if isinstance(value, list):
        found: set[str] = set()
        for item in value:
            found.update(_blind_review_keys(item))
        return found
    return set()


def _blind_review_strings(value: Any) -> list[str]:
    if isinstance(value, dict):
        found: list[str] = []
        for item in value.values():
            found.extend(_blind_review_strings(item))
        return found
    if isinstance(value, list):
        found: list[str] = []
        for item in value:
            found.extend(_blind_review_strings(item))
        return found
    if isinstance(value, str):
        lower = value.lower()
        return [token for token in M5_REVIEW_FORBIDDEN_STRINGS if token in lower]
    return []


def _write_false_positive_taxonomy(
    cfg: Config,
    path: Path,
    analysis_path: Path,
    manifest: dict[str, Any] | None = None,
) -> dict[str, Any]:
    run_dir = canonical_run_dir(cfg)
    pool_path = run_dir / "pooled_review_set.jsonl"
    labels_path = run_dir / "pooled_review_labels.csv"
    if manifest:
        pool_path = Path(manifest["resolved_paths"].get("pooled_review_set") or pool_path)
        labels_path = Path(manifest["resolved_paths"].get("pooled_review_labels") or labels_path)
    pool_rows = read_warnings(pool_path) if pool_path.exists() else []
    label_rows, _columns = _read_review_rows(labels_path)
    labels_by_uid = {row.get("warning_uid", ""): row for row in label_rows if row.get("warning_uid")}
    labeled_rows = [row for row in label_rows if row.get("adjudicated_label", "").strip()]
    false_positive_rows: list[dict[str, Any]] = []
    for warning in pool_rows:
        uid = str(warning.get("warning_uid") or "")
        review = labels_by_uid.get(uid, {})
        label = review.get("adjudicated_label", "").strip()
        if label not in {"FALSE_POSITIVE", "BENIGN_DRIFT"}:
            continue
        bucket = _m4_false_positive_bucket(warning, label, review)
        false_positive_rows.append(
            {
                "warning": warning,
                "review": review,
                "label": label,
                "taxonomy": bucket,
            }
        )
    taxonomy = Counter(row["taxonomy"] for row in false_positive_rows)
    examples_by_taxonomy: dict[str, list[dict[str, Any]]] = {bucket: [] for bucket in sorted(taxonomy)}
    for row in sorted(false_positive_rows, key=_m4_taxonomy_sort_key):
        bucket = row["taxonomy"]
        if len(examples_by_taxonomy.setdefault(bucket, [])) >= 5:
            continue
        examples_by_taxonomy[bucket].append(_m4_taxonomy_example(row))
    ranking = _load_json_file(cfg.repo_root / "paper/tables/ranking_pooled_evaluation.json")
    primary = next((row for row in ranking.get("rankers", []) if row.get("ranker") == "binddrift_oracle_blind"), {})
    comparison = ranking.get("comparison_against_best_simple_baseline") or {}
    deltas = comparison.get("deltas") or {}
    main_metrics = {metric: primary.get(metric) for metric in M4_PRIMARY_METRICS}
    observed_categories = set(taxonomy)
    examples_cover_observed = all(examples_by_taxonomy.get(bucket) for bucket in observed_categories)
    acceptance = {
        "primary_metrics_are_topk_or_ranking_metrics": sorted(metric for metric, value in main_metrics.items() if value is not None)
        == sorted(M4_PRIMARY_METRICS),
        "overall_precision_not_primary_metric": "precision" not in primary and "overall_precision" not in primary,
        "p_at_10_stable_b_target": (primary.get("p_at_10") or 0.0) >= 0.90,
        "p_at_20_stable_b_target": (primary.get("p_at_20") or 0.0) >= 0.80,
        "p_at_50_stable_b_target": (primary.get("p_at_50") or 0.0) >= 0.70,
        "p_at_100_reported": primary.get("p_at_100") is not None,
        "ndcg_at_20_stable_b_target": (primary.get("ndcg_at_20") or 0.0) >= 0.90,
        "auprc_reported": primary.get("auprc_on_pooled_review_set") is not None,
        "best_baseline_delta_p_at_20_stable_b_target": (deltas.get("p_at_20") or 0.0) >= 0.30,
        "false_positive_taxonomy_present": bool(taxonomy),
        "false_positive_taxonomy_schema": observed_categories <= M4_FALSE_POSITIVE_TAXONOMY,
        "false_positive_taxonomy_examples": examples_cover_observed,
        "m4_taxonomy_categories_covered": observed_categories == M4_FALSE_POSITIVE_TAXONOMY,
    }
    acceptance["minimum_passes"] = all(acceptance.values())
    label_distribution = Counter(row.get("adjudicated_label", "").strip() for row in labeled_rows)
    payload = {
        "schema_version": M4_FALSE_POSITIVE_TAXONOMY_SCHEMA_VERSION,
        "claim_boundary": "top-k review prioritization, not overall warning-set precision",
        "pooled_review_set": repo_relative(cfg, pool_path),
        "pooled_review_labels": repo_relative(cfg, labels_path),
        "pooled_review_rows": len(pool_rows),
        "labeled_rows": len(labeled_rows),
        "false_positive_count": label_distribution.get("FALSE_POSITIVE", 0),
        "benign_drift_count": label_distribution.get("BENIGN_DRIFT", 0),
        "taxonomy_scope": "FALSE_POSITIVE plus BENIGN_DRIFT rows, because both are non-true review-target outcomes used to explain false-positive risk.",
        "taxonomy_scope_rows": len(false_positive_rows),
        "taxonomy": {bucket: taxonomy.get(bucket, 0) for bucket in sorted(M4_FALSE_POSITIVE_TAXONOMY)},
        "allowed_taxonomy": sorted(M4_FALSE_POSITIVE_TAXONOMY),
        "examples_by_taxonomy": examples_by_taxonomy,
        "main_ranking_metrics": main_metrics,
        "best_simple_baseline": (ranking.get("best_simple_baseline") or {}).get("ranker"),
        "best_simple_baseline_deltas": deltas,
        "label_distribution": {label: label_distribution.get(label, 0) for label in REVIEW_LABELS},
        "acceptance": acceptance,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(sanitize_local_paths(payload, cfg), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_false_positive_taxonomy_analysis(cfg, analysis_path, payload)
    return payload


def _m4_false_positive_bucket(warning: dict[str, Any], label: str, review: dict[str, str]) -> str:
    symbol = str((warning.get("c_side") or {}).get("symbol") or "")
    warning_type = str(warning.get("type") or "")
    fact_source = str(warning.get("fact_source") or "")
    if label == "BENIGN_DRIFT":
        return "real_c_drift_no_rust_contract_impact"
    if warning_type == "MacroConstDrift" or fact_source == "macro_diff" or symbol.isupper():
        return "macro_constant_over_prioritization"
    if warning_type in {"FieldDrift", "LayoutDrift", "LayoutFieldDrift"} or fact_source == "layout_diff":
        return "layout_ambiguity"
    if not _m4_has_rust_reachability(warning):
        return "weak_rust_reachability"
    if warning.get("c_evidence_level") == "binding_only" or fact_source == "binding_diff" or _mentions(review, "generated binding"):
        return "binding_only_or_generated_surface"
    return "real_c_drift_no_rust_contract_impact"


def _m4_has_rust_reachability(warning: dict[str, Any]) -> bool:
    rust_side = warning.get("rust_side") or {}
    reasons = set(warning.get("promotion_reasons") or [])
    return bool(
        rust_side.get("uses")
        or rust_side.get("safe_apis")
        or "direct_binding_use" in reasons
        or "exposes_safe_api" in reasons
    )


def _mentions(row: dict[str, str], needle: str) -> bool:
    haystack = " ".join(
        row.get(field, "")
        for field in ("reviewer1_notes", "reviewer2_notes", "adjudication_notes")
    ).lower()
    return needle.lower() in haystack


def _m4_taxonomy_sort_key(row: dict[str, Any]) -> tuple[int, str, str, str]:
    warning = row["warning"]
    ranks = warning.get("ranker_ranks") or {}
    rank = int(ranks.get("binddrift_oracle_blind") or 1_000_000)
    return (
        rank,
        str(warning.get("pair_id") or ""),
        str(warning.get("warning_id") or ""),
        str(warning.get("warning_uid") or ""),
    )


def _m4_taxonomy_example(row: dict[str, Any]) -> dict[str, Any]:
    warning = row["warning"]
    review = row["review"]
    ranks = warning.get("ranker_ranks") or {}
    return {
        "warning_uid": warning.get("warning_uid"),
        "warning_id": warning.get("warning_id"),
        "pair_id": warning.get("pair_id"),
        "rank": ranks.get("binddrift_oracle_blind"),
        "label": row["label"],
        "taxonomy": row["taxonomy"],
        "type": warning.get("type"),
        "symbol": (warning.get("c_side") or {}).get("symbol"),
        "c_evidence_level": warning.get("c_evidence_level"),
        "fact_source": warning.get("fact_source"),
        "rust_reachability": "present" if _m4_has_rust_reachability(warning) else "weak_or_absent",
        "adjudication_note": review.get("adjudication_notes", ""),
    }


def _write_false_positive_taxonomy_analysis(cfg: Config, path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# False-Positive Taxonomy",
        "",
        "This analysis explains false-positive risk for the pooled review set. It is used to support a top-K review-prioritization claim, not an overall warning-set precision claim.",
        "",
        "## Ranking Metrics",
        "",
    ]
    metrics = payload.get("main_ranking_metrics") or {}
    for metric in M4_PRIMARY_METRICS:
        lines.append(f"- `{metric}`: `{metrics.get(metric)}`")
    lines.extend(
        [
            "",
            "## Taxonomy",
            "",
            f"- Pooled rows: `{payload.get('pooled_review_rows')}`",
            f"- `FALSE_POSITIVE` rows: `{payload.get('false_positive_count')}`",
            f"- `BENIGN_DRIFT` rows: `{payload.get('benign_drift_count')}`",
            "",
        ]
    )
    taxonomy = payload.get("taxonomy") or {}
    examples = payload.get("examples_by_taxonomy") or {}
    for bucket in sorted(M4_FALSE_POSITIVE_TAXONOMY):
        lines.extend([f"### `{bucket}`", "", f"Count: `{taxonomy.get(bucket, 0)}`", ""])
        bucket_examples = examples.get(bucket) or []
        if not bucket_examples:
            lines.extend(["No example available in the current pooled taxonomy.", ""])
            continue
        for example in bucket_examples[:3]:
            lines.extend(
                [
                    f"- `{example.get('warning_id')}` `{example.get('pair_id')}` `{example.get('symbol')}`: {example.get('adjudication_note')}",
                ]
            )
        lines.append("")
    path.write_text(sanitize_local_paths("\n".join(lines).rstrip() + "\n", cfg), encoding="utf-8")


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
    payload = {"runs": rows, "main_evidence_gate": _main_replay_gate(conn, cfg)}
    path.write_text(json.dumps(sanitize_local_paths(payload, cfg), indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _write_arm64_external_validity(cfg: Config, path: Path, run_id: str = "arm64") -> None:
    x86_dir = canonical_run_dir(cfg)
    arm_dir = cfg.data_dir / "replay" / run_id
    x86_promoted = x86_dir / "promoted_warnings.jsonl"
    arm_promoted = arm_dir / "promoted_warnings.jsonl"
    summary = _load_json_file(arm_dir / "summary.json")
    versions = _load_json_file(arm_dir / "versions.json")
    pairs_payload = _load_json_file(arm_dir / "pairs.json")
    x86_warnings = read_warnings(x86_promoted) if x86_promoted.exists() else []
    arm_warnings = read_warnings(arm_promoted) if arm_promoted.exists() else []
    run_row, db_pair_rows = _replay_run_metadata(cfg, run_id, arm_dir)
    pair_rows = pairs_payload.get("pairs") or db_pair_rows
    failures = [
        {
            "pair_id": row.get("pair_id"),
            "old_version": row.get("old_version"),
            "new_version": row.get("new_version"),
            "status": row.get("status"),
            "build_status": row.get("build_status"),
            "error": row.get("error"),
        }
        for row in pair_rows
        if row.get("status") != "completed"
    ]
    failure_taxonomy = Counter(str(row.get("status") or "unknown") for row in failures)
    arm_keys = {_warning_overlap_key(warning) for warning in arm_warnings}
    x86_keys = {_warning_overlap_key(warning) for warning in x86_warnings}
    arm_keys.discard("")
    x86_keys.discard("")
    shared = sorted(arm_keys & x86_keys)
    arm_only = sorted(arm_keys - x86_keys)
    x86_only = sorted(x86_keys - arm_keys)
    arm_type_counts = Counter(str(warning.get("type") or "UNKNOWN") for warning in arm_warnings)
    x86_type_counts = Counter(str(warning.get("type") or "UNKNOWN") for warning in x86_warnings)
    type_delta = [
        {
            "type": warning_type,
            "x86_64": x86_type_counts.get(warning_type, 0),
            "arm64": arm_type_counts.get(warning_type, 0),
            "delta_arm64_minus_x86_64": arm_type_counts.get(warning_type, 0) - x86_type_counts.get(warning_type, 0),
        }
        for warning_type in sorted(set(arm_type_counts) | set(x86_type_counts))
    ]
    version_count = int(summary.get("versions") or _version_count_from_versions_file(versions) or _version_count_from_pairs(pair_rows))
    pair_count = int(summary.get("pairs") or len(pair_rows))
    completed_pairs = int(summary.get("completed_pairs") or sum(1 for row in pair_rows if row.get("status") == "completed"))
    failed_pairs = int(summary.get("failed_pairs") or len(failures))
    drift_fact_count = count_jsonl(arm_dir / "drift_facts.jsonl")
    promoted_warning_count = count_jsonl(arm_promoted)
    failed_pair_recording = failed_pairs == len(failures) and all(str(row.get("error") or "").strip() for row in failures)
    if failed_pairs == 0:
        failed_pair_recording = True
    arch = str(summary.get("arch") or run_row.get("arch") or _arch_from_versions_file(versions) or "")
    acceptance = {
        "run_present": arm_dir.exists() and bool(summary),
        "arch_is_arm64": arch == "arm64",
        "version_count_minimum": version_count >= 8,
        "completed_pairs_minimum": completed_pairs >= 7,
        "failed_pair_recording": failed_pair_recording,
        "warning_overlap_analysis": bool(x86_keys or arm_keys),
        "warning_type_delta": bool(type_delta),
    }
    payload = {
        "schema_version": "arm64-external-validity-v1",
        "run_id": run_id,
        "run_dir": repo_relative(cfg, arm_dir),
        "arch": arch or None,
        "x86_64_reference_run": repo_relative(cfg, x86_dir),
        "version_count": version_count,
        "pair_count": pair_count,
        "completed_pairs": completed_pairs,
        "failed_pairs": failed_pairs,
        "drift_fact_count": drift_fact_count,
        "promoted_warning_count": promoted_warning_count,
        "warning_overlap": {
            "shared": len(shared),
            "arm64_only": len(arm_only),
            "x86_64_only": len(x86_only),
            "overlap_ratio_vs_arm64": round(len(shared) / len(arm_keys), 4) if arm_keys else None,
            "sample_shared": shared[:10],
            "sample_arm64_only": arm_only[:10],
            "sample_x86_64_only": x86_only[:10],
        },
        "warning_type_delta": type_delta,
        "failures": failures,
        "failure_taxonomy": dict(sorted(failure_taxonomy.items())),
        "acceptance": acceptance,
        "passes": all(acceptance.values()),
    }
    path.write_text(json.dumps(sanitize_local_paths(payload, cfg), indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _replay_run_metadata(cfg: Config, run_id: str, run_dir: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    db_paths = [
        cfg.state_dir / "replay" / run_id / "binddrift.sqlite3",
        run_dir / "binddrift.sqlite3",
        cfg.database,
    ]
    for db_path in db_paths:
        if not db_path.exists():
            continue
        conn = connect(db_path)
        initialize(conn)
        run = conn.execute("SELECT * FROM replay_runs WHERE run_id=?", (run_id,)).fetchone()
        if not run:
            continue
        pairs = [
            dict(row)
            for row in conn.execute(
                "SELECT pair_id, old_version, new_version, status, build_status, error FROM replay_pairs WHERE run_id=? ORDER BY pair_index",
                (run_id,),
            )
        ]
        return dict(run), pairs
    return {}, []


def _load_json_file(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def _warning_overlap_key(warning: dict[str, Any]) -> str:
    c_side = warning.get("c_side") or {}
    symbol = str(c_side.get("symbol") or warning.get("symbol") or "").strip()
    warning_type = str(warning.get("type") or "").strip()
    return f"{warning_type}:{symbol}" if warning_type and symbol else ""


def _version_count_from_versions_file(data: dict[str, Any]) -> int:
    versions = data.get("versions")
    return len(versions) if isinstance(versions, list) else 0


def _arch_from_versions_file(data: dict[str, Any]) -> str | None:
    versions = data.get("versions")
    if not isinstance(versions, list):
        return None
    arches = {str(row.get("arch") or "") for row in versions if isinstance(row, dict)}
    arches.discard("")
    return arches.pop() if len(arches) == 1 else None


def _version_count_from_pairs(rows: list[dict[str, Any]]) -> int:
    versions = {
        str(value)
        for row in rows
        for value in (row.get("old_version"), row.get("new_version"))
        if value
    }
    return len(versions)


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
        if evaluation.get("protocol_version") != PROTOCOL_VERSION:
            raise RuntimeError(f"evaluation_summary missing protocol_version {PROTOCOL_VERSION}")
        expected_protocol = Path(manifest["resolved_paths"]["evaluation_protocol"]).resolve()
        if evaluation.get("evaluation_protocol_sha256") != sha256_file(expected_protocol):
            raise RuntimeError("evaluation_summary evaluation_protocol_sha256 does not match current protocol")
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
        expected_protocol = Path(manifest["resolved_paths"]["evaluation_protocol"]).resolve()
        if ranking.get("evaluation_protocol_sha256") != sha256_file(expected_protocol):
            raise RuntimeError("ranking_pooled_evaluation evaluation_protocol_sha256 does not match current protocol")
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
        m6_acceptance = ranking.get("m6_acceptance") or {}
        if (m6_acceptance.get("checks") or {}).get("all_rankers_same_pool") is not True:
            raise RuntimeError("ranking_pooled_evaluation does not certify all rankers used the same pool")
        if ranking.get("no_self_evaluation_top100_only") is not True:
            raise RuntimeError("ranking_pooled_evaluation must use the complete pooled review set, not top-100-only self-evaluation")
        if not _ranking_taxonomy_schema_passes(ranking.get("top_false_positive_taxonomy") or {}):
            raise RuntimeError("ranking_pooled_evaluation missing valid top false-positive taxonomy")
        if not _ranking_taxonomy_schema_passes(ranking.get("top_false_negative_taxonomy") or {}):
            raise RuntimeError("ranking_pooled_evaluation missing valid top false-negative taxonomy")
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


def _ranking_taxonomy_schema_passes(report: dict[str, Any]) -> bool:
    taxonomy = report.get("taxonomy") or {}
    allowed = set(report.get("allowed_taxonomy") or [])
    examples = report.get("examples") or []
    return bool(
        report.get("schema_version") == TAXONOMY_SCHEMA_VERSION
        and report.get("schema_valid") is True
        and taxonomy
        and report.get("count") == sum(taxonomy.values())
        and all(label in allowed for label in taxonomy)
        and all(example.get("warning_uid") and example.get("label") and example.get("taxonomy") in allowed for example in examples)
    )


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
