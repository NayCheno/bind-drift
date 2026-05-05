import csv
import json
from pathlib import Path

from binddrift.detectors.semantic_review_targets import build_semantic_review_summary, select_semantic_targets


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


def test_semantic_target_selection_uses_only_adjudicated_labeled_rows() -> None:
    labeled_warning, labeled_review = _warning("labeled", warning_type="SignatureDrift", symbol="ERR_PTR", label="TRUE_SEMANTIC_DRIFT")
    unlabeled_warning, _ = _warning("unlabeled", warning_type="SignatureDrift", symbol="PTR_ERR", label="")

    selected, shortages = select_semantic_targets(
        [unlabeled_warning, labeled_warning],
        {"labeled": labeled_review},
        quotas={"NullabilityDrift": 2},
    )

    assert [row["warning_uid"] for row in selected] == ["labeled"]
    assert selected[0]["semantic_target_type"] == "NullabilityDrift"
    assert shortages["NullabilityDrift"] == "only 1 adjudicated labeled candidates available for quota 2"


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
    assert len(rows) == summary["candidates_reviewed"]
    assert all(row["reviewer1_label"] for row in rows)
    assert all(row["reviewer2_label"] for row in rows)
    assert all(row["adjudicated_label"] for row in rows)
    assert summary["true_semantic_drift_count"] < 8
    assert summary["claim_recommendation"] == "semantic drift claim must be downgraded to exploratory"
