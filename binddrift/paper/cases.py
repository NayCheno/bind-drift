from __future__ import annotations

import csv
from pathlib import Path

from binddrift.config import Config
from binddrift.db import connect, initialize
from binddrift.evaluation.metrics import TRUE_LABELS, label_for_warning, warning_label_key, warning_key
from binddrift.warnings import eligible_for_main_warning, read_warnings


CASE_TYPES = [
    "SignatureDrift",
    "LayoutDrift",
    "HelperDrift",
    "NullabilityDrift",
    "ErrorDrift",
    "OwnershipRefcountDrift",
    "AllocationFreePairingDrift",
    "SleepabilityDrift",
]


def generate_case_studies(cfg: Config) -> dict[str, object]:
    warning_source = _case_warning_source(cfg)
    warnings = read_warnings(warning_source)
    review_source = _case_review_source(cfg, warning_source)
    labels = _load_adjudicated_labels(review_source)
    cases_dir = cfg.repo_root / "paper/cases"
    cases_dir.mkdir(parents=True, exist_ok=True)
    for stale in cases_dir.glob("case-*.md"):
        stale.unlink()
    created = []
    selected = _select_cases(warnings, labels)
    for idx, warning in enumerate(selected, start=1):
        case_type = warning.get("type", "Warning")
        symbol = warning.get("c_side", {}).get("symbol", "unknown")
        path = cases_dir / f"case-{idx:02d}-{case_type.lower()}-{symbol.lower()}.md"
        path.write_text(_case_template(case_type, warning, label_for_warning(labels, warning)), encoding="utf-8")
        created.append(str(path))
    note = "only adjudicated true positives with C and Rust evidence are used"
    return {"cases": len(created), "files": created, "warning_source": str(warning_source), "manual_review": str(review_source), "note": note}


def _case_warning_source(cfg: Config) -> Path:
    conn = connect(cfg.database)
    initialize(conn)
    for row in conn.execute("SELECT summary FROM replay_runs WHERE status IN ('completed', 'completed_with_failures') ORDER BY started_at DESC"):
        try:
            import json

            aggregate = json.loads(row["summary"] or "{}").get("aggregate_warnings")
        except json.JSONDecodeError:
            aggregate = None
        if aggregate and Path(aggregate).exists():
            return Path(aggregate)
    return cfg.warnings_jsonl


def _case_review_source(cfg: Config, warning_source: Path) -> Path:
    adjacent = warning_source.parent / "manual_review.csv"
    if adjacent.exists():
        return adjacent
    return cfg.data_dir / "manual_review.csv"


def _select_cases(warnings: list[dict], labels: dict[str, str]) -> list[dict]:
    selected: list[dict] = []
    used_ids: set[str] = set()
    for case_type in CASE_TYPES:
        for warning in warnings:
            key = warning_key(warning)
            if warning.get("type") == case_type and key not in used_ids and _case_is_valid(warning, label_for_warning(labels, warning)):
                selected.append(warning)
                used_ids.add(key)
                break
    for warning in warnings:
        if len(selected) >= 8:
            break
        key = warning_key(warning)
        if key not in used_ids and _case_is_valid(warning, label_for_warning(labels, warning)):
            selected.append(warning)
            used_ids.add(key)
    return selected[:8]


def _case_is_valid(warning: dict, label: str | None) -> bool:
    return bool(label in TRUE_LABELS and eligible_for_main_warning(warning) and _has_c_evidence(warning) and _has_rust_impact(warning))


def _load_adjudicated_labels(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    labels: dict[str, str] = {}
    with path.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            warning_id = row.get("warning_id")
            label = row.get("adjudicated_label", "").strip()
            if warning_id and label:
                labels[warning_label_key(warning_id, row.get("pair_id", "").strip() or None)] = label
    return labels


def _has_c_evidence(warning: dict) -> bool:
    c_side = warning.get("c_side", {})
    structured_diff = c_side.get("old") is not None and c_side.get("new") is not None
    return bool(
        c_side.get("evidence")
        or c_side.get("old_indicators")
        or c_side.get("new_indicators")
        or (structured_diff and warning.get("c_evidence_level") != "binding_only")
        or warning.get("c_evidence_level") in {"c_source_diff", "c_behavior_indicator", "build_oracle", "wrapper_fix"}
    )


def _has_rust_impact(warning: dict) -> bool:
    rust_side = warning.get("rust_side", {})
    has_rust_reach = bool(
        rust_side.get("uses")
        or rust_side.get("safe_apis")
        or warning.get("rust_impact_level") in {"direct_unsafe_call", "safe_api", "contract_mapping", "oracle_confirmed"}
    )
    has_contract_or_oracle = bool(
        rust_side.get("safety_comments")
        or rust_side.get("error_mappings")
        or rust_side.get("lifetime_facts")
        or rust_side.get("oracle_hits")
    )
    return has_rust_reach and has_contract_or_oracle


def _case_template(case_type: str, warning: dict, oracle_label: str | None = None) -> str:
    c_side = warning.get("c_side", {})
    rust_side = warning.get("rust_side", {})
    symbol = c_side.get("symbol", "unknown")
    warning_id = warning.get("warning_id", "unknown")
    c_evidence = _format_c_evidence(c_side)
    rust_evidence = _format_rust_evidence(rust_side)
    old_version = c_side.get("old_version")
    impact = (
        "Single-version review candidate: no historical baseline was available for this warning, "
        "so the artifact does not claim a confirmed drift bug."
        if old_version is None
        else f"Historical warning from `{old_version}` to `{c_side.get('new_version')}`."
    )
    summary = _case_summary(symbol, warning_id, rust_side)
    return f"""# {case_type} Case Study

## One-Line Summary

{summary}

## C-Side Change

BindDrift observed `{case_type}` evidence for `{symbol}`.

{c_evidence}

## Rust-Side Dependency

BindDrift attached the following Rust impact evidence.

{rust_evidence}

## Why The Compiler Cannot Fully Catch It

This case is treated as a contract-review target. The type checker can validate the current call shape, but it does not verify that Rust wrapper assumptions about nullability, error representation, ownership, or context remain synchronized with C-side behavior.

## BindDrift Warning

- Warning: `{warning_id}`
- Drift type: `{case_type}`
- C symbol: `{symbol}`
- Risk: `{warning.get("risk", "Unknown")}`
- Score: `{warning.get("score", 0)}`
- Oracle label: `{oracle_label or "UNLABELED"}`
- Replay pair: `{warning.get("pair_id") or "n/a"}`

## Evidence

The evidence above is copied from the ranked BindDrift warning report. The current artifact keeps this case within the warning/prioritization claim boundary.

## Impact

{impact}

## Lesson

Safe Rust APIs can depend on C-side contracts that are not represented in the Rust function signature. BindDrift makes that dependency explicit so maintainers can prioritize review.
"""


def _case_summary(symbol: str, warning_id: str, rust_side: dict) -> str:
    if rust_side.get("oracle_hits"):
        evidence = "oracle evidence"
    elif rust_side.get("error_mappings") or rust_side.get("lifetime_facts") or rust_side.get("safety_comments"):
        evidence = "contract evidence"
    elif rust_side.get("safe_apis"):
        evidence = "safe API exposure"
    else:
        evidence = "direct Rust binding use"
    return f"`{symbol}` produced `{warning_id}` with adjudicated true-positive {evidence}."


def _format_c_evidence(c_side: dict) -> str:
    evidence = c_side.get("evidence") or []
    lines = [f"- Old indicators/value: `{c_side.get('old', c_side.get('old_indicators', []))}`", f"- New indicators/value: `{c_side.get('new', c_side.get('new_indicators', []))}`"]
    for item in evidence[:5]:
        if isinstance(item, dict):
            lines.append(f"- `{item.get('evidence_file')}:{item.get('evidence_line')}`: `{item.get('evidence_text', '')}`")
    return "\n".join(lines)


def _format_rust_evidence(rust_side: dict) -> str:
    lines: list[str] = []
    for use in (rust_side.get("uses") or [])[:5]:
        if isinstance(use, dict):
            lines.append(f"- `{use.get('rust_file')}:{use.get('line')}` in `{use.get('enclosing_function')}`")
    for item in (rust_side.get("safety_comments") or [])[:3]:
        if isinstance(item, dict):
            lines.append(f"- `{item.get('rust_file')}:{item.get('line')}`: `{item.get('text', '')}`")
    for item in (rust_side.get("error_mappings") or [])[:3]:
        if isinstance(item, dict):
            lines.append(f"- `{item.get('rust_file')}:{item.get('line')}` error mapping `{item.get('mapping_type')}`")
    for item in (rust_side.get("lifetime_facts") or [])[:3]:
        if isinstance(item, dict):
            lines.append(f"- `{item.get('rust_file')}:{item.get('line')}` lifetime fact `{item.get('fact_type')}`")
    for item in (rust_side.get("safe_apis") or [])[:3]:
        if isinstance(item, dict):
            lines.append(f"- safe API `{item.get('api_name')}`")
    for item in (rust_side.get("oracle_hits") or [])[:3]:
        if isinstance(item, dict):
            lines.append(f"- {item.get('oracle_type')}: `{item.get('symbol', item.get('commit_id', 'oracle'))}`")
    return "\n".join(lines) if lines else "- No Rust-side evidence was attached to this warning."
