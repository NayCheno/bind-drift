import json
from pathlib import Path

import pytest

from binddrift.cli import main
from binddrift.config import Config
from binddrift.paper.tables import generate_paper_tables
from binddrift.run_manifest import ArtifactConsistencyError, validate_run_manifest, write_run_manifest
from binddrift.warnings import make_warning_uid


def _write_latest_run(tmp_path: Path) -> Config:
    cfg = Config.from_args(repo_root=tmp_path)
    run_dir = tmp_path / "data/replay/latest"
    run_dir.mkdir(parents=True)
    warning = {
        "warning_id": "W-1",
        "run_id": "latest",
        "pair_id": "latest-p001",
        "old_version": "v6.1",
        "new_version": "v6.2",
        "promotion_status": "promoted",
        "type": "SignatureDrift",
        "c_side": {"symbol": "foo", "old": "a", "new": "b"},
    }
    warning["warning_uid"] = make_warning_uid(warning)
    (run_dir / "warnings.jsonl").write_text(json.dumps(warning, sort_keys=True) + "\n", encoding="utf-8")
    (run_dir / "drift_facts.jsonl").write_text('{"fact_id":"F-1"}\n', encoding="utf-8")
    (run_dir / "manual_review.csv").write_text(
        "warning_uid,warning_id,pair_id,reviewer1_label,reviewer2_label,adjudicated_label,label\n"
        f"{warning['warning_uid']},W-1,latest-p001,,,TRUE_WRAPPER_FIX,\n",
        encoding="utf-8",
    )
    (run_dir / "summary.json").write_text(
        json.dumps({"run_id": "latest", "pairs": 1, "versions": 2}),
        encoding="utf-8",
    )
    return cfg


def test_run_manifest_validates_counts_and_sha(tmp_path: Path):
    cfg = _write_latest_run(tmp_path)
    manifest = write_run_manifest(cfg)

    validated = validate_run_manifest(cfg)

    assert validated["warning_count"] == 1
    assert manifest["sha256"]["warnings.jsonl"] == validated["sha256"]["warnings.jsonl"]

    warnings = tmp_path / "data/replay/latest/warnings.jsonl"
    warnings.write_text(warnings.read_text(encoding="utf-8") + '{"warning_id":"W-2"}\n', encoding="utf-8")
    with pytest.raises(ArtifactConsistencyError, match="warning_count"):
        validate_run_manifest(cfg)


def test_run_manifest_rejects_empty_warning_file(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    run_dir = tmp_path / "data/replay/latest"
    run_dir.mkdir(parents=True)
    (run_dir / "warnings.jsonl").write_text("", encoding="utf-8")
    (run_dir / "drift_facts.jsonl").write_text("", encoding="utf-8")
    (run_dir / "manual_review.csv").write_text(
        "warning_id,pair_id,reviewer1_label,reviewer2_label,adjudicated_label,label\n",
        encoding="utf-8",
    )

    with pytest.raises(ArtifactConsistencyError, match="empty"):
        write_run_manifest(cfg)


def test_eval_manifest_cli_generates_review_and_manifest(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    run_dir = tmp_path / "data/replay/latest"
    pair_dir = run_dir / "latest-p001"
    pair_dir.mkdir(parents=True)
    (run_dir / "warnings.jsonl").write_text(
        '{"warning_id":"W-1","pair_id":"latest-p001","promotion_status":"promoted","c_side":{"symbol":"foo"}}\n',
        encoding="utf-8",
    )
    (pair_dir / "drift_facts.jsonl").write_text('{"fact_id":"F-1"}\n', encoding="utf-8")

    code = main(["--repo-root", str(tmp_path), "eval", "manifest"])

    assert code == 0
    assert (run_dir / "run_manifest.json").exists()
    assert (run_dir / "manual_review.csv").exists()
    assert validate_run_manifest(cfg)["drift_fact_count"] == 1


def test_paper_tables_fail_on_stale_evaluation_summary(tmp_path: Path):
    cfg = _write_latest_run(tmp_path)
    write_run_manifest(cfg)
    tables = tmp_path / "paper/tables"
    tables.mkdir(parents=True)
    (tables / "evaluation_summary.json").write_text('{"warnings": 999}\n', encoding="utf-8")

    with pytest.raises(RuntimeError, match="evaluation_summary warnings"):
        generate_paper_tables(cfg)


def test_paper_tables_fail_on_stale_manual_metrics(tmp_path: Path):
    cfg = _write_latest_run(tmp_path)
    write_run_manifest(cfg)
    tables = tmp_path / "paper/tables"
    tables.mkdir(parents=True)
    (tables / "evaluation_summary.json").write_text(
        json.dumps(
            {
                "warnings": 1,
                "run_manifest": str(tmp_path / "data/replay/latest/run_manifest.json"),
                "manual_review": {"labeled_warnings": 0},
            }
        )
        + "\n",
        encoding="utf-8",
    )

    with pytest.raises(RuntimeError, match="manual_review.labeled_warnings"):
        generate_paper_tables(cfg)


def test_paper_tables_fail_on_stale_baseline_warning_count(tmp_path: Path):
    cfg = _write_latest_run(tmp_path)
    write_run_manifest(cfg)
    tables = tmp_path / "paper/tables"
    tables.mkdir(parents=True)
    (tables / "baselines_ablations.json").write_text('{"counts": {"warnings": 2}}\n', encoding="utf-8")

    with pytest.raises(RuntimeError, match="baselines_ablations"):
        generate_paper_tables(cfg)


def test_paper_tables_fail_on_stale_evaluation_manifest(tmp_path: Path):
    cfg = _write_latest_run(tmp_path)
    write_run_manifest(cfg)
    tables = tmp_path / "paper/tables"
    tables.mkdir(parents=True)
    (tables / "evaluation_summary.json").write_text(
        '{"warnings": 1, "run_manifest": null, "manual_review": {"labeled_warnings": 1}}\n',
        encoding="utf-8",
    )

    with pytest.raises(RuntimeError, match="evaluation_summary run_manifest"):
        generate_paper_tables(cfg)


def test_paper_tables_fail_on_stale_baseline_review_source(tmp_path: Path):
    cfg = _write_latest_run(tmp_path)
    write_run_manifest(cfg)
    tables = tmp_path / "paper/tables"
    tables.mkdir(parents=True)
    (tables / "baselines_ablations.json").write_text(
        json.dumps(
            {
                "counts": {"warnings": 1},
                "source": {
                    "run_manifest": str(tmp_path / "data/replay/latest/run_manifest.json"),
                    "warnings": str(tmp_path / "data/replay/latest/warnings.jsonl"),
                    "manual_review": str(tmp_path / "data/manual_review.csv"),
                },
            }
        )
        + "\n",
        encoding="utf-8",
    )

    with pytest.raises(RuntimeError, match="source.manual_review"):
        generate_paper_tables(cfg)
