from pathlib import Path
import json

from binddrift.config import Config
from binddrift.db import connect, initialize, upsert_many
from binddrift.evaluation.protocol import write_default_evaluation_protocol
from binddrift.paper.cases import generate_case_studies
from binddrift.run_manifest import evaluation_protocol_split_hash, sha256_file
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
    assert "- Adjudicated label: `TRUE_SEMANTIC_DRIFT`" in text
    assert "## Summary" in text
    assert "## Old Version Evidence" in text
    assert "## New Version Evidence" in text
    assert "## C-Side Diff" in text
    assert "## Rust-Side Dependency" in text
    assert "## Safe API / Contract Assumption" in text
    assert "## Manual Review Label" in text
    assert "## Why This Is Not Generated-Binding-Only" in text
    assert "## Alternative Explanation Considered" in text
    assert "adjudicated positive review target" in text
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
    assert result["manual_review"] == "data/replay/latest/manual_review.csv"
    assert "- Adjudicated label: `TRUE_WRAPPER_FIX`" in text
    assert "wrapper validates flags" in text


def test_case_studies_main_mode_fails_without_two_true_positive_cases(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    run_dir = tmp_path / "data/replay/latest"
    run_dir.mkdir(parents=True)
    warning = {
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
    }
    warning["warning_uid"] = "uid-1"
    for name in ("warnings.jsonl", "promoted_warnings.jsonl"):
        (run_dir / name).write_text(json.dumps(warning, sort_keys=True) + "\n", encoding="utf-8")
    (run_dir / "manual_review.csv").write_text(
        "warning_uid,warning_id,pair_id,reviewer1_label,reviewer2_label,adjudicated_label,label\n"
        "uid-1,W-000001,latest-p001,,,TRUE_SEMANTIC_DRIFT,\n",
        encoding="utf-8",
    )
    (run_dir / "drift_facts.jsonl").write_text('{"fact_id":"F-1"}\n', encoding="utf-8")
    (run_dir / "single_version_review_targets.jsonl").write_text("", encoding="utf-8")
    write_default_evaluation_protocol(cfg)
    (run_dir / "run_manifest.json").write_text(
        json.dumps(
            {
                "run_id": "latest",
                "canonical_warning_file": "data/replay/latest/warnings.jsonl",
                "canonical_promoted_warnings_file": "data/replay/latest/promoted_warnings.jsonl",
                "canonical_review_file": "data/replay/latest/manual_review.csv",
                "canonical_drift_facts_file": "data/replay/latest/drift_facts.jsonl",
                "canonical_single_version_review_targets_file": "data/replay/latest/single_version_review_targets.jsonl",
                "canonical_evaluation_protocol_file": "data/replay/latest/evaluation_protocol.json",
                "canonical_database": ".binddrift/binddrift.sqlite3",
                "warning_count": 1,
                "promoted_warning_count": 1,
                "paper_topk": 1,
                "drift_fact_count": 1,
                "reviewed_warning_count": 1,
                "single_version_review_targets": 0,
                "sha256": {
                    "warnings.jsonl": "",
                    "promoted_warnings.jsonl": "",
                    "manual_review.csv": "",
                    "drift_facts.jsonl": "",
                    "single_version_review_targets.jsonl": "",
                    "evaluation_protocol.json": "",
                },
            },
            sort_keys=True,
        ),
        encoding="utf-8",
    )

    manifest = json.loads((run_dir / "run_manifest.json").read_text(encoding="utf-8"))
    manifest["sha256"] = {
        "warnings.jsonl": sha256_file(run_dir / "warnings.jsonl"),
        "promoted_warnings.jsonl": sha256_file(run_dir / "promoted_warnings.jsonl"),
        "manual_review.csv": sha256_file(run_dir / "manual_review.csv"),
        "drift_facts.jsonl": sha256_file(run_dir / "drift_facts.jsonl"),
        "single_version_review_targets.jsonl": sha256_file(run_dir / "single_version_review_targets.jsonl"),
        "evaluation_protocol.json": sha256_file(run_dir / "evaluation_protocol.json"),
    }
    manifest["locked_split_hash"] = evaluation_protocol_split_hash(
        json.loads((run_dir / "evaluation_protocol.json").read_text(encoding="utf-8"))
    )
    (run_dir / "run_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    import pytest

    with pytest.raises(RuntimeError, match="Fewer than 8"):
        generate_case_studies(cfg)


def test_case_suite_artifact_meets_strict_summary_gates() -> None:
    summary = json.loads(Path("paper/tables/case_study_summary.json").read_text(encoding="utf-8"))

    assert "case_studies" in summary
    assert "negative_case_studies" in summary
    assert "acceptance" in summary
    acceptance = summary["acceptance"]
    assert acceptance["minimum_passes"] is all(value for key, value in acceptance.items() if key != "minimum_passes")
    if summary["acceptance"]["minimum_passes"]:
        assert summary["case_studies"] >= 8
        assert summary["negative_case_studies"] >= 2
        assert summary["drift_type_count"] >= 4
        assert summary["semantic_true_cases"] >= 3
        assert summary["non_wrapper_semantic_cases"] >= 2
        assert summary["wrapper_fix_backed_cases"] <= summary["case_studies"] // 2
    assert summary["false_positive_cases"] == 0
    assert summary["benign_drift_cases"] == 0
    assert summary["unlabeled_cases"] == 0
    assert summary["absolute_local_paths"] == 0
