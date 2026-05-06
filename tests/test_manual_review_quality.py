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
    review_artifacts = tmp_path / "data/replay/latest/review_artifacts"
    review_artifacts.mkdir(parents=True, exist_ok=True)
    (tmp_path / "data/replay/latest/pooled_review_manifest.json").write_text(
        json.dumps({"blind_to_ranker": True}) + "\n",
        encoding="utf-8",
    )
    (review_artifacts / "m3_final_role_summary.json").write_text(
        json.dumps(
            {
                "binddrift_review_roles": ["evidence_collector", "reviewer1", "reviewer2", "adjudicator"],
                "blind_to_ranker": True,
                "blind_to_rank_and_score": True,
            }
        )
        + "\n",
        encoding="utf-8",
    )

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
    assert quality["acceptance_thresholds"]["cohen_kappa_minimum"] == 0.70
    assert quality["acceptance_thresholds"]["agreement_rate_minimum"] == 0.80
    assert quality["acceptance_thresholds"]["unclear_rate_maximum"] == 0.05
    assert quality["unclear_is_true_positive"] is False
    assert quality["true_wrapper_fix_and_true_semantic_drift_reported_separately"] is True
    protocol = quality["review_protocol"]
    assert protocol["method"] == "binddrift-review LLM-assisted independent double review with adjudication"
    assert protocol["reviewer_independence"] is True
    assert protocol["reviewers_blind_to_ranker"] is True
    assert protocol["reviewers_blind_to_rank_and_score"] is True
    assert protocol["reviewers_blind_to_each_other"] is True
    assert protocol["blind_review_leakage"] == []
    assert protocol["reviewers_blind_to_oracles"] is False
    assert "auxiliary validation" in protocol["oracle_evidence_visibility"]
    assert protocol["label_source_for_metrics"] == "adjudicated_label"
    assert protocol["llm_assisted_boundary"]["not_human_expert_manual_review"] is True
    assert protocol["llm_assisted_boundary"]["llm_participates_in_primary_score"] is False
    assert protocol["llm_assisted_boundary"]["reviewer_roles_receive_adjudicated_labels"] is False

    examples = (tmp_path / "paper/analysis/reviewer_disagreement_examples.md").read_text(encoding="utf-8")
    assert examples.count("## ") == 5
    assert "data/replay/latest/pooled_review_labels.csv" in examples
    index = json.loads((tmp_path / "paper/tables/table_index.json").read_text(encoding="utf-8"))
    assert index["manual_review_quality"]["available"] is True
    assert index["reviewer_disagreement_examples"]["available"] is True
