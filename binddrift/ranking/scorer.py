from __future__ import annotations

import json
from typing import Any

from binddrift.config import Config
from binddrift.warnings import read_warnings, write_warnings


SEVERITY = {
    "SignatureDrift": 3.0,
    "LayoutDrift": 3.0,
    "FieldDrift": 2.0,
    "MacroConstDrift": 2.0,
    "HelperDrift": 3.0,
    "NullabilityDrift": 3.0,
    "ErrorDrift": 2.0,
    "OwnershipRefcountDrift": 3.0,
    "AllocationFreePairingDrift": 3.0,
    "SleepabilityDrift": 2.0,
}

CONTRACT_TYPES = {
    "NullabilityDrift",
    "ErrorDrift",
    "OwnershipRefcountDrift",
    "AllocationFreePairingDrift",
    "SleepabilityDrift",
}


def _rust_exposure(warning: dict[str, Any]) -> float:
    rust_side = warning.get("rust_side", {})
    uses = rust_side.get("uses") or []
    exposure = rust_side.get("exposure") or {}
    edge_count = exposure.get("edge_count", 0) if isinstance(exposure, dict) else 0
    if uses:
        return min(3.0, 1.0 + len(uses) / 4)
    if edge_count:
        return min(3.0, 1.0 + edge_count / 10)
    return 0.5


def score_warning(warning: dict[str, Any]) -> float:
    drift_type = warning.get("type", "")
    severity = SEVERITY.get(drift_type, 1.0)
    exposure = _rust_exposure(warning)
    rust_side = warning.get("rust_side", {})
    uses = rust_side.get("uses") or []
    unsafe = 1.0 if any(use.get("enclosing_unsafe_block") for use in uses if isinstance(use, dict)) else 0.5
    contract = 1.0 if drift_type in CONTRACT_TYPES else 0.0
    helper = 1.0 if "Helper" in drift_type or "helper" in json.dumps(warning).lower() else 0.0
    historical = float(warning.get("confidence", 0.5))
    build = 1.0 if drift_type in {"SignatureDrift", "LayoutDrift", "FieldDrift"} else 0.0
    evidence = min(1.0, len(warning.get("evidence_chain") or []) / 5)
    return round(
        2.0 * severity
        + 2.0 * exposure
        + 1.5 * unsafe
        + 1.5 * contract
        + 1.0 * helper
        + 1.0 * historical
        + 1.0 * build
        + evidence,
        3,
    )


def rank_warnings(cfg: Config) -> dict[str, Any]:
    warnings = read_warnings(cfg.warnings_jsonl)
    for warning in warnings:
        warning.setdefault("evidence_chain", [])
        warning["score"] = score_warning(warning)
        if warning.get("score", 0) >= 10:
            warning["risk"] = "High"
        elif warning.get("score", 0) >= 7:
            warning["risk"] = "Medium"
        else:
            warning["risk"] = warning.get("risk", "Low")
    warnings.sort(key=lambda item: item.get("score", 0), reverse=True)
    write_warnings(cfg, warnings)
    cfg.report_md.write_text(_markdown(warnings), encoding="utf-8")
    return {"warnings": len(warnings), "warning_file": str(cfg.warnings_jsonl), "report": str(cfg.report_md)}


def _markdown(warnings: list[dict[str, Any]]) -> str:
    lines = ["# BindDrift Ranked Warnings", ""]
    if not warnings:
        lines.append("No warnings were generated for the current pilot inputs.")
        lines.append("")
        return "\n".join(lines)
    for warning in warnings:
        lines.extend(
            [
                f"## {warning['warning_id']} {warning.get('type', 'Warning')}",
                "",
                f"- Risk: {warning.get('risk', 'Unknown')}",
                f"- Score: {warning.get('score', 0)}",
                f"- Symbol: {warning.get('c_side', {}).get('symbol', 'unknown')}",
                f"- Explanation: {warning.get('explanation', '')}",
                f"- Suggested action: {warning.get('suggested_action', '')}",
                "",
                "### C Evidence",
                "",
                _format_c_side(warning),
                "",
                "### Rust Evidence",
                "",
                _format_rust_side(warning),
                "",
            ]
        )
    return "\n".join(lines)


def _format_c_side(warning: dict[str, Any]) -> str:
    c_side = warning.get("c_side", {})
    evidence = c_side.get("evidence") or []
    lines = [
        f"- Old: `{c_side.get('old', c_side.get('old_indicators', 'n/a'))}`",
        f"- New: `{c_side.get('new', c_side.get('new_indicators', 'n/a'))}`",
    ]
    for item in evidence[:5]:
        if isinstance(item, dict):
            lines.append(f"- {item.get('evidence_file')}:{item.get('evidence_line')} `{item.get('evidence_text', '')}`")
    return "\n".join(lines)


def _format_rust_side(warning: dict[str, Any]) -> str:
    rust_side = warning.get("rust_side", {})
    uses = rust_side.get("uses") or []
    exposure = rust_side.get("exposure") or {}
    lines: list[str] = []
    if isinstance(exposure, dict) and exposure.get("edge_count") is not None:
        lines.append(f"- Graph edges: `{exposure.get('edge_count')}`")
    for use in uses[:5]:
        if isinstance(use, dict):
            lines.append(
                f"- {use.get('rust_file')}:{use.get('line')} `{use.get('enclosing_function')}` "
                f"unsafe={use.get('enclosing_unsafe_block')}"
            )
    for item in (rust_side.get("safety_comments") or [])[:3]:
        if isinstance(item, dict):
            lines.append(f"- {item.get('rust_file')}:{item.get('line')} `{item.get('text', '')}`")
    for item in (rust_side.get("lifetime_facts") or [])[:3]:
        if isinstance(item, dict):
            lines.append(f"- {item.get('rust_file')}:{item.get('line')} `{item.get('fact_type')}`")
    return "\n".join(lines) if lines else "- No Rust exposure evidence recorded."
