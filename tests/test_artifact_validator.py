import json
import subprocess
import sys
from pathlib import Path

from binddrift.config import Config
from binddrift.artifact.strict_validator import _table_index_sha256_gate, validate_artifact


def test_artifact_validator_reports_m0_stage_ready() -> None:
    result = validate_artifact(Config.from_args(repo_root="."), strict_ccfb=True, stage="m0")

    assert result["passes"] is True
    assert result["status"] == ("ccfb_ready" if result["ccfb_submission_ready"] else "stage_ready")
    assert result["stage"] == "m0"
    assert isinstance(result["hard_gates"]["ranking"]["passes"], bool)
    assert isinstance(result["hard_gates"]["semantic"]["passes"], bool)
    assert isinstance(result["hard_gates"]["case_studies"]["passes"], bool)
    assert result["hard_gates"]["strict_extractor_audit"]["passes"] is True
    assert Path("paper/tables/artifact_reproducibility.json").exists()


def test_artifact_validator_reports_m2_ranking_ready() -> None:
    result = validate_artifact(Config.from_args(repo_root="."), strict_ccfb=True, stage="m2")

    assert result["passes"] is True
    assert result["stage"] == "m2"
    assert "oracle_blind_narrative_gate" in result["stage_required_checks"]
    ranking = result["hard_gates"]["ranking"]
    assert ranking["passes"] is True
    assert all(ranking["checks"].values())
    narrative = next(check for check in result["checks"] if check["name"] == "oracle_blind_narrative_gate")
    assert narrative["passes"] is True
    assert narrative["details"]["primary_ranker_display_name"] == "BindDrift-oracle-blind"
    assert narrative["details"]["forbidden_oracle_feature_keys"] == []
    assert all(narrative["details"]["checks"].values())


def test_artifact_validator_rejects_m2_forbidden_oracle_feature_keys() -> None:
    path = Path("paper/tables/evaluation_summary.json")
    original = path.read_text(encoding="utf-8")
    try:
        payload = json.loads(original)
        primary = payload["oracle_blind_primary_result"]
        primary["score_component_keys"] = list(primary.get("score_component_keys") or []) + ["wrapper_fix_hit"]
        primary["forbidden_oracle_feature_keys"] = ["wrapper_fix_hit"]
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

        result = validate_artifact(Config.from_args(repo_root="."), strict_ccfb=True, stage="m2")

        assert result["passes"] is False
        component = next(check for check in result["checks"] if check["name"] == "oracle_blind_primary_has_no_forbidden_components")
        assert component["passes"] is False
        assert "wrapper_fix_hit" in component["error"]
    finally:
        path.write_text(original, encoding="utf-8")


def test_artifact_validator_rejects_m2_oracle_edges_into_primary_figure() -> None:
    figure = Path("paper/figures/ranking-dataflow.md")
    original = figure.read_text(encoding="utf-8")
    try:
        figure.write_text(original.replace("  L --> M\n", "  L --> K\n"), encoding="utf-8")

        result = validate_artifact(Config.from_args(repo_root="."), strict_ccfb=True, stage="m2")

        assert result["passes"] is False
        narrative = next(check for check in result["checks"] if check["name"] == "oracle_blind_narrative_gate")
        assert narrative["passes"] is False
        assert narrative["details"]["checks"]["dataflow_figure_has_no_oracle_to_primary_edges"] is False
        assert narrative["details"]["forbidden_figure_edges"] == ["L->K"]
    finally:
        figure.write_text(original, encoding="utf-8")


def test_artifact_validator_rejects_m2_dashed_oracle_edges_into_primary_figure() -> None:
    figure = Path("paper/figures/ranking-dataflow.md")
    original = figure.read_text(encoding="utf-8")
    try:
        figure.write_text(original.replace("  BO --> L\n", '  BO -. "validation only" .-> S\n'), encoding="utf-8")

        result = validate_artifact(Config.from_args(repo_root="."), strict_ccfb=True, stage="m2")

        assert result["passes"] is False
        narrative = next(check for check in result["checks"] if check["name"] == "oracle_blind_narrative_gate")
        assert narrative["passes"] is False
        assert narrative["details"]["checks"]["dataflow_figure_has_no_oracle_to_primary_edges"] is False
        assert narrative["details"]["forbidden_figure_edges"] == ["BO->S"]
    finally:
        figure.write_text(original, encoding="utf-8")


def test_artifact_validator_reports_m1_external_validity_ready() -> None:
    result = validate_artifact(Config.from_args(repo_root="."), strict_ccfb=True, stage="m1")

    assert result["passes"] is True
    assert result["stage"] == "m1"
    external = next(check for check in result["checks"] if check["name"] == "arm64_external_validity_gate")
    assert external["passes"] is True
    assert external["details"]["version_count"] >= 8
    assert external["details"]["completed_pairs"] >= 7
    assert external["details"]["failed_pairs"] == 0
    assert all(external["details"]["checks"].values())


def test_artifact_validator_reports_m3_review_ready() -> None:
    result = validate_artifact(Config.from_args(repo_root="."), strict_ccfb=True, stage="m3")

    assert result["passes"] is True
    assert result["stage"] == "m3"
    role_check = next(check for check in result["checks"] if check["name"] == "binddrift_review_role_artifacts")
    assert role_check["passes"] is True
    assert role_check["details"]["blind_evidence_packets"] is True
    rq_check = next(check for check in result["checks"] if check["name"] == "m3_research_question_gate")
    assert rq_check["passes"] is True
    assert all(rq_check["details"]["checks"].values())
    assert all(rq_check["details"]["closed_loop"].values())
    assert rq_check["details"]["rq_metrics"]["strict_audit_total_samples"] >= 800
    assert rq_check["details"]["rq_metrics"]["semantic_true_count"] >= 8


def test_artifact_validator_rejects_m3_unclosed_rq_section() -> None:
    draft = Path("paper/draft.md")
    original = draft.read_text(encoding="utf-8")
    try:
        draft.write_text(original.replace("Problem. The raw drift stream", "Issue. The raw drift stream", 1), encoding="utf-8")

        result = validate_artifact(Config.from_args(repo_root="."), strict_ccfb=True, stage="m3")

        assert result["passes"] is False
        rq_check = next(check for check in result["checks"] if check["name"] == "m3_research_question_gate")
        assert rq_check["passes"] is False
        assert rq_check["details"]["closed_loop"]["rq2"] is False
    finally:
        draft.write_text(original, encoding="utf-8")


def test_artifact_validator_rejects_m3_stale_rq1_precision_summary() -> None:
    path = Path("paper/tables/strict_extractor_audit.json")
    original = path.read_text(encoding="utf-8")
    try:
        payload = json.loads(original)
        payload["extractors"]["c_functions"]["precision"] = 0.0
        payload["acceptance"]["c_functions"]["minimum_passes"] = True
        payload["acceptance"]["overall"]["passes"] = True
        payload["all_minimums_pass"] = True
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

        result = validate_artifact(Config.from_args(repo_root="."), strict_ccfb=True, stage="m3")

        assert result["passes"] is False
        assert result["hard_gates"]["strict_extractor_audit"]["passes"] is False
        rq_check = next(check for check in result["checks"] if check["name"] == "m3_research_question_gate")
        assert rq_check["passes"] is False
        assert rq_check["details"]["checks"]["rq1_strict_extractor_minimum"] is False
    finally:
        path.write_text(original, encoding="utf-8")


def test_artifact_validator_rejects_m3_stale_rq2_workload_numbers() -> None:
    path = Path("paper/tables/warning_volume_reduction.json")
    original = path.read_text(encoding="utf-8")
    try:
        payload = json.loads(original)
        payload["top_k_workload"]["20"]["share_of_drift_facts"] = 0.9999
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

        result = validate_artifact(Config.from_args(repo_root="."), strict_ccfb=True, stage="m3")

        assert result["passes"] is False
        rq_check = next(check for check in result["checks"] if check["name"] == "m3_research_question_gate")
        assert rq_check["passes"] is False
        assert rq_check["details"]["rq2_topk_checks"]["20"] is False
    finally:
        path.write_text(original, encoding="utf-8")


def test_artifact_validator_rejects_m3_stale_rq4_semantic_summary() -> None:
    path = Path("paper/tables/semantic_drift_review_summary.json")
    original = path.read_text(encoding="utf-8")
    try:
        payload = json.loads(original)
        payload["true_semantic_drift_count"] = 999
        payload["acceptance"]["minimum_passes"] = True
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

        result = validate_artifact(Config.from_args(repo_root="."), strict_ccfb=True, stage="m3")

        assert result["passes"] is False
        assert result["hard_gates"]["semantic"]["passes"] is False
        rq_check = next(check for check in result["checks"] if check["name"] == "m3_research_question_gate")
        assert rq_check["passes"] is False
        assert rq_check["details"]["checks"]["rq4_semantic_minimum"] is False
    finally:
        path.write_text(original, encoding="utf-8")


def test_artifact_validator_reports_m4_semantic_ready() -> None:
    result = validate_artifact(Config.from_args(repo_root="."), strict_ccfb=True, stage="m4")

    assert result["passes"] is True
    assert result["stage"] == "m4"
    semantic = result["hard_gates"]["semantic"]
    assert semantic["passes"] is True
    assert semantic["true_semantic_drift_count"] >= 8
    assert semantic["non_wrapper_semantic_true_positives"] >= 5
    assert semantic["semantic_drift_type_count"] >= 3


def test_artifact_validator_recomputes_m4_semantic_counts() -> None:
    summary_path = Path("paper/tables/semantic_drift_review_summary.json")
    original = summary_path.read_text(encoding="utf-8")
    try:
        payload = json.loads(original)
        payload["semantic_review_candidates"] = 999
        payload["acceptance"]["minimum_passes"] = True
        summary_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

        result = validate_artifact(Config.from_args(repo_root="."), strict_ccfb=True, stage="m4")

        semantic = result["hard_gates"]["semantic"]
        assert result["passes"] is False
        assert semantic["passes"] is False
        assert semantic["checks"]["summary_matches_recomputed_counts"] is False
        assert semantic["summary_matches"]["semantic_review_candidates"] is False
    finally:
        summary_path.write_text(original, encoding="utf-8")


def test_artifact_validate_module_command_accepts_stage() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "binddrift.artifact", "validate", "--strict-ccfb", "--stage", "m0"],
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["passes"] is True
    assert payload["status"] == ("ccfb_ready" if payload["ccfb_submission_ready"] else "stage_ready")
    assert payload["stage"] == "m0"


def test_artifact_validator_reports_m7_extractor_audit_ready() -> None:
    result = validate_artifact(Config.from_args(repo_root="."), strict_ccfb=True, stage="m7")

    assert result["passes"] is True
    assert result["stage"] == "m7"
    audit = result["hard_gates"]["strict_extractor_audit"]
    assert audit["passes"] is True
    assert all(audit["checks"].values())
    assert audit["negative_samples"]["passes"] is True
    assert audit["cross_version_sampling"]["passes"] is True
    assert audit["review_provenance"]["pending_rows"] == 0
    assert audit["review_provenance"]["generated_default_labels"] == 0


def test_artifact_validator_reports_m8_paper_submission_ready() -> None:
    result = validate_artifact(Config.from_args(repo_root="."), strict_ccfb=True, stage="m8")

    assert result["passes"] is True
    assert result["stage"] == "m8"
    m8 = next(check for check in result["checks"] if check["name"] == "m8_paper_submission_gate")
    assert m8["passes"] is True
    assert all(m8["details"]["checks"].values())
    assert m8["details"]["red_team"]["round_count"] >= 2
    assert m8["details"]["table_index"]["missing_sha256"] == []


def test_m8_table_index_gate_rejects_stale_sha256() -> None:
    path = Path("paper/tables/table_index.json")
    original = path.read_text(encoding="utf-8")
    try:
        payload = json.loads(original)
        first_name = next(iter(payload))
        payload[first_name]["sha256"] = "0" * 64
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

        result = _table_index_sha256_gate(Config.from_args(repo_root="."))

        assert result["passes"] is False
        assert first_name in result["mismatched_sha256"]
    finally:
        path.write_text(original, encoding="utf-8")


def test_binddrift_module_propagates_cli_return_code() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "binddrift", "paper", "build", "--stage", "final"],
        text=True,
        capture_output=True,
        check=False,
    )

    payload = json.loads(result.stdout)
    assert result.returncode == (0 if payload["validation"]["passes"] else 1)
    assert payload["validation"]["stage"] == "final"
