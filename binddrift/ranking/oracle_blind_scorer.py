from __future__ import annotations

import json
from typing import Any

from binddrift.evaluation.protocol import assert_oracle_blind_components


ORACLE_COMPONENTS = {"build_oracle_hit", "wrapper_fix_hit"}
C_SOURCE_EVIDENCE_LEVELS = {"c_source_diff", "c_behavior_indicator"}
ORACLE_PROMOTION_REASONS = {"oracle_hit"}


def _has_list(value: Any) -> bool:
    return isinstance(value, list) and bool(value)


def _c_source_or_indicator(warning: dict[str, Any]) -> bool:
    return warning.get("c_evidence_level") in C_SOURCE_EVIDENCE_LEVELS


def _binding_only(warning: dict[str, Any]) -> bool:
    return warning.get("c_evidence_level") == "binding_only" or warning.get("fact_source") == "binding_diff"


def _rust_side(warning: dict[str, Any]) -> dict[str, Any]:
    return warning.get("rust_side") or {}


def _direct_use(warning: dict[str, Any]) -> bool:
    rust_side = _rust_side(warning)
    return _has_list(rust_side.get("uses")) or "direct_binding_use" in set(warning.get("promotion_reasons") or [])


def _safe_api(warning: dict[str, Any]) -> bool:
    rust_side = _rust_side(warning)
    return _has_list(rust_side.get("safe_apis")) or "exposes_safe_api" in set(warning.get("promotion_reasons") or [])


def _contract_evidence(warning: dict[str, Any]) -> bool:
    rust_side = _rust_side(warning)
    return bool(
        _has_list(rust_side.get("safety_comments"))
        or _has_list(rust_side.get("error_mappings"))
        or _has_list(rust_side.get("lifetime_facts"))
    )


def generated_binding_only(warning: dict[str, Any]) -> bool:
    demotions = set(warning.get("demotion_reasons") or [])
    return bool(
        (_binding_only(warning) or "generated_binding_only" in demotions)
        and not _direct_use(warning)
        and not _safe_api(warning)
        and not _contract_evidence(warning)
    )


def oracle_only_promotion(warning: dict[str, Any]) -> bool:
    reasons = set(warning.get("promotion_reasons") or [])
    return bool(reasons and reasons <= ORACLE_PROMOTION_REASONS)


def oracle_dependent_binding_only(warning: dict[str, Any]) -> bool:
    reasons = set(warning.get("promotion_reasons") or [])
    return _binding_only(warning) and bool(reasons & ORACLE_PROMOTION_REASONS)


def primary_oracle_blind_eligible(warning: dict[str, Any]) -> bool:
    tier = eligibility_tier(warning)
    return bool(
        tier in {"A", "B", "C"}
        and not generated_binding_only(warning)
        and not oracle_only_promotion(warning)
        and not oracle_dependent_binding_only(warning)
    )


def strict_top50_eligible(warning: dict[str, Any]) -> bool:
    return primary_oracle_blind_eligible(warning)


def eligibility_tier(warning: dict[str, Any]) -> str:
    c_evidence = _c_source_or_indicator(warning)
    direct = _direct_use(warning)
    safe_or_contract = _safe_api(warning) or _contract_evidence(warning)
    if c_evidence and direct and safe_or_contract:
        return "A"
    if c_evidence and direct:
        return "B"
    if _binding_only(warning) and direct and safe_or_contract:
        return "C"
    return "D"


def score_components(warning: dict[str, Any]) -> dict[str, float]:
    rust_side = _rust_side(warning)
    evidence_kinds = [
        _c_source_or_indicator(warning),
        _binding_only(warning),
        _direct_use(warning),
        _safe_api(warning),
        _has_list(rust_side.get("safety_comments")),
        _has_list(rust_side.get("error_mappings")),
        _has_list(rust_side.get("lifetime_facts")),
    ]
    diversity = sum(1 for item in evidence_kinds if item)
    warning_type = str(warning.get("type") or "")
    contract_sensitive = warning_type in {
        "NullabilityDrift",
        "ErrorDrift",
        "OwnershipRefcountDrift",
        "AllocationFreeDrift",
        "AllocationFreePairingDrift",
        "SleepabilityContextDrift",
        "SleepabilityDrift",
        "LayoutFieldDrift",
        "FieldDrift",
        "LayoutDrift",
    }
    components = {
        "c_source_diff": 2.0 if _c_source_or_indicator(warning) else 0.0,
        "binding_diff": 0.8 if _binding_only(warning) else 0.0,
        "rust_direct_use": 2.0 if _direct_use(warning) else 0.0,
        "safe_api_exposure": 2.0 if _safe_api(warning) else 0.0,
        "contract_evidence": 2.0 if _contract_evidence(warning) else 0.0,
        "contract_sensitive_type": 1.2 if contract_sensitive else 0.0,
        "multi_evidence_bonus": min(2.0, diversity * 0.35),
        "cross_version_stability": 1.0 if len(warning.get("observed_pairs") or []) > 1 else 0.0,
        "generated_binding_only_penalty": -4.0 if _binding_only(warning) and not _contract_evidence(warning) else 0.0,
        "weak_graph_only_penalty": -3.0 if eligibility_tier(warning) == "D" else 0.0,
    }
    assert_oracle_blind_components(components, context=f"oracle-blind warning {warning.get('warning_id')}")
    return components


def score_warning(warning: dict[str, Any]) -> float:
    tier_bonus = {"A": 6.0, "B": 3.0, "C": 1.0, "D": -4.0}[eligibility_tier(warning)]
    return round(tier_bonus + sum(score_components(warning).values()), 3)


def annotate_warning(warning: dict[str, Any]) -> dict[str, Any]:
    row = dict(warning)
    components = score_components(row)
    row["eligibility_tier"] = eligibility_tier(row)
    row["score_components"] = components
    row["oracle_blind"] = True
    row["generated_binding_only"] = generated_binding_only(row)
    row["strict_top50_eligible"] = strict_top50_eligible(row)
    row["oracle_only_promotion"] = oracle_only_promotion(row)
    row["oracle_dependent_binding_only"] = oracle_dependent_binding_only(row)
    row["primary_oracle_blind_eligible"] = primary_oracle_blind_eligible(row)
    row["oracle_blind_score"] = round({"A": 6.0, "B": 3.0, "C": 1.0, "D": -4.0}[row["eligibility_tier"]] + sum(components.values()), 3)
    return row


def rank_warnings_oracle_blind(warnings: list[dict[str, Any]]) -> list[dict[str, Any]]:
    ranked = [annotate_warning(warning) for warning in warnings]
    ranked.sort(
        key=lambda warning: (
            bool(warning.get("strict_top50_eligible")),
            {"A": 3, "B": 2, "C": 1, "D": 0}[warning["eligibility_tier"]],
            float(warning.get("oracle_blind_score") or 0.0),
            str(warning.get("warning_uid") or warning.get("warning_id") or ""),
        ),
        reverse=True,
    )
    for idx, warning in enumerate(ranked, start=1):
        warning["oracle_blind_rank"] = idx
    return ranked


def rank_primary_warnings_oracle_blind(warnings: list[dict[str, Any]]) -> list[dict[str, Any]]:
    ranked = [warning for warning in rank_warnings_oracle_blind(warnings) if warning.get("primary_oracle_blind_eligible") is True]
    for idx, warning in enumerate(ranked, start=1):
        warning["oracle_blind_primary_rank"] = idx
    return ranked


def oracle_blind_result_summary(warnings: list[dict[str, Any]], top_k: int = 100) -> dict[str, Any]:
    ranked = rank_primary_warnings_oracle_blind(warnings)
    top = ranked[:top_k]
    return {
        "oracle_blind": True,
        "ranker": "OracleBlindBindDrift",
        "warning_count": len(warnings),
        "primary_candidate_count": len(ranked),
        "reported_top_k": len(top),
        "top_warning_uids": [warning.get("warning_uid") for warning in top],
        "tier_distribution_top_k": _count_by(top, "eligibility_tier"),
        "score_component_keys": sorted({key for warning in top for key in (warning.get("score_components") or {})}),
    }


def _count_by(warnings: list[dict[str, Any]], key: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for warning in warnings:
        value = str(warning.get(key) or "")
        counts[value] = counts.get(value, 0) + 1
    return counts


def dump_oracle_blind_jsonl(warnings: list[dict[str, Any]], path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for warning in rank_warnings_oracle_blind(warnings):
            fh.write(json.dumps(warning, sort_keys=True) + "\n")
