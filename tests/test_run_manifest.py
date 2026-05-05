import json
from pathlib import Path

import pytest

from binddrift.cli import main
from binddrift.config import Config
from binddrift.evaluation.protocol import write_default_evaluation_protocol
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
    (run_dir / "promoted_warnings.jsonl").write_text(json.dumps(warning, sort_keys=True) + "\n", encoding="utf-8")
    (run_dir / "drift_facts.jsonl").write_text('{"fact_id":"F-1"}\n', encoding="utf-8")
    (run_dir / "single_version_review_targets.jsonl").write_text("", encoding="utf-8")
    (run_dir / "manual_review.csv").write_text(
        "warning_uid,warning_id,pair_id,reviewer1_label,reviewer2_label,adjudicated_label,label\n"
        f"{warning['warning_uid']},W-1,latest-p001,,,TRUE_WRAPPER_FIX,\n",
        encoding="utf-8",
    )
    (run_dir / "summary.json").write_text(
        json.dumps({"run_id": "latest", "pairs": 1, "versions": 2}),
        encoding="utf-8",
    )
    write_default_evaluation_protocol(cfg)
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
    (run_dir / "promoted_warnings.jsonl").write_text("", encoding="utf-8")
    (run_dir / "drift_facts.jsonl").write_text("", encoding="utf-8")
    (run_dir / "single_version_review_targets.jsonl").write_text("", encoding="utf-8")
    (run_dir / "manual_review.csv").write_text(
        "warning_id,pair_id,reviewer1_label,reviewer2_label,adjudicated_label,label\n",
        encoding="utf-8",
    )
    write_default_evaluation_protocol(cfg)

    with pytest.raises(ArtifactConsistencyError, match="empty"):
        write_run_manifest(cfg)


def test_run_manifest_requires_single_version_target_file(tmp_path: Path):
    cfg = _write_latest_run(tmp_path)
    (tmp_path / "data/replay/latest/single_version_review_targets.jsonl").unlink()

    with pytest.raises(ArtifactConsistencyError, match="single-version"):
        write_run_manifest(cfg)


def test_run_manifest_rejects_single_version_warning_in_main_file(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    run_dir = tmp_path / "data/replay/latest"
    run_dir.mkdir(parents=True)
    (run_dir / "warnings.jsonl").write_text(
        '{"warning_id":"W-1","run_id":"latest","new_version":"v6.2","promotion_status":"promoted","c_side":{"symbol":"foo"}}\n',
        encoding="utf-8",
    )
    (run_dir / "promoted_warnings.jsonl").write_text(
        '{"warning_id":"W-1","run_id":"latest","new_version":"v6.2","promotion_status":"promoted","c_side":{"symbol":"foo"}}\n',
        encoding="utf-8",
    )
    (run_dir / "drift_facts.jsonl").write_text('{"fact_id":"F-1"}\n', encoding="utf-8")
    (run_dir / "manual_review.csv").write_text(
        "warning_id,pair_id,reviewer1_label,reviewer2_label,adjudicated_label,label\n"
        "W-1,,,,,\n",
        encoding="utf-8",
    )
    (run_dir / "single_version_review_targets.jsonl").write_text("", encoding="utf-8")
    write_default_evaluation_protocol(cfg)

    with pytest.raises(ArtifactConsistencyError, match="non-main"):
        write_run_manifest(cfg)


def test_eval_manifest_cli_generates_review_and_manifest(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    run_dir = tmp_path / "data/replay/latest"
    pair_dir = run_dir / "latest-p001"
    pair_dir.mkdir(parents=True)
    (run_dir / "warnings.jsonl").write_text(
        '{"warning_id":"W-1","run_id":"latest","pair_id":"latest-p001","old_version":"v6.1","new_version":"v6.2","type":"SignatureDrift","promotion_status":"promoted","c_side":{"symbol":"foo","old":"a","new":"b"}}\n'
        '{"warning_id":"W-2","run_id":"latest","new_version":"v6.2","type":"SignatureDrift","promotion_status":"promoted","c_side":{"symbol":"bar","new":"b"}}\n',
        encoding="utf-8",
    )
    (pair_dir / "drift_facts.jsonl").write_text('{"fact_id":"F-1"}\n', encoding="utf-8")

    code = main(["--repo-root", str(tmp_path), "eval", "manifest"])

    assert code == 0
    assert (run_dir / "run_manifest.json").exists()
    assert (run_dir / "manual_review.csv").exists()
    validated = validate_run_manifest(cfg)
    assert validated["drift_fact_count"] == 1
    assert validated["warning_count"] == 1
    assert validated["promoted_warning_count"] == 1
    assert validated["single_version_review_targets"] == 1

    code = main(["--repo-root", str(tmp_path), "eval", "manifest"])

    assert code == 0
    assert validate_run_manifest(cfg)["single_version_review_targets"] == 1


def test_eval_uses_manifest_single_version_count(tmp_path: Path, capsys):
    cfg = Config.from_args(repo_root=tmp_path)
    run_dir = tmp_path / "data/replay/latest"
    run_dir.mkdir(parents=True)
    warning = {
        "warning_id": "W-1",
        "run_id": "latest",
        "pair_id": "latest-p001",
        "old_version": "v6.1",
        "new_version": "v6.2",
        "type": "SignatureDrift",
        "promotion_status": "promoted",
        "c_side": {"symbol": "foo", "old": "a", "new": "b"},
    }
    warning["warning_uid"] = make_warning_uid(warning)
    (run_dir / "warnings.jsonl").write_text(json.dumps(warning, sort_keys=True) + "\n", encoding="utf-8")
    (run_dir / "promoted_warnings.jsonl").write_text(json.dumps(warning, sort_keys=True) + "\n", encoding="utf-8")
    (run_dir / "single_version_review_targets.jsonl").write_text(
        '{"warning_id":"W-2","run_id":"latest","new_version":"v6.2","promotion_status":"promoted","c_side":{"symbol":"bar"}}\n',
        encoding="utf-8",
    )
    (run_dir / "drift_facts.jsonl").write_text('{"fact_id":"F-1"}\n', encoding="utf-8")
    (run_dir / "manual_review.csv").write_text(
        "warning_uid,warning_id,pair_id,reviewer1_label,reviewer2_label,adjudicated_label,label\n"
        f"{warning['warning_uid']},W-1,latest-p001,,,,\n",
        encoding="utf-8",
    )
    write_default_evaluation_protocol(cfg)
    write_run_manifest(cfg)

    code = main(["--repo-root", str(tmp_path), "eval", "all"])
    captured = capsys.readouterr()

    assert code == 0
    assert '"single_version_review_targets": 1' in captured.out


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
                "protocol_version": "ccfb-strict-v1",
                "claim_boundary": "evidence-backed warning prioritization",
                "primary_warning_set": "oracle_blind_ranked_warnings",
                "oracle_blind_primary_result": {
                    "oracle_blind": True,
                    "top_warning_uids": [
                        json.loads((tmp_path / "data/replay/latest/warnings.jsonl").read_text(encoding="utf-8").splitlines()[0])["warning_uid"]
                    ],
                    "manual_review": {"labeled_warnings": 0},
                },
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


def test_paper_tables_fail_when_baseline_main_is_not_oracle_blind(tmp_path: Path):
    cfg = _write_latest_run(tmp_path)
    write_run_manifest(cfg)
    tables = tmp_path / "paper/tables"
    tables.mkdir(parents=True)
    run_dir = tmp_path / "data/replay/latest"
    (tables / "baselines_ablations.json").write_text(
        json.dumps(
            {
                "counts": {"warnings": 1},
                "source": {
                    "run_manifest": str(run_dir / "run_manifest.json"),
                    "warnings": str(run_dir / "warnings.jsonl"),
                    "manual_review": str(run_dir / "manual_review.csv"),
                },
                "variants": [{"variant": "BindDrift", "kind": "main", "oracle_blind": False}],
            }
        )
        + "\n",
        encoding="utf-8",
    )

    with pytest.raises(RuntimeError, match="main variant must be oracle-blind"):
        generate_paper_tables(cfg)


def test_paper_tables_fail_when_evaluation_primary_leaks_oracle_score_key(tmp_path: Path):
    cfg = _write_latest_run(tmp_path)
    write_run_manifest(cfg)
    tables = tmp_path / "paper/tables"
    tables.mkdir(parents=True)
    run_dir = tmp_path / "data/replay/latest"
    uid = json.loads((run_dir / "warnings.jsonl").read_text(encoding="utf-8").splitlines()[0])["warning_uid"]
    manual = {"labeled_warnings": 1}
    (tables / "evaluation_summary.json").write_text(
        json.dumps(
            {
                "warnings": 1,
                "run_manifest": str(run_dir / "run_manifest.json"),
                "protocol_version": "ccfb-strict-v1",
                "claim_boundary": "evidence-backed warning prioritization",
                "primary_warning_set": "oracle_blind_ranked_warnings",
                "manual_review": manual,
                "oracle_blind_primary_result": {
                    "oracle_blind": True,
                    "top_warning_uids": [uid],
                    "score_component_keys": ["wrapper_fix_hit"],
                    "manual_review": manual,
                },
            }
        )
        + "\n",
        encoding="utf-8",
    )

    with pytest.raises(RuntimeError, match="leaks oracle score components"):
        generate_paper_tables(cfg)


def test_paper_tables_fail_when_baseline_main_uid_order_is_not_oracle_blind(tmp_path: Path):
    cfg = _write_latest_run(tmp_path)
    write_run_manifest(cfg)
    tables = tmp_path / "paper/tables"
    tables.mkdir(parents=True)
    run_dir = tmp_path / "data/replay/latest"
    (tables / "baselines_ablations.json").write_text(
        json.dumps(
            {
                "counts": {"warnings": 1},
                "source": {
                    "run_manifest": str(run_dir / "run_manifest.json"),
                    "warnings": str(run_dir / "warnings.jsonl"),
                    "manual_review": str(run_dir / "manual_review.csv"),
                },
                "variants": [
                    {
                        "variant": "BindDrift",
                        "kind": "main",
                        "oracle_blind": True,
                        "top_warning_uids": ["wrong"],
                        "score_component_keys": [],
                    }
                ],
            }
        )
        + "\n",
        encoding="utf-8",
    )

    with pytest.raises(RuntimeError, match="does not match promoted oracle-blind top-k"):
        generate_paper_tables(cfg)


def test_paper_tables_fail_when_non_auxiliary_baseline_leaks_oracle_score_key(tmp_path: Path):
    cfg = _write_latest_run(tmp_path)
    write_run_manifest(cfg)
    tables = tmp_path / "paper/tables"
    tables.mkdir(parents=True)
    run_dir = tmp_path / "data/replay/latest"
    uid = json.loads((run_dir / "warnings.jsonl").read_text(encoding="utf-8").splitlines()[0])["warning_uid"]
    (tables / "baselines_ablations.json").write_text(
        json.dumps(
            {
                "counts": {"warnings": 1},
                "source": {
                    "run_manifest": str(run_dir / "run_manifest.json"),
                    "warnings": str(run_dir / "warnings.jsonl"),
                    "manual_review": str(run_dir / "manual_review.csv"),
                },
                "variants": [
                    {
                        "variant": "BindDrift",
                        "kind": "main",
                        "oracle_blind": True,
                        "top_warning_uids": [uid],
                        "score_component_keys": [],
                    },
                    {
                        "variant": "BindingDiffOnly",
                        "kind": "baseline",
                        "oracle_blind": True,
                        "top_warning_uids": [uid],
                        "score_component_keys": ["wrapper_fix_hit"],
                    },
                ],
            }
        )
        + "\n",
        encoding="utf-8",
    )

    with pytest.raises(RuntimeError, match="BindingDiffOnly variant leaks oracle score components"):
        generate_paper_tables(cfg)
