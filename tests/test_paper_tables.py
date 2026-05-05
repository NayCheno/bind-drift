import json
from pathlib import Path

import pytest

from binddrift.config import Config
from binddrift.db import connect, initialize, upsert_many
from binddrift.paper.tables import generate_paper_tables
from binddrift.run_manifest import ArtifactConsistencyError, write_run_manifest
from binddrift.warnings import make_warning_uid


def test_paper_tables_exclude_stale_and_zero_binding_replays(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    conn = connect(cfg.database)
    initialize(conn)
    upsert_many(
        conn,
        "versions",
        [
            {"version_id": "v6.1", "git_commit": "old", "tag": "v6.1", "date": "2026-01-01", "arch": "x86_64", "config_hash": None, "rustc_version": None, "clang_version": None, "bindgen_version": None},
            {"version_id": "v6.2", "git_commit": "new", "tag": "v6.2", "date": "2026-02-01", "arch": "x86_64", "config_hash": None, "rustc_version": None, "clang_version": None, "bindgen_version": None},
        ],
    )
    upsert_many(
        conn,
        "replay_runs",
        [
            {
                "run_id": "stale-run",
                "started_at": "2026-05-04T00:00:00+00:00",
                "completed_at": None,
                "status": "stale",
                "start_ref": "v6.1",
                "include_head": 0,
                "build_bindings": 1,
                "configure": 1,
                "jobs": 1,
                "arch": "x86_64",
                "c_roots": "[]",
                "max_files": None,
                "refs": json.dumps([{"version_id": "v6.1"}, {"version_id": "v6.2"}]),
                "summary": "{}",
                "error": "interrupted",
            },
            {
                "run_id": "zero-bindings-run",
                "started_at": "2026-05-04T00:01:00+00:00",
                "completed_at": "2026-05-04T00:02:00+00:00",
                "status": "completed",
                "start_ref": "v6.1",
                "include_head": 0,
                "build_bindings": 1,
                "configure": 1,
                "jobs": 1,
                "arch": "x86_64",
                "c_roots": "[]",
                "max_files": None,
                "refs": json.dumps([{"version_id": "v6.1"}, {"version_id": "v6.2"}]),
                "summary": "{}",
                "error": None,
            },
            {
                "run_id": "single-version-run",
                "started_at": "2026-05-04T00:03:00+00:00",
                "completed_at": "2026-05-04T00:04:00+00:00",
                "status": "completed",
                "start_ref": "v6.1",
                "include_head": 0,
                "build_bindings": 1,
                "configure": 1,
                "jobs": 1,
                "arch": "x86_64",
                "c_roots": "[]",
                "max_files": None,
                "refs": json.dumps([{"version_id": "v6.1"}]),
                "summary": "{}",
                "error": None,
            },
        ],
    )
    upsert_many(
        conn,
        "replay_pairs",
        [
            {
                "pair_id": "zero-pair",
                "run_id": "zero-bindings-run",
                "pair_index": 1,
                "old_ref": "v6.1",
                "new_ref": "v6.2",
                "old_version": "v6.1",
                "new_version": "v6.2",
                "old_commit": "old",
                "new_commit": "new",
                "started_at": "2026-05-04T00:01:00+00:00",
                "completed_at": "2026-05-04T00:02:00+00:00",
                "status": "completed",
                "warning_count": 0,
                "build_status": "built",
                "extraction_summary": "{}",
                "evaluation_summary": "{}",
                "warnings_jsonl": None,
                "report_md": None,
                "error": None,
            }
        ],
    )

    generate_paper_tables(cfg)

    fact_counts = json.loads((tmp_path / "paper/tables/fact_counts.json").read_text(encoding="utf-8"))
    replay_summary = json.loads((tmp_path / "paper/tables/replay_summary.json").read_text(encoding="utf-8"))
    assert fact_counts["main_by_version"] == []
    assert fact_counts["main_evidence_gate"]["usable"] is False
    excluded_reasons = {reason for run in replay_summary["main_evidence_gate"]["excluded_runs"] for reason in run["reasons"]}
    assert "status:stale" in excluded_reasons
    assert "single_version" in excluded_reasons
    assert "zero_binding_facts:v6.1,v6.2" in excluded_reasons


def test_manual_review_summary_marks_all_unclear_as_not_main(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    review = cfg.data_dir / "manual_review.csv"
    review.parent.mkdir(parents=True, exist_ok=True)
    review.write_text(
        "warning_id,reviewer1_label,reviewer2_label,adjudicated_label,label\n"
        "W-1,,,,UNCLEAR\n",
        encoding="utf-8",
    )

    generate_paper_tables(cfg)

    summary = json.loads((tmp_path / "paper/tables/manual_review_summary.json").read_text(encoding="utf-8"))
    assert summary["labeled_warnings"] == 1
    assert summary["all_labels_unclear"] is True
    assert summary["usable_for_main"] is False


def test_manual_review_summary_prefers_latest_eligible_replay_csv(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    conn = connect(cfg.database)
    initialize(conn)
    run_dir = tmp_path / "data/replay/main-run"
    run_dir.mkdir(parents=True)
    (run_dir / "manual_review.csv").write_text(
        "warning_id,reviewer1_label,reviewer2_label,adjudicated_label,label\n"
        "W-1,,,TRUE_WRAPPER_FIX,\n",
        encoding="utf-8",
    )
    upsert_many(
        conn,
        "versions",
        [
            {"version_id": "v6.6", "git_commit": "old", "tag": "v6.6", "date": "2026-01-01", "arch": "x86_64", "config_hash": "a", "rustc_version": "rustc", "clang_version": "clang", "bindgen_version": "bindgen"},
            {"version_id": "v6.7", "git_commit": "new", "tag": "v6.7", "date": "2026-02-01", "arch": "x86_64", "config_hash": "b", "rustc_version": "rustc", "clang_version": "clang", "bindgen_version": "bindgen"},
        ],
    )
    upsert_many(
        conn,
        "binding_functions",
        [
            {"version_id": "v6.6", "rust_symbol": "foo", "c_symbol": "foo", "params": "[]", "return_type": "void", "is_unsafe": 1, "source_file": "bindings.rs", "line": 1},
            {"version_id": "v6.7", "rust_symbol": "foo", "c_symbol": "foo", "params": "[]", "return_type": "void", "is_unsafe": 1, "source_file": "bindings.rs", "line": 1},
        ],
    )
    upsert_many(
        conn,
        "replay_runs",
        [
            {
                "run_id": "main-run",
                "started_at": "2026-05-04T00:00:00+00:00",
                "completed_at": "2026-05-04T00:01:00+00:00",
                "status": "completed",
                "start_ref": "v6.6",
                "include_head": 0,
                "build_bindings": 1,
                "configure": 1,
                "jobs": 1,
                "arch": "x86_64",
                "c_roots": "[]",
                "max_files": None,
                "refs": json.dumps([{"version_id": "v6.6"}, {"version_id": "v6.7"}]),
                "summary": json.dumps({"run_dir": str(run_dir)}),
                "error": None,
            }
        ],
    )
    upsert_many(
        conn,
        "replay_pairs",
        [
            {
                "pair_id": "main-pair",
                "run_id": "main-run",
                "pair_index": 1,
                "old_ref": "v6.6",
                "new_ref": "v6.7",
                "old_version": "v6.6",
                "new_version": "v6.7",
                "old_commit": "old",
                "new_commit": "new",
                "started_at": "2026-05-04T00:00:00+00:00",
                "completed_at": "2026-05-04T00:01:00+00:00",
                "status": "completed",
                "warning_count": 1,
                "build_status": "built",
                "extraction_summary": "{}",
                "evaluation_summary": "{}",
                "warnings_jsonl": str(run_dir / "warnings.jsonl"),
                "report_md": str(run_dir / "warnings.md"),
                "error": None,
            }
        ],
    )

    generate_paper_tables(cfg)

    summary = json.loads((tmp_path / "paper/tables/manual_review_summary.json").read_text(encoding="utf-8"))
    assert summary["source_run_id"] == "main-run"
    assert summary["manual_review_csv"] == str(run_dir / "manual_review.csv")
    assert summary["true_labeled_warnings"] == 1


def test_manual_review_summary_prefers_canonical_latest_run(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    conn = connect(cfg.database)
    initialize(conn)
    upsert_many(
        conn,
        "versions",
        [
            {"version_id": "v6.1", "git_commit": "old", "tag": "v6.1", "date": "2026-01-01", "arch": "x86_64", "config_hash": "a", "rustc_version": "rustc", "clang_version": "clang", "bindgen_version": "bindgen"},
            {"version_id": "v6.2", "git_commit": "new", "tag": "v6.2", "date": "2026-02-01", "arch": "x86_64", "config_hash": "b", "rustc_version": "rustc", "clang_version": "clang", "bindgen_version": "bindgen"},
        ],
    )
    upsert_many(
        conn,
        "binding_functions",
        [
            {"version_id": "v6.1", "rust_symbol": "foo", "c_symbol": "foo", "params": "[]", "return_type": "void", "is_unsafe": 1, "source_file": "bindings.rs", "line": 1},
            {"version_id": "v6.2", "rust_symbol": "foo", "c_symbol": "foo", "params": "[]", "return_type": "void", "is_unsafe": 1, "source_file": "bindings.rs", "line": 1},
        ],
    )
    rows = []
    pair_rows = []
    for run_id, started_at in (("newer-timestamp-run", "2026-05-04T00:02:00+00:00"), ("latest", "2026-05-04T00:01:00+00:00")):
        run_dir = tmp_path / f"data/replay/{run_id}"
        run_dir.mkdir(parents=True)
        warning = {
            "warning_id": "W-1",
            "run_id": run_id,
            "pair_id": f"{run_id}-pair",
            "old_version": "v6.1",
            "new_version": "v6.2",
            "type": "SignatureDrift",
            "promotion_status": "promoted",
            "c_side": {"symbol": "foo", "old": "a", "new": "b"},
        }
        warning["warning_uid"] = make_warning_uid(warning)
        (run_dir / "warnings.jsonl").write_text(json.dumps(warning, sort_keys=True) + "\n", encoding="utf-8")
        (run_dir / "promoted_warnings.jsonl").write_text(json.dumps(warning, sort_keys=True) + "\n", encoding="utf-8")
        (run_dir / "drift_facts.jsonl").write_text('{"fact_id":"F-1"}\n', encoding="utf-8")
        (run_dir / "single_version_review_targets.jsonl").write_text("", encoding="utf-8")
        (run_dir / "manual_review.csv").write_text(
            "warning_uid,warning_id,pair_id,reviewer1_label,reviewer2_label,adjudicated_label,label\n"
            f"{warning['warning_uid']},W-1,{run_id}-pair,,,TRUE_WRAPPER_FIX,\n",
            encoding="utf-8",
        )
        rows.append(
            {
                "run_id": run_id,
                "started_at": started_at,
                "completed_at": "2026-05-04T00:03:00+00:00",
                "status": "completed",
                "start_ref": "v6.1",
                "include_head": 0,
                "build_bindings": 1,
                "configure": 1,
                "jobs": 1,
                "arch": "x86_64",
                "c_roots": "[]",
                "max_files": None,
                "refs": json.dumps([{"version_id": "v6.1"}, {"version_id": "v6.2"}]),
                "summary": json.dumps({"run_dir": str(run_dir), "aggregate_warnings": str(run_dir / "warnings.jsonl")}),
                "error": None,
            }
        )
        pair_rows.append(
            {
                "pair_id": f"{run_id}-pair",
                "run_id": run_id,
                "pair_index": 1,
                "old_ref": "v6.1",
                "new_ref": "v6.2",
                "old_version": "v6.1",
                "new_version": "v6.2",
                "old_commit": "old",
                "new_commit": "new",
                "started_at": started_at,
                "completed_at": "2026-05-04T00:03:00+00:00",
                "status": "completed",
                "warning_count": 1,
                "build_status": "built",
                "extraction_summary": "{}",
                "evaluation_summary": "{}",
                "warnings_jsonl": str(run_dir / "warnings.jsonl"),
                "report_md": str(run_dir / "warnings.md"),
                "error": None,
            }
        )
    upsert_many(conn, "replay_runs", rows)
    upsert_many(conn, "replay_pairs", pair_rows)
    write_run_manifest(cfg)

    generate_paper_tables(cfg)

    summary = json.loads((tmp_path / "paper/tables/manual_review_summary.json").read_text(encoding="utf-8"))
    replay_summary = json.loads((tmp_path / "paper/tables/replay_summary.json").read_text(encoding="utf-8"))
    gate = replay_summary["main_evidence_gate"]
    assert summary["source_run_id"] == "latest"
    assert gate["canonical_run_id"] == "latest"
    assert gate["eligible_run_ids"] == ["latest"]
    assert set(gate["candidate_run_ids"]) == {"latest", "newer-timestamp-run"}
    assert {"run_id": "newer-timestamp-run", "reasons": ["superseded_by:latest"]} in gate["excluded_runs"]


def test_manual_review_summary_rejects_stale_review_rows_without_warnings(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    conn = connect(cfg.database)
    initialize(conn)
    run_dir = tmp_path / "data/replay/latest"
    run_dir.mkdir(parents=True)
    (run_dir / "warnings.jsonl").write_text("", encoding="utf-8")
    (run_dir / "promoted_warnings.jsonl").write_text("", encoding="utf-8")
    (run_dir / "manual_review.csv").write_text(
        "warning_id,reviewer1_label,reviewer2_label,adjudicated_label,label\n"
        "W-stale,,,BENIGN_DRIFT,\n",
        encoding="utf-8",
    )
    upsert_many(
        conn,
        "versions",
        [
            {"version_id": "v6.1", "git_commit": "old", "tag": "v6.1", "date": "2026-01-01", "arch": "x86_64", "config_hash": "a", "rustc_version": "rustc", "clang_version": "clang", "bindgen_version": "bindgen"},
            {"version_id": "v6.2", "git_commit": "new", "tag": "v6.2", "date": "2026-02-01", "arch": "x86_64", "config_hash": "b", "rustc_version": "rustc", "clang_version": "clang", "bindgen_version": "bindgen"},
        ],
    )
    upsert_many(
        conn,
        "binding_functions",
        [
            {"version_id": "v6.1", "rust_symbol": "foo", "c_symbol": "foo", "params": "[]", "return_type": "void", "is_unsafe": 1, "source_file": "bindings.rs", "line": 1},
            {"version_id": "v6.2", "rust_symbol": "foo", "c_symbol": "foo", "params": "[]", "return_type": "void", "is_unsafe": 1, "source_file": "bindings.rs", "line": 1},
        ],
    )
    upsert_many(
        conn,
        "replay_runs",
        [
            {
                "run_id": "latest",
                "started_at": "2026-05-04T00:00:00+00:00",
                "completed_at": "2026-05-04T00:01:00+00:00",
                "status": "completed",
                "start_ref": "v6.1",
                "include_head": 0,
                "build_bindings": 1,
                "configure": 1,
                "jobs": 1,
                "arch": "x86_64",
                "c_roots": "[]",
                "max_files": None,
                "refs": json.dumps([{"version_id": "v6.1"}, {"version_id": "v6.2"}]),
                "summary": json.dumps({"run_dir": str(run_dir), "aggregate_warnings": str(run_dir / "warnings.jsonl")}),
                "error": None,
            }
        ],
    )
    upsert_many(
        conn,
        "replay_pairs",
        [
            {
                "pair_id": "latest-pair",
                "run_id": "latest",
                "pair_index": 1,
                "old_ref": "v6.1",
                "new_ref": "v6.2",
                "old_version": "v6.1",
                "new_version": "v6.2",
                "old_commit": "old",
                "new_commit": "new",
                "started_at": "2026-05-04T00:00:00+00:00",
                "completed_at": "2026-05-04T00:01:00+00:00",
                "status": "completed",
                "warning_count": 0,
                "build_status": "built",
                "extraction_summary": "{}",
                "evaluation_summary": "{}",
                "warnings_jsonl": str(run_dir / "warnings.jsonl"),
                "report_md": str(run_dir / "warnings.md"),
                "error": None,
            }
        ],
    )

    (run_dir / "drift_facts.jsonl").write_text("", encoding="utf-8")
    (run_dir / "single_version_review_targets.jsonl").write_text("", encoding="utf-8")
    with pytest.raises(ArtifactConsistencyError, match="empty"):
        write_run_manifest(cfg)
