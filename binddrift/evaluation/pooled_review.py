from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

from binddrift.config import Config
from binddrift.artifact_paths import sanitize_local_paths
from binddrift.evaluation.baselines import _candidate_pool, _refresh_pool_scores, _variant_warnings
from binddrift.evaluation.metrics import label_for_warning, load_manual_labels, manual_review_row_key
from binddrift.evaluation.wrapper_oracle import replay_head_date, version_dates_from_db
from binddrift.db import connect, initialize
from binddrift.ranking.oracle_blind_scorer import rank_primary_warnings_oracle_blind
from binddrift.run_manifest import canonical_run_dir, repo_relative, validate_run_manifest
from binddrift.warnings import ensure_warning_uid, read_warnings, write_jsonl


DEFAULT_RANKERS = [
    "binddrift_oracle_blind",
    "binddrift_current",
    "binding_diff",
    "c_signature",
    "c_indicator",
    "rust_use",
    "no_graph",
    "no_impact_gate",
    "no_ranking",
    "random",
]

RANKER_TO_BASELINE = {
    "binding_diff": "BindingDiffOnly",
    "c_signature": "CSignatureDiffOnly",
    "c_indicator": "CIndicatorOnly",
    "rust_use": "RustUseOnly",
    "no_graph": "NoGraph",
    "no_impact_gate": "NoImpactGate",
    "no_ranking": "NoRanking",
    "random": "Random",
}

LABEL_FIELDS = [
    "warning_uid",
    "warning_id",
    "pair_id",
    "ranker_source",
    "type",
    "symbol",
    "reviewer1_label",
    "reviewer1_notes",
    "reviewer2_label",
    "reviewer2_notes",
    "adjudicated_label",
    "adjudication_notes",
    "label_source",
]


def generate_pooled_review_set(
    cfg: Config,
    *,
    run_id: str = "latest",
    rankers: list[str] | None = None,
    output: Path | None = None,
    labels_output: Path | None = None,
) -> dict[str, Any]:
    manifest = validate_run_manifest(cfg)
    run_dir = canonical_run_dir(cfg, run_id)
    output = output or run_dir / "pooled_review_set.jsonl"
    labels_output = labels_output or run_dir / "pooled_review_labels.csv"
    rankers = rankers or DEFAULT_RANKERS
    warnings = read_warnings(Path(manifest["resolved_paths"]["warnings"]))
    promoted = read_warnings(Path(manifest["resolved_paths"]["promoted_warnings"]))
    ranked_by_source = ranker_outputs(cfg, warnings, promoted, rankers, run_manifest=str(run_dir / "run_manifest.json"))

    by_uid: dict[str, dict[str, Any]] = {}
    source_ranks: dict[str, dict[str, int]] = defaultdict(dict)
    for source, ranked in ranked_by_source.items():
        for rank, warning in enumerate(ranked[:100], start=1):
            uid = ensure_warning_uid(warning)
            by_uid.setdefault(uid, dict(warning))
            source_ranks[uid][source] = rank

    for warning in _stratified_by_type(promoted, 120) + _stratified_by_pair(promoted, 80):
        uid = ensure_warning_uid(warning)
        by_uid.setdefault(uid, dict(warning))

    rows = _compress_pool(by_uid, source_ranks)
    for row in rows:
        uid = ensure_warning_uid(row)
        row["ranker_sources"] = sorted(source_ranks.get(uid, {}))
        row["ranker_ranks"] = source_ranks.get(uid, {})
        row["pooled_review"] = True
    rows = [sanitize_local_paths(row, cfg) for row in rows]

    write_jsonl(output, rows)
    label_summary = write_pooled_review_labels(
        pool_rows=rows,
        manual_review=Path(manifest["resolved_paths"]["manual_review"]),
        output=labels_output,
    )
    manifest_path = run_dir / "pooled_review_manifest.json"
    manifest_data = {
        "run_id": run_id,
        "pool_rows": len(rows),
        "rankers": rankers,
        "ranker_top100_union": len(by_uid),
        "labels": label_summary,
        "pool": repo_relative(cfg, output),
        "label_file": repo_relative(cfg, labels_output),
        "selection_policy": "ranker_top100_union_plus_type_and_pair_stratified_samples",
    }
    manifest_path.write_text(json.dumps(manifest_data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return {**manifest_data, "pool": str(output), "label_file": str(labels_output), "manifest": str(manifest_path)}


def ranker_outputs(
    cfg: Config,
    warnings: list[dict[str, Any]],
    promoted: list[dict[str, Any]],
    rankers: list[str],
    *,
    run_manifest: str | None = None,
) -> dict[str, list[dict[str, Any]]]:
    return {
        name: details["ranked"]
        for name, details in ranker_output_details(
            cfg,
            warnings,
            promoted,
            rankers,
            run_manifest=run_manifest,
        ).items()
    }


def ranker_output_details(
    cfg: Config,
    warnings: list[dict[str, Any]],
    promoted: list[dict[str, Any]],
    rankers: list[str],
    *,
    run_manifest: str | None = None,
) -> dict[str, dict[str, Any]]:
    conn = connect(cfg.database)
    initialize(conn)
    version_dates = version_dates_from_db(conn)
    head_date = replay_head_date(promoted, version_dates)
    pool = _refresh_pool_scores(_candidate_pool(cfg, warnings, run_manifest), warnings, version_dates, head_date)
    out: dict[str, dict[str, Any]] = {}
    for name in rankers:
        if name == "binddrift_oracle_blind":
            ranked = rank_primary_warnings_oracle_blind(pool)
            out[name] = {"ranked": ranked, "candidate_count": len(ranked), "warning_volume": len(pool)}
        elif name == "binddrift_current":
            out[name] = {
                "ranked": sorted(pool, key=lambda warning: (float(warning.get("score") or 0.0), str(warning.get("warning_uid"))), reverse=True),
                "candidate_count": len(pool),
                "warning_volume": len(pool),
            }
        else:
            baseline = RANKER_TO_BASELINE.get(name)
            if not baseline:
                raise ValueError(f"unknown ranker: {name}")
            candidates, _count = _variant_warnings(baseline, warnings, pool)
            out[name] = {"ranked": candidates, "candidate_count": _count, "warning_volume": _count}
    return out


def write_pooled_review_labels(pool_rows: list[dict[str, Any]], manual_review: Path, output: Path) -> dict[str, Any]:
    manual_rows = _manual_rows_by_key(manual_review)
    labels = load_manual_labels(manual_review, uid_only=True)
    existing_rows = _manual_rows_by_key(output) if output.exists() else {}
    output.parent.mkdir(parents=True, exist_ok=True)
    labeled = 0
    with output.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=LABEL_FIELDS, lineterminator="\n")
        writer.writeheader()
        for warning in pool_rows:
            uid = ensure_warning_uid(warning)
            manual_label = label_for_warning(labels, warning)
            if manual_label:
                source = manual_rows.get(uid, {})
                label = manual_label
                label_source = "manual_review.csv"
            else:
                source = existing_rows.get(uid, {})
                label = source.get("adjudicated_label", "").strip()
                label_source = source.get("label_source", "")
            if label:
                labeled += 1
            writer.writerow(
                {
                    "warning_uid": uid,
                    "warning_id": warning.get("warning_id", ""),
                    "pair_id": warning.get("pair_id", ""),
                    "ranker_source": ",".join(warning.get("ranker_sources") or []),
                    "type": warning.get("type", ""),
                    "symbol": (warning.get("c_side") or {}).get("symbol", ""),
                    "reviewer1_label": source.get("reviewer1_label", ""),
                    "reviewer1_notes": source.get("reviewer1_notes", ""),
                    "reviewer2_label": source.get("reviewer2_label", ""),
                    "reviewer2_notes": source.get("reviewer2_notes", ""),
                    "adjudicated_label": source.get("adjudicated_label", ""),
                    "adjudication_notes": source.get("adjudication_notes", ""),
                    "label_source": label_source if label else "",
                }
            )
    coverage = round(labeled / len(pool_rows), 4) if pool_rows else 0.0
    return {"label_rows": len(pool_rows), "labeled_rows": labeled, "coverage": coverage}


def _manual_rows_by_key(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    rows: dict[str, dict[str, str]] = {}
    with path.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            key = manual_review_row_key(row, uid_only=True)
            if key:
                rows[key] = dict(row)
    return rows


def _stratified_by_type(warnings: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    by_type: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for warning in sorted(warnings, key=lambda item: str(item.get("warning_uid"))):
        by_type[str(warning.get("type"))].append(warning)
    per_type = max(1, limit // max(1, len(by_type)))
    rows: list[dict[str, Any]] = []
    for items in by_type.values():
        rows.extend(items[:per_type])
    return rows[:limit]


def _stratified_by_pair(warnings: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    by_pair: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for warning in sorted(warnings, key=lambda item: str(item.get("warning_uid"))):
        by_pair[str(warning.get("pair_id"))].append(warning)
    per_pair = max(1, limit // max(1, len(by_pair)))
    rows: list[dict[str, Any]] = []
    for items in by_pair.values():
        rows.extend(items[:per_pair])
    return rows[:limit]


def _compress_pool(by_uid: dict[str, dict[str, Any]], source_ranks: dict[str, dict[str, int]]) -> list[dict[str, Any]]:
    rows = list(by_uid.values())
    if len(rows) <= 500:
        return sorted(rows, key=lambda warning: str(warning.get("warning_uid")))
    keep: dict[str, dict[str, Any]] = {}
    for uid, ranks in source_ranks.items():
        if any(rank <= 20 for rank in ranks.values()):
            keep[uid] = by_uid[uid]
    for uid, warning in by_uid.items():
        rust_side = warning.get("rust_side") or {}
        if warning.get("type") != "SignatureDrift" or rust_side.get("safe_apis"):
            keep[uid] = warning
    counts: dict[str, int] = defaultdict(int)
    for warning in keep.values():
        counts[str(warning.get("type"))] += 1
    for warning in sorted(rows, key=lambda item: str(item.get("warning_uid"))):
        drift_type = str(warning.get("type"))
        if counts[drift_type] < 30:
            uid = ensure_warning_uid(warning)
            keep[uid] = warning
            counts[drift_type] += 1
    for warning in sorted(rows, key=lambda item: str(item.get("warning_uid"))):
        if len(keep) >= 500:
            break
        keep.setdefault(ensure_warning_uid(warning), warning)
    return sorted(keep.values(), key=lambda warning: str(warning.get("warning_uid")))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a locked BindDrift pooled review set.")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--run", default="latest")
    parser.add_argument("--rankers", default=",".join(DEFAULT_RANKERS))
    parser.add_argument("--output")
    args = parser.parse_args(argv)
    cfg = Config.from_args(repo_root=args.repo_root)
    output = Path(args.output).resolve() if args.output else None
    result = generate_pooled_review_set(
        cfg,
        run_id=args.run,
        rankers=[item for item in args.rankers.split(",") if item],
        output=output,
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
