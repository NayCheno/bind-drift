from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from typing import Any

from binddrift.config import Config
from binddrift.db import connect, initialize, upsert_many
from binddrift.gitutil import git_output
from binddrift.warnings import read_warnings
from .baselines import generate_baselines
from .metrics import labeled_summary, load_manual_labels, manual_review_agreement, oracle_summary


BUILD_ERROR_RE = re.compile(r"(bindings::(?P<binding>[A-Za-z_][A-Za-z0-9_]*)|missing field|mismatched types|layout)")


def parse_build_log(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    findings = []
    for idx, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), start=1):
        if match := BUILD_ERROR_RE.search(line):
            findings.append({"line": idx, "symbol": match.groupdict().get("binding"), "text": line[:1000]})
    return findings


def mine_wrapper_fixes(cfg: Config, limit: int = 200) -> list[dict[str, Any]]:
    rows = []
    log = git_output(cfg.linux_tree, ["log", f"--max-count={limit}", "--format=%H%x1f%aI%x1f%s", "--", "rust/kernel", "rust/helpers", "rust/bindings"])
    for raw in log.splitlines():
        parts = raw.split("\x1f")
        if len(parts) != 3:
            continue
        commit, date, subject = parts
        lowered = subject.lower()
        likely = any(word in lowered for word in ("fix", "api", "binding", "wrapper", "error", "refcount", "null"))
        changed_files = git_output(cfg.linux_tree, ["show", "--name-only", "--format=", commit]).splitlines()
        diff = git_output(cfg.linux_tree, ["show", "--format=", "--unified=0", commit, "--", "rust/kernel", "rust/helpers", "rust/bindings"])
        matched_symbols = sorted(set(re.findall(r"bindings::([A-Za-z_][A-Za-z0-9_]*)|rust_helper_([A-Za-z_][A-Za-z0-9_]*)", diff)))
        flattened_symbols = sorted({item for pair in matched_symbols for item in pair if item})
        rows.append(
            {
                "commit": commit,
                "date": date,
                "subject": subject,
                "changed_files": changed_files,
                "matched_symbols": flattened_symbols,
                "likely_wrapper_fix": likely,
            }
        )
    return rows


def persist_ground_truth(
    cfg: Config,
    build_log: Path | None,
    build_findings: list[dict[str, Any]],
    wrapper_fixes: list[dict[str, Any]],
    run_id: str | None = None,
    pair_id: str | None = None,
) -> dict[str, int]:
    conn = connect(cfg.database)
    initialize(conn)
    if build_log:
        upsert_many(
            conn,
            "build_breakage_events",
            [
                {
                    "event_id": f"{build_log}:{item['line']}",
                    "run_id": run_id,
                    "pair_id": pair_id,
                    "build_log": str(build_log),
                    "line": item["line"],
                    "symbol": item.get("symbol"),
                    "text": item["text"],
                }
                for item in build_findings
            ],
        )
    upsert_many(
        conn,
        "wrapper_fix_events",
        [
            {
                "commit_id": item["commit"],
                "date": item["date"],
                "subject": item["subject"],
                "changed_files": json.dumps(item["changed_files"], sort_keys=True),
                "likely_wrapper_fix": int(item["likely_wrapper_fix"]),
                "matched_symbols": json.dumps(item["matched_symbols"], sort_keys=True),
            }
            for item in wrapper_fixes
        ],
    )
    return {"build_breakage_events": len(build_findings), "wrapper_fix_events": len(wrapper_fixes)}


def generate_manual_review(cfg: Config, warnings: list[dict[str, Any]], top_k: int = 100) -> Path:
    path = cfg.data_dir / "manual_review.csv"
    cfg.data_dir.mkdir(parents=True, exist_ok=True)
    existing: dict[str, dict[str, str]] = {}
    if path.exists():
        with path.open(newline="", encoding="utf-8") as fh:
            existing = {row["warning_id"]: row for row in csv.DictReader(fh) if row.get("warning_id")}
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "warning_id",
                "type",
                "risk",
                "score",
                "symbol",
                "reviewer1_label",
                "reviewer1_notes",
                "reviewer2_label",
                "reviewer2_notes",
                "adjudicated_label",
                "adjudication_notes",
                "label",
                "reviewer_notes",
            ],
        )
        writer.writeheader()
        selected = _manual_review_sample(warnings, top_k=top_k)
        for warning in selected:
            prior = existing.get(str(warning.get("warning_id")), {})
            writer.writerow(
                {
                    "warning_id": warning.get("warning_id"),
                    "type": warning.get("type"),
                    "risk": warning.get("risk"),
                    "score": warning.get("score"),
                    "symbol": warning.get("c_side", {}).get("symbol"),
                    "reviewer1_label": prior.get("reviewer1_label", ""),
                    "reviewer1_notes": prior.get("reviewer1_notes", ""),
                    "reviewer2_label": prior.get("reviewer2_label", ""),
                    "reviewer2_notes": prior.get("reviewer2_notes", ""),
                    "adjudicated_label": prior.get("adjudicated_label", ""),
                    "adjudication_notes": prior.get("adjudication_notes", ""),
                    "label": prior.get("label", ""),
                    "reviewer_notes": prior.get("reviewer_notes", ""),
                }
            )
    return path


def _manual_review_sample(warnings: list[dict[str, Any]], top_k: int = 100, stratified_k: int = 100) -> list[dict[str, Any]]:
    selected: list[dict[str, Any]] = []
    used: set[str] = set()
    for warning in warnings[:top_k]:
        warning_id = str(warning.get("warning_id"))
        if warning_id not in used:
            selected.append(warning)
            used.add(warning_id)
    types = sorted({str(warning.get("type")) for warning in warnings})
    per_type = max(1, stratified_k // len(types)) if types else 0
    for drift_type in types:
        for warning in warnings:
            if warning.get("type") != drift_type:
                continue
            warning_id = str(warning.get("warning_id"))
            if warning_id in used:
                continue
            selected.append(warning)
            used.add(warning_id)
            if len(selected) >= top_k + stratified_k:
                return selected
            if sum(1 for row in selected[top_k:] if row.get("type") == drift_type) >= per_type:
                break
    return selected


def _build_symbols(build_findings: list[dict[str, Any]]) -> set[str]:
    return {str(item["symbol"]) for item in build_findings if item.get("symbol")}


def _wrapper_symbols(wrapper_fixes: list[dict[str, Any]]) -> set[str]:
    symbols: set[str] = set()
    for item in wrapper_fixes:
        if not item.get("likely_wrapper_fix"):
            continue
        symbols.update(str(symbol) for symbol in item.get("matched_symbols", []) if symbol)
    return symbols


def run_evaluation(
    cfg: Config,
    build_log: Path | None = None,
    top_k: int = 100,
    run_id: str | None = None,
    pair_id: str | None = None,
) -> dict[str, Any]:
    cfg.ensure_dirs()
    warnings = read_warnings(cfg.warnings_jsonl)
    build_findings = parse_build_log(build_log) if build_log else []
    wrapper_fixes = mine_wrapper_fixes(cfg)
    persisted = persist_ground_truth(cfg, build_log, build_findings, wrapper_fixes, run_id=run_id, pair_id=pair_id)
    review_path = generate_manual_review(cfg, warnings, top_k=top_k)
    labels = load_manual_labels(review_path)
    metrics = labeled_summary(warnings, labels)
    agreement = manual_review_agreement(review_path)
    build_metrics = oracle_summary(warnings, _build_symbols(build_findings))
    wrapper_metrics = oracle_summary(warnings, _wrapper_symbols(wrapper_fixes))
    table = {
        "warnings": len(warnings),
        "build_breakage_findings": len(build_findings),
        "wrapper_fix_candidates": sum(1 for row in wrapper_fixes if row["likely_wrapper_fix"]),
        "ground_truth_rows": persisted,
        "manual_review": metrics,
        "manual_review_agreement": agreement,
        "build_breakage_prediction": build_metrics,
        "wrapper_fix_prediction": wrapper_metrics,
        "recall": {
            "build_breakage": build_metrics["recall"],
            "wrapper_fix": wrapper_metrics["recall"],
        },
        "note": "Build and wrapper-fix recall are symbol-level replay-oracle estimates; semantic precision comes from manual labels.",
    }
    tables_dir = cfg.repo_root / "paper/tables"
    tables_dir.mkdir(parents=True, exist_ok=True)
    (tables_dir / "evaluation_summary.json").write_text(json.dumps(table, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    baselines = generate_baselines(cfg)
    return {
        "summary": table,
        "baselines": baselines,
        "manual_review": str(review_path),
        "evaluation_table": str(tables_dir / "evaluation_summary.json"),
    }
