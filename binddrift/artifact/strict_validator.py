from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

from binddrift.artifact_paths import LOCAL_PATH_MARKERS, repo_relative, sanitize_local_paths
from binddrift.config import Config
from binddrift.detectors.semantic_review_targets import generate_semantic_review_targets
from binddrift.evaluation.protocol import assert_oracle_blind_components, load_evaluation_protocol
from binddrift.paper.audit import generate_strict_extractor_audit
from binddrift.paper.cases import generate_case_studies
from binddrift.paper.tables import generate_paper_tables
from binddrift.ranking.score_audit import generate_ranking_score_audit
from binddrift.run_manifest import canonical_run_dir, validate_run_manifest

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
    "m3": {"pooled_review_coverage", "manual_review_quality_gate"},
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
    outputs = {
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
    passes = bool(
        (primary.get("p_at_10") or 0.0) >= 0.50
        and (primary.get("p_at_20") or 0.0) >= 0.45
        and (primary.get("p_at_50") or 0.0) >= 0.42
        and (primary.get("p_at_100") or 0.0) >= 0.40
        and (primary.get("ndcg_at_20") or 0.0) >= 0.55
    )
    return {"passes": passes, "metrics": {key: primary.get(key) for key in ("p_at_10", "p_at_20", "p_at_50", "p_at_100", "ndcg_at_20")}, "claim": data.get("claim_recommendation")}


def _semantic_gate(cfg: Config) -> dict[str, Any]:
    data = _json(cfg, "paper/tables/semantic_drift_review_summary.json")
    acceptance = data.get("acceptance") or {}
    return {
        "passes": bool(acceptance.get("minimum_passes")),
        "true_semantic_drift_count": data.get("true_semantic_drift_count"),
        "non_wrapper_semantic_true_positives": data.get("non_wrapper_semantic_true_positives"),
        "semantic_drift_type_count": data.get("semantic_drift_type_count"),
        "claim": data.get("claim_recommendation"),
    }


def _manual_review_quality_gate(cfg: Config) -> dict[str, Any]:
    data = _json(cfg, "paper/tables/manual_review_quality.json")
    acceptance = data.get("acceptance") or {}
    return {
        "passes": bool(acceptance.get("minimum_passes")),
        "source_csv": data.get("source_csv"),
        "reviewed_warnings": data.get("reviewed_warnings"),
        "label_coverage": data.get("label_coverage"),
        "cohen_kappa": data.get("cohen_kappa"),
        "adjudication_notes_missing_rate": data.get("adjudication_notes_missing_rate"),
        "label_leakage_check": data.get("label_leakage_check"),
        "acceptance": acceptance,
    }


def _case_study_gate(cfg: Config) -> dict[str, Any]:
    data = _json(cfg, "paper/tables/case_study_summary.json")
    return {"passes": bool((data.get("acceptance") or {}).get("minimum_passes")), **data}


def _strict_extractor_gate(cfg: Config) -> dict[str, Any]:
    data = _json(cfg, "paper/tables/strict_extractor_audit.json")
    return {"passes": bool(data.get("all_minimums_pass")), "total_samples": data.get("total_samples"), "agreement": data.get("agreement")}


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


def _json(cfg: Config, path: str) -> dict[str, Any]:
    return json.loads((cfg.repo_root / path).read_text(encoding="utf-8"))
