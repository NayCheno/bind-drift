from pathlib import Path

from binddrift.config import Config
from binddrift.cli import main
from binddrift.evaluation.diagnostics import diagnose_false_positives
from binddrift.evaluation.evaluator import generate_manual_review, parse_build_log
from binddrift.evaluation.metrics import labeled_summary, load_manual_labels, manual_review_agreement, oracle_summary
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

    assert labels["p1:W-1"] == "TRUE_SEMANTIC_DRIFT"
    assert labels["p2:W-1"] == ""


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
