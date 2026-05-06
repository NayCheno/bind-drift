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
from binddrift.evaluation.protocol import FORBIDDEN_PRIMARY_SCORE_COMPONENTS, load_evaluation_protocol, protocol_provenance
from binddrift.run_manifest import canonical_run_dir, repo_relative, sha256_file, validate_run_manifest
from binddrift.warnings import read_warnings


SIMPLE_BASELINES = {"binding_diff", "c_signature", "c_indicator", "rust_use", "no_ranking", "random"}
ABLATIONS = {"no_graph", "no_impact_gate"}
TOP_K = 100
KS = (10, 20, 50, 100)
TAXONOMY_SCHEMA_VERSION = "m4-ranking-taxonomy-v2"
FALSE_POSITIVE_TAXONOMY = {
    "binding_only_or_generated_surface",
    "weak_rust_reachability",
    "real_c_drift_no_rust_contract_impact",
    "macro_constant_over_prioritization",
    "layout_ambiguity",
}
FALSE_NEGATIVE_TAXONOMY = {
    "not_ranked_by_primary_candidate_filter",
    "binding_or_layout_tail_candidate",
    "direct_rust_use_without_contract_boost",
    "contract_drift_ranked_below_top100",
    "true_label_ranked_below_top100",
}


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
    output = output or cfg.repo_root / "paper/tables/ranking_pooled_evaluation.json"
    table = build_ranker_evaluation(
        cfg,
        pool=pool,
        labels=labels,
        protocol_path=protocol_path,
        rankers=rankers,
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(table, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_split_tables(cfg, table)
    return table


def build_ranker_evaluation(
    cfg: Config,
    *,
    pool: Path,
    labels: Path,
    protocol_path: Path | None = None,
    rankers: list[str] | None = None,
) -> dict[str, Any]:
    manifest = validate_run_manifest(cfg)
    protocol = load_evaluation_protocol(cfg)
    if protocol_path and protocol_path.exists():
        protocol = {**protocol, "path": str(protocol_path)}
    run_dir = canonical_run_dir(cfg)
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
    ranked_pool_rows: dict[str, list[dict[str, Any]]] = {}
    for name, details in ranked_by_source.items():
        ranked = _dedupe_ranked_pool_rows(details["ranked"], pool_uids)
        label_values = [label_for_warning(label_map, warning) for warning in ranked]
        ranked_labels[name] = label_values
        ranked_pool_rows[name] = ranked
        rows.append(
            _ranker_metrics(
                name,
                ranked,
                label_values,
                pool_rows,
                pool_label_values,
                candidate_count=int(details["candidate_count"]),
                warning_volume=int(details["warning_volume"]),
                score_component_keys=list(details.get("score_component_keys") or []),
                ranking_feature_keys=list(details.get("ranking_feature_keys") or []),
                forbidden_oracle_feature_keys=list(details.get("forbidden_oracle_feature_keys") or []),
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
    ablation_story = _ablation_story(rows, primary)
    taxonomies = _ranking_error_taxonomies(
        pool_rows,
        label_map,
        ranked_pool_rows.get("binddrift_oracle_blind", []),
    )
    acceptance = _m6_acceptance(
        rows,
        primary,
        comparison,
        random_comparison,
        label_coverage,
        pool_size=len(pool_rows),
        ablation_story=ablation_story,
        taxonomies=taxonomies,
    )
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
        "all_rankers_same_pool": acceptance["checks"]["all_rankers_same_pool"],
        "primary_beats_best_simple_baseline": acceptance["checks"]["primary_beats_best_simple_baseline"],
        "no_self_evaluation_top100_only": acceptance["checks"]["no_self_evaluation_top100_only"],
        "top_false_positive_taxonomy": taxonomies["top_false_positive_taxonomy"],
        "top_false_negative_taxonomy": taxonomies["top_false_negative_taxonomy"],
        "ablation_story": ablation_story,
        "m6_acceptance": acceptance,
        "coverage_acceptance": {
            "minimum": 0.95,
            "passes": label_coverage["coverage"] >= 0.95,
        },
        "claim_recommendation": _claim_recommendation(comparison, label_coverage, primary),
    }
    if table["coverage_acceptance"]["passes"] is not True:
        raise RankerEvaluationError(f"pooled review label coverage below 95%: {label_coverage['coverage']}")
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
    score_component_keys: list[str],
    ranking_feature_keys: list[str],
    forbidden_oracle_feature_keys: list[str],
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
        "oracle_blind": name != "binddrift_current",
        "warning_volume": warning_volume,
        "candidate_count": candidate_count,
        "score_component_keys": sorted(score_component_keys),
        "ranking_feature_keys": sorted(ranking_feature_keys),
        "forbidden_oracle_feature_keys": sorted(forbidden_oracle_feature_keys),
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
        "minimum_required_conditions": 3,
        "passes_minimum_lift": passed == 3,
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


def _minimum_topk_passes(primary: dict[str, Any] | None) -> bool:
    primary = primary or {}
    return bool(
        (primary.get("p_at_10") or 0.0) >= 0.50
        and (primary.get("p_at_20") or 0.0) >= 0.45
        and (primary.get("p_at_50") or 0.0) >= 0.42
        and (primary.get("p_at_100") or 0.0) >= 0.40
        and (primary.get("ndcg_at_20") or 0.0) >= 0.55
    )


def _claim_recommendation(comparison: dict[str, Any], coverage: dict[str, Any], primary: dict[str, Any] | None) -> str:
    if coverage["coverage"] < 0.95:
        return "pooled labels incomplete; do not claim ranking improvement"
    if comparison.get("passes_minimum_lift") and _minimum_topk_passes(primary):
        return "ranking improvement claim supported on pooled labels"
    return "evidence gate claim only; ranking improvement not supported"


def _all_rankers_same_pool(rows: list[dict[str, Any]], pool_size: int) -> bool:
    if not rows:
        return False
    distributions = {json.dumps(row.get("label_distribution") or {}, sort_keys=True) for row in rows}
    return (
        all(row.get("evaluated_pool_rows") == pool_size for row in rows)
        and all(row.get("evaluation_denominator") == "complete_pooled_review_set" for row in rows)
        and len(distributions) == 1
    )


def _no_self_evaluation_top100_only(rows: list[dict[str, Any]], pool_size: int) -> bool:
    return bool(
        pool_size > TOP_K
        and rows
        and all(row.get("evaluated_pool_rows") == pool_size for row in rows)
        and all(row.get("evaluation_denominator") == "complete_pooled_review_set" for row in rows)
    )


def _significance_passes(comparison: dict[str, Any]) -> bool:
    metrics = ((comparison.get("paired_bootstrap_significance") or {}).get("metrics") or {})
    return all(
        ((metrics.get(metric) or {}).get("bootstrap_delta_ci") or [0.0])[0] > 0.0
        and ((metrics.get(metric) or {}).get("p_value_primary_not_better") or 1.0) < 0.05
        for metric in ("p_at_20", "p_at_50", "ndcg_at_20")
    )


def _primary_beats_best_simple_baseline(comparison: dict[str, Any]) -> bool:
    deltas = comparison.get("deltas") or {}
    return bool(
        (deltas.get("p_at_20") or 0.0) >= 0.10
        and (deltas.get("p_at_50") or 0.0) >= 0.07
        and (deltas.get("ndcg_at_20") or 0.0) >= 0.10
        and _significance_passes(comparison)
    )


def _random_baseline_sanity(comparison: dict[str, Any]) -> bool:
    deltas = comparison.get("deltas") or {}
    return bool(
        (deltas.get("p_at_20") or 0.0) > 0.0
        and (deltas.get("p_at_50") or 0.0) > 0.0
        and (deltas.get("ndcg_at_20") or 0.0) > 0.0
        and _significance_passes(comparison)
    )


def _oracle_blind_eval_has_no_oracle_leakage(rows: list[dict[str, Any]]) -> bool:
    for row in rows:
        if row.get("kind") not in {"primary", "simple_baseline", "ablation"}:
            continue
        keys = set(row.get("score_component_keys") or []) | set(row.get("ranking_feature_keys") or [])
        if row.get("oracle_blind") is not True:
            return False
        if row.get("forbidden_oracle_feature_keys"):
            return False
        if FORBIDDEN_PRIMARY_SCORE_COMPONENTS & keys:
            return False
    return True


def _ablation_story(rows: list[dict[str, Any]], primary: dict[str, Any] | None) -> dict[str, Any]:
    primary = primary or {}
    by_name = {row.get("ranker"): row for row in rows}
    labels = {
        "no_graph": "Graph evidence keeps weak symbol-only matches below better-supported C/Rust contract evidence.",
        "no_impact_gate": "Impact gating helps keep C-only or weak-reachability drift below Rust-impact review targets.",
    }
    ablations: list[dict[str, Any]] = []
    for name in sorted(ABLATIONS):
        row = by_name.get(name)
        if not row:
            continue
        deltas = {
            metric: round((primary.get(metric) or 0.0) - (row.get(metric) or 0.0), 4)
            for metric in ("p_at_20", "p_at_50", "ndcg_at_20", "auprc_on_pooled_review_set")
        }
        supports = deltas["p_at_20"] > 0.0 and deltas["ndcg_at_20"] > 0.0
        ablations.append(
            {
                "ablation": name,
                "design_choice": labels.get(name, "Ablation supports an oracle-blind ranking design choice."),
                "primary_minus_ablation": deltas,
                "supports_design_choice": supports,
            }
        )
    supporting = sum(1 for row in ablations if row["supports_design_choice"])
    return {
        "minimum_required_supporting_ablations": 2,
        "supporting_ablation_count": supporting,
        "supports_design": supporting >= 2,
        "ablations": ablations,
    }


def _ranking_error_taxonomies(
    pool_rows: list[dict[str, Any]],
    labels: dict[str, str],
    primary_ranked: list[dict[str, Any]],
    *,
    top_k: int = TOP_K,
) -> dict[str, Any]:
    top = primary_ranked[:top_k]
    rank_by_uid = {str(warning.get("warning_uid")): rank for rank, warning in enumerate(primary_ranked, start=1)}
    top_uids = {str(warning.get("warning_uid")) for warning in top}
    false_positives = [
        warning
        for warning in top
        if label_for_warning(labels, warning) and label_for_warning(labels, warning) not in TRUE_LABELS
    ]
    false_negatives = [
        warning
        for warning in pool_rows
        if label_for_warning(labels, warning) in TRUE_LABELS and str(warning.get("warning_uid")) not in top_uids
    ]
    return {
        "top_false_positive_taxonomy": _taxonomy_report(
            false_positives,
            labels,
            rank_by_uid,
            classifier=_false_positive_bucket,
            allowed_labels=FALSE_POSITIVE_TAXONOMY,
            window=f"primary_top_{top_k}",
        ),
        "top_false_negative_taxonomy": _taxonomy_report(
            false_negatives,
            labels,
            rank_by_uid,
            classifier=_false_negative_bucket,
            allowed_labels=FALSE_NEGATIVE_TAXONOMY,
            window=f"pooled_true_labels_outside_primary_top_{top_k}",
        ),
    }


def _taxonomy_report(
    warnings: list[dict[str, Any]],
    labels: dict[str, str],
    rank_by_uid: dict[str, int],
    *,
    classifier,
    allowed_labels: set[str],
    window: str,
    example_limit: int = 10,
) -> dict[str, Any]:
    taxonomy = Counter(classifier(warning, rank_by_uid.get(str(warning.get("warning_uid")))) for warning in warnings)
    unknown_labels = sorted(set(taxonomy) - allowed_labels)
    examples = []
    for warning in sorted(warnings, key=lambda row: (rank_by_uid.get(str(row.get("warning_uid")), 10**9), str(row.get("warning_uid"))))[:example_limit]:
        uid = str(warning.get("warning_uid"))
        examples.append(
            {
                "warning_uid": uid,
                "warning_id": warning.get("warning_id"),
                "pair_id": warning.get("pair_id"),
                "rank": rank_by_uid.get(uid),
                "label": label_for_warning(labels, warning),
                "type": warning.get("type"),
                "symbol": (warning.get("c_side") or {}).get("symbol"),
                "taxonomy": classifier(warning, rank_by_uid.get(uid)),
            }
        )
    return {
        "schema_version": TAXONOMY_SCHEMA_VERSION,
        "window": window,
        "count": len(warnings),
        "allowed_taxonomy": sorted(allowed_labels),
        "taxonomy": dict(taxonomy),
        "examples": examples,
        "schema_valid": not unknown_labels and sum(taxonomy.values()) == len(warnings),
        "unknown_taxonomy": unknown_labels,
    }


def _false_positive_bucket(warning: dict[str, Any], _rank: int | None = None) -> str:
    symbol = str((warning.get("c_side") or {}).get("symbol") or "")
    warning_type = str(warning.get("type") or "")
    fact_source = str(warning.get("fact_source") or "")
    if warning_type == "MacroConstDrift" or fact_source == "macro_diff" or symbol.isupper():
        return "macro_constant_over_prioritization"
    if warning_type in {"FieldDrift", "LayoutDrift", "LayoutFieldDrift"} or fact_source == "layout_diff":
        return "layout_ambiguity"
    if not _has_rust_reachability(warning):
        return "weak_rust_reachability"
    if warning.get("c_evidence_level") == "binding_only" or fact_source == "binding_diff":
        return "binding_only_or_generated_surface"
    return "real_c_drift_no_rust_contract_impact"


def _false_negative_bucket(warning: dict[str, Any], rank: int | None = None) -> str:
    if rank is None:
        return "not_ranked_by_primary_candidate_filter"
    if warning.get("c_evidence_level") == "binding_only":
        return "binding_or_layout_tail_candidate"
    if not _has_safe_or_contract_evidence(warning):
        return "direct_rust_use_without_contract_boost"
    if str(warning.get("type") or "").endswith("Drift"):
        return "contract_drift_ranked_below_top100"
    return "true_label_ranked_below_top100"


def _has_rust_reachability(warning: dict[str, Any]) -> bool:
    rust_side = warning.get("rust_side") or {}
    reasons = set(warning.get("promotion_reasons") or [])
    return bool(rust_side.get("uses") or rust_side.get("safe_apis") or "direct_binding_use" in reasons or "exposes_safe_api" in reasons)


def _has_safe_or_contract_evidence(warning: dict[str, Any]) -> bool:
    rust_side = warning.get("rust_side") or {}
    reasons = set(warning.get("promotion_reasons") or [])
    return bool(
        rust_side.get("safe_apis")
        or rust_side.get("safety_comments")
        or rust_side.get("error_mappings")
        or rust_side.get("lifetime_facts")
        or "exposes_safe_api" in reasons
        or "contract_evidence" in reasons
    )


def _taxonomy_accepts(report: dict[str, Any]) -> bool:
    examples = report.get("examples") or []
    return bool(
        report.get("schema_version") == TAXONOMY_SCHEMA_VERSION
        and report.get("schema_valid") is True
        and report.get("taxonomy")
        and report.get("count") == sum((report.get("taxonomy") or {}).values())
        and (report.get("count") or 0) >= len(examples)
        and all(
            example.get("warning_uid")
            and example.get("label")
            and example.get("taxonomy") in set(report.get("allowed_taxonomy") or [])
            for example in examples
        )
    )


def _m6_acceptance(
    rows: list[dict[str, Any]],
    primary: dict[str, Any] | None,
    comparison: dict[str, Any],
    random_comparison: dict[str, Any],
    label_coverage: dict[str, Any],
    *,
    pool_size: int,
    ablation_story: dict[str, Any],
    taxonomies: dict[str, Any],
) -> dict[str, Any]:
    deltas = comparison.get("deltas") or {}
    checks = {
        "all_rankers_same_pool": _all_rankers_same_pool(rows, pool_size),
        "pool_label_coverage": (label_coverage.get("coverage") or 0.0) >= 0.95,
        "primary_beats_best_simple_baseline": _primary_beats_best_simple_baseline(comparison),
        "p_at_20_delta": (deltas.get("p_at_20") or 0.0) >= 0.10,
        "p_at_50_delta": (deltas.get("p_at_50") or 0.0) >= 0.07,
        "ndcg_at_20_delta": (deltas.get("ndcg_at_20") or 0.0) >= 0.10,
        "bootstrap_ci_lower_bound": _significance_passes(comparison),
        "p_value": _significance_passes(comparison),
        "random_baseline_sanity": _random_baseline_sanity(random_comparison),
        "ablation_story": bool(ablation_story.get("supports_design")),
        "no_oracle_leakage": _oracle_blind_eval_has_no_oracle_leakage(rows),
        "no_self_evaluation_top100_only": _no_self_evaluation_top100_only(rows, pool_size),
        "top_false_positive_taxonomy": _taxonomy_accepts(taxonomies.get("top_false_positive_taxonomy") or {}),
        "top_false_negative_taxonomy": _taxonomy_accepts(taxonomies.get("top_false_negative_taxonomy") or {}),
    }
    return {
        "checks": checks,
        "minimum_passes": all(checks.values()),
        "thresholds": {
            "pool_label_coverage": 0.95,
            "p_at_20_delta": 0.10,
            "p_at_50_delta": 0.07,
            "ndcg_at_20_delta": 0.10,
            "p_value": 0.05,
            "supporting_ablations": 2,
        },
    }


def _write_split_tables(cfg: Config, table: dict[str, Any]) -> None:
    tables = cfg.repo_root / "paper/tables"
    manifest = validate_run_manifest(cfg)
    drift_fact_count = int(manifest.get("drift_fact_count") or 0)
    promoted_warning_count = int(manifest.get("promoted_warning_count") or 0)
    paper_topk = int(manifest.get("paper_topk") or TOP_K)
    baseline_rows = [row for row in table["rankers"] if row["kind"] in {"primary", "simple_baseline"}]
    ablation_rows = [row for row in table["rankers"] if row["kind"] in {"primary", "ablation"}]
    primary_warning_volume = next((row["warning_volume"] for row in table["rankers"] if row["ranker"] == "binddrift_oracle_blind"), None)
    warning_volume = {
        "drift_fact_count": drift_fact_count,
        "promoted_warning_count": promoted_warning_count,
        "primary_warning_volume": primary_warning_volume,
        "drift_facts_to_promoted_warnings_reduction": _reduction(drift_fact_count, promoted_warning_count),
        "paper_topk": paper_topk,
        "top_k_workload": {
            str(k): {
                "review_budget": min(k, promoted_warning_count) if promoted_warning_count else k,
                "share_of_drift_facts": _share(drift_fact_count, k),
                "share_of_promoted_warnings": _share(promoted_warning_count, k),
                "reduction_from_drift_facts": _reduction(drift_fact_count, k),
                "reduction_from_promoted_warnings": _reduction(promoted_warning_count, k),
            }
            for k in KS
        },
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
                "all_rankers_same_pool": table.get("all_rankers_same_pool"),
                "primary_beats_best_simple_baseline": table.get("primary_beats_best_simple_baseline"),
                "no_self_evaluation_top100_only": table.get("no_self_evaluation_top100_only"),
                "top_false_positive_taxonomy": table.get("top_false_positive_taxonomy"),
                "top_false_negative_taxonomy": table.get("top_false_negative_taxonomy"),
                "m6_acceptance": table.get("m6_acceptance"),
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    (tables / "ablation_strict_comparison.json").write_text(
        json.dumps({"rankers": ablation_rows, "ablation_story": table.get("ablation_story")}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (tables / "warning_volume_reduction.json").write_text(
        json.dumps(warning_volume, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def _share(denominator: int, numerator: int) -> float | None:
    if denominator <= 0:
        return None
    return round(min(numerator, denominator) / denominator, 4)


def _reduction(original: int, remaining: int) -> float | None:
    if original <= 0:
        return None
    return round(1.0 - min(remaining, original) / original, 4)


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
