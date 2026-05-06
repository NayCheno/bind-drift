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


def _detection_time_drift_evidence(warning: dict[str, Any]) -> bool:
    return bool(_c_source_or_indicator(warning) or _binding_only(warning) or warning.get("fact_source") == "layout_diff")


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


def _error_mapping(warning: dict[str, Any]) -> bool:
    rust_side = _rust_side(warning)
    return _has_list(rust_side.get("error_mappings")) or "has_error_mapping" in set(warning.get("promotion_reasons") or [])


def _lifetime_or_ownership(warning: dict[str, Any]) -> bool:
    rust_side = _rust_side(warning)
    return _has_list(rust_side.get("lifetime_facts")) or "has_lifetime_fact" in set(warning.get("promotion_reasons") or [])


def _safety_comment(warning: dict[str, Any]) -> bool:
    rust_side = _rust_side(warning)
    return _has_list(rust_side.get("safety_comments")) or "has_safety_comment" in set(warning.get("promotion_reasons") or [])


def _contract_symbol_indicator(warning: dict[str, Any]) -> bool:
    symbol = str((warning.get("c_side") or {}).get("symbol") or "").lower()
    tokens = (
        "err",
        "null",
        "secctx",
        "refcount",
        "kref",
        "request",
        "firmware",
        "release",
        "free",
        "alloc",
        "fsleep",
        "sleep",
        "mutex",
        "lock",
        "compat_ptr_ioctl",
        "dma_resv",
    )
    return any(token in symbol for token in tokens)


def _rust_wrapper_surface_indicator(warning: dict[str, Any]) -> bool:
    symbol = str((warning.get("c_side") or {}).get("symbol") or "").lower()
    warning_type = str(warning.get("type") or "")
    direct_symbols = {
        "errname",
        "__mutex_init",
        "compat_ptr_ioctl",
        "fsleep",
        "dma_resv_lock",
    }
    if symbol in direct_symbols:
        return True
    return bool(warning_type == "FieldDrift" and symbol in {"request", "firmware", "device"})


def _macro_like_binding_surface(warning: dict[str, Any]) -> bool:
    symbol = str((warning.get("c_side") or {}).get("symbol") or "")
    return bool(
        _binding_only(warning)
        and (
            symbol.isupper()
            or symbol in {"PTR_ERR", "IS_ERR", "ERR_PTR", "REFCOUNT_INIT"}
        )
    )


def _ambiguous_binding_contract_surface(warning: dict[str, Any]) -> bool:
    symbol = str((warning.get("c_side") or {}).get("symbol") or "").lower()
    return bool(
        _binding_only(warning)
        and (
            symbol.startswith("gpu_buddy")
            or symbol.startswith("refcount")
            or symbol in {"errno_to_blk_status", "device_add_disk"}
        )
    )


def _non_oracle_rust_evidence(warning: dict[str, Any]) -> bool:
    return bool(_direct_use(warning) or _safe_api(warning) or _contract_evidence(warning) or _safety_comment(warning))


def _count_rust_items(warning: dict[str, Any], key: str) -> int:
    value = _rust_side(warning).get(key)
    return len(value) if isinstance(value, list) else 0


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
    return bool(
        reasons
        and reasons <= ORACLE_PROMOTION_REASONS
        and not _detection_time_drift_evidence(warning)
        and not _non_oracle_rust_evidence(warning)
    )


def oracle_dependent_binding_only(warning: dict[str, Any]) -> bool:
    reasons = set(warning.get("promotion_reasons") or [])
    return bool(
        _binding_only(warning)
        and reasons
        and reasons <= ORACLE_PROMOTION_REASONS
        and not _detection_time_drift_evidence(warning)
        and not _non_oracle_rust_evidence(warning)
    )


def primary_oracle_blind_eligible(warning: dict[str, Any]) -> bool:
    return bool(_detection_time_drift_evidence(warning) and not oracle_only_promotion(warning))


def strict_top50_eligible(warning: dict[str, Any]) -> bool:
    return bool(primary_oracle_blind_eligible(warning) and not generated_binding_only(warning) and _non_oracle_rust_evidence(warning))


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
    evidence_kinds = [
        _c_source_or_indicator(warning),
        _binding_only(warning),
        _direct_use(warning),
        _safe_api(warning),
        _safety_comment(warning),
        _error_mapping(warning),
        _lifetime_or_ownership(warning),
    ]
    diversity = sum(1 for item in evidence_kinds if item)
    warning_type = str(warning.get("type") or "")
    fact_source = str(warning.get("fact_source") or "")
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
    direct = _direct_use(warning)
    safe = _safe_api(warning)
    safety = _safety_comment(warning)
    error = _error_mapping(warning)
    lifetime = _lifetime_or_ownership(warning)
    binding = _binding_only(warning)
    c_source = _c_source_or_indicator(warning)
    field_layout = warning_type == "FieldDrift" and fact_source == "layout_diff"
    signature = warning_type == "SignatureDrift"
    macro_const = warning_type == "MacroConstDrift"
    weak_graph = not _non_oracle_rust_evidence(warning)
    contract_symbol = _contract_symbol_indicator(warning)
    rust_wrapper_surface = _rust_wrapper_surface_indicator(warning)
    added_without_old_c_evidence = "added_symbol_without_old_c_evidence" in set(warning.get("demotion_reasons") or [])
    rust_use_count = min(_count_rust_items(warning, "uses"), 5)
    safety_comment_count = min(_count_rust_items(warning, "safety_comments"), 5)
    safe_api_count = min(_count_rust_items(warning, "safe_apis"), 3)
    components = {
        "c_source_diff_strength": 20.0 if c_source else 0.0,
        "binding_diff_strength": 0.0 if binding else 0.0,
        "rust_direct_use": 4.0 if direct else 0.0,
        "safe_api_exposure": 4.0 if safe else 0.0,
        "safety_comment_proximity": 5.0 if safety else 0.0,
        "error_mapping_evidence": 4.0 if error else 0.0,
        "lifetime_ownership_evidence": 3.0 if lifetime else 0.0,
        "contract_sensitive_type": 2.0 if contract_sensitive else 0.0,
        "signature_contract_surface": 0.5 if signature else 0.0,
        "field_layout_contract_surface": 0.0 if field_layout else 0.0,
        "layout_safe_field_evidence": 0.0,
        "direct_c_contract_chain": 5.0 if c_source and direct and (safe or _contract_evidence(warning)) else 0.0,
        "direct_c_error_chain": 3.0 if c_source and error else 0.0,
        "direct_c_lifetime_chain": 3.0 if c_source and lifetime else 0.0,
        "contract_symbol_indicator": 12.0 if contract_symbol else 0.0,
        "rust_wrapper_surface_indicator": 12.0 if rust_wrapper_surface else 0.0,
        "evidence_diversity": min(2.0, diversity * 0.35),
        "rust_use_density": round(rust_use_count * 0.15 + safety_comment_count * 0.10 + safe_api_count * 0.15, 3),
        "cross_version_stability": 1.0 if len(warning.get("observed_pairs") or []) > 1 else 0.0,
        "binding_only_surface_penalty": -12.0 if binding and not c_source else 0.0,
        "macro_like_binding_surface_penalty": -10.0 if _macro_like_binding_surface(warning) else 0.0,
        "ambiguous_binding_contract_surface_penalty": -4.0 if _ambiguous_binding_contract_surface(warning) else 0.0,
        "added_symbol_without_old_c_evidence_penalty": -5.0 if added_without_old_c_evidence else 0.0,
        "macro_constant_penalty": -6.0 if macro_const and not c_source else 0.0,
        "weak_graph_only_penalty": -10.0 if weak_graph else 0.0,
        "binding_layout_surface_penalty": -8.0 if field_layout and binding and not safe else 0.0,
        "layout_lifetime_ambiguity_penalty": -12.0 if field_layout and lifetime and not safe else 0.0,
    }
    assert_oracle_blind_components(components, context=f"oracle-blind warning {warning.get('warning_id')}")
    return components


def score_warning(warning: dict[str, Any]) -> float:
    return round(sum(score_components(warning).values()), 3)


def score_explanation(components: dict[str, float]) -> list[str]:
    ranked = sorted(
        ((key, value) for key, value in components.items() if value),
        key=lambda item: (-abs(float(item[1])), item[0]),
    )
    return [f"{key}={value:g}" for key, value in ranked[:5]]


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
    row["oracle_blind_score"] = round(sum(components.values()), 3)
    row["score_explanation"] = score_explanation(components)
    return row


def rank_warnings_oracle_blind(warnings: list[dict[str, Any]]) -> list[dict[str, Any]]:
    ranked = [annotate_warning(warning) for warning in warnings]
    ranked.sort(
        key=lambda warning: (
            bool(warning.get("strict_top50_eligible")),
            float(warning.get("oracle_blind_score") or 0.0),
            {"A": 3, "B": 2, "C": 1, "D": 0}[warning["eligibility_tier"]],
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
