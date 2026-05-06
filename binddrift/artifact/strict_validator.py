from __future__ import annotations

import csv
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any

from binddrift.artifact_paths import LOCAL_PATH_MARKERS, repo_relative, sanitize_local_paths
from binddrift.config import Config
from binddrift.detectors.semantic_review_targets import SEMANTIC_REVIEW_QUOTAS, generate_semantic_review_targets
from binddrift.evaluation.evaluate_rankers import TAXONOMY_SCHEMA_VERSION, build_ranker_evaluation, evaluate_rankers
from binddrift.evaluation.protocol import assert_oracle_blind_components, load_evaluation_protocol
from binddrift.paper.audit import STRICT_AUDIT_TARGETS, STRICT_TARGET_PRECISION, generate_strict_extractor_audit
from binddrift.paper.cases import generate_case_studies
from binddrift.paper.tables import generate_paper_tables
from binddrift.ranking.oracle_blind_scorer import generated_binding_only, rank_primary_warnings_oracle_blind
from binddrift.ranking.score_audit import generate_ranking_score_audit
from binddrift.run_manifest import canonical_run_dir, validate_run_manifest
from binddrift.warnings import read_warnings

VALIDATION_STAGES = ("m0", "m1", "m2", "m3", "m4", "m5", "m6", "m7", "m8", "final")

STAGE_REQUIRED_CHECKS: dict[str, set[str]] = {
    "m0": {
        "run_manifest_valid",
        "evaluation_protocol_valid",
        "required_tables_exist",
        "oracle_blind_primary_has_no_forbidden_components",
        "paper_claims_match_downgrades",
    },
    "m1": {"no_local_absolute_paths"},
    "m2": {"ranking"},
    "m3": {"pooled_review_coverage", "manual_review_quality_gate", "binddrift_review_role_artifacts"},
    "m4": {"semantic"},
    "m5": {"case_study_gate"},
    "m6": {"ranking"},
    "m7": {"strict_extractor_audit_gate"},
    "m8": {"ranking", "semantic", "manual_review_quality_gate", "case_study_gate", "strict_extractor_audit_gate"},
    "final": {"ranking", "semantic", "manual_review_quality_gate", "case_study_gate", "strict_extractor_audit_gate"},
}

HARD_GATE_CHECK_NAMES = {
    "ranking",
    "semantic",
    "manual_review_quality_gate",
    "case_study_gate",
    "strict_extractor_audit_gate",
}


def _stage_index(stage: str) -> int:
    if stage == "final":
        return VALIDATION_STAGES.index("m8")
    return VALIDATION_STAGES.index(stage)


def _required_for_stage(stage: str) -> set[str]:
    required: set[str] = set()
    for name in VALIDATION_STAGES:
        if name == "final":
            continue
        required.update(STAGE_REQUIRED_CHECKS.get(name, set()))
        if _stage_index(name) >= _stage_index(stage):
            break
    if stage == "final":
        required.update(STAGE_REQUIRED_CHECKS["final"])
    return required


def reproduce_artifact(cfg: Config) -> dict[str, Any]:
    manifest = validate_run_manifest(cfg)
    pooled_review_set = Path(manifest["resolved_paths"]["pooled_review_set"])
    pooled_review_labels = Path(manifest["resolved_paths"]["pooled_review_labels"])
    outputs = {
        "ranking_pooled_evaluation": evaluate_rankers(cfg, pool=pooled_review_set, labels=pooled_review_labels),
        "ranking_score_audit": generate_ranking_score_audit(cfg),
        "semantic_review_targets": generate_semantic_review_targets(cfg),
        "case_studies": generate_case_studies(cfg),
        "strict_extractor_audit": generate_strict_extractor_audit(cfg, manifest=manifest),
        "paper_tables": generate_paper_tables(cfg),
    }
    report = validate_artifact(cfg, strict_ccfb=True, run_tests=False, stage="final")
    outputs["validation"] = report
    return sanitize_local_paths({
        "passes": report["passes"],
        "status": report["status"],
        "outputs": outputs,
    }, cfg)


def validate_artifact(
    cfg: Config,
    *,
    strict_ccfb: bool = False,
    run_tests: bool = False,
    stage: str = "final",
) -> dict[str, Any]:
    if stage not in VALIDATION_STAGES:
        raise ValueError(f"unknown validation stage {stage!r}; expected one of {', '.join(VALIDATION_STAGES)}")
    checks: list[dict[str, Any]] = []
    manifest = _check("run_manifest_valid", checks, lambda: validate_run_manifest(cfg))
    protocol = _check("evaluation_protocol_valid", checks, lambda: load_evaluation_protocol(cfg))
    _check("required_tables_exist", checks, lambda: _required_tables(cfg))
    _check("oracle_blind_primary_has_no_forbidden_components", checks, lambda: _oracle_blind_components(cfg))
    _check("pooled_review_coverage", checks, lambda: _pooled_review_coverage(cfg))
    _check("manual_review_quality_gate", checks, lambda: _manual_review_quality_gate(cfg))
    _check("binddrift_review_role_artifacts", checks, lambda: _binddrift_review_role_artifacts(cfg))
    _check("case_study_gate", checks, lambda: _case_study_gate(cfg))
    _check("strict_extractor_audit_gate", checks, lambda: _strict_extractor_gate(cfg))
    _check("paper_claims_match_downgrades", checks, lambda: _paper_claims(cfg))
    _check("no_local_absolute_paths", checks, lambda: _no_local_paths(cfg))
    if run_tests:
        _check("pytest", checks, lambda: _run_pytest(cfg))
    ranking = _gate(lambda: _ranking_gate(cfg))
    semantic = _gate(lambda: _semantic_gate(cfg))
    hard_gates = {
        "ranking": ranking,
        "semantic": semantic,
        "manual_review_quality": _gate(lambda: _manual_review_quality_gate(cfg)),
        "case_studies": _gate(lambda: _case_study_gate(cfg)),
        "strict_extractor_audit": _gate(lambda: _strict_extractor_gate(cfg)),
    }
    checks_by_name = {check["name"]: check for check in checks}
    required_names = _required_for_stage(stage)
    stage_check_names = required_names - HARD_GATE_CHECK_NAMES
    consistency_passes = all(checks_by_name.get(name, {"passes": False})["passes"] for name in stage_check_names)
    hard_gate_passes = {
        "ranking": ranking["passes"],
        "semantic": semantic["passes"],
        "manual_review_quality_gate": hard_gates["manual_review_quality"]["passes"],
        "case_study_gate": hard_gates["case_studies"]["passes"],
        "strict_extractor_audit_gate": hard_gates["strict_extractor_audit"]["passes"],
    }
    required_hard_passes = all(hard_gate_passes[name] for name in required_names if name in hard_gate_passes)
    stage_passes = consistency_passes and required_hard_passes
    submission_ready = (
        all(check["passes"] for check in checks)
        and ranking["passes"]
        and semantic["passes"]
        and hard_gates["manual_review_quality"]["passes"]
        and hard_gates["case_studies"]["passes"]
    )
    report = {
        "passes": stage_passes,
        "status": "ccfb_ready" if submission_ready else ("stage_ready" if stage_passes else "failed"),
        "strict_ccfb": strict_ccfb,
        "stage": stage,
        "stage_required_checks": sorted(required_names),
        "ccfb_submission_ready": submission_ready,
        "checks": checks,
        "hard_gates": hard_gates,
        "run_manifest": repo_relative(cfg, canonical_run_dir(cfg) / "run_manifest.json"),
        "protocol_version": (protocol or {}).get("protocol_version") if isinstance(protocol, dict) else None,
        "claim_policy": "ranking and semantic claims are downgraded when strict gates fail",
    }
    report = sanitize_local_paths(report, cfg)
    out = cfg.repo_root / "paper/tables/artifact_reproducibility.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def _check(name: str, checks: list[dict[str, Any]], fn) -> Any:
    try:
        details = fn()
        passes = bool(details.get("passes", True)) if isinstance(details, dict) else True
        checks.append({"name": name, "passes": passes, "details": details})
        return details
    except Exception as exc:  # pragma: no cover - exercised through command path.
        checks.append({"name": name, "passes": False, "error": str(exc)})
        return None


def _gate(fn) -> dict[str, Any]:
    try:
        return fn()
    except Exception as exc:  # pragma: no cover - exercised through command path.
        return {"passes": False, "error": str(exc)}


def _required_tables(cfg: Config) -> dict[str, Any]:
    paths = [
        "paper/tables/evaluation_summary.json",
        "paper/tables/baseline_strict_comparison.json",
        "paper/tables/ablation_strict_comparison.json",
        "paper/tables/warning_volume_reduction.json",
        "paper/tables/ranking_pooled_evaluation.json",
        "paper/tables/ranking_score_audit.json",
        "paper/tables/semantic_drift_review_summary.json",
        "paper/tables/manual_review_quality.json",
        "paper/tables/case_study_summary.json",
        "paper/tables/strict_extractor_audit.json",
        "paper/tables/table_index.json",
    ]
    missing = [path for path in paths if not (cfg.repo_root / path).exists()]
    return {"passes": not missing, "missing": missing, "paths": paths}


def _oracle_blind_components(cfg: Config) -> dict[str, Any]:
    data = _json(cfg, "paper/tables/evaluation_summary.json")
    keys = (data.get("oracle_blind_primary_result") or {}).get("score_component_keys") or []
    assert_oracle_blind_components({key: 0.0 for key in keys}, context="artifact validator")
    return {"passes": True, "score_component_keys": keys}


def _pooled_review_coverage(cfg: Config) -> dict[str, Any]:
    data = _json(cfg, "paper/tables/ranking_pooled_evaluation.json")
    coverage = (data.get("label_coverage") or {}).get("coverage", 0.0)
    return {"passes": coverage >= 0.95, "coverage": coverage}


def _ranking_gate(cfg: Config) -> dict[str, Any]:
    data = _json(cfg, "paper/tables/ranking_pooled_evaluation.json")
    primary = next((row for row in data.get("rankers", []) if row.get("ranker") == "binddrift_oracle_blind"), {})
    best = data.get("best_simple_baseline") or {}
    comparison = data.get("comparison_against_best_simple_baseline") or {}
    random_comparison = data.get("comparison_against_random") or {}
    significance = (comparison.get("paired_bootstrap_significance") or {}).get("metrics") or {}
    deltas = comparison.get("deltas") or {}
    acceptance = (data.get("m6_acceptance") or {}).get("checks") or {}
    ablation_story = data.get("ablation_story") or {}
    top_fp_taxonomy = data.get("top_false_positive_taxonomy") or {}
    top_fn_taxonomy = data.get("top_false_negative_taxonomy") or {}
    audit = _json(cfg, "paper/tables/ranking_score_audit.json")
    manifest = validate_run_manifest(cfg)
    recomputed = build_ranker_evaluation(
        cfg,
        pool=Path(manifest["resolved_paths"]["pooled_review_set"]),
        labels=Path(manifest["resolved_paths"]["pooled_review_labels"]),
    )
    recompute_mismatches = _ranking_table_mismatches(data, recomputed)
    ranked = rank_primary_warnings_oracle_blind(read_warnings(Path(manifest["resolved_paths"]["promoted_warnings"])))
    top100_generated_binding_only = sum(1 for warning in ranked[:100] if generated_binding_only(warning))
    top100_oracle_only = sum(1 for warning in ranked[:100] if warning.get("oracle_only_promotion") is True)
    candidate_oracle_only = sum(1 for warning in ranked if warning.get("oracle_only_promotion") is True)
    top50_checks = audit.get("strict_top50_checks") or {}
    checks = {
        "candidate_count": (primary.get("candidate_count") or 0) >= 150,
        "candidate_count_matches_recomputed": primary.get("candidate_count") == len(ranked),
        "ranking_table_matches_recomputed": not recompute_mismatches,
        "m6_acceptance_minimum": _m6_acceptance_passes(data),
        "m6_no_oracle_leakage": acceptance.get("no_oracle_leakage") is True,
        "primary_candidates_exclude_pure_oracle_only": candidate_oracle_only == 0,
        "reported_top100_complete": (primary.get("review_pool_ranked_count") or 0) >= 100 and (primary.get("labeled_at_100") or 0) >= 100,
        "p_at_10": (primary.get("p_at_10") or 0.0) >= 0.50,
        "p_at_20": (primary.get("p_at_20") or 0.0) >= 0.45,
        "p_at_50": (primary.get("p_at_50") or 0.0) >= 0.42,
        "p_at_100": (primary.get("p_at_100") or 0.0) >= 0.40,
        "ndcg_at_20": (primary.get("ndcg_at_20") or 0.0) >= 0.55,
        "auprc_at_least_best_simple": (primary.get("auprc_on_pooled_review_set") or 0.0) >= (best.get("auprc_on_pooled_review_set") or 0.0),
        "p_at_20_lift": (deltas.get("p_at_20") or 0.0) >= 0.10,
        "p_at_50_lift": (deltas.get("p_at_50") or 0.0) >= 0.07,
        "ndcg_at_20_lift": (deltas.get("ndcg_at_20") or 0.0) >= 0.10,
        "bootstrap_ci_lower_bound_positive": all(
            ((significance.get(metric) or {}).get("bootstrap_delta_ci") or [0.0])[0] > 0.0
            for metric in ("p_at_20", "p_at_50", "ndcg_at_20")
        ),
        "significance_p_value": all(
            ((significance.get(metric) or {}).get("p_value_primary_not_better") or 1.0) < 0.05
            for metric in ("p_at_20", "p_at_50", "ndcg_at_20")
        ),
        "all_rankers_same_pool": data.get("all_rankers_same_pool") is True and acceptance.get("all_rankers_same_pool") is True,
        "primary_beats_best_simple_baseline": data.get("primary_beats_best_simple_baseline") is True
        and acceptance.get("primary_beats_best_simple_baseline") is True,
        "primary_beats_random": bool(random_comparison.get("passes_minimum_lift")),
        "random_baseline_sanity": acceptance.get("random_baseline_sanity") is True,
        "ablation_story": acceptance.get("ablation_story") is True and (ablation_story.get("supporting_ablation_count") or 0) >= 2,
        "top_false_positive_taxonomy": _taxonomy_schema_passes(top_fp_taxonomy),
        "top_false_negative_taxonomy": _taxonomy_schema_passes(top_fn_taxonomy),
        "no_self_evaluation_top100_only": data.get("no_self_evaluation_top100_only") is True
        and acceptance.get("no_self_evaluation_top100_only") is True,
        "top100_oracle_only": top100_oracle_only == 0,
        "top50_generated_binding_only": (top50_checks.get("generated_binding_only_warnings") or 0) == 0,
        "top100_generated_binding_only_limit": top100_generated_binding_only <= 10,
        "top50_score_explanations": (top50_checks.get("missing_score_explanations") or 0) == 0,
        "oracle_leakage": _oracle_blind_components(cfg).get("passes") is True,
    }
    return {
        "passes": all(checks.values()),
        "checks": checks,
        "metrics": {
            key: primary.get(key)
            for key in ("candidate_count", "review_pool_ranked_count", "p_at_10", "p_at_20", "p_at_50", "p_at_100", "ndcg_at_20", "auprc_on_pooled_review_set")
        },
        "comparison": comparison,
        "m6_acceptance": data.get("m6_acceptance") or {},
        "ablation_story": ablation_story,
        "top_false_positive_taxonomy": top_fp_taxonomy,
        "top_false_negative_taxonomy": top_fn_taxonomy,
        "ranking_table_recompute_mismatches": recompute_mismatches,
        "top100_generated_binding_only": top100_generated_binding_only,
        "top100_oracle_only": top100_oracle_only,
        "candidate_oracle_only": candidate_oracle_only,
        "claim": data.get("claim_recommendation"),
    }


def _ranking_table_mismatches(data: dict[str, Any], recomputed: dict[str, Any]) -> list[str]:
    keys = [
        "pool_sha256",
        "labels_sha256",
        "pool_size",
        "label_coverage",
        "rankers",
        "best_simple_baseline",
        "random_baseline",
        "comparison_against_best_simple_baseline",
        "comparison_against_random",
        "all_rankers_same_pool",
        "primary_beats_best_simple_baseline",
        "no_self_evaluation_top100_only",
        "top_false_positive_taxonomy",
        "top_false_negative_taxonomy",
        "ablation_story",
        "m6_acceptance",
        "coverage_acceptance",
        "claim_recommendation",
    ]
    return [key for key in keys if data.get(key) != recomputed.get(key)]


def _m6_acceptance_passes(data: dict[str, Any]) -> bool:
    m6 = data.get("m6_acceptance") or {}
    checks = m6.get("checks") or {}
    required = {
        "all_rankers_same_pool",
        "pool_label_coverage",
        "primary_beats_best_simple_baseline",
        "p_at_20_delta",
        "p_at_50_delta",
        "ndcg_at_20_delta",
        "bootstrap_ci_lower_bound",
        "p_value",
        "random_baseline_sanity",
        "ablation_story",
        "no_oracle_leakage",
        "no_self_evaluation_top100_only",
        "top_false_positive_taxonomy",
        "top_false_negative_taxonomy",
    }
    return bool(m6.get("minimum_passes") is True and all(checks.get(name) is True for name in required))


def _taxonomy_schema_passes(report: dict[str, Any]) -> bool:
    examples = report.get("examples") or []
    allowed = set(report.get("allowed_taxonomy") or [])
    taxonomy = report.get("taxonomy") or {}
    return bool(
        report.get("schema_version") == TAXONOMY_SCHEMA_VERSION
        and report.get("schema_valid") is True
        and taxonomy
        and report.get("count") == sum(taxonomy.values())
        and all(label in allowed for label in taxonomy)
        and all(example.get("warning_uid") and example.get("label") and example.get("taxonomy") in allowed for example in examples)
    )


def _semantic_gate(cfg: Config) -> dict[str, Any]:
    data = _json(cfg, "paper/tables/semantic_drift_review_summary.json")
    target_set = cfg.repo_root / str(data.get("target_set") or "data/replay/latest/semantic_target_review_set.jsonl")
    target_review = cfg.repo_root / str(data.get("target_review") or "data/replay/latest/semantic_target_review.csv")
    target_rows = read_warnings(target_set)
    review_rows = _csv_rows(target_review)
    labels = {row.get("warning_uid", ""): row.get("adjudicated_label", "").strip() for row in review_rows}
    target_uids = [str(row.get("warning_uid") or "") for row in target_rows]
    review_uids = [str(row.get("warning_uid") or "") for row in review_rows]
    reviewed = [row for row in target_rows if labels.get(str(row.get("warning_uid") or ""))]
    reviewed_labels = [labels[str(row.get("warning_uid") or "")] for row in reviewed]
    true_semantic = [
        row
        for row in target_rows
        if labels.get(str(row.get("warning_uid") or "")) == "TRUE_SEMANTIC_DRIFT"
    ]
    true_wrapper = [
        row
        for row in target_rows
        if labels.get(str(row.get("warning_uid") or "")) == "TRUE_WRAPPER_FIX"
    ]
    non_wrapper_semantic = [row for row in true_semantic if not _semantic_has_wrapper_oracle(row)]
    type_distribution = Counter(str(row.get("semantic_target_type") or row.get("type") or "") for row in target_rows)
    semantic_examples_by_type = Counter(str(row.get("semantic_target_type") or "") for row in true_semantic)
    unclear_count = sum(1 for label in reviewed_labels if label == "UNCLEAR")
    unclear_rate = round(unclear_count / len(reviewed_labels), 4) if reviewed_labels else 1.0
    recomputed = {
        "semantic_review_candidates": len(target_rows),
        "candidates_reviewed": len(reviewed),
        "reviewed_semantic_targets": len(reviewed),
        "true_semantic_drift_count": len(true_semantic),
        "true_wrapper_fix_count": len(true_wrapper),
        "non_wrapper_semantic_true_positives": len(non_wrapper_semantic),
        "semantic_drift_type_count": len(semantic_examples_by_type),
        "semantic_drift_types": sorted(semantic_examples_by_type),
        "unclear_count": unclear_count,
        "unclear_rate": unclear_rate,
        "type_distribution": dict(type_distribution),
        "examples_per_semantic_type": dict(semantic_examples_by_type),
    }
    summary_matches = {
        "semantic_review_candidates": data.get("semantic_review_candidates") == recomputed["semantic_review_candidates"],
        "candidates_reviewed": data.get("candidates_reviewed") == recomputed["candidates_reviewed"],
        "reviewed_semantic_targets": data.get("reviewed_semantic_targets") == recomputed["reviewed_semantic_targets"],
        "true_semantic_drift_count": data.get("true_semantic_drift_count") == recomputed["true_semantic_drift_count"],
        "true_wrapper_fix_count": data.get("true_wrapper_fix_count") == recomputed["true_wrapper_fix_count"],
        "non_wrapper_semantic_true_positives": data.get("non_wrapper_semantic_true_positives") == recomputed["non_wrapper_semantic_true_positives"],
        "semantic_drift_type_count": data.get("semantic_drift_type_count") == recomputed["semantic_drift_type_count"],
        "unclear_count": data.get("unclear_count") == recomputed["unclear_count"],
        "unclear_rate": data.get("unclear_rate") == recomputed["unclear_rate"],
    }
    per_type_quota = {
        category: type_distribution.get(category, 0) >= quota
        for category, quota in SEMANTIC_REVIEW_QUOTAS.items()
    }
    checks = {
        "target_set_exists": target_set.exists(),
        "target_review_exists": target_review.exists(),
        "target_review_matches_target_set": bool(target_rows) and target_uids == review_uids,
        "summary_matches_recomputed_counts": all(summary_matches.values()),
        "semantic_review_candidates": len(target_rows) >= 400,
        "semantic_review_candidate_type_quota": all(per_type_quota.values()),
        "reviewed_semantic_targets": len(reviewed) >= 200,
        "true_semantic_drift": len(true_semantic) >= 8,
        "non_wrapper_semantic_true_positives": len(non_wrapper_semantic) >= 5,
        "semantic_drift_types": len(semantic_examples_by_type) >= 3,
        "unclear_rate": unclear_rate <= 0.05,
        "examples_per_semantic_type": bool(semantic_examples_by_type) and all(count >= 2 for count in semantic_examples_by_type.values()),
        "wrapper_fix_only_not_counted_as_semantic": not any(labels.get(str(row.get("warning_uid") or "")) == "TRUE_WRAPPER_FIX" for row in true_semantic),
        "false_positive_taxonomy_generated": bool(data.get("false_positive_taxonomy")),
    }
    return {
        "passes": all(checks.values()),
        "checks": checks,
        "summary_matches": summary_matches,
        **recomputed,
        "per_type_quota": per_type_quota,
        "claim": data.get("claim_recommendation"),
    }


def _manual_review_quality_gate(cfg: Config) -> dict[str, Any]:
    data = _json(cfg, "paper/tables/manual_review_quality.json")
    acceptance = data.get("acceptance") or {}
    unclear_count = data.get("unclear_count") or 0
    reviewed_warnings = data.get("reviewed_warnings") or 0
    unclear_rate = data.get("unclear_rate")
    if unclear_rate is None:
        unclear_rate = round(unclear_count / reviewed_warnings, 4) if reviewed_warnings else 1.0
    pooled_manifest = _json(cfg, "data/replay/latest/pooled_review_manifest.json")
    ranker_coverage = pooled_manifest.get("ranker_top100_coverage") or {}
    ranker_coverage_passes = bool(ranker_coverage) and all((row.get("coverage") or 0.0) >= 0.95 for row in ranker_coverage.values())
    disagreement_examples = data.get("reviewer_disagreement_examples") or {}
    strict_checks = {
        "pooled_review_size": 450 <= reviewed_warnings <= 600,
        "label_coverage": (data.get("label_coverage") or 0.0) >= 1.0,
        "double_review_complete": bool(acceptance.get("double_review_complete")),
        "adjudication_complete": bool(acceptance.get("adjudication_complete") or acceptance.get("all_main_labels_adjudicated")),
        "blind_to_ranker": pooled_manifest.get("blind_to_ranker") is True,
        "cohen_kappa": (data.get("cohen_kappa") or 0.0) >= 0.60,
        "agreement_rate": (data.get("agreement_rate") or 0.0) >= 0.75,
        "adjudication_notes_missing": data.get("adjudication_notes_missing_rate") == 0.0,
        "unclear_rate": unclear_rate <= 0.05,
        "label_leakage_check": data.get("label_leakage_check") == "passed",
        "ranker_top100_coverage": ranker_coverage_passes,
        "reviewer_disagreement_examples": (disagreement_examples.get("examples") or 0) >= 10,
    }
    return {
        "passes": all(strict_checks.values()),
        "source_csv": data.get("source_csv"),
        "reviewed_warnings": reviewed_warnings,
        "label_coverage": data.get("label_coverage"),
        "cohen_kappa": data.get("cohen_kappa"),
        "agreement_rate": data.get("agreement_rate"),
        "unclear_rate": unclear_rate,
        "adjudication_notes_missing_rate": data.get("adjudication_notes_missing_rate"),
        "label_leakage_check": data.get("label_leakage_check"),
        "acceptance": acceptance,
        "strict_checks": strict_checks,
        "ranker_top100_coverage": ranker_coverage,
        "reviewer_disagreement_examples": disagreement_examples,
    }


def _binddrift_review_role_artifacts(cfg: Config) -> dict[str, Any]:
    review_dir = canonical_run_dir(cfg) / "review_artifacts"
    expected_files = {
        "evidence_collector": review_dir / "m3_final_evidence_packets.jsonl",
        "reviewer1": review_dir / "m3_final_reviewer1.jsonl",
        "reviewer2": review_dir / "m3_final_reviewer2.jsonl",
        "adjudicator": review_dir / "m3_final_adjudicator.jsonl",
        "merge_report": review_dir / "m3_final_merge_report.json",
        "role_summary": review_dir / "m3_final_role_summary.json",
    }
    missing = [repo_relative(cfg, path) for path in expected_files.values() if not path.exists()]
    if missing:
        return {"passes": False, "missing": missing}

    labels_path = canonical_run_dir(cfg) / "pooled_review_labels.csv"
    reviewed_warnings = _csv_row_count(labels_path)
    counts = {
        role: _jsonl_count(path)
        for role, path in expected_files.items()
        if path.suffix == ".jsonl"
    }
    count_matches = {role: count == reviewed_warnings for role, count in counts.items()}
    role_leakage = {
        role: _blind_review_leakage(path)
        for role, path in expected_files.items()
        if path.suffix == ".jsonl"
    }
    role_summary = _json(cfg, repo_relative(cfg, expected_files["role_summary"]))
    merge_report = _json(cfg, repo_relative(cfg, expected_files["merge_report"]))
    required_roles = {"evidence_collector", "reviewer1", "reviewer2", "adjudicator"}
    reported_roles = set(role_summary.get("binddrift_review_roles") or [])
    roles_are_blind = role_summary.get("blind_to_ranker") is True and all(not findings for findings in role_leakage.values())
    merge_complete = (
        merge_report.get("complete_rows") == reviewed_warnings
        and merge_report.get("double_labeled_rows") == reviewed_warnings
        and merge_report.get("adjudicated_rows") == reviewed_warnings
        and merge_report.get("validation_error_count") == 0
    )
    return {
        "passes": bool(
            reviewed_warnings
            and all(count_matches.values())
            and roles_are_blind
            and required_roles.issubset(reported_roles)
            and merge_complete
        ),
        "reviewed_warnings": reviewed_warnings,
        "counts": counts,
        "count_matches": count_matches,
        "blind_evidence_packets": not role_leakage.get("evidence_collector"),
        "blind_role_artifacts": roles_are_blind,
        "blind_review_leakage": {role: findings[:20] for role, findings in role_leakage.items() if findings},
        "reported_roles": sorted(reported_roles),
        "merge_complete": merge_complete,
        "merge_report": repo_relative(cfg, expected_files["merge_report"]),
        "role_summary": repo_relative(cfg, expected_files["role_summary"]),
    }


def _case_study_gate(cfg: Config) -> dict[str, Any]:
    data = _json(cfg, "paper/tables/case_study_summary.json")
    return {"passes": bool((data.get("acceptance") or {}).get("minimum_passes")), **data}


def _strict_extractor_gate(cfg: Config) -> dict[str, Any]:
    data = _json(cfg, "paper/tables/strict_extractor_audit.json")
    extractors = data.get("extractors") or {}
    acceptance = data.get("acceptance") or {}
    negative_samples = data.get("negative_samples") or {}
    cross_version_sampling = data.get("cross_version_sampling") or {}
    taxonomy = cfg.repo_root / "paper/analysis/extractor_error_taxonomy.md"
    taxonomy_text = taxonomy.read_text(encoding="utf-8") if taxonomy.exists() else ""
    required_precision = STRICT_TARGET_PRECISION
    precision_checks = {
        name: (extractors.get(name, {}).get("precision") or 0.0) >= minimum
        for name, minimum in required_precision.items()
    }
    sample_checks = {
        name: (extractors.get(name, {}).get("sampled") or 0) == STRICT_AUDIT_TARGETS.get(name, 0)
        for name in required_precision
    }
    checks = {
        "all_minimums_pass": data.get("all_minimums_pass") is True,
        "total_samples": (data.get("total_samples") or 0) >= 800,
        "promoted_warning_evidence_samples": (extractors.get("promoted_warning_evidence", {}).get("sampled") or 0) >= 150,
        "cohen_kappa": ((data.get("agreement") or {}).get("cohen_kappa") or 0.0) >= 0.80,
        "negative_samples": negative_samples.get("passes") is True and (negative_samples.get("total") or 0) >= len(required_precision),
        "cross_version_sampling": cross_version_sampling.get("passes") is True,
        "cross_version_pair_coverage": all(
            ((item or {}).get("pair_count") or 0) >= 10
            for item in (cross_version_sampling.get("extractors") or {}).values()
        ),
        "parser_limitations": _strict_parser_limitations_cover_extractors(data),
        "failure_taxonomy": taxonomy.exists()
        and "Parser Limitations" in taxonomy_text
        and "Negative Controls" in taxonomy_text
        and "Observed Incorrect Rows" in taxonomy_text,
        "review_provenance": _strict_review_provenance_passes(data),
        "target_precision": all(precision_checks.values()),
        "target_sample_sizes": all(sample_checks.values()),
        "acceptance_target_passes": all((acceptance.get(name) or {}).get("target_passes") is True for name in required_precision),
    }
    return {
        "passes": all(checks.values()),
        "checks": checks,
        "precision_checks": precision_checks,
        "sample_checks": sample_checks,
        "total_samples": data.get("total_samples"),
        "agreement": data.get("agreement"),
        "negative_samples": negative_samples,
        "cross_version_sampling": cross_version_sampling,
        "parser_limitations": data.get("parser_limitations"),
        "review_provenance": data.get("review_provenance"),
    }


def _strict_parser_limitations_cover_extractors(data: dict[str, Any]) -> bool:
    limitations = data.get("parser_limitations") or []
    by_extractor = {
        item.get("extractor_name")
        for item in limitations
        if item.get("extractor_name") and item.get("limitation")
    }
    return set(STRICT_AUDIT_TARGETS).issubset(by_extractor)


def _strict_review_provenance_passes(data: dict[str, Any]) -> bool:
    provenance = data.get("review_provenance") or {}
    return bool(
        provenance.get("requires_explicit_provenance") is True
        and provenance.get("generated_default_labels") == 0
        and provenance.get("pending_rows") == 0
        and provenance.get("review_labels_transferred") == data.get("total_samples")
    )


def _paper_claims(cfg: Config) -> dict[str, Any]:
    text = (cfg.repo_root / "paper/draft.md").read_text(encoding="utf-8").lower()
    forbidden = [
        "bug detector",
        "soundness proof",
        "complete detection",
        "ranking improves prioritization",
        "outperforms all baselines",
    ]
    found = [phrase for phrase in forbidden if phrase in text]
    required = [
        "warnings are review targets",
        "not every warning is a confirmed bug",
        "wrapper-fix oracle is auxiliary validation",
        "semantic drift result remains exploratory",
    ]
    missing = [phrase for phrase in required if phrase not in text]
    return {"passes": not found and not missing, "forbidden_found": found, "required_missing": missing}


def _no_local_paths(cfg: Config) -> dict[str, Any]:
    replay = canonical_run_dir(cfg)
    roots = [cfg.repo_root / "paper/tables", cfg.repo_root / "paper/cases", cfg.repo_root / "paper/analysis", replay]
    files = [
        cfg.data_dir / "audit/strict_extractor_sample.csv",
        cfg.data_dir / "audit/strict_extractor_review.csv",
        replay / "warnings.jsonl",
        replay / "promoted_warnings.jsonl",
        replay / "drift_facts.jsonl",
        replay / "pooled_review_set.jsonl",
        replay / "pooled_review_labels.csv",
        replay / "pooled_review_manifest.json",
        replay / "semantic_target_review_set.jsonl",
        replay / "semantic_target_review.csv",
        replay / "summary.json",
        replay / "run_manifest.json",
        replay / "evaluation_protocol.json",
    ]
    hits: list[str] = []
    for root in roots:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file() or path.suffix not in {".json", ".md", ".csv", ".jsonl"}:
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            if any(marker in text for marker in LOCAL_PATH_MARKERS):
                hits.append(repo_relative(cfg, path))
    for path in files:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if any(marker in text for marker in LOCAL_PATH_MARKERS):
            hits.append(repo_relative(cfg, path))
    return {"passes": not hits, "files_with_local_paths": sorted(set(hits))}


def _run_pytest(cfg: Config) -> dict[str, Any]:
    result = subprocess.run([sys.executable, "-m", "pytest"], cwd=cfg.repo_root, text=True, capture_output=True, check=False)
    return {"passes": result.returncode == 0, "returncode": result.returncode, "stdout_tail": result.stdout[-4000:], "stderr_tail": result.stderr[-4000:]}


def _csv_row_count(path: Path) -> int:
    with path.open(encoding="utf-8") as fh:
        return max(0, sum(1 for _line in fh) - 1)


def _csv_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as fh:
        return [{key: str(value or "") for key, value in row.items()} for row in csv.DictReader(fh)]


def _jsonl_count(path: Path) -> int:
    with path.open(encoding="utf-8") as fh:
        return sum(1 for line in fh if line.strip())


def _semantic_has_wrapper_oracle(warning: dict[str, Any]) -> bool:
    evidence = list(warning.get("evidence_chain") or []) + list((warning.get("rust_side") or {}).get("oracle_hits") or [])
    return any(isinstance(item, dict) and item.get("oracle_type") == "wrapper_fix" for item in evidence)


def _blind_review_leakage(path: Path) -> list[str]:
    forbidden_strings = ("score_breakdown", "wrapper_fix_hit=", "build_oracle_hit=")
    findings: list[str] = []
    with path.open(encoding="utf-8") as fh:
        for line_number, line in enumerate(fh, start=1):
            if not line.strip():
                continue
            row = json.loads(line)
            leaked = sorted(_blind_review_keys(row))
            leaked.extend(_blind_review_strings(row, forbidden_strings))
            if leaked:
                warning_id = row.get("warning_id") or row.get("warning_uid") or f"line:{line_number}"
                findings.append(f"{warning_id}: {','.join(leaked)}")
    return findings


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


def _blind_review_strings(value: Any, forbidden: tuple[str, ...]) -> list[str]:
    if isinstance(value, dict):
        found: list[str] = []
        for item in value.values():
            found.extend(_blind_review_strings(item, forbidden))
        return found
    if isinstance(value, list):
        found: list[str] = []
        for item in value:
            found.extend(_blind_review_strings(item, forbidden))
        return found
    if isinstance(value, str):
        return [token for token in forbidden if token in value]
    return []


def _json(cfg: Config, path: str) -> dict[str, Any]:
    return json.loads((cfg.repo_root / path).read_text(encoding="utf-8"))
