import json
from pathlib import Path

import pytest

from binddrift.cli import main
from binddrift.config import Config
from binddrift.evaluation.protocol import write_default_evaluation_protocol
from binddrift.paper.tables import generate_paper_tables
from binddrift.run_manifest import ArtifactConsistencyError, evaluation_protocol_split_hash, sha256_file, validate_run_manifest, write_run_manifest
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
        "c_evidence_level": "c_source_diff",
        "promotion_reasons": ["direct_binding_use"],
        "c_side": {"symbol": "foo", "old": "a", "new": "b"},
        "rust_side": {"uses": [{"rust_file": "x.rs", "line": 1}]},
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
    protocol = json.loads((tmp_path / "data/replay/latest/evaluation_protocol.json").read_text(encoding="utf-8"))
    assert manifest["locked_split_hash"] == evaluation_protocol_split_hash(protocol)

    warnings = tmp_path / "data/replay/latest/warnings.jsonl"
    original_warnings = warnings.read_text(encoding="utf-8")
    warnings.write_text(original_warnings + '{"warning_id":"W-2"}\n', encoding="utf-8")
    with pytest.raises(ArtifactConsistencyError, match="warning_count"):
        validate_run_manifest(cfg)
    warnings.write_text(original_warnings, encoding="utf-8")

    write_run_manifest(cfg)
    manifest_path = tmp_path / "data/replay/latest/run_manifest.json"
    stale = json.loads(manifest_path.read_text(encoding="utf-8"))
    stale["locked_split_hash"] = "stale"
    manifest_path.write_text(json.dumps(stale, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    with pytest.raises(ArtifactConsistencyError, match="locked_split_hash"):
        validate_run_manifest(cfg)


def test_run_manifest_tracks_pooled_review_artifacts_when_present(tmp_path: Path):
    cfg = _write_latest_run(tmp_path)
    run_dir = tmp_path / "data/replay/latest"
    warning = json.loads((run_dir / "warnings.jsonl").read_text(encoding="utf-8").splitlines()[0])
    (run_dir / "pooled_review_set.jsonl").write_text(json.dumps(warning, sort_keys=True) + "\n", encoding="utf-8")
    (run_dir / "pooled_review_labels.csv").write_text(
        "warning_uid,warning_id,pair_id,ranker_source,type,symbol,reviewer1_label,reviewer1_notes,reviewer2_label,reviewer2_notes,adjudicated_label,adjudication_notes,label_source\n"
        f"{warning['warning_uid']},W-1,latest-p001,binddrift_oracle_blind,SignatureDrift,foo,TRUE_WRAPPER_FIX,r1,TRUE_WRAPPER_FIX,r2,TRUE_WRAPPER_FIX,adj,manual_review.csv\n",
        encoding="utf-8",
    )
    (run_dir / "pooled_review_manifest.json").write_text('{"pool_rows": 1}\n', encoding="utf-8")

    manifest = write_run_manifest(cfg)
    validated = validate_run_manifest(cfg)

    assert manifest["pooled_review_set_count"] == 1
    assert manifest["pooled_review_label_count"] == 1
    assert "pooled_review_set.jsonl" in manifest["sha256"]
    assert Path(validated["resolved_paths"]["pooled_review_labels"]).exists()

    (run_dir / "pooled_review_labels.csv").write_text(
        (run_dir / "pooled_review_labels.csv").read_text(encoding="utf-8")
        + f"{warning['warning_uid']},W-1,latest-p001,random,SignatureDrift,foo,UNCLEAR,r1,UNCLEAR,r2,UNCLEAR,adj,manual_review.csv\n",
        encoding="utf-8",
    )
    with pytest.raises(ArtifactConsistencyError, match="pooled_review_label_count"):
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
                "protocol_version": "ccfb-strict-v2",
                "evaluation_protocol_sha256": sha256_file(tmp_path / "data/replay/latest/evaluation_protocol.json"),
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
                "protocol_version": "ccfb-strict-v2",
                "evaluation_protocol_sha256": sha256_file(run_dir / "evaluation_protocol.json"),
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


def test_paper_tables_fail_when_pooled_label_coverage_is_low(tmp_path: Path):
    cfg = _write_latest_run(tmp_path)
    write_run_manifest(cfg)
    run_dir = tmp_path / "data/replay/latest"
    warning = json.loads((run_dir / "warnings.jsonl").read_text(encoding="utf-8").splitlines()[0])
    pool = run_dir / "pooled_review_set.jsonl"
    labels = run_dir / "pooled_review_labels.csv"
    pool.write_text(json.dumps(warning, sort_keys=True) + "\n", encoding="utf-8")
    labels.write_text(
        "warning_uid,warning_id,pair_id,ranker_source,type,symbol,reviewer1_label,reviewer1_notes,reviewer2_label,reviewer2_notes,adjudicated_label,adjudication_notes,label_source\n"
        f"{warning['warning_uid']},W-1,latest-p001,binddrift_oracle_blind,SignatureDrift,foo,,,TRUE_WRAPPER_FIX,,TRUE_WRAPPER_FIX,,manual_review.csv\n",
        encoding="utf-8",
    )
    tables = tmp_path / "paper/tables"
    tables.mkdir(parents=True)
    (tables / "ranking_pooled_evaluation.json").write_text(
        json.dumps(
                {
                    "pool": str(pool),
                    "pool_sha256": sha256_file(pool),
                    "labels": str(labels),
                    "labels_sha256": sha256_file(labels),
                    "evaluation_protocol_sha256": sha256_file(run_dir / "evaluation_protocol.json"),
                    "label_coverage": {"coverage": 1.0, "labeled_rows": 1, "pool_rows": 1},
                "coverage_acceptance": {"minimum": 0.95, "passes": True},
                "rankers": [
                    {
                        "ranker": "binddrift_oracle_blind",
                        "evaluated_pool_rows": 1,
                        "label_distribution": {"TRUE_WRAPPER_FIX": 1},
                    }
                ],
            }
        )
        + "\n",
        encoding="utf-8",
    )

    with pytest.raises(RuntimeError, match="label coverage below 95%"):
        generate_paper_tables(cfg)


def test_paper_tables_fail_when_pooled_ranking_hash_is_stale(tmp_path: Path):
    cfg = _write_latest_run(tmp_path)
    write_run_manifest(cfg)
    run_dir = tmp_path / "data/replay/latest"
    warning = json.loads((run_dir / "warnings.jsonl").read_text(encoding="utf-8").splitlines()[0])
    pool = run_dir / "pooled_review_set.jsonl"
    labels = run_dir / "pooled_review_labels.csv"
    pool.write_text(json.dumps(warning, sort_keys=True) + "\n", encoding="utf-8")
    labels.write_text(
        "warning_uid,warning_id,pair_id,ranker_source,type,symbol,reviewer1_label,reviewer1_notes,reviewer2_label,reviewer2_notes,adjudicated_label,adjudication_notes,label_source\n"
        f"{warning['warning_uid']},W-1,latest-p001,binddrift_oracle_blind,SignatureDrift,foo,TRUE_WRAPPER_FIX,r1,TRUE_WRAPPER_FIX,r2,TRUE_WRAPPER_FIX,adj,manual_review.csv\n",
        encoding="utf-8",
    )
    tables = tmp_path / "paper/tables"
    tables.mkdir(parents=True)
    (tables / "ranking_pooled_evaluation.json").write_text(
        json.dumps(
            {
                "pool": str(pool),
                "pool_sha256": "stale",
                "labels": str(labels),
                "labels_sha256": sha256_file(labels),
                "label_coverage": {"coverage": 1.0, "labeled_rows": 1, "pool_rows": 1},
                "coverage_acceptance": {"minimum": 0.95, "passes": True},
                "rankers": [
                    {
                        "ranker": "binddrift_oracle_blind",
                        "evaluated_pool_rows": 1,
                        "label_distribution": {"TRUE_WRAPPER_FIX": 1},
                    }
                ],
            }
        )
        + "\n",
        encoding="utf-8",
    )

    with pytest.raises(RuntimeError, match="pool_sha256"):
        generate_paper_tables(cfg)
