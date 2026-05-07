import json
import subprocess
import sys
from pathlib import Path

from binddrift.config import Config
from binddrift.artifact.strict_validator import (
    _blind_review_leakage,
    _m0_claim_boundary_gate,
    _oracle_blind_narrative_gate,
    _table_index_sha256_gate,
    validate_artifact,
)


def test_artifact_validator_reports_m0_stage_ready() -> None:
    result = validate_artifact(Config.from_args(repo_root="."), strict_ccfb=True, stage="m0")

    assert result["passes"] is True
    assert result["status"] == ("ccfb_ready" if result["ccfb_submission_ready"] else "stage_ready")
    assert result["stage"] == "m0"
    assert isinstance(result["hard_gates"]["ranking"]["passes"], bool)
    assert isinstance(result["hard_gates"]["semantic"]["passes"], bool)
    assert isinstance(result["hard_gates"]["case_studies"]["passes"], bool)
    assert result["hard_gates"]["strict_extractor_audit"]["passes"] is True
    assert "m0_claim_boundary_gate" in result["stage_required_checks"]
    m0 = next(check for check in result["checks"] if check["name"] == "m0_claim_boundary_gate")
    assert m0["passes"] is True
    assert all(m0["details"]["checks"].values())
    assert Path("paper/tables/artifact_reproducibility.json").exists()


def test_artifact_validator_rejects_m0_readme_overclaim() -> None:
    readme = Path("README.md")
    original = readme.read_text(encoding="utf-8")
    try:
        readme.write_text(
            original + "\nBindDrift detects bugs.\n",
            encoding="utf-8",
        )

        result = _m0_claim_boundary_gate(Config.from_args(repo_root="."))

        assert result["passes"] is False
        assert "detects bugs" in result["doc_forbidden"]["README.md"]
        assert "detects bugs" in result["paper_facing_forbidden"]["README.md"]
    finally:
        readme.write_text(original, encoding="utf-8")


def test_artifact_validator_rejects_m0_body_overclaim() -> None:
    discussion = Path("paper-latex/sections/08-discussion.tex")
    original = discussion.read_text(encoding="utf-8")
    try:
        discussion.write_text(original + "\nBindDrift detects bugs.\n", encoding="utf-8")

        result = _m0_claim_boundary_gate(Config.from_args(repo_root="."))

        assert result["passes"] is False
        assert result["paper_facing_forbidden"]["paper-latex/sections/08-discussion.tex"] == ["detects bugs"]
    finally:
        discussion.write_text(original, encoding="utf-8")


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
        assert "L->K" in narrative["details"]["forbidden_figure_edges"]
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


def test_artifact_validator_rejects_m2_indirect_oracle_edges_into_primary_figure() -> None:
    figure = Path("paper/figures/ranking-dataflow.md")
    original = figure.read_text(encoding="utf-8")
    try:
        figure.write_text(original.replace("  C --> S\n", "  C --> S\n  BO --> C\n"), encoding="utf-8")

        narrative = _oracle_blind_narrative_gate(Config.from_args(repo_root="."))

        assert narrative["passes"] is False
        assert narrative["checks"]["dataflow_figure_has_no_oracle_to_primary_edges"] is False
        assert "BO->C->S" in narrative["forbidden_figure_edges"]
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


def test_blind_review_leakage_detects_ranker_source_strings(tmp_path: Path) -> None:
    packet = tmp_path / "packets.jsonl"
    packet.write_text(
        json.dumps(
            {
                "warning_id": "W-1",
                "binding_side": {
                    "summary": "fact_source=binding_diff; promotion_reasons=oracle_hit; ranker_sources=random"
                },
            }
        )
        + "\n",
        encoding="utf-8",
    )

    findings = _blind_review_leakage(packet)

    assert findings == ["W-1: ranker_sources="]


def test_blind_review_leakage_detects_score_component_strings(tmp_path: Path) -> None:
    packet = tmp_path / "packets.jsonl"
    packet.write_text(
        json.dumps(
            {
                "warning_id": "W-2",
                "binding_side": {
                    "summary": "promotion_reasons=oracle_hit; binding_only_penalty=-5.0, direct_rust_use=0.0, safe_api_exposure=0.0"
                },
            }
        )
        + "\n",
        encoding="utf-8",
    )

    findings = _blind_review_leakage(packet)

    assert findings == ["W-2: binding_only_penalty,direct_rust_use=,safe_api_exposure="]


def test_blind_review_leakage_detects_reviewer_cross_labels(tmp_path: Path) -> None:
    packet = tmp_path / "reviewer1.jsonl"
    packet.write_text(
        json.dumps(
            {
                "warning_id": "W-3",
                "reviewer1_label": "FALSE_POSITIVE",
                "reviewer2_label": "TRUE_SEMANTIC_DRIFT",
                "adjudicated_label": "TRUE_SEMANTIC_DRIFT",
            }
        )
        + "\n",
        encoding="utf-8",
    )

    findings = _blind_review_leakage(packet, role="reviewer1")

    assert findings == ["W-3: adjudicated_label,reviewer2_label"]


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
    m4_check = next(check for check in result["checks"] if check["name"] == "m4_false_positive_gate")
    assert m4_check["passes"] is True
    assert m4_check["details"]["checks"]["p_at_20_stable_b_target"] is True
    assert m4_check["details"]["checks"]["taxonomy_examples"] is True
    assert m4_check["details"]["checks"]["draft_threats_admit_semantic_label_subjectivity"] is True
    assert set(m4_check["details"]["observed_taxonomy"]) == {
        "binding_only_or_generated_surface",
        "weak_rust_reachability",
        "real_c_drift_no_rust_contract_impact",
        "macro_constant_over_prioritization",
        "layout_ambiguity",
    }


def test_artifact_validator_reports_m5_manual_review_ready() -> None:
    result = validate_artifact(Config.from_args(repo_root="."), strict_ccfb=True, stage="m5")

    assert result["passes"] is True
    assert result["stage"] == "m5"
    assert "manual_review_quality_gate" in result["stage_required_checks"]
    assert "binddrift_review_role_artifacts" in result["stage_required_checks"]
    assert "case_study_gate" not in result["stage_required_checks"]

    manual = result["hard_gates"]["manual_review_quality"]
    assert manual["passes"] is True
    assert manual["reviewed_warnings"] == 500
    assert manual["cohen_kappa"] >= 0.70
    assert manual["agreement_rate"] >= 0.80
    assert manual["unclear_rate"] <= 0.05
    assert manual["reviewer_disagreement_examples"]["examples"] >= 10
    assert all(manual["strict_checks"].values())


def test_artifact_validator_reports_m6_case_study_ready() -> None:
    result = validate_artifact(Config.from_args(repo_root="."), strict_ccfb=True, stage="m6")

    assert result["passes"] is True
    assert result["stage"] == "m6"
    assert "case_study_gate" in result["stage_required_checks"]
    case_gate = result["hard_gates"]["case_studies"]
    assert case_gate["passes"] is True
    assert case_gate["draft_main_case_count"] == 3
    assert case_gate["false_positive_negative_cases"] >= 1
    assert all(case_gate["checks"].values())


def test_artifact_validator_rejects_m6_when_body_case_is_missing() -> None:
    draft_path = Path("paper/draft.md")
    original = draft_path.read_text(encoding="utf-8")
    try:
        draft_path.write_text(original.replace("### Case 3:", "### Appendix Case 3:", 1), encoding="utf-8")

        result = validate_artifact(Config.from_args(repo_root="."), strict_ccfb=True, stage="m6")

        assert result["passes"] is False
        case_gate = result["hard_gates"]["case_studies"]
        assert case_gate["passes"] is False
        assert case_gate["checks"]["draft_main_case_studies_exactly_three"] is False
    finally:
        draft_path.write_text(original, encoding="utf-8")


def test_artifact_validator_rejects_m6_when_body_case_family_is_missing() -> None:
    draft_path = Path("paper/draft.md")
    original = draft_path.read_text(encoding="utf-8")
    try:
        modified = original.replace("### Case 2: Sleepability/Context Drift", "### Case 2: Nullability/Error Drift", 1)
        draft_path.write_text(modified, encoding="utf-8")

        result = validate_artifact(Config.from_args(repo_root="."), strict_ccfb=True, stage="m6")

        assert result["passes"] is False
        case_gate = result["hard_gates"]["case_studies"]
        assert case_gate["passes"] is False
        assert case_gate["checks"]["draft_main_case_families"] is False
    finally:
        draft_path.write_text(original, encoding="utf-8")


def test_artifact_validator_rejects_m6_positive_non_true_label() -> None:
    path = Path("paper/tables/case_study_summary.json")
    original = path.read_text(encoding="utf-8")
    try:
        payload = json.loads(original)
        payload["positive_label_distribution"]["UNCLEAR"] = 1
        payload["positive_label_distribution"]["TRUE_WRAPPER_FIX"] -= 1
        payload["acceptance"]["minimum_passes"] = True
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

        result = validate_artifact(Config.from_args(repo_root="."), strict_ccfb=True, stage="m6")

        assert result["passes"] is False
        case_gate = result["hard_gates"]["case_studies"]
        assert case_gate["passes"] is False
        assert case_gate["checks"]["artifact_positive_labels_all_true"] is False
    finally:
        path.write_text(original, encoding="utf-8")


def test_artifact_validator_rejects_m6_case_overclaim() -> None:
    draft_path = Path("paper/draft.md")
    original = draft_path.read_text(encoding="utf-8")
    try:
        draft_path.write_text(
            original.replace(
                "The main paper uses three representative case studies.",
                "The main paper uses three representative case studies. These are confirmed defects.",
                1,
            ),
            encoding="utf-8",
        )

        result = validate_artifact(Config.from_args(repo_root="."), strict_ccfb=True, stage="m6")

        assert result["passes"] is False
        case_gate = result["hard_gates"]["case_studies"]
        assert case_gate["passes"] is False
        assert case_gate["checks"]["draft_uses_review_target_boundary"] is False
        assert "confirmed defect" in case_gate["forbidden_case_claims_found"]
    finally:
        draft_path.write_text(original, encoding="utf-8")


def test_artifact_validator_rejects_m5_posthoc_role_summary() -> None:
    path = Path("data/replay/latest/review_artifacts/m3_final_role_summary.json")
    original = path.read_text(encoding="utf-8")
    try:
        payload = json.loads(original)
        payload["disagreement_selection_policy"] = (
            "40 conservative Reviewer 1 labels retained from independent v1 role output for disagreement coverage"
        )
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

        result = validate_artifact(Config.from_args(repo_root="."), strict_ccfb=True, stage="m5")

        assert result["passes"] is False
        role_check = next(check for check in result["checks"] if check["name"] == "binddrift_review_role_artifacts")
        assert role_check["passes"] is False
        assert role_check["details"]["role_summary_process_findings"]
    finally:
        path.write_text(original, encoding="utf-8")


def test_artifact_validator_m4_requires_semantic_label_subjectivity_threat() -> None:
    draft_path = Path("paper/draft.md")
    original = draft_path.read_text(encoding="utf-8")
    required_sentence = "Semantic labels have unavoidable subjectivity."
    try:
        assert required_sentence in original
        modified = original.replace(required_sentence, "Semantic labels are adjudicated through the review protocol.")
        modified = modified.replace(
            "Semantic labels have\nunavoidable subjectivity",
            "Semantic labels are adjudicated through the review protocol",
        )
        draft_path.write_text(modified, encoding="utf-8")

        result = validate_artifact(Config.from_args(repo_root="."), strict_ccfb=True, stage="m4")

        m4_check = next(check for check in result["checks"] if check["name"] == "m4_false_positive_gate")
        assert result["passes"] is False
        assert m4_check["passes"] is False
        assert m4_check["details"]["checks"]["draft_threats_admit_semantic_label_subjectivity"] is False
    finally:
        draft_path.write_text(original, encoding="utf-8")


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


def test_artifact_validator_reports_m7_latex_paper_ready() -> None:
    result = validate_artifact(Config.from_args(repo_root="."), strict_ccfb=True, stage="m7")

    assert result["passes"] is True
    assert result["ccfb_submission_ready"] is False
    assert result["status"] == "stage_ready"
    assert result["stage"] == "m7"
    assert "m7_latex_paper_gate" in result["stage_required_checks"]
    latex = next(check for check in result["checks"] if check["name"] == "m7_latex_paper_gate")
    assert latex["passes"] is True
    assert all(latex["details"]["checks"].values())
    assert latex["details"]["missing"] == []
    assert latex["details"]["missing_numbers"] == []
    assert latex["details"]["forbidden_found"] == []
    assert len(latex["details"]["sections"]) == 11
    assert len(latex["details"]["tables"]) == 5


def test_artifact_validator_rejects_m7_missing_latex_claim_boundary() -> None:
    abstract = Path("paper-latex/sections/00-abstract.tex")
    original = abstract.read_text(encoding="utf-8")
    try:
        abstract.write_text(original.replace("does not prove Rust abstraction soundness", "claims Rust abstraction soundness"), encoding="utf-8")

        result = validate_artifact(Config.from_args(repo_root="."), strict_ccfb=True, stage="m7")

        assert result["passes"] is False
        latex = next(check for check in result["checks"] if check["name"] == "m7_latex_paper_gate")
        assert latex["passes"] is False
        assert latex["details"]["checks"]["abstract_claim_boundary"] is False
    finally:
        abstract.write_text(original, encoding="utf-8")


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
