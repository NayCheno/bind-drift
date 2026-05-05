import csv
import json
from pathlib import Path

from binddrift.paper.audit import STRICT_AUDIT_TARGETS, STRICT_FIELDS


def test_strict_extractor_audit_artifacts_exist_and_meet_thresholds() -> None:
    sample_path = Path("data/audit/strict_extractor_sample.csv")
    review_path = Path("data/audit/strict_extractor_review.csv")
    summary_path = Path("paper/tables/strict_extractor_audit.json")
    taxonomy_path = Path("paper/analysis/extractor_error_taxonomy.md")

    assert sample_path.exists()
    assert review_path.exists()
    assert summary_path.exists()
    assert taxonomy_path.exists()

    with review_path.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
        assert fh
    assert rows
    assert set(STRICT_FIELDS).issubset(rows[0])
    assert len(rows) >= 600
    assert all(row["reviewer1_label"] for row in rows)
    assert all(row["reviewer2_label"] for row in rows)
    assert all(row["adjudicated_label"] for row in rows)

    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    assert summary["total_samples"] == 600
    assert summary["all_minimums_pass"] is True
    assert summary["agreement"]["cohen_kappa"] >= 0.70
    for extractor, target in STRICT_AUDIT_TARGETS.items():
        assert summary["extractors"][extractor]["sampled"] == target
        assert summary["acceptance"][extractor]["passes"] is True


def test_strict_extractor_audit_reports_promoted_warning_precision_gate() -> None:
    summary = json.loads(Path("paper/tables/strict_extractor_audit.json").read_text(encoding="utf-8"))
    promoted = summary["extractors"]["promoted_warning_evidence"]

    assert promoted["precision"] >= 0.85
    assert summary["acceptance"]["promoted_warning_evidence"]["passes"] is True
