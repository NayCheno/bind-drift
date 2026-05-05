import json
from pathlib import Path

from binddrift.config import Config
from binddrift.cli import main
from binddrift.evaluation.diagnostics import diagnose_false_positives
from binddrift.evaluation.evaluator import generate_manual_review, parse_build_log
from binddrift.evaluation.metrics import label_for_warning, labeled_summary, load_manual_labels, manual_review_agreement, oracle_summary
from binddrift.evaluation.review_merge import merge_manual_review
from binddrift.evaluation.wrapper_oracle import classify_fix_kinds, replay_head_date, typed_wrapper_oracle_summary, wrapper_fix_events_from_warnings
from binddrift.warnings import write_warnings


def test_parse_build_log_extracts_binding_symbol(tmp_path: Path):
    log = tmp_path / "build.log"
    log.write_text(
        "error[E0425]: cannot find function `foo_get` in module `bindings::foo_get`\n"
        "error: mismatched types\n",
        encoding="utf-8",
    )

    findings = parse_build_log(log)

    assert findings[0]["symbol"] == "foo_get"
    assert len(findings) == 2


def test_labeled_summary_reports_precision_at_k():
    warnings = [{"warning_id": "W-1"}, {"warning_id": "W-2"}, {"warning_id": "W-3"}]
    labels = {"W-1": "TRUE_SEMANTIC_DRIFT", "W-2": "FALSE_POSITIVE"}

    summary = labeled_summary(warnings, labels, ks=(2,))

    assert summary["labeled_warnings"] == 2
    assert summary["precision"] == 0.5
    assert summary["precision_at_k"]["2"] == 0.5


def test_labeled_summary_does_not_cross_match_reused_warning_ids():
    warnings = [
        {"pair_id": "p1", "warning_id": "W-1"},
        {"pair_id": "p2", "warning_id": "W-1"},
    ]
    labels = {"p1:W-1": "TRUE_SEMANTIC_DRIFT"}

    summary = labeled_summary(warnings, labels, ks=(2,))

    assert summary["labeled_warnings"] == 1
    assert summary["true_labeled_warnings"] == 1
    assert summary["precision_at_k"]["2"] == 1.0


def test_labeled_summary_distribution_is_scoped_to_warning_subset():
    warnings = [{"warning_id": "W-1"}]
    labels = {"W-1": "FALSE_POSITIVE", "W-2": "UNCLEAR"}

    summary = labeled_summary(warnings, labels, ks=(1,))

    assert summary["label_distribution"] == {"FALSE_POSITIVE": 1}
    assert summary["unclear_warnings"] == 0


def test_oracle_summary_reports_symbol_recall_and_mrr():
    warnings = [
        {"warning_id": "W-1", "c_side": {"symbol": "foo_get"}},
        {"warning_id": "W-2", "c_side": {"symbol": "bar_put"}},
        {"warning_id": "W-3", "c_side": {"symbol": "baz_alloc"}},
    ]

    summary = oracle_summary(warnings, {"bar_put", "missing_symbol"}, ks=(2,))

    assert summary["matched_symbols"] == 1
    assert summary["recall"] == 0.5
    assert summary["precision_at_k"]["2"] == 0.5
    assert summary["mrr"] == 0.25


def test_oracle_summary_does_not_cross_match_reused_warning_ids():
    warnings = [
        {"warning_id": "W-1", "c_side": {"symbol": "foo_get"}},
        {"warning_id": "W-1", "c_side": {"symbol": "unrelated_symbol"}},
        {"warning_id": "W-2", "c_side": {"symbol": "bar_put"}},
    ]

    summary = oracle_summary(warnings, {"foo_get"}, ks=(3,))

    assert summary["matched_symbols"] == 1
    assert summary["recall"] == 1.0
    assert summary["precision"] == 0.3333
    assert summary["precision_at_k"]["3"] == 0.3333


def test_typed_wrapper_oracle_requires_fix_kind_compatibility():
    warnings = [
        {"warning_id": "W-1", "type": "ErrorDrift", "old_version": "v1", "c_side": {"symbol": "ERR_PTR"}},
        {"warning_id": "W-2", "type": "OwnershipRefcountDrift", "old_version": "v1", "c_side": {"symbol": "ERR_PTR"}},
    ]
    events = [
        {
            "commit": "c1",
            "date": "2024-01-01",
            "subject": "rust: error: Add Error::to_ptr()",
            "changed_files": ["rust/kernel/error.rs"],
            "matched_symbols": ["ERR_PTR"],
            "likely_wrapper_fix": True,
        }
    ]

    summary = typed_wrapper_oracle_summary(warnings, events, version_dates={"v1": "2023-01-01"})

    assert "error_mapping" in classify_fix_kinds("rust: error: Add Error::to_ptr()", ["rust/kernel/error.rs"], ["ERR_PTR"])
    assert summary["matched_warnings"] == 1
    assert summary["precision_at_k"]["10"] == 0.5
    assert summary["matched_fix_kind_distribution"]["error_mapping"] == 1


def test_typed_wrapper_oracle_can_enforce_time_relation():
    warnings = [{"warning_id": "W-1", "type": "SignatureDrift", "old_version": "v2", "c_side": {"symbol": "foo"}}]
    events = [
        {
            "commit": "before",
            "date": "2023-01-01",
            "subject": "rust: bindings: add foo wrapper",
            "changed_files": ["rust/kernel/foo.rs"],
            "matched_symbols": ["foo"],
            "likely_wrapper_fix": True,
        },
        {
            "commit": "after",
            "date": "2025-01-01",
            "subject": "rust: bindings: fix foo wrapper",
            "changed_files": ["rust/kernel/foo.rs"],
            "matched_symbols": ["foo"],
            "likely_wrapper_fix": True,
        },
    ]

    summary = typed_wrapper_oracle_summary(warnings, events, version_dates={"v2": "2024-01-01"}, enforce_time=True)

    assert summary["matched_warnings"] == 1
    assert summary["matched_oracle_rows"] == 1
    assert summary["time_relation_distribution"] == {"after_drift": 1}
    assert summary["enforce_time"] is True
    assert summary["time_window"] == "old_to_head"


def test_typed_wrapper_oracle_old_to_new_window_rejects_late_fix():
    warnings = [{"warning_id": "W-1", "type": "SignatureDrift", "old_version": "v1", "new_version": "v2", "c_side": {"symbol": "foo"}}]
    events = [
        {
            "commit": "same-pair",
            "date": "2024-06-01",
            "subject": "rust: bindings: fix foo wrapper",
            "changed_files": ["rust/kernel/foo.rs"],
            "matched_symbols": ["foo"],
            "likely_wrapper_fix": True,
        },
        {
            "commit": "late",
            "date": "2025-01-01",
            "subject": "rust: bindings: fix foo wrapper",
            "changed_files": ["rust/kernel/foo.rs"],
            "matched_symbols": ["foo"],
            "likely_wrapper_fix": True,
        },
    ]

    summary = typed_wrapper_oracle_summary(
        warnings,
        events,
        version_dates={"v1": "2024-01-01", "v2": "2024-07-01"},
        time_window="old_to_new",
    )

    assert summary["matched_warnings"] == 1
    assert summary["matched_oracle_rows"] == 1
    assert summary["time_relation_distribution"] == {"same_pair": 1}


def test_replay_head_date_prefers_canonical_head_pseudo_version():
    warnings = [
        {"new_version": "v7.0"},
        {"new_version": "HEAD_abc123"},
    ]
    version_dates = {
        "v7.0": "2026-04-01T00:00:00+00:00",
        "HEAD_abc123": "2026-05-03T00:00:00+00:00",
        "abc123": "2026-05-04T00:00:00+00:00",
    }

    assert replay_head_date(warnings, version_dates) == "2026-05-03T00:00:00+00:00"


def test_wrapper_fix_events_from_warnings_normalizes_embedded_oracles():
    warnings = [
        {
            "warning_id": "W-1",
            "rust_side": {
                "oracle_hits": [
                    {
                        "oracle_type": "wrapper_fix",
                        "commit_id": "c1",
                        "date": "2024-01-01",
                        "subject": "rust: bindings: add foo wrapper",
                        "changed_files": "[\"rust/kernel/foo.rs\"]",
                        "matched_symbols": "[\"foo\"]",
                    }
                ]
            },
        }
    ]

    events = wrapper_fix_events_from_warnings(warnings)

    assert events == [
        {
            "commit": "c1",
            "date": "2024-01-01",
            "subject": "rust: bindings: add foo wrapper",
            "changed_files": ["rust/kernel/foo.rs"],
            "matched_symbols": ["foo"],
            "likely_wrapper_fix": True,
        }
    ]


def test_manual_labels_prefer_adjudicated_label_and_report_agreement(tmp_path: Path):
    review = tmp_path / "manual_review.csv"
    review.write_text(
        "warning_id,reviewer1_label,reviewer2_label,adjudicated_label,label\n"
        "W-1,TRUE_SEMANTIC_DRIFT,TRUE_SEMANTIC_DRIFT,TRUE_SEMANTIC_DRIFT,FALSE_POSITIVE\n"
        "W-2,FALSE_POSITIVE,UNCLEAR,,TRUE_WRAPPER_FIX\n",
        encoding="utf-8",
    )

    labels = load_manual_labels(review)
    agreement = manual_review_agreement(review)

    assert labels["W-1"] == "TRUE_SEMANTIC_DRIFT"
    assert labels["W-2"] == "TRUE_WRAPPER_FIX"
    assert agreement["double_labeled"] == 2
    assert agreement["agreements"] == 1


def test_manual_labels_include_pair_id_when_present(tmp_path: Path):
    review = tmp_path / "manual_review.csv"
    review.write_text(
        "warning_id,pair_id,reviewer1_label,reviewer2_label,adjudicated_label,label\n"
        "W-1,p1,TRUE_SEMANTIC_DRIFT,TRUE_SEMANTIC_DRIFT,TRUE_SEMANTIC_DRIFT,\n",
        encoding="utf-8",
    )

    labels = load_manual_labels(review)

    assert labels == {"p1:W-1": "TRUE_SEMANTIC_DRIFT"}


def test_generate_manual_review_migrates_legacy_rows_by_warning_shape(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path, data_dir="data/replay/latest")
    cfg.data_dir.mkdir(parents=True)
    (cfg.data_dir / "manual_review.csv").write_text(
        "warning_id,type,risk,score,symbol,reviewer1_label,reviewer2_label,adjudicated_label,label\n"
        "W-1,SignatureDrift,High,1.0,foo,TRUE_SEMANTIC_DRIFT,TRUE_SEMANTIC_DRIFT,TRUE_SEMANTIC_DRIFT,\n",
        encoding="utf-8",
    )
    warnings = [
        {"pair_id": "p1", "warning_id": "W-1", "type": "SignatureDrift", "risk": "High", "score": 1.0, "c_side": {"symbol": "foo"}},
        {"pair_id": "p2", "warning_id": "W-1", "type": "SignatureDrift", "risk": "High", "score": 1.0, "c_side": {"symbol": "bar"}},
    ]

    review = generate_manual_review(cfg, warnings, top_k=2)
    labels = load_manual_labels(review)

    assert label_for_warning(labels, warnings[0]) == "TRUE_SEMANTIC_DRIFT"
    assert label_for_warning(labels, warnings[1]) == ""


def test_manual_labels_prefer_warning_uid(tmp_path: Path):
    review = tmp_path / "manual_review.csv"
    review.write_text(
        "warning_uid,warning_id,pair_id,adjudicated_label,label\n"
        "uid-1,W-1,p1,TRUE_SEMANTIC_DRIFT,\n",
        encoding="utf-8",
    )
    warning = {"warning_uid": "uid-1", "pair_id": "p2", "warning_id": "W-1"}

    labels = load_manual_labels(review)

    assert label_for_warning(labels, warning) == "TRUE_SEMANTIC_DRIFT"


def test_diagnose_false_positives_writes_hard_negative_and_true_positive_csvs(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    write_warnings(
        cfg,
        [
            {
                "warning_id": "W-1",
                "pair_id": "p1",
                "type": "SignatureDrift",
                "c_evidence_level": "binding_only",
                "c_side": {"symbol": "foo_get", "old": "absent", "new": "added"},
                "rust_side": {"exposure": {"edge_count": 3}},
                "demotion_reasons": ["generated_binding_only"],
            },
            {
                "warning_id": "W-2",
                "pair_id": "p2",
                "type": "ErrorDrift",
                "c_evidence_level": "c_behavior_indicator",
                "c_side": {"symbol": "bar_get"},
                "rust_side": {"uses": [{"rust_file": "device.rs", "line": 1}]},
            },
        ],
    )
    review = tmp_path / "manual_review.csv"
    review.write_text(
        "warning_id,pair_id,adjudicated_label,label,reviewer_notes\n"
        "W-1,p1,FALSE_POSITIVE,,\n"
        "W-2,p2,TRUE_SEMANTIC_DRIFT,,\n",
        encoding="utf-8",
    )

    summary = diagnose_false_positives(review, cfg.warnings_jsonl, tmp_path / "manual")
    hard_negatives = (tmp_path / "manual/hard_negatives.csv").read_text(encoding="utf-8")
    true_positives = (tmp_path / "manual/true_positives.csv").read_text(encoding="utf-8")

    assert summary["false_positive_reasons"] == {"ADDED_SYMBOL_NO_OLD_EVIDENCE": 1}
    assert summary["split"]["strategy"] == "pair_holdout"
    assert "W-1,foo_get,SignatureDrift,p1,FALSE_POSITIVE,ADDED_SYMBOL_NO_OLD_EVIDENCE" in hard_negatives
    assert "W-2,bar_get,ErrorDrift,p2,TRUE_SEMANTIC_DRIFT,," in true_positives


def test_diagnose_false_positives_cli(tmp_path: Path, capsys):
    cfg = Config.from_args(repo_root=tmp_path)
    write_warnings(
        cfg,
        [
            {
                "warning_id": "W-1",
                "type": "SignatureDrift",
                "c_evidence_level": "binding_only",
                "c_side": {"symbol": "foo_get", "old": "present", "new": "removed"},
                "rust_side": {"exposure": {"edge_count": 1}},
            },
        ],
    )
    review = tmp_path / "manual_review.csv"
    review.write_text(
        "warning_id,adjudicated_label,label,reviewer_notes\n"
        "W-1,FALSE_POSITIVE,,generated binding only\n",
        encoding="utf-8",
    )
    output_dir = tmp_path / "manual"

    code = main(
        [
            "--repo-root",
            str(tmp_path),
            "eval",
            "diagnose-false-positives",
            "--manual-review",
            str(review),
            "--warnings",
            str(cfg.warnings_jsonl),
            "--output-dir",
            str(output_dir),
        ]
    )
    captured = capsys.readouterr()

    assert code == 0
    assert "BINDING_ONLY" in captured.out
    assert (output_dir / "hard_negatives.csv").exists()


def test_check_label_join_cli_reports_unmatched_and_orphans(tmp_path: Path, capsys):
    cfg = Config.from_args(repo_root=tmp_path)
    warning = {
        "warning_id": "W-1",
        "run_id": "latest",
        "pair_id": "latest-p001",
        "old_version": "v6.1",
        "new_version": "v6.2",
        "type": "SignatureDrift",
        "c_side": {"symbol": "foo", "old": "a", "new": "b"},
    }
    write_warnings(cfg, [warning])
    uid = cfg.warnings_jsonl.read_text(encoding="utf-8").split('"warning_uid": "')[1].split('"')[0]
    review = tmp_path / "manual_review.csv"
    review.write_text(
        "warning_uid,warning_id,pair_id,adjudicated_label,label\n"
        f"{uid},W-1,latest-p001,TRUE_WRAPPER_FIX,\n"
        "missing,W-2,latest-p001,FALSE_POSITIVE,\n",
        encoding="utf-8",
    )

    code = main(
        [
            "--repo-root",
            str(tmp_path),
            "eval",
            "check-label-join",
            "--warnings",
            str(cfg.warnings_jsonl),
            "--manual-review",
            str(review),
        ]
    )
    captured = capsys.readouterr()

    assert code == 0
    assert '"matched_review_rows": 1' in captured.out
    assert '"orphan_review_rows": [' in captured.out
    assert "TRUE_WRAPPER_FIX" in captured.out


def test_merge_manual_review_copies_pair_rows_and_codes_reasons(tmp_path: Path):
    run_dir = tmp_path / "data/replay/latest"
    pair_dir = run_dir / "latest-p001-v6.1-to-v6.2"
    pair_dir.mkdir(parents=True)
    warning = {
        "warning_id": "W-1",
        "warning_uid": "uid-1",
        "run_id": "latest",
        "pair_id": "latest-p001-v6.1-to-v6.2",
        "old_version": "v6.1",
        "new_version": "v6.2",
        "type": "SignatureDrift",
        "c_evidence_level": "c_source_diff",
        "c_side": {"symbol": "foo", "old": "a", "new": "b"},
        "rust_side": {"oracle_hits": [{"oracle_type": "wrapper_fix"}]},
    }
    (run_dir / "warnings.jsonl").write_text(json.dumps(warning) + "\n", encoding="utf-8")
    (run_dir / "manual_review.csv").write_text(
        "warning_uid,run_id,pair_id,warning_id,type,symbol,reviewer1_label,reviewer1_notes,"
        "reviewer2_label,reviewer2_notes,adjudicated_label,adjudication_notes,true_reason,"
        "false_reason,label,reviewer_notes\n"
        "uid-1,latest,latest-p001-v6.1-to-v6.2,W-1,SignatureDrift,foo,,,,,,,,,legacy,note\n",
        encoding="utf-8",
    )
    (pair_dir / "manual_review.csv").write_text(
        "warning_id,pair_id,type,risk,score,symbol,reviewer1_label,reviewer1_notes,"
        "reviewer2_label,reviewer2_notes,adjudicated_label,adjudication_notes,label,reviewer_notes\n"
        "W-1,latest-p001-v6.1-to-v6.2,SignatureDrift,High,1.0,foo,"
        "TRUE_WRAPPER_FIX,r1,TRUE_WRAPPER_FIX,r2,TRUE_WRAPPER_FIX,adj,,\n",
        encoding="utf-8",
    )

    result = merge_manual_review(run_dir)
    labels = load_manual_labels(run_dir / "manual_review.csv", uid_only=True)
    merged = (run_dir / "manual_review.csv").read_text(encoding="utf-8")

    assert result["updated_rows"] == 1
    assert result["label_distribution"] == {"TRUE_WRAPPER_FIX": 1}
    assert result["missing_sources"] == []
    assert labels == {"uid-1": "TRUE_WRAPPER_FIX"}
    assert "WRAPPER_FIX_COMMIT_MATCH" in merged
    assert "legacy,note" not in merged


def test_merge_manual_review_supports_non_latest_pair_dirs(tmp_path: Path):
    run_dir = tmp_path / "data/replay/replay-1"
    pair_dir = run_dir / "replay-1-p001-v6.1-to-v6.2"
    pair_dir.mkdir(parents=True)
    warning = {
        "warning_id": "W-1",
        "warning_uid": "uid-1",
        "run_id": "replay-1",
        "pair_id": "replay-1-p001-v6.1-to-v6.2",
        "old_version": "v6.1",
        "new_version": "v6.2",
        "type": "SignatureDrift",
        "c_side": {"symbol": "foo", "old": "a", "new": "b"},
    }
    (run_dir / "warnings.jsonl").write_text(json.dumps(warning) + "\n", encoding="utf-8")
    (run_dir / "manual_review.csv").write_text(
        "warning_uid,run_id,pair_id,warning_id,type,symbol,reviewer1_label,reviewer1_notes,"
        "reviewer2_label,reviewer2_notes,adjudicated_label,adjudication_notes,true_reason,"
        "false_reason,label,reviewer_notes\n"
        "uid-1,replay-1,replay-1-p001-v6.1-to-v6.2,W-1,SignatureDrift,foo,,,,,,,,,,\n",
        encoding="utf-8",
    )
    (pair_dir / "manual_review.csv").write_text(
        "warning_id,pair_id,type,risk,score,symbol,reviewer1_label,reviewer1_notes,"
        "reviewer2_label,reviewer2_notes,adjudicated_label,adjudication_notes,label,reviewer_notes\n"
        "W-1,replay-1-p001-v6.1-to-v6.2,SignatureDrift,High,1.0,foo,"
        "FALSE_POSITIVE,parser artifact,FALSE_POSITIVE,parser artifact,FALSE_POSITIVE,parser artifact,,\n",
        encoding="utf-8",
    )

    result = merge_manual_review(run_dir)
    merged = (run_dir / "manual_review.csv").read_text(encoding="utf-8")

    assert result["updated_rows"] == 1
    assert result["missing_sources"] == []
    assert "EXTRACTOR_ERROR" in merged
