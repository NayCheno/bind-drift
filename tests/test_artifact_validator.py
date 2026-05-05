import json
import subprocess
import sys
from pathlib import Path

from binddrift.config import Config
from binddrift.artifact.strict_validator import validate_artifact


def test_artifact_validator_reports_valid_with_downgrades() -> None:
    result = validate_artifact(Config.from_args(repo_root="."), strict_ccfb=True)

    assert result["passes"] is True
    assert result["status"] == "valid_with_downgrades"
    assert result["ccfb_submission_ready"] is False
    assert result["hard_gates"]["ranking"]["passes"] is False
    assert result["hard_gates"]["semantic"]["passes"] is False
    assert result["hard_gates"]["case_studies"]["passes"] is True
    assert result["hard_gates"]["strict_extractor_audit"]["passes"] is True
    assert Path("paper/tables/artifact_reproducibility.json").exists()


def test_artifact_validate_module_command() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "binddrift.artifact", "validate", "--strict-ccfb"],
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["passes"] is True
    assert payload["status"] == "valid_with_downgrades"
