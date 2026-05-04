from __future__ import annotations

from pathlib import Path

from binddrift.config import Config
from binddrift.warnings import read_warnings


CASE_TYPES = ["SignatureDrift", "LayoutDrift", "HelperDrift", "NullabilityDrift", "OwnershipRefcountDrift"]


def generate_case_studies(cfg: Config) -> dict[str, object]:
    warnings = read_warnings(cfg.warnings_jsonl)
    cases_dir = cfg.repo_root / "paper/cases"
    cases_dir.mkdir(parents=True, exist_ok=True)
    created = []
    by_type = {warning.get("type"): warning for warning in warnings}
    for idx, case_type in enumerate(CASE_TYPES, start=1):
        warning = by_type.get(case_type)
        path = cases_dir / f"case-{idx:02d}-{case_type.lower()}.md"
        path.write_text(_case_template(case_type, warning), encoding="utf-8")
        created.append(str(path))
    return {"cases": len(created), "files": created}


def _case_template(case_type: str, warning: dict | None) -> str:
    symbol = warning.get("c_side", {}).get("symbol", "TBD") if warning else "TBD"
    warning_id = warning.get("warning_id", "TBD") if warning else "TBD"
    return f"""# {case_type} Case Study

## One-Line Summary

TBD: summarize how `{symbol}` changed and why the Rust safe abstraction may need review.

## C-Side Change

TBD: describe the C API or contract evidence.

## Rust-Side Dependency

TBD: identify the binding, unsafe call site, and safe abstraction.

## Why The Compiler Cannot Fully Catch It

TBD: explain whether the issue is type-visible, layout-visible, helper-mediated, or semantic-only.

## BindDrift Warning

- Warning: `{warning_id}`
- Drift type: `{case_type}`
- C symbol: `{symbol}`

## Evidence

TBD: add C evidence, Rust evidence, and commit/build evidence.

## Impact

TBD: classify as build breakage, wrapper fix, semantic drift, benign drift, or unclear.

## Lesson

TBD: state the general cross-language drift pattern.
"""
