from pathlib import Path
import json

from binddrift.config import Config
from binddrift.db import connect, initialize, upsert_many
from binddrift.paper.cases import generate_case_studies
from binddrift.warnings import write_warnings


def test_case_studies_only_use_true_labels_with_strong_evidence(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    warnings = [
            {
                "warning_id": "W-000001",
                "run_id": "latest",
                "pair_id": "latest-p001",
                "old_version": "old",
                "new_version": "new",
                "type": "NullabilityDrift",
                "promotion_status": "promoted",
                "risk": "High",
            "score": 12.0,
            "c_evidence_level": "c_behavior_indicator",
            "c_side": {
                "symbol": "foo_get",
                "old_indicators": ["NULL_RETURN"],
                "new_indicators": ["ERR_PTR_RETURN"],
                "old_version": "old",
                "new_version": "new",
                "evidence": [{"evidence_file": "foo.c", "evidence_line": 1, "evidence_text": "return ERR_PTR(-ENOMEM);"}],
            },
            "rust_side": {
                "uses": [{"rust_file": "device.rs", "line": 10, "enclosing_function": "Device::get"}],
                "error_mappings": [{"rust_file": "device.rs", "line": 11, "mapping_type": "ERR_PTR_MAPPING"}],
            },
        },
        {
            "warning_id": "W-000002",
            "type": "SignatureDrift",
            "risk": "Medium",
            "score": 8.0,
            "c_side": {"symbol": "false_positive", "old": "present", "new": "removed"},
            "rust_side": {"uses": [{"rust_file": "device.rs", "line": 20, "enclosing_function": "Device::false_positive"}]},
        },
        {
            "warning_id": "W-000003",
            "type": "HelperDrift",
            "risk": "Medium",
            "score": 8.0,
            "c_side": {"symbol": "missing_rust", "old": ["NULL_RETURN"], "new": ["ERR_PTR_RETURN"]},
            "rust_side": {},
        },
        {
            "warning_id": "W-000004",
            "type": "NullabilityDrift",
            "risk": "High",
            "score": 12.0,
            "c_evidence_level": "c_behavior_indicator",
            "c_side": {"symbol": "legacy_label", "old_indicators": ["NULL_RETURN"], "new_indicators": ["ERR_PTR_RETURN"]},
            "rust_side": {
                "uses": [{"rust_file": "device.rs", "line": 30, "enclosing_function": "Device::legacy"}],
                "error_mappings": [{"rust_file": "device.rs", "line": 31, "mapping_type": "ERR_PTR_MAPPING"}],
            },
        },
        {
            "warning_id": "W-000005",
            "type": "SignatureDrift",
            "risk": "High",
            "score": 12.0,
            "c_side": {"symbol": "binding_only", "old": "present", "new": "removed"},
            "rust_side": {"uses": [{"rust_file": "device.rs", "line": 40, "enclosing_function": "Device::binding_only"}]},
        },
    ]
    write_warnings(cfg, warnings)
    review = cfg.data_dir / "manual_review.csv"
    review.write_text(
        "warning_id,reviewer1_label,reviewer2_label,adjudicated_label,label\n"
        "W-000001,,,TRUE_SEMANTIC_DRIFT,\n"
        "W-000002,,,FALSE_POSITIVE,\n"
        "W-000003,,,TRUE_WRAPPER_FIX,\n"
        "W-000004,,,,TRUE_SEMANTIC_DRIFT\n"
        "W-000005,,,TRUE_SEMANTIC_DRIFT,\n",
        encoding="utf-8",
    )
    stale = tmp_path / "paper/cases/case-99-stale.md"
    stale.parent.mkdir(parents=True, exist_ok=True)
    stale.write_text("Oracle label: `UNLABELED`\n", encoding="utf-8")

    result = generate_case_studies(cfg)
    files = [Path(path) for path in result["files"]]

    assert result["cases"] == 1
    assert not stale.exists()
    assert files[0].name.startswith("case-01-nullabilitydrift-foo_get")
    text = files[0].read_text(encoding="utf-8")
    assert "Oracle label: `TRUE_SEMANTIC_DRIFT`" in text
    assert "adjudicated true-positive contract evidence" in text
    assert "ERR_PTR_MAPPING" in text


def test_case_studies_use_replay_adjacent_review_and_structured_diff(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    run_dir = tmp_path / "data/replay/latest"
    run_dir.mkdir(parents=True)
    warning = {
        "warning_id": "W-000010",
        "run_id": "latest",
        "pair_id": "latest-p001",
        "old_version": "old",
        "new_version": "new",
        "type": "SignatureDrift",
        "promotion_status": "promoted",
        "risk": "High",
        "score": 12.0,
        "c_evidence_level": "c_source_diff",
        "c_side": {
            "symbol": "foo_get",
            "old": {"params": [], "return_type": "void *"},
            "new": {"params": [{"name": "flags", "type": "unsigned int"}], "return_type": "void *"},
            "old_version": "old",
            "new_version": "new",
        },
        "rust_side": {
            "uses": [{"rust_file": "device.rs", "line": 10, "enclosing_function": "Device::get"}],
            "safety_comments": [{"rust_file": "device.rs", "line": 9, "text": "SAFETY: wrapper validates flags"}],
        },
    }
    (run_dir / "warnings.jsonl").write_text(json.dumps(warning, sort_keys=True) + "\n", encoding="utf-8")
    (run_dir / "manual_review.csv").write_text(
        "warning_id,pair_id,reviewer1_label,reviewer2_label,adjudicated_label,label\n"
        "W-000010,latest-p001,,,TRUE_WRAPPER_FIX,\n",
        encoding="utf-8",
    )
    conn = connect(cfg.database)
    initialize(conn)
    upsert_many(
        conn,
        "replay_runs",
        [
            {
                "run_id": "latest",
                "started_at": "2026-05-05T00:00:00+00:00",
                "completed_at": "2026-05-05T00:01:00+00:00",
                "status": "completed",
                "start_ref": "old",
                "include_head": 0,
                "build_bindings": 1,
                "configure": 1,
                "jobs": 1,
                "arch": "x86_64",
                "c_roots": "[]",
                "max_files": None,
                "refs": "[]",
                "summary": json.dumps({"aggregate_warnings": str(run_dir / "warnings.jsonl")}),
                "error": None,
            }
        ],
    )

    result = generate_case_studies(cfg)
    text = Path(result["files"][0]).read_text(encoding="utf-8")

    assert result["cases"] == 1
    assert result["manual_review"] == str(run_dir / "manual_review.csv")
    assert "Oracle label: `TRUE_WRAPPER_FIX`" in text
    assert "wrapper validates flags" in text
