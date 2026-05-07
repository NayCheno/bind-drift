import csv
import json
from pathlib import Path

from binddrift.paper.audit import M2_GOLD_TARGETS, M2_MIN_NEGATIVE_CONTROLS_PER_EXTRACTOR, STRICT_AUDIT_TARGETS, STRICT_FIELDS


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


def test_m2_extractor_precision_recall_artifacts_meet_thresholds() -> None:
    gold_path = Path("data/audit/extractor_gold_labels.csv")
    manifest_path = Path("data/audit/extractor_audit_manifest.json")
    precision_recall_path = Path("paper/tables/extractor_precision_recall.json")
    confusion_path = Path("paper/tables/extractor_confusion_matrix.json")
    limitations_path = Path("paper/analysis/extractor_limitations.md")
    false_negatives_path = Path("paper/analysis/extractor_false_negatives.md")

    for path in (gold_path, manifest_path, precision_recall_path, confusion_path, limitations_path, false_negatives_path):
        assert path.exists(), path

    with gold_path.open(newline="", encoding="utf-8") as fh:
        gold_rows = list(csv.DictReader(fh))
    assert len(gold_rows) >= sum(int(item["target_positive"]) for item in M2_GOLD_TARGETS.values())
    assert all(row["reviewer1_label"] for row in gold_rows)
    assert all(row["reviewer2_label"] for row in gold_rows)
    assert all(row["adjudicated_label"] for row in gold_rows)

    summary = json.loads(precision_recall_path.read_text(encoding="utf-8"))
    confusion = json.loads(confusion_path.read_text(encoding="utf-8"))
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    assert summary["acceptance"]["passes"] is True
    assert summary["overall"]["positive_gold_samples"] >= 2050
    assert summary["overall"]["precision"] >= 0.95
    assert summary["overall"]["recall"] >= 0.88
    assert summary["overall"]["agreement"]["cohen_kappa"] >= 0.80
    assert summary["overall"]["sample_hash"] == manifest["sample_hash"]
    assert summary["overall"]["tp"] == confusion["overall"]["tp"]
    assert summary["overall"]["fp"] == confusion["overall"]["fp"]
    assert summary["overall"]["fn"] == confusion["overall"]["fn"]
    assert summary["overall"]["tn"] == confusion["overall"]["tn"]

    for extractor, target in M2_GOLD_TARGETS.items():
        row = summary["extractors"][extractor]
        assert row["positive_gold_samples"] >= target["target_positive"]
        assert row["negative_controls"] >= M2_MIN_NEGATIVE_CONTROLS_PER_EXTRACTOR
        assert row["precision"] >= target["minimum_precision"]
        assert row["recall"] >= target["minimum_recall"]
        assert "extractor_gold_labels.csv" not in row["precision_source"]
        assert row["precision_reviewed"] > 0
        assert row["passes"] is True

    limitations = limitations_path.read_text(encoding="utf-8")
    false_negatives = false_negatives_path.read_text(encoding="utf-8")
    for extractor in M2_GOLD_TARGETS:
        assert f"## {extractor}" in limitations
        assert f"`{extractor}`" in false_negatives
    assert "## Taxonomy" in false_negatives
