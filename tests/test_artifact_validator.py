import json
import subprocess
import sys
from pathlib import Path

from binddrift.config import Config
from binddrift.artifact.strict_validator import validate_artifact


def test_artifact_validator_reports_m0_stage_ready() -> None:
    result = validate_artifact(Config.from_args(repo_root="."), strict_ccfb=True, stage="m0")

    assert result["passes"] is True
    assert result["status"] == "stage_ready"
    assert result["stage"] == "m0"
    assert result["ccfb_submission_ready"] is False
    assert isinstance(result["hard_gates"]["ranking"]["passes"], bool)
    assert isinstance(result["hard_gates"]["semantic"]["passes"], bool)
    assert isinstance(result["hard_gates"]["case_studies"]["passes"], bool)
    assert result["hard_gates"]["strict_extractor_audit"]["passes"] is True
    assert Path("paper/tables/artifact_reproducibility.json").exists()


def test_artifact_validator_reports_m2_ranking_ready() -> None:
    result = validate_artifact(Config.from_args(repo_root="."), strict_ccfb=True, stage="m2")

    assert result["passes"] is True
    assert result["stage"] == "m2"
    ranking = result["hard_gates"]["ranking"]
    assert ranking["passes"] is True
    assert all(ranking["checks"].values())


def test_artifact_validator_reports_m3_review_ready() -> None:
    result = validate_artifact(Config.from_args(repo_root="."), strict_ccfb=True, stage="m3")

    assert result["passes"] is True
    assert result["stage"] == "m3"
    role_check = next(check for check in result["checks"] if check["name"] == "binddrift_review_role_artifacts")
    assert role_check["passes"] is True
    assert role_check["details"]["blind_evidence_packets"] is True


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
    assert payload["status"] == "stage_ready"
    assert payload["stage"] == "m0"


def test_binddrift_module_propagates_cli_return_code() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "binddrift", "paper", "build", "--stage", "final"],
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 1
    payload = json.loads(result.stdout)
    assert payload["validation"]["passes"] is False
    assert payload["validation"]["stage"] == "final"
