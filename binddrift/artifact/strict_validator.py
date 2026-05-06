from __future__ import annotations

import csv
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Any

from binddrift.artifact_paths import LOCAL_PATH_MARKERS, repo_relative, sanitize_local_paths
from binddrift.config import Config
from binddrift.detectors.semantic_review_targets import SEMANTIC_REVIEW_QUOTAS, generate_semantic_review_targets
from binddrift.evaluation.evaluator import run_evaluation
from binddrift.evaluation.evaluate_rankers import TAXONOMY_SCHEMA_VERSION, build_ranker_evaluation, evaluate_rankers
from binddrift.evaluation.protocol import (
    EvaluationProtocolError,
    FORBIDDEN_PRIMARY_SCORE_COMPONENTS,
    assert_oracle_blind_components,
    load_evaluation_protocol,
)
from binddrift.paper.audit import STRICT_AUDIT_TARGETS, STRICT_TARGET_PRECISION, generate_strict_extractor_audit
from binddrift.paper.cases import generate_case_studies
from binddrift.paper.tables import (
    M4_FALSE_POSITIVE_TAXONOMY,
    M4_PRIMARY_METRICS,
    M5_MAX_UNCLEAR_RATE,
    M5_MIN_AGREEMENT_RATE,
    M5_MIN_COHEN_KAPPA,
    M5_MIN_DISAGREEMENT_EXAMPLES,
    M5_REVIEW_FORBIDDEN_STRINGS,
    generate_paper_tables,
)
from binddrift.ranking.oracle_blind_scorer import (
    PRIMARY_RANKER_DISPLAY_NAME,
    generated_binding_only,
    rank_primary_warnings_oracle_blind,
)
from binddrift.ranking.score_audit import generate_ranking_score_audit
from binddrift.run_manifest import canonical_run_dir, sha256_file, validate_run_manifest
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
    "m1": {"no_local_absolute_paths", "arm64_external_validity_gate"},
    "m2": {"ranking", "oracle_blind_narrative_gate"},
    "m3": {
        "pooled_review_coverage",
        "manual_review_quality_gate",
        "binddrift_review_role_artifacts",
        "m3_research_question_gate",
        "semantic",
        "strict_extractor_audit_gate",
    },
    "m4": {"semantic", "m4_false_positive_gate"},
    "m5": {"manual_review_quality_gate", "binddrift_review_role_artifacts"},
    "m6": {"case_study_gate"},
    "m7": {"strict_extractor_audit_gate"},
    "m8": {
        "ranking",
        "semantic",
        "manual_review_quality_gate",
        "case_study_gate",
        "strict_extractor_audit_gate",
        "m8_paper_submission_gate",
    },
    "final": {
        "ranking",
        "semantic",
        "manual_review_quality_gate",
        "case_study_gate",
        "strict_extractor_audit_gate",
        "m8_paper_submission_gate",
    },
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
        "evaluation": run_evaluation(cfg, top_k=int(manifest.get("paper_topk", 100)), run_id=str(manifest.get("run_id", "latest"))),
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
    _check("oracle_blind_narrative_gate", checks, lambda: _oracle_blind_narrative_gate(cfg))
    _check("pooled_review_coverage", checks, lambda: _pooled_review_coverage(cfg))
    _check("manual_review_quality_gate", checks, lambda: _manual_review_quality_gate(cfg))
    _check("binddrift_review_role_artifacts", checks, lambda: _binddrift_review_role_artifacts(cfg))
    _check("m3_research_question_gate", checks, lambda: _m3_research_question_gate(cfg))
    _check("m4_false_positive_gate", checks, lambda: _m4_false_positive_gate(cfg))
    _check("case_study_gate", checks, lambda: _case_study_gate(cfg))
    _check("strict_extractor_audit_gate", checks, lambda: _strict_extractor_gate(cfg))
    _check("paper_claims_match_downgrades", checks, lambda: _paper_claims(cfg))
    _check("m8_paper_submission_gate", checks, lambda: _m8_paper_submission_gate(cfg))
    _check("arm64_external_validity_gate", checks, lambda: _arm64_external_validity_gate(cfg))
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
        "paper/tables/false_positive_taxonomy.json",
        "paper/tables/case_study_summary.json",
        "paper/tables/strict_extractor_audit.json",
        "paper/tables/arm64_external_validity.json",
        "paper/tables/table_index.json",
    ]
    missing = [path for path in paths if not (cfg.repo_root / path).exists()]
    return {"passes": not missing, "missing": missing, "paths": paths}


def _oracle_blind_components(cfg: Config) -> dict[str, Any]:
    evaluation = _json(cfg, "paper/tables/evaluation_summary.json")
    ranking = _json(cfg, "paper/tables/ranking_pooled_evaluation.json")
    evaluation_primary = evaluation.get("oracle_blind_primary_result") or {}
    ranking_primary = next(
        (row for row in ranking.get("rankers", []) if row.get("ranker") == "binddrift_oracle_blind"),
        {},
    )
    score_keys = sorted(
        set(evaluation_primary.get("score_component_keys") or [])
        | set(ranking_primary.get("score_component_keys") or [])
    )
    forbidden_keys = sorted(
        set(evaluation_primary.get("forbidden_oracle_feature_keys") or [])
        | set(ranking_primary.get("forbidden_oracle_feature_keys") or [])
        | (FORBIDDEN_PRIMARY_SCORE_COMPONENTS & set(score_keys))
    )
    assert_oracle_blind_components({key: 0.0 for key in score_keys}, context="artifact validator")
    if forbidden_keys:
        raise EvaluationProtocolError("primary ranker exposes forbidden oracle feature keys: " + ", ".join(forbidden_keys))
    return {
        "passes": True,
        "ranker": evaluation_primary.get("ranker"),
        "score_component_keys": score_keys,
        "forbidden_oracle_feature_keys": forbidden_keys,
    }


def _oracle_blind_narrative_gate(cfg: Config) -> dict[str, Any]:
    draft_path = cfg.repo_root / "paper/draft.md"
    figure_path = cfg.repo_root / "paper/figures/ranking-dataflow.md"
    draft = draft_path.read_text(encoding="utf-8") if draft_path.exists() else ""
    figure = figure_path.read_text(encoding="utf-8") if figure_path.exists() else ""
    text = _normal_text(draft)
    figure_text = _normal_text(figure)
    component_gate = _gate(lambda: _oracle_blind_components(cfg))
    score_keys = component_gate.get("score_component_keys") or []
    forbidden_keys = component_gate.get("forbidden_oracle_feature_keys")
    display_name = PRIMARY_RANKER_DISPLAY_NAME.lower()
    draft_figure_edges = _mermaid_edges(_markdown_section(draft, "```mermaid", "```"))
    figure_edges = _mermaid_edges(figure)
    all_figure_edges = sorted(set(draft_figure_edges + figure_edges))
    forbidden_edges = _forbidden_oracle_blind_figure_edges(all_figure_edges)
    checks = {
        "primary_ranker_name_in_paper": display_name in text,
        "legacy_display_name_absent_from_paper": "oracleblindbinddrift" not in text,
        "internal_key_absent_from_paper": "binddrift_oracle_blind" not in text,
        "dataflow_figure_file_present": figure_path.exists(),
        "dataflow_figure_embedded_in_draft": "flowchart lr" in text
        and "detection-time features" in text
        and "primary oracle-blind ranking" in text
        and "auxiliary validation oracles" in text,
        "dataflow_figure_file_has_three_layers": all(
            phrase in figure_text
            for phrase in (
                "detection-time features",
                "primary oracle-blind ranking",
                "auxiliary validation oracles",
            )
        ),
        "dataflow_figure_has_evaluation_sink": "evaluation and validation" in text
        and "evaluation and validation" in figure_text,
        "dataflow_figure_has_no_oracle_to_primary_edges": not forbidden_edges,
        "current_scorer_difference_explained": "current scorer" in text
        and "may contain build/wrapper oracle components" in text,
        "build_oracle_auxiliary_only": (
            "build-breakage oracle is used only for labels and auxiliary validation" in text
            or "build-breakage oracle and wrapper-fix oracle are auxiliary validation only" in text
        ),
        "wrapper_oracle_auxiliary_only": "wrapper-fix oracle is auxiliary validation" in text,
        "no_primary_score_edge": "neither oracle has a data path into the" in text
        and "do not feed the primary score or top-k selection" in figure_text,
        "wrapper_fix_not_detection_or_promotion_evidence": "or wrapper-fix evidence" not in text
        and "wrapper-fix evidence is not used to promote warnings" in text,
        "score_component_keys_reported": bool(score_keys),
        "forbidden_oracle_feature_keys_empty": forbidden_keys == [],
    }
    return {
        "passes": all(checks.values()),
        "checks": checks,
        "figure": repo_relative(cfg, figure_path),
        "figure_edges": all_figure_edges,
        "forbidden_figure_edges": forbidden_edges,
        "primary_ranker_display_name": PRIMARY_RANKER_DISPLAY_NAME,
        "score_component_keys": score_keys,
        "forbidden_oracle_feature_keys": forbidden_keys,
    }


def _mermaid_edges(text: str) -> list[tuple[str, str]]:
    edges: list[tuple[str, str]] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if "-->" not in line and "-." not in line:
            continue
        if "-->" in line:
            left, right = line.split("-->", 1)
            source = _mermaid_node_id(left)
        else:
            left, right = line.split("-.", 1)
            source = _mermaid_node_id(left)
            if ".->" in right:
                _label, right = right.rsplit(".->", 1)
            elif ".-" in right:
                _label, right = right.rsplit(".-", 1)
        target = _mermaid_node_id(right)
        if source and target:
            edges.append((source, target))
    return edges


def _mermaid_node_id(text: str) -> str:
    match = re.search(r"\b([A-Za-z][A-Za-z0-9_]*)\b", text)
    return match.group(1) if match else ""


def _forbidden_oracle_blind_figure_edges(edges: list[tuple[str, str]]) -> list[str]:
    auxiliary_nodes = {"BO", "WO", "L"}
    primary_nodes = {"S", "K"}
    forbidden = []
    for source, target in edges:
        if source in auxiliary_nodes and target in primary_nodes:
            forbidden.append(f"{source}->{target}")
    return forbidden


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


def _m4_false_positive_gate(cfg: Config) -> dict[str, Any]:
    data = _json(cfg, "paper/tables/false_positive_taxonomy.json")
    ranking = _json(cfg, "paper/tables/ranking_pooled_evaluation.json")
    primary = next((row for row in ranking.get("rankers", []) if row.get("ranker") == "binddrift_oracle_blind"), {})
    comparison = ranking.get("comparison_against_best_simple_baseline") or {}
    deltas = comparison.get("deltas") or {}
    acceptance = data.get("acceptance") or {}
    taxonomy = data.get("taxonomy") or {}
    examples = data.get("examples_by_taxonomy") or {}
    manual_quality = _json(cfg, "paper/tables/manual_review_quality.json")
    label_distribution = manual_quality.get("label_distribution") or {}
    observed = {bucket for bucket, count in taxonomy.items() if count}
    draft = (cfg.repo_root / "paper/draft.md").read_text(encoding="utf-8").lower()
    threat_section = draft[draft.find("## 7. threats to validity") :] if "## 7. threats to validity" in draft else draft
    draft_text = re.sub(r"\s+", " ", draft)
    threat_text = re.sub(r"\s+", " ", threat_section)
    checks = {
        "taxonomy_table_exists": bool(data),
        "pooled_false_positive_count": data.get("false_positive_count") == label_distribution.get("FALSE_POSITIVE"),
        "taxonomy_schema": observed <= M4_FALSE_POSITIVE_TAXONOMY,
        "taxonomy_categories_covered": observed == M4_FALSE_POSITIVE_TAXONOMY,
        "taxonomy_examples": bool(observed) and all(examples.get(bucket) for bucket in observed),
        "p_at_10_stable_b_target": (primary.get("p_at_10") or 0.0) >= 0.90,
        "p_at_20_stable_b_target": (primary.get("p_at_20") or 0.0) >= 0.80,
        "p_at_50_stable_b_target": (primary.get("p_at_50") or 0.0) >= 0.70,
        "p_at_100_reported": primary.get("p_at_100") is not None,
        "ndcg_at_20_stable_b_target": (primary.get("ndcg_at_20") or 0.0) >= 0.90,
        "auprc_reported": primary.get("auprc_on_pooled_review_set") is not None,
        "best_baseline_delta_p_at_20_stable_b_target": (deltas.get("p_at_20") or 0.0) >= 0.30,
        "table_acceptance": acceptance.get("minimum_passes") is True,
        "primary_metrics_are_topk_or_ranking_metrics": sorted(
            metric for metric, value in (data.get("main_ranking_metrics") or {}).items() if value is not None
        )
        == sorted(M4_PRIMARY_METRICS),
        "draft_uses_topk_prioritization_story": "top-k review-prioritization" in draft_text or "top-k review prioritization" in draft_text,
        "draft_threats_admit_low_overall_warning_precision": "overall warning-set precision is low" in threat_text,
        "draft_threats_keep_prioritization_claim": "method targets prioritization" in threat_text,
        "draft_threats_admit_semantic_label_subjectivity": "semantic labels have unavoidable subjectivity" in threat_text,
        "draft_does_not_make_overall_precision_primary": "overall precision as a primary metric" not in draft_text,
    }
    return {
        "passes": all(checks.values()),
        "checks": checks,
        "metrics": {metric: primary.get(metric) for metric in M4_PRIMARY_METRICS},
        "best_baseline_deltas": deltas,
        "taxonomy": taxonomy,
        "observed_taxonomy": sorted(observed),
        "claim": data.get("claim_boundary"),
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
    return [
        key
        for key in keys
        if _stable_ranking_table_value(data, key) != _stable_ranking_table_value(recomputed, key)
    ]


def _stable_ranking_table_value(table: dict[str, Any], key: str) -> Any:
    value = table.get(key)
    if key != "rankers" or not isinstance(value, list):
        return value
    return [
        row
        for row in value
        if row.get("kind") in {"primary", "simple_baseline", "ablation"}
    ]


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
    review_protocol = data.get("review_protocol") or {}
    llm_boundary = review_protocol.get("llm_assisted_boundary") or {}
    strict_checks = {
        "pooled_review_size": 450 <= reviewed_warnings <= 600,
        "label_coverage": (data.get("label_coverage") or 0.0) >= 1.0,
        "double_review_complete": bool(acceptance.get("double_review_complete")),
        "adjudication_complete": bool(acceptance.get("adjudication_complete") or acceptance.get("all_main_labels_adjudicated")),
        "blind_to_ranker": pooled_manifest.get("blind_to_ranker") is True,
        "blind_to_rank_and_score": review_protocol.get("reviewers_blind_to_rank_and_score") is True,
        "reviewer_independence": review_protocol.get("reviewer_independence") is True,
        "reviewers_blind_to_each_other": review_protocol.get("reviewers_blind_to_each_other") is True,
        "cohen_kappa": (data.get("cohen_kappa") or 0.0) >= M5_MIN_COHEN_KAPPA,
        "agreement_rate": (data.get("agreement_rate") or 0.0) >= M5_MIN_AGREEMENT_RATE,
        "adjudication_notes_missing": data.get("adjudication_notes_missing_rate") == 0.0,
        "unclear_rate": unclear_rate <= M5_MAX_UNCLEAR_RATE,
        "label_leakage_check": data.get("label_leakage_check") == "passed",
        "review_process_notes": data.get("review_process_note_check") == "passed",
        "ranker_top100_coverage": ranker_coverage_passes,
        "reviewer_disagreement_examples": (disagreement_examples.get("examples") or 0) >= M5_MIN_DISAGREEMENT_EXAMPLES,
        "oracle_visibility_declared": review_protocol.get("reviewers_blind_to_oracles") is False
        and "auxiliary validation" in str(review_protocol.get("oracle_evidence_visibility") or ""),
        "llm_boundary_declared": llm_boundary.get("not_human_expert_manual_review") is True,
        "llm_not_in_primary_score": llm_boundary.get("llm_participates_in_primary_score") is False,
        "llm_not_given_adjudicated_labels": llm_boundary.get("reviewer_roles_receive_adjudicated_labels") is False,
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
        role: _blind_review_leakage(path, role=role)
        for role, path in expected_files.items()
        if path.suffix == ".jsonl"
    }
    role_summary = _json(cfg, repo_relative(cfg, expected_files["role_summary"]))
    merge_report = _json(cfg, repo_relative(cfg, expected_files["merge_report"]))
    required_roles = {"evidence_collector", "reviewer1", "reviewer2", "adjudicator"}
    reported_roles = set(role_summary.get("binddrift_review_roles") or [])
    role_summary_findings = _role_summary_process_findings(role_summary)
    roles_are_blind = role_summary.get("blind_to_ranker") is True and all(not findings for findings in role_leakage.values())
    roles_are_blind = roles_are_blind and role_summary.get("blind_to_rank_and_score") is True
    roles_are_blind = roles_are_blind and not role_summary_findings
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
        "role_summary_process_findings": role_summary_findings[:20],
        "reported_roles": sorted(reported_roles),
        "merge_complete": merge_complete,
        "merge_report": repo_relative(cfg, expected_files["merge_report"]),
        "role_summary": repo_relative(cfg, expected_files["role_summary"]),
    }


def _m3_research_question_gate(cfg: Config) -> dict[str, Any]:
    draft_path = cfg.repo_root / "paper/draft.md"
    draft = draft_path.read_text(encoding="utf-8") if draft_path.exists() else ""
    sections = _rq_sections(draft)
    normalized_sections = {rq: _normal_text(section) for rq, section in sections.items()}
    closure_markers = ("problem.", "method.", "data.", "result.", "interpretation.", "threat.")
    closed_loop = {
        rq: all(marker in normalized_sections.get(rq, "") for marker in closure_markers)
        for rq in ("rq1", "rq2", "rq3", "rq4", "rq5")
    }

    manifest = validate_run_manifest(cfg)
    strict_audit = _json(cfg, "paper/tables/strict_extractor_audit.json")
    strict_gate = _strict_extractor_gate(cfg)
    volume = _json(cfg, "paper/tables/warning_volume_reduction.json")
    ranking = _json(cfg, "paper/tables/ranking_pooled_evaluation.json")
    semantic = _json(cfg, "paper/tables/semantic_drift_review_summary.json")
    semantic_gate = _semantic_gate(cfg)
    primary = next((row for row in ranking.get("rankers", []) if row.get("ranker") == "binddrift_oracle_blind"), {})
    best = ranking.get("best_simple_baseline") or {}
    deltas = (ranking.get("comparison_against_best_simple_baseline") or {}).get("deltas") or {}
    top_k_workload = volume.get("top_k_workload") or {}
    expected_volume_reduction = _workload_reduction(manifest.get("drift_fact_count") or 0, manifest.get("promoted_warning_count") or 0)
    expected_top_k_workload = _expected_top_k_workload(
        manifest.get("drift_fact_count") or 0,
        manifest.get("promoted_warning_count") or 0,
    )
    table_index = _table_index_sha256_gate(cfg)
    readme = _normal_text((cfg.repo_root / "README.md").read_text(encoding="utf-8"))
    artifact_guide = _normal_text((cfg.repo_root / "docs/artifact-guide.md").read_text(encoding="utf-8"))
    one_command = "uv run python -m binddrift.artifact reproduce"
    paper_build = "uv run binddrift paper build --stage final"

    metric_keys = ("p_at_10", "p_at_20", "p_at_50", "p_at_100", "ndcg_at_20", "auprc_on_pooled_review_set")
    metric_better_than_best = {
        key: primary.get(key) is not None and best.get(key) is not None and primary.get(key) > best.get(key)
        for key in metric_keys
    }
    strict_acceptance = strict_audit.get("acceptance") or {}
    strict_overall = strict_acceptance.get("overall") or {}
    strict_extractor_checks = {
        name: (details or {}).get("minimum_passes") is True
        for name, details in strict_acceptance.items()
        if name != "overall"
    }
    rq2_topk_checks = {
        key: _workload_entry_matches(top_k_workload.get(key) or {}, expected)
        for key, expected in expected_top_k_workload.items()
    }
    rq2_text_checks = {
        key: f"{_fmt_percent(expected['share_of_drift_facts'])} of drift facts" in normalized_sections.get("rq2", "")
        and f"{_fmt_percent(expected['share_of_promoted_warnings'])} of promoted warnings" in normalized_sections.get("rq2", "")
        for key, expected in expected_top_k_workload.items()
    }
    semantic_recomputed = {
        "true_semantic_drift_count": semantic_gate.get("true_semantic_drift_count"),
        "semantic_drift_type_count": semantic_gate.get("semantic_drift_type_count"),
        "non_wrapper_semantic_true_positives": semantic_gate.get("non_wrapper_semantic_true_positives"),
    }
    semantic_summary_matches_gate = {
        key: semantic.get(key) == value
        for key, value in semantic_recomputed.items()
    }
    strict_gate_checks = strict_gate.get("checks") or {}
    strict_summary_matches_gate = {
        "total_samples": strict_audit.get("total_samples") == strict_gate.get("total_samples"),
        "cohen_kappa": (strict_audit.get("agreement") or {}).get("cohen_kappa")
        == (strict_gate.get("agreement") or {}).get("cohen_kappa"),
        "all_gate_checks": all(strict_gate_checks.values()),
    }
    rq_text_checks = {
        "rq1_reports_audit": f"{strict_audit.get('total_samples')} facts" in normalized_sections.get("rq1", "")
        and "all_minimums_pass = true" in normalized_sections.get("rq1", ""),
        "rq2_reports_volume": f"{_fmt_int(manifest.get('drift_fact_count'))} drift facts" in normalized_sections.get("rq2", "")
        and f"{_fmt_int(manifest.get('promoted_warning_count'))} promoted" in normalized_sections.get("rq2", "")
        and all(rq2_text_checks.values())
        and f"{_fmt_percent(expected_volume_reduction)} reduction" in normalized_sections.get("rq2", "")
        and "top-10" in normalized_sections.get("rq2", "")
        and "top-20" in normalized_sections.get("rq2", "")
        and "top-50" in normalized_sections.get("rq2", "")
        and "top-100" in normalized_sections.get("rq2", ""),
        "rq3_reports_metrics": all(
            phrase in normalized_sections.get("rq3", "")
            for phrase in (
                f"p@10 = {_fmt_metric(primary.get('p_at_10'))}",
                f"p@20 = {_fmt_metric(primary.get('p_at_20'))}",
                f"p@50 = {_fmt_metric(primary.get('p_at_50'))}",
                f"p@100 = {_fmt_metric(primary.get('p_at_100'))}",
                f"ndcg@20 = {_fmt_metric(primary.get('ndcg_at_20'))}",
                f"auprc = {_fmt_metric(primary.get('auprc_on_pooled_review_set'), digits=4)}",
                f"{_fmt_metric(deltas.get('p_at_20'))} p@20",
                f"{_fmt_metric(deltas.get('p_at_50'))} p@50",
                f"{_fmt_metric(deltas.get('ndcg_at_20'), digits=4)} ndcg@20",
            )
        ),
        "rq4_reports_semantic_gate": f"{semantic.get('true_semantic_drift_count')} `true_semantic_drift` rows"
        in normalized_sections.get("rq4", "")
        and f"{semantic.get('semantic_drift_type_count')} semantic drift types" in normalized_sections.get("rq4", "")
        and "semantic gate passes" in normalized_sections.get("rq4", ""),
        "rq5_reports_reproduction": one_command in normalized_sections.get("rq5", "")
        and paper_build in normalized_sections.get("rq5", "")
        and "sha256 provenance" in normalized_sections.get("rq5", ""),
    }
    checks = {
        "all_rq_sections_present": all(normalized_sections.get(rq) for rq in ("rq1", "rq2", "rq3", "rq4", "rq5")),
        "all_rq_sections_closed_loop": all(closed_loop.values()),
        "rq1_strict_extractor_minimum": (strict_audit.get("total_samples") or 0) >= 800
        and strict_audit.get("all_minimums_pass") is True
        and strict_overall.get("passes") is True
        and all(strict_extractor_checks.values())
        and strict_gate.get("passes") is True
        and all(strict_summary_matches_gate.values()),
        "rq2_workload_reduction_reported": volume.get("drift_fact_count") == manifest.get("drift_fact_count")
        and volume.get("promoted_warning_count") == manifest.get("promoted_warning_count")
        and volume.get("primary_warning_volume") == manifest.get("promoted_warning_count")
        and volume.get("drift_facts_to_promoted_warnings_reduction") == expected_volume_reduction
        and all(rq2_topk_checks.values()),
        "rq3_primary_beats_best_simple_baseline": ranking.get("primary_beats_best_simple_baseline") is True
        and all(metric_better_than_best.values()),
        "rq4_semantic_minimum": (semantic.get("true_semantic_drift_count") or 0) >= 8
        and (semantic.get("semantic_drift_type_count") or 0) >= 3
        and (semantic.get("acceptance") or {}).get("minimum_passes") is True
        and semantic_gate.get("passes") is True
        and all(semantic_summary_matches_gate.values())
        and "binddrift-review" in str(semantic.get("review_method") or ""),
        "rq5_reproducibility": one_command in readme
        and one_command in artifact_guide
        and paper_build in readme
        and paper_build in artifact_guide
        and table_index["passes"]
        and bool(manifest.get("sha256")),
        "rq_text_reports_acceptance_numbers": all(rq_text_checks.values()),
    }
    return {
        "passes": all(checks.values()),
        "checks": checks,
        "closed_loop": closed_loop,
        "rq_text_checks": rq_text_checks,
        "rq2_topk_checks": rq2_topk_checks,
        "rq2_text_checks": rq2_text_checks,
        "expected_top_k_workload": expected_top_k_workload,
        "metric_better_than_best": metric_better_than_best,
        "strict_extractor_checks": strict_extractor_checks,
        "strict_recomputed_gate": {
            "passes": strict_gate.get("passes"),
            "checks": strict_gate_checks,
            "total_samples": strict_gate.get("total_samples"),
            "agreement": strict_gate.get("agreement"),
        },
        "strict_summary_matches_gate": strict_summary_matches_gate,
        "semantic_recomputed_gate": {
            "passes": semantic_gate.get("passes"),
            "checks": semantic_gate.get("checks"),
            **semantic_recomputed,
        },
        "semantic_summary_matches_gate": semantic_summary_matches_gate,
        "table_index": table_index,
        "rq_metrics": {
            "strict_audit_total_samples": strict_audit.get("total_samples"),
            "drift_fact_count": volume.get("drift_fact_count"),
            "promoted_warning_count": volume.get("promoted_warning_count"),
            "primary_metrics": {key: primary.get(key) for key in metric_keys},
            "best_simple_metrics": {key: best.get(key) for key in metric_keys},
            "semantic_true_count": semantic.get("true_semantic_drift_count"),
            "semantic_drift_type_count": semantic.get("semantic_drift_type_count"),
        },
    }


def _expected_top_k_workload(drift_fact_count: Any, promoted_warning_count: Any) -> dict[str, dict[str, Any]]:
    drift_facts = int(drift_fact_count or 0)
    promoted = int(promoted_warning_count or 0)
    return {
        str(k): {
            "review_budget": min(k, promoted) if promoted else k,
            "share_of_drift_facts": _workload_share(drift_facts, k),
            "share_of_promoted_warnings": _workload_share(promoted, k),
            "reduction_from_drift_facts": _workload_reduction(drift_facts, k),
            "reduction_from_promoted_warnings": _workload_reduction(promoted, k),
        }
        for k in (10, 20, 50, 100)
    }


def _workload_entry_matches(actual: dict[str, Any], expected: dict[str, Any]) -> bool:
    return all(actual.get(key) == value for key, value in expected.items())


def _workload_share(denominator: Any, numerator: Any) -> float | None:
    denominator_int = int(denominator or 0)
    numerator_int = int(numerator or 0)
    if denominator_int <= 0:
        return None
    return round(min(numerator_int, denominator_int) / denominator_int, 4)


def _workload_reduction(original: Any, remaining: Any) -> float | None:
    original_int = int(original or 0)
    remaining_int = int(remaining or 0)
    if original_int <= 0:
        return None
    return round(1.0 - min(remaining_int, original_int) / original_int, 4)


def _fmt_percent(value: Any) -> str:
    return f"{float(value or 0.0) * 100:.2f}%"


def _rq_sections(draft: str) -> dict[str, str]:
    return {
        "rq1": _markdown_section(draft, "### RQ1:", "### RQ2:"),
        "rq2": _markdown_section(draft, "### RQ2:", "### RQ3:"),
        "rq3": _markdown_section(draft, "### RQ3:", "### RQ4:"),
        "rq4": _markdown_section(draft, "### RQ4:", "### RQ5:"),
        "rq5": _markdown_section(draft, "### RQ5:", "## 6. Case Studies"),
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


def _arm64_external_validity_gate(cfg: Config) -> dict[str, Any]:
    data = _json(cfg, "paper/tables/arm64_external_validity.json")
    acceptance = data.get("acceptance") or {}
    run_dir = _artifact_path(cfg, str(data.get("run_dir") or "data/replay/arm64"))
    versions = _json_file(run_dir / "versions.json").get("versions") or []
    pairs = _json_file(run_dir / "pairs.json").get("pairs") or []
    arm_warnings = read_warnings(run_dir / "promoted_warnings.jsonl")
    x86_warnings = read_warnings(canonical_run_dir(cfg) / "promoted_warnings.jsonl")
    raw = {
        "version_count": len(versions),
        "pair_count": len(pairs),
        "completed_pairs": sum(1 for pair in pairs if pair.get("status") == "completed"),
        "failed_pairs": sum(1 for pair in pairs if pair.get("status") != "completed"),
        "drift_fact_count": _jsonl_count(run_dir / "drift_facts.jsonl") if (run_dir / "drift_facts.jsonl").exists() else 0,
        "promoted_warning_count": len(arm_warnings),
    }
    arm_keys = {_warning_overlap_key(warning) for warning in arm_warnings}
    x86_keys = {_warning_overlap_key(warning) for warning in x86_warnings}
    arm_keys.discard("")
    x86_keys.discard("")
    raw_overlap = {
        "shared": len(arm_keys & x86_keys),
        "arm64_only": len(arm_keys - x86_keys),
        "x86_64_only": len(x86_keys - arm_keys),
    }
    raw_type_delta = _warning_type_delta(x86_warnings, arm_warnings)
    draft_text = _normal_text((cfg.repo_root / "paper/draft.md").read_text(encoding="utf-8"))
    discussion_checks = {
        "external_validity_section": "arm64 external-validity slice" in draft_text,
        "warning_overlap_discussed": "warning overlap" in draft_text,
        "failed_pairs_discussed": "failed pairs" in draft_text or "failed pair" in draft_text,
        "threats_discuss_arm64": "arm64" in draft_text and "external validity" in draft_text,
    }
    checks = {
        "run_present": acceptance.get("run_present") is True,
        "arch_is_arm64": acceptance.get("arch_is_arm64") is True,
        "version_count_minimum": acceptance.get("version_count_minimum") is True,
        "completed_pairs_minimum": acceptance.get("completed_pairs_minimum") is True,
        "failed_pair_recording": acceptance.get("failed_pair_recording") is True,
        "warning_overlap_analysis": acceptance.get("warning_overlap_analysis") is True,
        "warning_type_delta": acceptance.get("warning_type_delta") is True,
        "raw_version_count_matches_table": raw["version_count"] == data.get("version_count"),
        "raw_pair_count_matches_table": raw["pair_count"] == data.get("pair_count"),
        "raw_completed_pairs_matches_table": raw["completed_pairs"] == data.get("completed_pairs"),
        "raw_failed_pairs_matches_table": raw["failed_pairs"] == data.get("failed_pairs"),
        "raw_drift_fact_count_matches_table": raw["drift_fact_count"] == data.get("drift_fact_count"),
        "raw_promoted_warning_count_matches_table": raw["promoted_warning_count"] == data.get("promoted_warning_count"),
        "raw_warning_overlap_matches_table": raw_overlap == {
            key: (data.get("warning_overlap") or {}).get(key)
            for key in ("shared", "arm64_only", "x86_64_only")
        },
        "raw_warning_type_delta_matches_table": raw_type_delta == data.get("warning_type_delta"),
        **discussion_checks,
    }
    return {
        "passes": all(checks.values()),
        "checks": checks,
        "run_id": data.get("run_id"),
        "run_dir": data.get("run_dir"),
        "version_count": data.get("version_count"),
        "pair_count": data.get("pair_count"),
        "completed_pairs": data.get("completed_pairs"),
        "failed_pairs": data.get("failed_pairs"),
        "drift_fact_count": data.get("drift_fact_count"),
        "promoted_warning_count": data.get("promoted_warning_count"),
        "warning_overlap": data.get("warning_overlap"),
        "raw_counts": raw,
        "failure_taxonomy": data.get("failure_taxonomy"),
    }


def _artifact_path(cfg: Config, value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else cfg.repo_root / path


def _json_file(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _warning_overlap_key(warning: dict[str, Any]) -> str:
    c_side = warning.get("c_side") or {}
    symbol = str(c_side.get("symbol") or warning.get("symbol") or "").strip()
    warning_type = str(warning.get("type") or "").strip()
    return f"{warning_type}:{symbol}" if warning_type and symbol else ""


def _warning_type_delta(x86_warnings: list[dict[str, Any]], arm_warnings: list[dict[str, Any]]) -> list[dict[str, Any]]:
    x86_counts = Counter(str(warning.get("type") or "UNKNOWN") for warning in x86_warnings)
    arm_counts = Counter(str(warning.get("type") or "UNKNOWN") for warning in arm_warnings)
    return [
        {
            "type": warning_type,
            "x86_64": x86_counts.get(warning_type, 0),
            "arm64": arm_counts.get(warning_type, 0),
            "delta_arm64_minus_x86_64": arm_counts.get(warning_type, 0) - x86_counts.get(warning_type, 0),
        }
        for warning_type in sorted(set(x86_counts) | set(arm_counts))
    ]


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
    text = _normal_text((cfg.repo_root / "paper/draft.md").read_text(encoding="utf-8"))
    ranking = _json(cfg, "paper/tables/ranking_pooled_evaluation.json")
    semantic = _json(cfg, "paper/tables/semantic_drift_review_summary.json")
    ranking_passes = _m6_acceptance_passes(ranking) and ranking.get("primary_beats_best_simple_baseline") is True
    semantic_passes = (semantic.get("acceptance") or {}).get("minimum_passes") is True
    forbidden = [
        "bug detector",
        "soundness proof",
        "complete detection",
        "guaranteed stale abstraction",
        "proves rust abstraction unsoundness",
        "detects real bugs automatically",
        "ranking improves prioritization",
        "outperforms all baselines",
        "many semantic bugs",
    ]
    if ranking_passes:
        forbidden.extend(["ranking result is downgraded", "evidence gate is supported as the stronger claim"])
    else:
        forbidden.append("strict ranking gate passes")
    if semantic_passes:
        forbidden.append("semantic drift result remains exploratory")
    else:
        forbidden.append("semantic gate passes")
    found = [phrase for phrase in forbidden if phrase in text]
    required = [
        "binddrift prioritizes review targets for rust-for-linux cross-language api and contract drift",
        "warnings are review targets",
        "not every warning is a confirmed bug",
        "does not prove rust safe abstraction soundness",
        "does not automatically detect bugs",
        "tier 2 semantic findings are review targets",
        "`true_wrapper_fix` is not counted as `true_semantic_drift`",
        "wrapper-fix oracle is auxiliary validation",
    ]
    required.append("strict ranking gate passes" if ranking_passes else "evidence gate is supported as the stronger claim")
    required.append("semantic gate passes" if semantic_passes else "semantic drift result remains exploratory")
    missing = [phrase for phrase in required if phrase not in text]
    return {
        "passes": not found and not missing,
        "ranking_gate_passes": ranking_passes,
        "semantic_gate_passes": semantic_passes,
        "required_claim_phrases": required,
        "forbidden_claim_phrases": forbidden,
        "forbidden_found": found,
        "required_missing": missing,
    }


def _m8_paper_submission_gate(cfg: Config) -> dict[str, Any]:
    draft_path = cfg.repo_root / "paper/draft.md"
    readme_path = cfg.repo_root / "README.md"
    artifact_guide_path = cfg.repo_root / "docs/artifact-guide.md"
    draft = draft_path.read_text(encoding="utf-8")
    text = _normal_text(draft)
    abstract = _normal_text(_markdown_section(draft, "## Abstract", "## 1. Introduction"))
    readme = _normal_text(readme_path.read_text(encoding="utf-8"))
    artifact_guide = _normal_text(artifact_guide_path.read_text(encoding="utf-8"))

    expected = _m8_expected_paper_phrases(cfg)
    abstract_missing = [phrase for phrase in expected["abstract"] if phrase not in abstract]
    body_missing = [phrase for phrase in expected["body"] if phrase not in text]
    stale_found = [phrase for phrase in expected["stale"] if phrase in text]
    rq_missing = [phrase for phrase in expected["rqs"] if phrase not in text]
    threat_missing = [phrase for phrase in expected["threats"] if phrase not in text]
    forbidden_found = [phrase for phrase in expected["forbidden"] if phrase in text]
    table_index = _table_index_sha256_gate(cfg)
    red_team = _red_team_gate(cfg)

    one_command = "uv run python -m binddrift.artifact reproduce"
    paper_build = "uv run binddrift paper build --stage final"
    docs_checks = {
        "readme_reproduce_command": one_command in readme,
        "readme_paper_build_final": paper_build in readme,
        "artifact_guide_reproduce_command": one_command in artifact_guide,
        "artifact_guide_paper_build_final": paper_build in artifact_guide,
        "artifact_guide_mentions_main_tables": "main tables" in artifact_guide,
    }
    checks = {
        "abstract_numbers_from_tables": not abstract_missing,
        "body_numbers_from_tables": not body_missing,
        "no_stale_numbers": not stale_found,
        "research_questions_present": not rq_missing,
        "threats_to_validity_present": not threat_missing,
        "forbidden_claims_absent": not forbidden_found,
        "table_index_sha256_provenance": table_index["passes"],
        "artifact_guide_one_command": all(docs_checks.values()),
        "red_team_two_rounds_closed": red_team["passes"],
    }
    return {
        "passes": all(checks.values()),
        "checks": checks,
        "abstract_missing": abstract_missing,
        "body_missing": body_missing,
        "stale_found": stale_found,
        "rq_missing": rq_missing,
        "threat_missing": threat_missing,
        "forbidden_found": forbidden_found,
        "docs_checks": docs_checks,
        "table_index": table_index,
        "red_team": red_team,
    }


def _m8_expected_paper_phrases(cfg: Config) -> dict[str, list[str]]:
    manifest = validate_run_manifest(cfg)
    ranking = _json(cfg, "paper/tables/ranking_pooled_evaluation.json")
    manual = _json(cfg, "paper/tables/manual_review_quality.json")
    semantic = _json(cfg, "paper/tables/semantic_drift_review_summary.json")
    cases = _json(cfg, "paper/tables/case_study_summary.json")
    extractor = _json(cfg, "paper/tables/strict_extractor_audit.json")
    primary = next((row for row in ranking.get("rankers", []) if row.get("ranker") == "binddrift_oracle_blind"), {})
    best = ranking.get("best_simple_baseline") or {}
    deltas = (ranking.get("comparison_against_best_simple_baseline") or {}).get("deltas") or {}
    manual_true = (
        (manual.get("label_distribution") or {}).get("TRUE_BUILD_BREAKAGE", 0)
        + (manual.get("label_distribution") or {}).get("TRUE_WRAPPER_FIX", 0)
        + (manual.get("label_distribution") or {}).get("TRUE_SEMANTIC_DRIFT", 0)
    )
    return {
        "abstract": [
            f"{manifest['version_count']} linux snapshots",
            f"{manifest['pair_count']} adjacent version pairs",
            f"{_fmt_int(manifest['drift_fact_count'])} drift facts",
            f"{_fmt_int(manifest['promoted_warning_count'])} rust-impact warnings",
            f"{manual.get('reviewed_warnings')}-item pooled review set",
            f"p@10 = {_fmt_metric(primary.get('p_at_10'))}",
            f"p@20 = {_fmt_metric(primary.get('p_at_20'))}",
            f"p@50 = {_fmt_metric(primary.get('p_at_50'))}",
            f"p@100 = {_fmt_metric(primary.get('p_at_100'))}",
            f"ndcg@20 = {_fmt_metric(primary.get('ndcg_at_20'))}",
            f"p@20 by {_fmt_metric(deltas.get('p_at_20'))}",
            f"p@50 by {_fmt_metric(deltas.get('p_at_50'))}",
            f"ndcg@20 by {_fmt_metric(deltas.get('ndcg_at_20'), digits=4)}",
            f"{manual_true} adjudicated true-positive review targets",
            f"{manual.get('true_semantic_drift_count')} `true_semantic_drift`",
            f"{manual.get('true_wrapper_fix_count')} `true_wrapper_fix`",
        ],
        "body": [
            f"{manual.get('reviewed_warnings')} pooled warnings are double-labeled and adjudicated",
            f"cohen's kappa = {_fmt_metric(manual.get('cohen_kappa'), digits=4)}",
            f"agreement rate {_fmt_metric(manual.get('agreement_rate'), digits=3)}",
            f"{manual.get('true_build_breakage_count')} `true_build_breakage`",
            f"{manual.get('true_wrapper_fix_count')} `true_wrapper_fix`",
            f"{manual.get('true_semantic_drift_count')} `true_semantic_drift`",
            f"{(manual.get('label_distribution') or {}).get('false_positive'.upper(), 0)} `false_positive`",
            f"p@20 = {_fmt_metric(best.get('p_at_20'))}",
            f"p@50 = {_fmt_metric(best.get('p_at_50'))}",
            f"ndcg@20 = {_fmt_metric(best.get('ndcg_at_20'), digits=4)}",
            f"{_fmt_metric(deltas.get('p_at_20'))} p@20",
            f"{_fmt_metric(deltas.get('p_at_50'))} p@50",
            f"{_fmt_metric(deltas.get('ndcg_at_20'), digits=4)} ndcg@20",
            f"{semantic.get('semantic_review_candidates')} semantic target candidates",
            f"reviews {semantic.get('reviewed_semantic_targets')} adjudicated rows",
            f"{semantic.get('true_semantic_drift_count')} `true_semantic_drift` rows",
            f"{semantic.get('non_wrapper_semantic_true_positives')} non-wrapper semantic true positives",
            f"{semantic.get('semantic_drift_type_count')} semantic drift types",
            f"{cases.get('positive_case_studies')} positive warning-backed case studies",
            f"{cases.get('negative_case_studies')} negative/failure-analysis cases",
            f"{cases.get('semantic_true_cases')} semantic true cases",
            f"{cases.get('non_wrapper_semantic_cases')} non-wrapper semantic cases",
            f"{cases.get('wrapper_fix_backed_cases')} wrapper-fix-backed cases",
            f"{extractor.get('total_samples')} facts",
            f"{(extractor.get('extractors') or {}).get('promoted_warning_evidence', {}).get('sampled')} promoted warning evidence chains",
            f"cohen's kappa = {_fmt_metric(((extractor.get('agreement') or {}).get('cohen_kappa')), digits=1)}",
        ],
        "stale": [
            "17,867 drift facts",
            "331 rust-impact warnings",
            "37 adjudicated true-positive",
            "p@10 = 0.30",
            "p@20 = 0.20",
            "p@50 = 0.08",
            "p@100 = 0.04",
            "ndcg@20 = 0.1966",
            "semantic drift result remains exploratory",
        ],
        "rqs": [
            "rq1: can binddrift extract reliable cross-language drift facts?",
            "rq2: does evidence gating reduce review volume while preserving useful review targets?",
            "rq3: does `binddrift-oracle-blind` improve top-k review yield over strong baselines?",
            "rq4: what semantic drift patterns appear in adjudicated cases?",
            "rq5: how reproducible is the artifact across versioned toolchains?",
        ],
        "threats": [
            "parser incompleteness",
            "label ambiguity",
            "x86_64",
            "oracle limitations",
        ],
        "forbidden": [
            "bug detector",
            "soundness proof",
            "complete detection",
            "outperforms all baselines",
            "many semantic bugs",
            "detects real bugs automatically",
            "proves rust abstraction unsoundness",
        ],
    }


def _table_index_sha256_gate(cfg: Config) -> dict[str, Any]:
    path = cfg.repo_root / "paper/tables/table_index.json"
    if not path.exists():
        return {"passes": False, "missing_index": True}
    index = json.loads(path.read_text(encoding="utf-8"))
    missing_sha: list[str] = []
    mismatched_sha: list[str] = []
    unavailable: list[str] = []
    for name, entry in index.items():
        relpath = entry.get("path")
        table_path = cfg.repo_root / str(relpath or "")
        if not entry.get("available"):
            unavailable.append(name)
            continue
        if not relpath or not table_path.exists():
            unavailable.append(name)
            continue
        reported = entry.get("sha256")
        if not reported:
            missing_sha.append(name)
            continue
        actual = sha256_file(table_path)
        if reported != actual:
            mismatched_sha.append(name)
    return {
        "passes": not missing_sha and not mismatched_sha and not unavailable,
        "entries": len(index),
        "missing_sha256": missing_sha,
        "mismatched_sha256": mismatched_sha,
        "unavailable": unavailable,
    }


def _red_team_gate(cfg: Config) -> dict[str, Any]:
    path = cfg.repo_root / "paper/analysis/red_team_review.json"
    if not path.exists():
        return {"passes": False, "missing": repo_relative(cfg, path)}
    data = json.loads(path.read_text(encoding="utf-8"))
    rounds = data.get("rounds") or []
    issues = [issue for round_item in rounds for issue in (round_item.get("issues") or [])]
    open_issues = [
        issue.get("id", "")
        for issue in issues
        if issue.get("status") != "closed" or not issue.get("closure_evidence")
    ]
    checks = {
        "two_rounds": len(rounds) >= 2,
        "independent_reviewers": all(len(set(round_item.get("reviewers") or [])) >= 2 for round_item in rounds),
        "issues_present": bool(issues),
        "all_issues_closed": not open_issues,
        "claim_boundary_checked": data.get("claim_boundary_checked") is True,
        "table_provenance_checked": data.get("table_provenance_checked") is True,
        "artifact_quickstart_checked": data.get("artifact_quickstart_checked") is True,
    }
    return {
        "passes": all(checks.values()),
        "path": repo_relative(cfg, path),
        "checks": checks,
        "round_count": len(rounds),
        "issue_count": len(issues),
        "open_issues": open_issues,
    }


def _markdown_section(text: str, start: str, end: str) -> str:
    try:
        start_index = text.index(start)
    except ValueError:
        return ""
    try:
        end_index = text.index(end, start_index + len(start))
    except ValueError:
        end_index = len(text)
    return text[start_index:end_index]


def _normal_text(text: str) -> str:
    return " ".join(text.lower().split())


def _fmt_int(value: Any) -> str:
    return f"{int(value):,}"


def _fmt_metric(value: Any, *, digits: int = 2) -> str:
    return f"{float(value or 0.0):.{digits}f}"


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


def _blind_review_leakage(path: Path, *, role: str | None = None) -> list[str]:
    findings: list[str] = []
    with path.open(encoding="utf-8") as fh:
        for line_number, line in enumerate(fh, start=1):
            if not line.strip():
                continue
            row = json.loads(line)
            leaked = sorted(_blind_review_keys(row))
            leaked.extend(_blind_review_strings(row))
            if role:
                leaked.extend(_role_specific_review_leakage(role, row))
            if leaked:
                warning_id = row.get("warning_id") or row.get("warning_uid") or f"line:{line_number}"
                findings.append(f"{warning_id}: {','.join(leaked)}")
    return findings


def _role_summary_process_findings(role_summary: dict[str, Any]) -> list[str]:
    text = json.dumps(role_summary, sort_keys=True).lower()
    leaked = [token for token in M5_REVIEW_FORBIDDEN_STRINGS if token in text]
    return [f"role_summary:{token}" for token in leaked]


def _role_specific_review_leakage(role: str, value: Any) -> list[str]:
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


def _json(cfg: Config, path: str) -> dict[str, Any]:
    return json.loads((cfg.repo_root / path).read_text(encoding="utf-8"))
