from __future__ import annotations

from pathlib import Path

from binddrift.config import Config
from binddrift.db import connect, initialize
from binddrift.evaluation.metrics import load_manual_labels
from binddrift.warnings import read_warnings


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
    labels = load_manual_labels(cfg.data_dir / "manual_review.csv")
    cases_dir = cfg.repo_root / "paper/cases"
    cases_dir.mkdir(parents=True, exist_ok=True)
    created = []
    selected = _select_cases(warnings)
    for idx, warning in enumerate(selected, start=1):
        case_type = warning.get("type", "Warning")
        symbol = warning.get("c_side", {}).get("symbol", "unknown")
        path = cases_dir / f"case-{idx:02d}-{case_type.lower()}-{symbol.lower()}.md"
        path.write_text(_case_template(case_type, warning, labels.get(str(warning.get("warning_id")))), encoding="utf-8")
        created.append(str(path))
    return {"cases": len(created), "files": created, "warning_source": str(warning_source)}


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


def _select_cases(warnings: list[dict]) -> list[dict]:
    selected: list[dict] = []
    used_ids: set[str] = set()
    for case_type in CASE_TYPES:
        for warning in warnings:
            if warning.get("type") == case_type and warning.get("warning_id") not in used_ids:
                selected.append(warning)
                used_ids.add(warning["warning_id"])
                break
    for warning in warnings:
        if len(selected) >= 8:
            break
        if warning.get("warning_id") not in used_ids:
            selected.append(warning)
            used_ids.add(warning["warning_id"])
    return selected[:8]


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
    return f"""# {case_type} Case Study

## One-Line Summary

`{symbol}` produced `{warning_id}` because C-side contract evidence reaches Rust-for-Linux wrapper code.

## C-Side Change

BindDrift observed `{case_type}` evidence for `{symbol}`.

{c_evidence}

## Rust-Side Dependency

The symbol is used through Rust binding calls or nearby wrapper code.

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
    for item in (rust_side.get("lifetime_facts") or [])[:3]:
        if isinstance(item, dict):
            lines.append(f"- `{item.get('rust_file')}:{item.get('line')}` lifetime fact `{item.get('fact_type')}`")
    return "\n".join(lines) if lines else "- No Rust-side evidence was attached to this warning."
