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
        assert not row.get("forbidden_oracle_feature_keys")
    significance = table["comparison"]["paired_bootstrap_significance"]
    assert significance["method"] == "paired_rank_position_bootstrap"
    assert set(significance["metrics"]) == {"p_at_20", "p_at_50", "ndcg_at_20"}
    assert table["all_rankers_same_pool"] is True
    assert table["primary_beats_best_simple_baseline"] is True
    assert table["no_self_evaluation_top100_only"] is True
    assert table["m6_acceptance"]["minimum_passes"] is True
    assert table["top_false_positive_taxonomy"]["taxonomy"]
    assert table["top_false_negative_taxonomy"]["taxonomy"]
    assert table["top_false_positive_taxonomy"]["schema_valid"] is True
    assert table["top_false_negative_taxonomy"]["schema_valid"] is True


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
    assert table["all_rankers_same_pool"] is True
    assert table["primary_beats_best_simple_baseline"] is True
    assert table["no_self_evaluation_top100_only"] is True
    assert table["m6_acceptance"]["checks"]["random_baseline_sanity"] is True
    assert table["m6_acceptance"]["checks"]["ablation_story"] is True
    assert table["top_false_positive_taxonomy"]["window"] == "primary_top_100"
    assert table["top_false_negative_taxonomy"]["window"] == "pooled_true_labels_outside_primary_top_100"
    ablation_path = Path("paper/tables/ablation_strict_comparison.json")
    ablation = json.loads(ablation_path.read_text(encoding="utf-8"))
    assert ablation["ablation_story"]["supporting_ablation_count"] >= 2
