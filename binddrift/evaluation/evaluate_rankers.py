from __future__ import annotations

import argparse
import csv
import json
import math
import random
from collections import Counter
from pathlib import Path
from typing import Any

from binddrift.config import Config
from binddrift.evaluation.metrics import TRUE_LABELS, label_for_warning, load_manual_labels
from binddrift.evaluation.pooled_review import DEFAULT_RANKERS, ranker_output_details
from binddrift.evaluation.protocol import load_evaluation_protocol, protocol_provenance
from binddrift.run_manifest import canonical_run_dir, repo_relative, sha256_file, validate_run_manifest
from binddrift.warnings import read_warnings


SIMPLE_BASELINES = {"binding_diff", "c_signature", "c_indicator", "rust_use", "no_ranking", "random"}
ABLATIONS = {"no_graph", "no_impact_gate"}
KS = (10, 20, 50, 100)


class RankerEvaluationError(RuntimeError):
    pass


def evaluate_rankers(
    cfg: Config,
    *,
    pool: Path,
    labels: Path,
    protocol_path: Path | None = None,
    output: Path | None = None,
    rankers: list[str] | None = None,
) -> dict[str, Any]:
    manifest = validate_run_manifest(cfg)
    protocol = load_evaluation_protocol(cfg)
    if protocol_path and protocol_path.exists():
        protocol = {**protocol, "path": str(protocol_path)}
    run_dir = canonical_run_dir(cfg)
    output = output or cfg.repo_root / "paper/tables/ranking_pooled_evaluation.json"
    rankers = rankers or DEFAULT_RANKERS
    pool_rows = read_warnings(pool)
    label_map = load_manual_labels(labels, uid_only=True)
    warnings = read_warnings(Path(manifest["resolved_paths"]["warnings"]))
    promoted = read_warnings(Path(manifest["resolved_paths"]["promoted_warnings"]))
    ranked_by_source = ranker_output_details(cfg, warnings, promoted, rankers, run_manifest=str(run_dir / "run_manifest.json"))
    pool_by_uid = {str(row.get("warning_uid")): row for row in pool_rows}
    pool_uids = set(pool_by_uid)
    pool_label_values = [label_for_warning(label_map, warning) for warning in pool_rows]
    rows: list[dict[str, Any]] = []
    ranked_labels: dict[str, list[str]] = {}
    for name, details in ranked_by_source.items():
        ranked = _dedupe_ranked_pool_rows(details["ranked"], pool_uids)
        label_values = [label_for_warning(label_map, warning) for warning in ranked]
        ranked_labels[name] = label_values
        rows.append(
            _ranker_metrics(
                name,
                ranked,
                label_values,
                pool_rows,
                pool_label_values,
                candidate_count=int(details["candidate_count"]),
                warning_volume=int(details["warning_volume"]),
            )
        )
    best_simple = _best_simple(rows)
    random_baseline = next((row for row in rows if row["ranker"] == "random"), {})
    primary = next((row for row in rows if row["ranker"] == "binddrift_oracle_blind"), None)
    significance = _paired_bootstrap_significance(
        ranked_labels.get("binddrift_oracle_blind", []),
        ranked_labels.get(str(best_simple.get("ranker")), []),
        pool_label_values,
    )
    comparison = _comparison(primary, best_simple, significance=significance)
    random_comparison = _comparison(
        primary,
        random_baseline,
        significance=_paired_bootstrap_significance(
            ranked_labels.get("binddrift_oracle_blind", []),
            ranked_labels.get("random", []),
            pool_label_values,
        ),
    )
    label_coverage = _strict_label_coverage(pool_rows, labels)
    table = {
        **protocol_provenance(protocol),
        "pool": repo_relative(cfg, pool),
        "pool_sha256": sha256_file(pool),
        "labels": repo_relative(cfg, labels),
        "labels_sha256": sha256_file(labels),
        "pool_size": len(pool_rows),
        "label_coverage": label_coverage,
        "rankers": rows,
        "best_simple_baseline": best_simple,
        "random_baseline": random_baseline,
        "comparison_against_best_simple_baseline": comparison,
        "comparison_against_random": random_comparison,
        "coverage_acceptance": {
            "minimum": 0.95,
            "passes": label_coverage["coverage"] >= 0.95,
        },
        "claim_recommendation": _claim_recommendation(comparison, label_coverage),
    }
    if table["coverage_acceptance"]["passes"] is not True:
        raise RankerEvaluationError(f"pooled review label coverage below 95%: {label_coverage['coverage']}")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(table, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_split_tables(cfg, table)
    return table


def _ranker_metrics(
    name: str,
    ranked: list[dict[str, Any]],
    ranked_labels: list[str],
    pool_rows: list[dict[str, Any]],
    pool_labels: list[str],
    *,
    candidate_count: int,
    warning_volume: int,
) -> dict[str, Any]:
    metrics = {f"p_at_{k}": _precision_at_k(ranked_labels, k, pool_size=len(pool_rows)) for k in KS}
    metrics["ndcg_at_20"] = _ndcg_at_k(ranked_labels, pool_labels, 20)
    metrics["auprc_on_pooled_review_set"] = _average_precision_on_pool(ranked_labels, pool_labels)
    ci = {
        key: _bootstrap_ci(ranked_labels, pool_labels, key)
        for key in ("p_at_20", "p_at_50", "ndcg_at_20")
    }
    return {
        "ranker": name,
        "kind": _ranker_kind(name),
        "warning_volume": warning_volume,
        "candidate_count": candidate_count,
        "evaluated_pool_rows": len(pool_rows),
        "evaluation_denominator": "complete_pooled_review_set",
        "review_pool_ranked_count": len(ranked),
        "review_pool_covered": round(len(ranked) / len(pool_rows), 4) if pool_rows else 0.0,
        "labeled_at_100": sum(1 for label in ranked_labels[:100] if label),
        "label_distribution": dict(Counter(label for label in pool_labels if label)),
        "ranked_label_distribution": dict(Counter(label for label in ranked_labels if label)),
        "true_label_distribution": dict(Counter(label for label in pool_labels if label in TRUE_LABELS)),
        "ranked_true_label_distribution": dict(Counter(label for label in ranked_labels if label in TRUE_LABELS)),
        **metrics,
        "bootstrap_ci": ci,
    }


def _dedupe_ranked_pool_rows(ranked: list[dict[str, Any]], pool_uids: set[str]) -> list[dict[str, Any]]:
    seen: set[str] = set()
    rows: list[dict[str, Any]] = []
    for warning in ranked:
        uid = str(warning.get("warning_uid"))
        if uid not in pool_uids or uid in seen:
            continue
        rows.append(warning)
        seen.add(uid)
    return rows


def _ranker_kind(name: str) -> str:
    if name == "binddrift_oracle_blind":
        return "primary"
    if name in SIMPLE_BASELINES:
        return "simple_baseline"
    if name in ABLATIONS:
        return "ablation"
    return "auxiliary"


def _label_coverage(pool_rows: list[dict[str, Any]], labels: dict[str, str]) -> dict[str, Any]:
    labeled = sum(1 for warning in pool_rows if label_for_warning(labels, warning))
    return {
        "labeled_rows": labeled,
        "pool_rows": len(pool_rows),
        "coverage": round(labeled / len(pool_rows), 4) if pool_rows else 0.0,
    }


def _strict_label_coverage(pool_rows: list[dict[str, Any]], labels_path: Path) -> dict[str, Any]:
    rows_by_uid: dict[str, dict[str, str]] = {}
    with labels_path.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            if row.get("warning_uid"):
                rows_by_uid[row["warning_uid"]] = row
    reviewed = 0
    excluded_conservative = 0
    for warning in pool_rows:
        row = rows_by_uid.get(str(warning.get("warning_uid"))) or {}
        source = row.get("label_source", "")
        complete = bool(
            row.get("reviewer1_label", "").strip()
            and row.get("reviewer2_label", "").strip()
            and row.get("adjudicated_label", "").strip()
            and row.get("adjudication_notes", "").strip()
        )
        if "conservative" in source.lower():
            excluded_conservative += 1
            continue
        if complete:
            reviewed += 1
    return {
        "labeled_rows": reviewed,
        "pool_rows": len(pool_rows),
        "coverage": round(reviewed / len(pool_rows), 4) if pool_rows else 0.0,
        "excluded_conservative_backfill_rows": excluded_conservative,
    }


def _precision_at_k(labels: list[str], k: int, *, pool_size: int | None = None) -> float | None:
    denominator = min(k, pool_size) if pool_size is not None else k
    if denominator <= 0:
        return None
    top = labels[:k]
    return round(sum(1 for label in top if label in TRUE_LABELS) / denominator, 4)


def _ndcg_at_k(labels: list[str], pool_labels: list[str], k: int) -> float | None:
    if not pool_labels:
        return None
    rel = [1.0 if label in TRUE_LABELS else 0.0 for label in labels[:k]]
    rel.extend([0.0] * max(0, min(k, len(pool_labels)) - len(rel)))
    dcg = sum(value / math.log2(idx + 2) for idx, value in enumerate(rel))
    ideal = sorted([1.0 if label in TRUE_LABELS else 0.0 for label in pool_labels], reverse=True)[:k]
    idcg = sum(value / math.log2(idx + 2) for idx, value in enumerate(ideal))
    return round(dcg / idcg, 4) if idcg else 0.0


def _average_precision_on_pool(ranked_labels: list[str], pool_labels: list[str]) -> float | None:
    positives = 0
    total = sum(1 for label in pool_labels if label in TRUE_LABELS)
    if total == 0:
        return 0.0 if pool_labels else None
    precision_sum = 0.0
    for idx, label in enumerate(ranked_labels, start=1):
        if label in TRUE_LABELS:
            positives += 1
            precision_sum += positives / idx
    return round(precision_sum / total, 4)


def _bootstrap_ci(ranked_labels: list[str], pool_labels: list[str], metric: str, trials: int = 500) -> list[float | None]:
    if not pool_labels:
        return [None, None]
    observed = _metric_value(ranked_labels, pool_labels, metric)
    rng = random.Random(0)
    values: list[float] = []
    sample_length = _bootstrap_sample_length(metric, len(pool_labels))
    for _idx in range(trials):
        sample: list[str] = []
        for _sample_idx in range(sample_length):
            position = rng.randrange(sample_length)
            sample.append(ranked_labels[position] if position < len(ranked_labels) else "")
        value = _metric_value(sample, pool_labels, metric)
        if value is not None:
            values.append(value)
    if not values:
        return [None, None]
    values.sort()
    lo = min(values[int(0.025 * (len(values) - 1))], observed if observed is not None else values[0])
    hi = max(values[int(0.975 * (len(values) - 1))], observed if observed is not None else values[-1])
    return [round(lo, 4), round(hi, 4)]


def _bootstrap_sample_length(metric: str, pool_size: int) -> int:
    if metric.startswith("p_at_"):
        return min(int(metric.rsplit("_", 1)[1]), pool_size)
    if metric == "ndcg_at_20":
        return min(20, pool_size)
    return pool_size


def _metric_value(labels: list[str], pool_labels: list[str], metric: str) -> float | None:
    if metric.startswith("p_at_"):
        return _precision_at_k(labels, int(metric.rsplit("_", 1)[1]), pool_size=len(pool_labels))
    if metric == "ndcg_at_20":
        return _ndcg_at_k(labels, pool_labels, 20)
    return None


def _best_simple(rows: list[dict[str, Any]]) -> dict[str, Any]:
    simple = [row for row in rows if row["kind"] == "simple_baseline" and row["ranker"] != "random"]
    if not simple:
        simple = [row for row in rows if row["kind"] == "simple_baseline"]
    if not simple:
        return {}
    return max(simple, key=lambda row: ((row.get("p_at_20") or 0.0), (row.get("ndcg_at_20") or 0.0)))


def _comparison(
    primary: dict[str, Any] | None,
    best: dict[str, Any],
    *,
    significance: dict[str, Any] | None = None,
) -> dict[str, Any]:
    if not primary or not best:
        return {"passes_minimum_lift": False}
    deltas = {
        "p_at_20": round((primary.get("p_at_20") or 0.0) - (best.get("p_at_20") or 0.0), 4),
        "p_at_50": round((primary.get("p_at_50") or 0.0) - (best.get("p_at_50") or 0.0), 4),
        "ndcg_at_20": round((primary.get("ndcg_at_20") or 0.0) - (best.get("ndcg_at_20") or 0.0), 4),
    }
    passed = sum(
        [
            deltas["p_at_20"] >= 0.10,
            deltas["p_at_50"] >= 0.07,
            deltas["ndcg_at_20"] >= 0.10,
        ]
    )
    return {
        "primary_ranker": primary["ranker"],
        "best_simple_baseline": best["ranker"],
        "deltas": deltas,
        "minimum_conditions_passed": passed,
        "passes_minimum_lift": passed >= 2,
        "paired_bootstrap_significance": significance or {},
    }


def _paired_bootstrap_significance(
    primary_labels: list[str],
    best_labels: list[str],
    pool_labels: list[str],
    trials: int = 500,
) -> dict[str, Any]:
    if not pool_labels:
        return {"method": "paired_rank_position_bootstrap", "trials": trials, "metrics": {}}
    rng = random.Random(0)
    metrics: dict[str, Any] = {}
    for metric in ("p_at_20", "p_at_50", "ndcg_at_20"):
        observed = round((_metric_value(primary_labels, pool_labels, metric) or 0.0) - (_metric_value(best_labels, pool_labels, metric) or 0.0), 4)
        length = _bootstrap_sample_length(metric, len(pool_labels))
        pairs = [
            (
                primary_labels[idx] if idx < len(primary_labels) else "",
                best_labels[idx] if idx < len(best_labels) else "",
            )
            for idx in range(length)
        ]
        deltas: list[float] = []
        for _trial in range(trials):
            sample = [pairs[rng.randrange(length)] for _idx in range(length)]
            primary_sample = [left for left, _right in sample]
            best_sample = [right for _left, right in sample]
            deltas.append((_metric_value(primary_sample, pool_labels, metric) or 0.0) - (_metric_value(best_sample, pool_labels, metric) or 0.0))
        not_better = sum(1 for delta in deltas if delta <= 0.0)
        sorted_deltas = sorted(deltas)
        metrics[metric] = {
            "observed_delta": observed,
            "p_value_primary_not_better": round((not_better + 1) / (trials + 1), 4),
            "significant_primary_better": observed > 0.0 and ((not_better + 1) / (trials + 1)) <= 0.05,
            "bootstrap_delta_ci": [
                round(min(sorted_deltas[int(0.025 * (len(sorted_deltas) - 1))], observed), 4),
                round(max(sorted_deltas[int(0.975 * (len(sorted_deltas) - 1))], observed), 4),
            ],
        }
    return {
        "method": "paired_rank_position_bootstrap",
        "trials": trials,
        "best_simple_baseline": "same_as_comparison",
        "metrics": metrics,
    }


def _claim_recommendation(comparison: dict[str, Any], coverage: dict[str, Any]) -> str:
    if coverage["coverage"] < 0.95:
        return "pooled labels incomplete; do not claim ranking improvement"
    if comparison.get("passes_minimum_lift"):
        return "ranking improvement claim supported on pooled labels"
    return "evidence gate claim only; ranking improvement not supported"


def _write_split_tables(cfg: Config, table: dict[str, Any]) -> None:
    tables = cfg.repo_root / "paper/tables"
    baseline_rows = [row for row in table["rankers"] if row["kind"] in {"primary", "simple_baseline"}]
    ablation_rows = [row for row in table["rankers"] if row["kind"] in {"primary", "ablation"}]
    warning_volume = {
        "primary_warning_volume": next((row["warning_volume"] for row in table["rankers"] if row["ranker"] == "binddrift_oracle_blind"), None),
        "ranker_warning_volumes": {row["ranker"]: row["warning_volume"] for row in table["rankers"]},
    }
    (tables / "baseline_strict_comparison.json").write_text(
        json.dumps(
            {
                "rankers": baseline_rows,
                "best_simple_baseline": table["best_simple_baseline"],
                "random_baseline": table.get("random_baseline", {}),
                "comparison": table["comparison_against_best_simple_baseline"],
                "comparison_against_random": table.get("comparison_against_random", {}),
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    (tables / "ablation_strict_comparison.json").write_text(
        json.dumps({"rankers": ablation_rows}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (tables / "warning_volume_reduction.json").write_text(
        json.dumps(warning_volume, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Evaluate rankers on one pooled BindDrift label set.")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--pool", required=True)
    parser.add_argument("--labels", required=True)
    parser.add_argument("--protocol")
    parser.add_argument("--output")
    args = parser.parse_args(argv)
    cfg = Config.from_args(repo_root=args.repo_root)
    result = evaluate_rankers(
        cfg,
        pool=Path(args.pool).resolve(),
        labels=Path(args.labels).resolve(),
        protocol_path=Path(args.protocol).resolve() if args.protocol else None,
        output=Path(args.output).resolve() if args.output else None,
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
