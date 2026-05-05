import json
from pathlib import Path


def test_strict_baseline_table_has_required_metric_fields() -> None:
    path = Path("paper/tables/baseline_strict_comparison.json")
    assert path.exists()
    table = json.loads(path.read_text(encoding="utf-8"))
    assert "rankers" in table
    expected = {"binddrift_oracle_blind", "binding_diff", "c_signature", "c_indicator", "rust_use", "no_ranking", "random"}
    assert {row["ranker"] for row in table["rankers"]} == expected
    for row in table["rankers"]:
        for field in ("ranker", "candidate_count", "p_at_10", "p_at_20", "p_at_50", "p_at_100", "ndcg_at_20", "bootstrap_ci"):
            assert field in row
        assert row["evaluation_denominator"] == "complete_pooled_review_set"
        assert row["evaluated_pool_rows"] == table["rankers"][0]["evaluated_pool_rows"]
        assert not ({"wrapper_fix_hit", "build_oracle_hit"} & set(row.get("score_component_keys", [])))
    significance = table["comparison"]["paired_bootstrap_significance"]
    assert significance["method"] == "paired_rank_position_bootstrap"
    assert set(significance["metrics"]) == {"p_at_20", "p_at_50", "ndcg_at_20"}


def test_pooled_ranking_table_uses_one_label_pool() -> None:
    path = Path("paper/tables/ranking_pooled_evaluation.json")
    assert path.exists()
    table = json.loads(path.read_text(encoding="utf-8"))
    assert Path(table["pool"]).exists()
    assert Path(table["labels"]).exists()
    assert "pool_sha256" in table
    assert "labels_sha256" in table
    assert table["label_coverage"]["coverage"] >= 0.95
    assert table["coverage_acceptance"]["passes"] is True
    assert "label_coverage" in table
    assert all("review_pool_covered" in row for row in table["rankers"])
    assert all(row["candidate_count"] >= row["review_pool_ranked_count"] for row in table["rankers"])
