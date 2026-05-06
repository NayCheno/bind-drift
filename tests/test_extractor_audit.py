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
    assert len(rows) >= sum(STRICT_AUDIT_TARGETS.values())
    assert all(row["reviewer1_label"] for row in rows)
    assert all(row["reviewer2_label"] for row in rows)
    assert all(row["adjudicated_label"] for row in rows)

    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    assert summary["total_samples"] == sum(STRICT_AUDIT_TARGETS.values())
    assert summary["all_minimums_pass"] is True
    assert summary["agreement"]["cohen_kappa"] >= 0.80
    assert summary["negative_samples"]["passes"] is True
    assert summary["negative_samples"]["total"] >= len(STRICT_AUDIT_TARGETS)
    assert summary["cross_version_sampling"]["passes"] is True
    assert summary["review_provenance"]["pending_rows"] == 0
    assert summary["review_provenance"]["generated_default_labels"] == 0
    assert summary["review_provenance"]["review_labels_transferred"] == summary["total_samples"]
    assert len(summary["parser_limitations"]) >= len(STRICT_AUDIT_TARGETS)
    taxonomy = taxonomy_path.read_text(encoding="utf-8")
    assert "Parser Limitations" in taxonomy
    assert "Negative Controls" in taxonomy
    assert "Observed Incorrect Rows" in taxonomy
    for extractor, target in STRICT_AUDIT_TARGETS.items():
        assert summary["extractors"][extractor]["sampled"] == target
        assert summary["extractors"][extractor]["version_count"] >= 10
        assert summary["extractors"][extractor]["pair_count"] >= 10
        assert summary["acceptance"][extractor]["passes"] is True
        assert summary["acceptance"][extractor]["target_passes"] is True
        assert summary["negative_samples"]["extractors"][extractor]["count"] >= 1


def test_strict_extractor_audit_reports_promoted_warning_precision_gate() -> None:
    summary = json.loads(Path("paper/tables/strict_extractor_audit.json").read_text(encoding="utf-8"))
    promoted = summary["extractors"]["promoted_warning_evidence"]

    assert promoted["sampled"] >= 150
    assert promoted["precision"] >= 0.85
    assert promoted["pair_count"] >= 10
    assert summary["acceptance"]["promoted_warning_evidence"]["passes"] is True
