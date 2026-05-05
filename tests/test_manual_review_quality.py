import csv
import json
from pathlib import Path

from binddrift.config import Config
from binddrift.paper.tables import generate_paper_tables


def _write_pooled_labels(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = [
        ("u1", "W-1", "p1", "binddrift_oracle_blind", "SignatureDrift", "foo", "TRUE_WRAPPER_FIX", "TRUE_WRAPPER_FIX"),
        ("u2", "W-2", "p1", "no_graph", "NullabilityDrift", "bar", "TRUE_SEMANTIC_DRIFT", "UNCLEAR"),
        ("u3", "W-3", "p2", "rust_use", "FieldDrift", "baz", "FALSE_POSITIVE", "BENIGN_DRIFT"),
        ("u4", "W-4", "p2", "no_ranking", "FieldDrift", "qux", "BENIGN_DRIFT", "FALSE_POSITIVE"),
        ("u5", "W-5", "p3", "random", "SignatureDrift", "zed", "FALSE_POSITIVE", "UNCLEAR"),
        ("u6", "W-6", "p3", "binding_diff", "SignatureDrift", "zap", "UNCLEAR", "FALSE_POSITIVE"),
    ]
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "warning_uid",
                "warning_id",
                "pair_id",
                "ranker_source",
                "type",
                "symbol",
                "reviewer1_label",
                "reviewer1_notes",
                "reviewer2_label",
                "reviewer2_notes",
                "adjudicated_label",
                "adjudication_notes",
                "label_source",
            ],
            lineterminator="\n",
        )
        writer.writeheader()
        for uid, warning_id, pair_id, ranker, drift_type, symbol, reviewer1, reviewer2 in rows:
            writer.writerow(
                {
                    "warning_uid": uid,
                    "warning_id": warning_id,
                    "pair_id": pair_id,
                    "ranker_source": ranker,
                    "type": drift_type,
                    "symbol": symbol,
                    "reviewer1_label": reviewer1,
                    "reviewer1_notes": f"{reviewer1} note",
                    "reviewer2_label": reviewer2,
                    "reviewer2_notes": f"{reviewer2} note",
                    "adjudicated_label": reviewer1,
                    "adjudication_notes": f"adjudicated {warning_id}",
                    "label_source": "existing_binddrift_review_artifacts",
                }
            )


def test_manual_review_quality_uses_pooled_labels_and_writes_examples(tmp_path: Path) -> None:
    cfg = Config.from_args(repo_root=tmp_path)
    _write_pooled_labels(tmp_path / "data/replay/latest/pooled_review_labels.csv")

    generate_paper_tables(cfg)

    quality = json.loads((tmp_path / "paper/tables/manual_review_quality.json").read_text(encoding="utf-8"))
    assert quality["source_csv"] == "data/replay/latest/pooled_review_labels.csv"
    assert quality["strict_gate_active"] is True
    assert quality["pooled_review_labels_primary_source"] is True
    assert quality["reviewed_warnings"] == 6
    assert quality["double_labeled_warnings"] == 6
    assert quality["adjudicated"] is True
    assert quality["label_coverage"] == 1.0
    assert quality["cohen_kappa"] is not None
    assert quality["disagreements"] == 5
    assert quality["reviewer_disagreement_examples"]["examples"] == 5
    assert quality["adjudication_notes_missing_rate"] == 0.0
    assert quality["label_leakage_check"] == "passed"
    assert quality["acceptance"]["minimum_passes"] is True
    assert quality["acceptance"]["pooled_review_labels_primary_source"] is True
    assert quality["unclear_is_true_positive"] is False
    assert quality["true_wrapper_fix_and_true_semantic_drift_reported_separately"] is True

    examples = (tmp_path / "paper/analysis/reviewer_disagreement_examples.md").read_text(encoding="utf-8")
    assert examples.count("## ") == 5
    assert "data/replay/latest/pooled_review_labels.csv" in examples
    index = json.loads((tmp_path / "paper/tables/table_index.json").read_text(encoding="utf-8"))
    assert index["manual_review_quality"]["available"] is True
    assert index["reviewer_disagreement_examples"]["available"] is True
