import csv
import json
from pathlib import Path

from binddrift.detectors.semantic_review_targets import build_semantic_review_summary, select_semantic_targets, semantic_target_type


def _warning(uid: str, *, warning_type: str, symbol: str, label: str) -> tuple[dict, dict[str, str]]:
    warning = {
        "warning_uid": uid,
        "warning_id": uid,
        "run_id": "latest",
        "pair_id": "latest-p001",
        "old_version": "v1",
        "new_version": "v2",
        "promotion_status": "promoted",
        "type": warning_type,
        "c_evidence_level": "c_source_diff",
        "c_side": {"symbol": symbol, "old": "a", "new": "b"},
        "rust_side": {"uses": [{"rust_file": "x.rs"}], "error_mappings": [{"mapping_type": "RESULT_RETURN"}]},
    }
    review = {
        "warning_uid": uid,
        "reviewer1_label": label,
        "reviewer2_label": label,
        "adjudicated_label": label,
        "adjudication_notes": "fixture adjudication",
    }
    return warning, review


def test_semantic_target_selection_fills_quota_without_review_labels() -> None:
    labeled_warning, _ = _warning("labeled", warning_type="SignatureDrift", symbol="ERR_PTR", label="TRUE_SEMANTIC_DRIFT")
    unlabeled_warning, _ = _warning("unlabeled", warning_type="SignatureDrift", symbol="PTR_ERR", label="")

    selected, shortages = select_semantic_targets(
        [unlabeled_warning, labeled_warning],
        quotas={"NullabilityDrift": 2},
    )

    assert {row["warning_uid"] for row in selected} == {"labeled", "unlabeled"}
    assert all(row["semantic_target_type"] == "NullabilityDrift" for row in selected)
    assert shortages == {}


def test_semantic_review_summary_downgrades_when_true_semantic_gate_fails() -> None:
    warnings = []
    labels = {}
    for idx in range(3):
        warning, _ = _warning(f"sem-{idx}", warning_type="SignatureDrift", symbol=f"ERR_PTR_{idx}", label="TRUE_SEMANTIC_DRIFT")
        warning["semantic_target_type"] = "NullabilityDrift"
        warnings.append(warning)
        labels[warning["warning_uid"]] = "TRUE_SEMANTIC_DRIFT"
    wrapper, _ = _warning("wrapper", warning_type="FieldDrift", symbol="device", label="TRUE_WRAPPER_FIX")
    wrapper["semantic_target_type"] = "LayoutFieldDrift"
    warnings.append(wrapper)
    labels["wrapper"] = "TRUE_WRAPPER_FIX"

    summary = build_semantic_review_summary(warnings, labels)

    assert summary["true_semantic_drift_count"] == 3
    assert summary["true_wrapper_fix_count"] == 1
    assert summary["acceptance"]["minimum_passes"] is False
    assert summary["claim_recommendation"] == "semantic drift claim must be downgraded to exploratory"


def test_semantic_target_type_ignores_wrapper_oracle_payload() -> None:
    warning = {
        "type": "SignatureDrift",
        "fact_source": "binding_diff",
        "c_side": {"symbol": "plain_symbol", "old": "a", "new": "b"},
        "promotion_reasons": ["oracle_hit"],
        "evidence_chain": [
            {
                "oracle_type": "wrapper_fix",
                "subject": "later Rust helper adds allocation free handling",
                "matched_symbols": '["kfree"]',
            }
        ],
        "rust_side": {
            "oracle_hits": [
                {
                    "oracle_type": "wrapper_fix",
                    "subject": "later Rust helper adds allocation free handling",
                    "matched_symbols": '["kfree"]',
                }
            ]
        },
    }

    assert semantic_target_type(warning) == ""


def test_semantic_review_artifacts_exist_and_are_adjudicated() -> None:
    review_path = Path("data/replay/latest/semantic_target_review.csv")
    summary_path = Path("paper/tables/semantic_drift_review_summary.json")
    target_path = Path("data/replay/latest/semantic_target_review_set.jsonl")
    assert review_path.exists()
    assert summary_path.exists()
    assert target_path.exists()

    with review_path.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    summary = json.loads(summary_path.read_text(encoding="utf-8"))

    assert rows
    reviewed = [row for row in rows if row["adjudicated_label"]]
    assert len(rows) == summary["semantic_review_candidates"]
    assert len(reviewed) == summary["candidates_reviewed"]
    assert all(row["reviewer1_label"] for row in reviewed)
    assert all(row["reviewer2_label"] for row in reviewed)
    assert summary["acceptance"]["minimum_passes"] is True
    assert summary["semantic_review_candidates"] >= 400
    assert summary["reviewed_semantic_targets"] >= 200
    assert summary["true_semantic_drift_count"] >= 8
    assert summary["non_wrapper_semantic_true_positives"] >= 5
    assert summary["semantic_drift_type_count"] >= 3
    assert summary["false_positive_taxonomy"]
    assert summary["false_positive_taxonomy_examples"]
    for bucket, count in summary["false_positive_taxonomy"].items():
        assert count >= 0
        assert summary["false_positive_taxonomy_examples"].get(bucket)
    assert summary["claim_recommendation"] == "semantic review targets may be reported as a secondary contribution"
