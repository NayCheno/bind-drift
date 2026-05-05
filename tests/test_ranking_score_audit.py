import json
from pathlib import Path

from binddrift.ranking.score_audit import build_ranking_score_audit


def _warning(uid: str, *, c_evidence_level: str, rust_side: dict, promotion_reasons=None) -> dict:
    return {
        "warning_uid": uid,
        "warning_id": uid,
        "run_id": "latest",
        "pair_id": "latest-p001",
        "old_version": "v1",
        "new_version": "v2",
        "promotion_status": "promoted",
        "type": "SignatureDrift",
        "c_evidence_level": c_evidence_level,
        "fact_source": "binding_diff" if c_evidence_level == "binding_only" else "c_api_diff",
        "promotion_reasons": promotion_reasons or [],
        "c_side": {"symbol": uid, "old": "a", "new": "b"},
        "rust_side": rust_side,
    }


def test_ranking_score_audit_uses_strict_top50_window() -> None:
    supported = _warning(
        "supported",
        c_evidence_level="c_source_diff",
        rust_side={"uses": [{"rust_file": "x.rs"}]},
        promotion_reasons=["direct_binding_use"],
    )
    binding_only = _warning(
        "binding-only",
        c_evidence_level="binding_only",
        rust_side={"uses": [{"rust_file": "x.rs"}], "safety_comments": [{"line": 1}]},
        promotion_reasons=["direct_binding_use"],
    )
    generated_only = _warning(
        "generated-only",
        c_evidence_level="binding_only",
        rust_side={},
    )

    audit = build_ranking_score_audit(
        [binding_only, generated_only, supported],
        {"supported": "TRUE_WRAPPER_FIX", "binding-only": "BENIGN_DRIFT", "generated-only": "FALSE_POSITIVE"},
        ranking_eval={"rankers": [{"ranker": "binddrift_oracle_blind", "p_at_10": 0.1, "p_at_20": 0.1, "p_at_50": 0.1, "p_at_100": 0.1, "ndcg_at_20": 0.1}]},
    )

    assert audit["oracle_blind"] is True
    assert audit["strict_top50_window_size"] == 2
    assert audit["strict_top50_checks"]["tier_d_warnings"] == 0
    assert audit["strict_top50_checks"]["generated_binding_only_warnings"] == 0
    assert audit["strict_top50_checks"]["binding_only_c_evidence_warnings"] == 1
    assert audit["strict_top50_checks"]["unsupported_c_evidence_warnings"] == 1
    assert audit["strict_top50_checks"]["unsupported_rust_reachability_warnings"] == 0
    assert audit["full_rank_top50_checks"]["unsupported_c_evidence_warnings"] == 2
    assert audit["full_rank_top50_checks"]["binding_only_c_evidence_warnings"] == 2
    assert audit["full_rank_top50_checks"]["generated_binding_only_warnings"] == 1
    assert audit["claim_recommendation"] == "evidence gate claim only; ranking improvement not supported"


def test_ranking_score_audit_artifact_exists_and_downgrades_claim() -> None:
    path = Path("paper/tables/ranking_score_audit.json")
    assert path.exists()
    audit = json.loads(path.read_text(encoding="utf-8"))

    assert audit["oracle_blind"] is True
    assert audit["strict_top50_checks"]["tier_d_warnings"] == 0
    assert audit["strict_top50_checks"]["generated_binding_only_warnings"] == 0
    assert audit["strict_top50_checks"]["unsupported_rust_reachability_warnings"] == 0
    assert audit["strict_top50_checks"]["missing_score_components"] == 0
    assert audit["strict_top50_checks"]["oracle_only_promotion_warnings"] == 0
    assert audit["strict_top50_checks"]["oracle_dependent_binding_only_warnings"] == 0
    assert audit["primary_metrics"]["p_at_10"] < 0.50
    assert audit["claim_recommendation"] == "evidence gate claim only; ranking improvement not supported"
    assert Path("paper/analysis/top20_false_positive_analysis.md").exists()
