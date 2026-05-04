from pathlib import Path

from binddrift.evaluation.evaluator import parse_build_log
from binddrift.evaluation.metrics import labeled_summary


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
