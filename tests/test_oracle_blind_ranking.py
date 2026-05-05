from binddrift.ranking.oracle_blind_scorer import rank_primary_warnings_oracle_blind, rank_warnings_oracle_blind, score_components


def test_oracle_blind_ranking_ignores_wrapper_oracle_hits():
    base = {
        "warning_id": "W-1",
        "warning_uid": "uid-1",
        "type": "SignatureDrift",
        "c_evidence_level": "c_source_diff",
        "promotion_reasons": ["direct_binding_use"],
        "rust_side": {"uses": [{"rust_file": "x.rs"}]},
    }
    with_oracle = {
        **base,
        "warning_id": "W-2",
        "warning_uid": "uid-2",
        "score_breakdown": {"wrapper_fix_hit": 99.0},
        "rust_side": {
            "uses": [{"rust_file": "x.rs"}],
            "oracle_hits": [{"oracle_type": "wrapper_fix"}],
        },
    }

    components = score_components(with_oracle)
    ranked = rank_warnings_oracle_blind([with_oracle, base])

    assert "wrapper_fix_hit" not in components
    assert ranked[0]["oracle_blind"] is True
    assert ranked[0]["oracle_blind_score"] == ranked[1]["oracle_blind_score"]


def test_oracle_blind_tier_d_stays_below_supported_warning():
    supported = {
        "warning_id": "W-good",
        "warning_uid": "uid-good",
        "type": "NullabilityDrift",
        "c_evidence_level": "c_behavior_indicator",
        "promotion_reasons": ["direct_binding_use", "exposes_safe_api"],
        "rust_side": {
            "uses": [{"rust_file": "x.rs"}],
            "safe_apis": [{"api_name": "Foo::bar"}],
            "error_mappings": [{"mapping_type": "ERR_PTR"}],
        },
    }
    weak = {
        "warning_id": "W-weak",
        "warning_uid": "uid-weak",
        "type": "SignatureDrift",
        "c_evidence_level": "binding_only",
        "rust_side": {"uses": [{"rust_file": "x.rs"}]},
    }

    ranked = rank_warnings_oracle_blind([weak, supported])

    assert ranked[0]["warning_id"] == "W-good"
    assert ranked[0]["eligibility_tier"] == "A"
    assert ranked[1]["eligibility_tier"] == "D"


def test_primary_oracle_blind_excludes_binding_only_oracle_promoted_rows():
    supported = {
        "warning_id": "W-supported",
        "warning_uid": "uid-supported",
        "type": "SignatureDrift",
        "c_evidence_level": "c_source_diff",
        "fact_source": "c_api_diff",
        "promotion_reasons": ["direct_binding_use"],
        "rust_side": {"uses": [{"rust_file": "x.rs"}]},
    }
    binding_layout = {
        "warning_id": "W-layout",
        "warning_uid": "uid-layout",
        "type": "FieldDrift",
        "c_evidence_level": "binding_only",
        "fact_source": "layout_diff",
        "promotion_reasons": ["direct_binding_use", "oracle_hit"],
        "rust_side": {
            "uses": [{"rust_file": "x.rs"}],
            "safe_apis": [{"api_name": "Foo::bar"}],
            "safety_comments": [{"line": 1}],
        },
    }

    ranked = rank_warnings_oracle_blind([binding_layout, supported])
    primary = rank_primary_warnings_oracle_blind([binding_layout, supported])

    assert ranked[0]["warning_id"] == "W-supported"
    assert ranked[1]["c_evidence_level"] == "binding_only"
    assert ranked[1]["primary_oracle_blind_eligible"] is False
    assert [warning["warning_id"] for warning in primary] == ["W-supported"]


def test_primary_oracle_blind_includes_tier_c_without_oracle_dependency():
    tier_c = {
        "warning_id": "W-tier-c",
        "warning_uid": "uid-tier-c",
        "type": "FieldDrift",
        "c_evidence_level": "binding_only",
        "fact_source": "layout_diff",
        "promotion_reasons": ["direct_binding_use"],
        "rust_side": {
            "uses": [{"rust_file": "x.rs"}],
            "safe_apis": [{"api_name": "Foo::bar"}],
            "safety_comments": [{"line": 1}],
        },
    }

    primary = rank_primary_warnings_oracle_blind([tier_c])

    assert primary[0]["warning_id"] == "W-tier-c"
    assert primary[0]["eligibility_tier"] == "C"
    assert primary[0]["primary_oracle_blind_eligible"] is True
