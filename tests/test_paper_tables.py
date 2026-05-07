import csv
import json
from pathlib import Path

import pytest

from binddrift.config import Config
from binddrift.db import connect, initialize, upsert_many
from binddrift.evaluation.protocol import write_default_evaluation_protocol
from binddrift.paper.audit import M2_GOLD_FIELDS, generate_extractor_precision_recall_audit
from binddrift.paper.tables import generate_paper_tables
from binddrift.run_manifest import ArtifactConsistencyError, write_run_manifest
from binddrift.warnings import make_warning_uid


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as fh:
        return [dict(row) for row in csv.DictReader(fh)]


def _write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def _m2_match_key(row: dict[str, str]) -> str:
    import hashlib

    payload = {
        "extractor_name": row["extractor_name"],
        "gold_kind": row["gold_kind"].removesuffix("_negative_control"),
        "source_table": row["source_table"],
        "version": row["version"],
        "symbol": row["symbol"],
        "file": row["file"],
        "line": row["line"],
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def _m2_gold_row(**overrides: str) -> dict[str, str]:
    row = {
        "gold_id": "c_function_signatures-0001",
        "extractor_name": "c_function_signatures",
        "gold_kind": "function_signature",
        "source_table": "c_functions",
        "version": "v6.1",
        "audit_pair_id": "p1",
        "file": "foo.h",
        "line": "1",
        "symbol": "foo",
        "expected_present": "true",
        "expected_fact": "{}",
        "match_key": "",
        "reviewer1_label": "SHOULD_EXTRACT",
        "reviewer1_notes": "independent source packet",
        "reviewer2_label": "SHOULD_EXTRACT",
        "reviewer2_notes": "independent source packet",
        "adjudicated_label": "SHOULD_EXTRACT",
        "adjudication_notes": "adjudicated independent gold row",
    }
    row.update(overrides)
    row["match_key"] = row["match_key"] or _m2_match_key(row)
    return row


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


def test_arm64_external_validity_table_reports_overlap_and_failures(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    latest = tmp_path / "data/replay/latest"
    arm64 = tmp_path / "data/replay/arm64"
    latest.mkdir(parents=True)
    arm64.mkdir(parents=True)
    latest_warning = {
        "warning_id": "W-x86",
        "run_id": "latest",
        "pair_id": "latest-p001-v6.1-to-v6.2",
        "old_version": "v6.1",
        "new_version": "v6.2",
        "type": "SignatureDrift",
        "c_side": {"symbol": "foo"},
    }
    arm64_warning = {
        **latest_warning,
        "warning_id": "W-arm64",
        "run_id": "arm64",
        "pair_id": "arm64-p001-v6.1-to-v6.2",
    }
    latest_warning["warning_uid"] = make_warning_uid(latest_warning)
    arm64_warning["warning_uid"] = make_warning_uid(arm64_warning)
    (latest / "promoted_warnings.jsonl").write_text(json.dumps(latest_warning, sort_keys=True) + "\n", encoding="utf-8")
    (arm64 / "promoted_warnings.jsonl").write_text(json.dumps(arm64_warning, sort_keys=True) + "\n", encoding="utf-8")
    (arm64 / "drift_facts.jsonl").write_text('{"fact_id":"F-1"}\n', encoding="utf-8")
    (arm64 / "summary.json").write_text(
        json.dumps(
            {
                "run_id": "arm64",
                "versions": 8,
                "pairs": 7,
                "completed_pairs": 7,
                "failed_pairs": 0,
            },
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    conn = connect(cfg.database)
    initialize(conn)
    upsert_many(
        conn,
        "replay_runs",
        [
            {
                "run_id": "arm64",
                "started_at": "2026-05-04T00:00:00+00:00",
                "completed_at": "2026-05-04T00:01:00+00:00",
                "status": "completed",
                "start_ref": "v6.1",
                "include_head": 0,
                "build_bindings": 1,
                "configure": 1,
                "jobs": 1,
                "arch": "arm64",
                "c_roots": "[]",
                "max_files": None,
                "refs": "[]",
                "summary": "{}",
                "error": None,
            }
        ],
    )
    upsert_many(
        conn,
        "replay_pairs",
        [
            {
                "pair_id": f"arm64-p{index:03d}",
                "run_id": "arm64",
                "pair_index": index,
                "old_ref": f"v6.{index}",
                "new_ref": f"v6.{index + 1}",
                "old_version": f"v6.{index}",
                "new_version": f"v6.{index + 1}",
                "old_commit": "old",
                "new_commit": "new",
                "started_at": "2026-05-04T00:00:00+00:00",
                "completed_at": "2026-05-04T00:01:00+00:00",
                "status": "completed",
                "warning_count": 1,
                "build_status": "built",
                "extraction_summary": "{}",
                "evaluation_summary": "{}",
                "warnings_jsonl": None,
                "report_md": None,
                "error": None,
            }
            for index in range(1, 8)
        ],
    )

    generate_paper_tables(cfg)

    table = json.loads((tmp_path / "paper/tables/arm64_external_validity.json").read_text(encoding="utf-8"))
    assert table["passes"] is True
    assert table["arch"] == "arm64"
    assert table["version_count"] == 8
    assert table["completed_pairs"] == 7
    assert table["drift_fact_count"] == 1
    assert table["promoted_warning_count"] == 1
    assert table["warning_overlap"]["shared"] == 1
    assert table["warning_type_delta"] == [
        {"type": "SignatureDrift", "x86_64": 1, "arm64": 1, "delta_arm64_minus_x86_64": 0}
    ]
    index = json.loads((tmp_path / "paper/tables/table_index.json").read_text(encoding="utf-8"))
    assert index["arm64_external_validity"]["available"] is True


def test_extractor_audit_transfers_matching_previous_sample_labels(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    conn = connect(cfg.database)
    initialize(conn)
    upsert_many(
        conn,
        "c_functions",
        [
            {
                "version_id": "v6.1",
                "c_symbol": "foo",
                "return_type": "int",
                "params": "[]",
                "header_file": str(tmp_path / "foo.h"),
                "definition_file": str(tmp_path / "foo.h"),
                "line": 1,
            }
        ],
    )

    generate_paper_tables(cfg)

    sample = cfg.data_dir / "audit/extractor_sample.csv"
    rows = _read_csv(sample)
    rows[0]["is_correct"] = "false"
    rows[0]["error_type"] = "REGEX_ARTIFACT"
    rows[0]["notes"] = "macro expansion artifact"
    _write_csv(sample, rows)

    generate_paper_tables(cfg)

    assert "macro expansion artifact" in sample.read_text(encoding="utf-8")
    audit = json.loads((tmp_path / "paper/tables/extractor_audit.json").read_text(encoding="utf-8"))
    c_functions = audit["tables"]["c_functions"]
    assert c_functions["reviewed"] == 1
    assert c_functions["pending"] == 0
    assert c_functions["precision"] == 0.0
    assert c_functions["error_type_distribution"] == {"REGEX_ARTIFACT": 1}
    assert audit["acceptance"]["c_functions"]["passes"] is False
    assert audit["provenance"]["review_label_sources"]["previous_sample_labels_transferred"] == 1


def test_extractor_audit_rewrites_unreviewed_stale_generated_rows_as_pending(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    conn = connect(cfg.database)
    initialize(conn)
    upsert_many(
        conn,
        "c_functions",
        [
            {
                "version_id": "v6.1",
                "c_symbol": "foo",
                "return_type": "int",
                "params": "[]",
                "header_file": str(tmp_path / "foo.h"),
                "definition_file": str(tmp_path / "foo.h"),
                "line": 1,
            }
        ],
    )
    sample = cfg.data_dir / "audit/extractor_sample.csv"
    sample.parent.mkdir(parents=True)
    sample.write_text(
        "sample_id,table,symbol,file,line,extracted_fact,is_correct,corrected_fact,error_type,notes\n"
        'c_functions-001,c_functions,foo,/tmp/foo.h,1,"{}",,,,heuristic fact-shape and source-location check\n',
        encoding="utf-8",
    )

    generate_paper_tables(cfg)

    rewritten = sample.read_text(encoding="utf-8")
    assert "heuristic fact-shape and source-location check" not in rewritten
    audit = json.loads((tmp_path / "paper/tables/extractor_audit.json").read_text(encoding="utf-8"))
    assert audit["tables"]["c_functions"]["sampled"] == 1
    assert audit["tables"]["c_functions"]["pending"] == 1
    assert audit["all_minimums_pass"] is False


def test_extractor_audit_drops_stale_reviewed_rows_without_matching_fingerprint(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    conn = connect(cfg.database)
    initialize(conn)
    upsert_many(
        conn,
        "c_functions",
        [
            {
                "version_id": "v6.1",
                "c_symbol": "foo",
                "return_type": "int",
                "params": "[]",
                "header_file": str(tmp_path / "foo.h"),
                "definition_file": str(tmp_path / "foo.h"),
                "line": 1,
            }
        ],
    )
    sample = cfg.data_dir / "audit/extractor_sample.csv"
    sample.parent.mkdir(parents=True)
    sample.write_text(
        "sample_id,table,symbol,file,line,extracted_fact,is_correct,corrected_fact,error_type,notes\n"
        'c_functions-001,c_functions,foo,/tmp/foo.h,1,"{}",true,,,heuristic fact-shape and source-location check\n',
        encoding="utf-8",
    )

    generate_paper_tables(cfg)

    assert "heuristic fact-shape and source-location check" not in sample.read_text(encoding="utf-8")
    audit = json.loads((tmp_path / "paper/tables/extractor_audit.json").read_text(encoding="utf-8"))
    assert audit["tables"]["c_functions"]["reviewed"] == 0
    assert audit["tables"]["c_functions"]["pending"] == 1
    assert audit["provenance"]["review_label_sources"]["stale_or_unmatched_previous_rows"] == 1


def test_extractor_audit_prefers_matching_split_review_csv(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    conn = connect(cfg.database)
    initialize(conn)
    upsert_many(
        conn,
        "c_functions",
        [
            {
                "version_id": "v6.1",
                "c_symbol": "foo",
                "return_type": "int",
                "params": "[]",
                "header_file": str(tmp_path / "foo.h"),
                "definition_file": str(tmp_path / "foo.h"),
                "line": 1,
            }
        ],
    )
    generate_paper_tables(cfg)
    review = cfg.data_dir / "audit/reviews/c_functions_review.csv"
    review.parent.mkdir(parents=True)
    review.write_text(
        "sample_id,is_correct,error_type,notes\n"
        "c_functions-001,false,REGEX_ARTIFACT,split review label wins\n",
        encoding="utf-8",
    )

    generate_paper_tables(cfg)

    assert "split review label wins" in (cfg.data_dir / "audit/extractor_sample.csv").read_text(encoding="utf-8")
    audit = json.loads((tmp_path / "paper/tables/extractor_audit.json").read_text(encoding="utf-8"))
    c_functions = audit["tables"]["c_functions"]
    assert c_functions["reviewed"] == 1
    assert c_functions["precision"] == 0.0
    assert audit["provenance"]["review_label_sources"]["split_review_labels_transferred"] == 1


def test_extractor_audit_rejects_invalid_split_review_error_type(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    conn = connect(cfg.database)
    initialize(conn)
    upsert_many(
        conn,
        "c_functions",
        [
            {
                "version_id": "v6.1",
                "c_symbol": "foo",
                "return_type": "int",
                "params": "[]",
                "header_file": str(tmp_path / "foo.h"),
                "definition_file": str(tmp_path / "foo.h"),
                "line": 1,
            }
        ],
    )
    generate_paper_tables(cfg)
    review = cfg.data_dir / "audit/reviews/c_functions_review.csv"
    review.parent.mkdir(parents=True)
    review.write_text(
        "sample_id,is_correct,error_type,notes\n"
        "c_functions-001,false,NOT_A_REASON,bad label\n",
        encoding="utf-8",
    )

    with pytest.raises(RuntimeError, match="invalid error_type"):
        generate_paper_tables(cfg)


def test_extractor_audit_promoted_warning_uses_evidence_chain_location(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    cfg.data_dir.mkdir(parents=True)
    warning = {
        "warning_id": "W-1",
        "pair_id": "p1",
        "old_version": "v6.1",
        "new_version": "v6.2",
        "promotion_status": "promoted",
        "type": "SignatureDrift",
        "c_side": {"symbol": "foo", "evidence": None},
        "evidence_chain": [{"rust_file": "rust/kernel/foo.rs", "line": 42, "text": "bindings::foo()"}],
    }
    cfg.warnings_jsonl.write_text(json.dumps(warning) + "\n", encoding="utf-8")

    generate_paper_tables(cfg)

    rows = _read_csv(cfg.data_dir / "audit/extractor_sample.csv")
    promoted = next(row for row in rows if row["table"] == "promoted_warnings")
    assert promoted["file"] == "rust/kernel/foo.rs"
    assert promoted["line"] == "42"


def test_extractor_audit_promoted_review_survives_location_metadata_upgrade(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    cfg.data_dir.mkdir(parents=True)
    warning = {
        "warning_id": "W-1",
        "pair_id": "p1",
        "old_version": "v6.1",
        "new_version": "v6.2",
        "promotion_status": "promoted",
        "type": "SignatureDrift",
        "c_side": {"symbol": "foo", "evidence": None},
        "evidence_chain": [{"changed_files": json.dumps(["rust/helpers/foo.c"]), "subject": "rust: add helper"}],
    }
    cfg.warnings_jsonl.write_text(json.dumps(warning) + "\n", encoding="utf-8")
    generate_paper_tables(cfg)

    sample = cfg.data_dir / "audit/extractor_sample.csv"
    rows = _read_csv(sample)
    promoted = next(row for row in rows if row["table"] == "promoted_warnings")
    fact = json.loads(promoted["extracted_fact"])
    fact.pop("evidence_location")
    promoted["extracted_fact"] = json.dumps(fact, sort_keys=True)
    promoted["file"] = "p1"
    _write_csv(sample, rows)
    review = cfg.data_dir / "audit/reviews/promoted_warnings_review.csv"
    review.parent.mkdir(parents=True)
    review.write_text(
        "sample_id,is_correct,error_type,notes\n"
        f"{promoted['sample_id']},true,,same warning reviewed before location upgrade\n",
        encoding="utf-8",
    )

    generate_paper_tables(cfg)

    audit = json.loads((tmp_path / "paper/tables/extractor_audit.json").read_text(encoding="utf-8"))
    promoted_summary = audit["tables"]["promoted_warnings"]
    assert promoted_summary["reviewed"] == 1
    assert promoted_summary["precision"] == 1.0
    assert audit["provenance"]["review_label_sources"]["split_review_labels_transferred"] == 1


def test_extractor_audit_rejects_invalid_error_type(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    sample = cfg.data_dir / "audit/extractor_sample.csv"
    sample.parent.mkdir(parents=True)
    sample.write_text(
        "sample_id,table,symbol,file,line,extracted_fact,is_correct,corrected_fact,error_type,notes\n"
        'c_functions-001,c_functions,foo,/tmp/foo.h,1,"{}",false,,NOT_A_REASON,bad label\n',
        encoding="utf-8",
    )

    with pytest.raises(RuntimeError, match="invalid error_type"):
        generate_paper_tables(cfg)


def test_m2_precision_recall_audit_matches_gold_true_positive(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    conn = connect(cfg.database)
    initialize(conn)
    upsert_many(
        conn,
        "c_functions",
        [
            {
                "version_id": "v6.1",
                "c_symbol": "foo",
                "return_type": "int",
                "params": "[]",
                "header_file": str(tmp_path / "foo.h"),
                "definition_file": str(tmp_path / "foo.h"),
                "line": 1,
            }
        ],
    )
    gold = cfg.data_dir / "audit/extractor_gold_labels.csv"
    _write_csv(
        gold,
        [
            _m2_gold_row(
                file="./foo.h",
                expected_fact=json.dumps({"source_basis": "independent source packet", "symbol": "foo"}, sort_keys=True),
            )
        ],
    )

    result = generate_extractor_precision_recall_audit(cfg)

    summary = json.loads((tmp_path / result["extractor_precision_recall"]).read_text(encoding="utf-8"))
    manifest = json.loads((tmp_path / result["extractor_audit_manifest"]).read_text(encoding="utf-8"))
    c_functions = summary["extractors"]["c_function_signatures"]
    assert c_functions["positive_gold_samples"] == 1
    assert c_functions["tp"] == 1
    assert c_functions["fn"] == 0
    assert c_functions["recall"] == 1.0
    assert summary["overall"]["sample_hash"] == manifest["sample_hash"]


def test_m2_precision_recall_audit_reports_false_negative_from_checked_in_gold(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    initialize(connect(cfg.database))
    gold = cfg.data_dir / "audit/extractor_gold_labels.csv"
    row = _m2_gold_row(file="include/linux/missing.h", line="7", symbol="missing_symbol")
    _write_csv(gold, [{field: row[field] for field in M2_GOLD_FIELDS}])

    result = generate_extractor_precision_recall_audit(cfg)

    summary = json.loads((tmp_path / result["extractor_precision_recall"]).read_text(encoding="utf-8"))
    confusion = json.loads((tmp_path / result["extractor_confusion_matrix"]).read_text(encoding="utf-8"))
    c_functions = summary["extractors"]["c_function_signatures"]
    assert c_functions["tp"] == 0
    assert c_functions["fn"] == 1
    assert c_functions["recall"] == 0.0
    assert confusion["false_negative_examples"][0]["symbol"] == "missing_symbol"


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
    assert summary["manual_review_csv"] == "data/replay/main-run/manual_review.csv"
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
    write_default_evaluation_protocol(cfg)
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
    write_default_evaluation_protocol(cfg)
    with pytest.raises(ArtifactConsistencyError, match="empty"):
        write_run_manifest(cfg)
