from __future__ import annotations

import json
import random
from pathlib import Path
from typing import Any

from binddrift.config import Config
from binddrift.artifact_paths import repo_relative
from binddrift.db import connect, initialize
from binddrift.ranking.oracle_blind_scorer import rank_primary_warnings_oracle_blind
from binddrift.ranking.scorer import score_breakdown as ranking_score_breakdown
from binddrift.warnings import read_warnings, split_main_and_single_version
from .metrics import TRUE_LABELS, label_for_warning, labeled_summary, load_manual_labels, oracle_summary
from .wrapper_oracle import replay_head_date, typed_wrapper_oracle_summary, version_dates_from_db, wrapper_fix_events_from_db


TOP_K = 100
BASELINES = ["BindingDiffOnly", "CSignatureDiffOnly", "CIndicatorOnly", "RustUseOnly", "NoRanking", "Random"]
ABLATIONS = ["NoGraph", "NoImpactGate"]


def generate_baselines(
    cfg: Config,
    warnings_path=None,
    review_path=None,
    run_manifest: str | None = None,
    uid_only_labels: bool = False,
) -> dict[str, Any]:
    conn = connect(cfg.database)
    initialize(conn)
    warnings, _single_version_targets = split_main_and_single_version(read_warnings(warnings_path or cfg.warnings_jsonl))
    labels = load_manual_labels(review_path or (cfg.data_dir / "manual_review.csv"), uid_only=uid_only_labels)
    build_symbols = _build_symbols(conn, warnings)
    wrapper_events = wrapper_fix_events_from_db(conn)
    wrapper_symbols: set[str] = set()
    for event in wrapper_events:
        wrapper_symbols.update(str(symbol) for symbol in event.get("matched_symbols", []) if symbol)
    version_dates = version_dates_from_db(conn)
    head_date = replay_head_date(warnings, version_dates)
    candidate_pool = _refresh_pool_scores(_candidate_pool(cfg, warnings, run_manifest), warnings, version_dates, head_date)
    counts = {
        "binding_functions": conn.execute("SELECT COUNT(*) AS n FROM binding_functions").fetchone()["n"],
        "c_functions": conn.execute("SELECT COUNT(*) AS n FROM c_functions").fetchone()["n"],
        "rust_binding_uses": conn.execute("SELECT COUNT(*) AS n FROM rust_binding_uses").fetchone()["n"],
        "graph_edges": conn.execute("SELECT COUNT(*) AS n FROM graph_edges").fetchone()["n"],
        "build_breakage_events": conn.execute("SELECT COUNT(*) AS n FROM build_breakage_events").fetchone()["n"],
        "warnings": len(warnings),
        "promoted_warning_pool": len(candidate_pool),
    }
    rows = []
    oracle_blind_candidates = rank_primary_warnings_oracle_blind(candidate_pool)
    oracle_blind_primary = oracle_blind_candidates[:TOP_K]
    rows.append(
        _variant_row(
            "BindDrift",
            "main",
            oracle_blind_primary,
            len(oracle_blind_candidates),
            labels,
            build_symbols,
            wrapper_symbols,
            wrapper_events,
            version_dates,
            head_date,
            "Primary oracle-blind BindDrift top-100 ranked warnings.",
            oracle_blind=True,
        )
    )
    rows.append(
        _variant_row(
            "FullBindDriftWithOracleAuxiliary",
            "auxiliary",
            warnings,
            len(candidate_pool),
            labels,
            build_symbols,
            wrapper_symbols,
            wrapper_events,
            version_dates,
            head_date,
            "Auxiliary validation only; this ranking may include wrapper/build oracle score components and is not a primary result.",
            oracle_blind=False,
        )
    )
    for name in BASELINES:
        candidates, candidate_count = _variant_warnings(name, warnings, candidate_pool)
        rows.append(
            _variant_row(
                name,
                "baseline",
                candidates,
                candidate_count,
                labels,
                build_symbols,
                wrapper_symbols,
                wrapper_events,
                version_dates,
                head_date,
                "Baseline owns its top-100 candidate list from the promoted warning pool.",
                oracle_blind=True,
            )
        )
    for name in ABLATIONS:
        candidates, candidate_count = _variant_warnings(name, warnings, candidate_pool)
        rows.append(
            _variant_row(
                name,
                "ablation",
                candidates,
                candidate_count,
                labels,
                build_symbols,
                wrapper_symbols,
                wrapper_events,
                version_dates,
                head_date,
                "Ablation re-ranks the promoted warning pool after removing one BindDrift signal.",
                oracle_blind=True,
            )
        )
    path = cfg.repo_root / "paper/tables/baselines_ablations.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    source = {
        "warnings": repo_relative(cfg, Path(warnings_path or cfg.warnings_jsonl)),
        "promoted_warnings": repo_relative(cfg, _promoted_warnings_path(cfg, run_manifest)) if _promoted_warnings_path(cfg, run_manifest) else "",
        "manual_review": repo_relative(cfg, Path(review_path or (cfg.data_dir / "manual_review.csv"))),
        "run_manifest": repo_relative(cfg, Path(run_manifest)) if run_manifest else None,
        "score_source": "promoted warning candidates are rescored in memory with the current ranking scorer before baseline sorting",
    }
    comparison = _comparison_summary(rows)
    path.write_text(json.dumps({"counts": counts, "source": source, "comparison": comparison, "variants": rows}, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return {"baseline_table": str(path), "variants": len(rows), "counts": counts}


def _variant_row(
    name: str,
    kind: str,
    candidates: list[dict[str, Any]],
    candidate_count: int,
    labels: dict[str, str],
    build_symbols: set[str],
    wrapper_symbols: set[str],
    wrapper_events: list[dict[str, Any]],
    version_dates: dict[str, str],
    head_date: str | None,
    note: str,
    oracle_blind: bool,
) -> dict[str, Any]:
    manual = labeled_summary(candidates, labels)
    manual["review_coverage_at_k"] = _review_coverage_at_k(candidates, labels)
    manual["conservative_precision_at_k"] = _conservative_precision_at_k(candidates, labels)
    return {
        "variant": name,
        "kind": kind,
        "oracle_blind": oracle_blind,
        "top_warning_uids": [warning.get("warning_uid") for warning in candidates],
        "score_component_keys": sorted({key for warning in candidates for key in (warning.get("score_components") or {})}),
        "candidate_count": candidate_count,
        "warning_count": len(candidates),
        "manual_review": manual,
        "build_breakage_prediction": oracle_summary(candidates, build_symbols),
        "wrapper_fix_prediction": oracle_summary(candidates, wrapper_symbols),
        "symbol_level_wrapper_prediction": oracle_summary(candidates, wrapper_symbols),
        "typed_wrapper_prediction": typed_wrapper_oracle_summary(candidates, wrapper_events, version_dates=version_dates, head_date=head_date),
        "typed_wrapper_compatibility_prediction": typed_wrapper_oracle_summary(candidates, wrapper_events, version_dates=version_dates, head_date=head_date, enforce_time=False),
        "note": note,
    }


def _symbol(warning: dict[str, Any]) -> str | None:
    symbol = warning.get("c_side", {}).get("symbol")
    return str(symbol) if symbol else None


def _build_symbols(conn, warnings: list[dict[str, Any]]) -> set[str]:
    pair_ids = {warning.get("pair_id") for warning in warnings if warning.get("pair_id")}
    run_ids = {warning.get("run_id") for warning in warnings if warning.get("run_id")}
    if len(pair_ids) == 1:
        return {
            str(row["symbol"])
            for row in conn.execute("SELECT DISTINCT symbol FROM build_breakage_events WHERE pair_id=? AND symbol IS NOT NULL", (next(iter(pair_ids)),))
        }
    if len(run_ids) == 1:
        return {
            str(row["symbol"])
            for row in conn.execute("SELECT DISTINCT symbol FROM build_breakage_events WHERE run_id=? AND symbol IS NOT NULL", (next(iter(run_ids)),))
        }
    return {
        str(row["symbol"])
        for row in conn.execute("SELECT DISTINCT symbol FROM build_breakage_events WHERE symbol IS NOT NULL")
    }


def _variant_warnings(
    name: str,
    warnings: list[dict[str, Any]],
    pool: list[dict[str, Any]],
    *,
    top_k: int | None = TOP_K,
) -> tuple[list[dict[str, Any]], int]:
    def window(ranked: list[dict[str, Any]]) -> list[dict[str, Any]]:
        return ranked if top_k is None else ranked[:top_k]

    if name == "BindingDiffOnly":
        candidates = [
            warning
            for warning in pool
            if warning.get("fact_source") == "binding_diff" or warning.get("c_evidence_level") == "binding_only"
        ]
        ranked = sorted(candidates, key=lambda warning: (_change_size(warning), _rust_use_count(warning), str(warning.get("warning_uid"))), reverse=True)
        return window(ranked), len(candidates)
    if name == "CSignatureDiffOnly":
        candidates = [warning for warning in pool if warning.get("type") == "SignatureDrift"]
        ranked = sorted(candidates, key=lambda warning: (_change_size(warning), str(warning.get("warning_uid"))), reverse=True)
        return window(ranked), len(candidates)
    if name == "CIndicatorOnly":
        candidates = [
            warning
            for warning in pool
            if warning.get("indicator_based") or warning.get("c_evidence_level") == "c_behavior_indicator"
        ]
        ranked = sorted(candidates, key=lambda warning: (float(warning.get("confidence") or 0.0), _change_size(warning)), reverse=True)
        return window(ranked), len(candidates)
    if name == "RustUseOnly":
        ranked = sorted(pool, key=lambda warning: (_rust_use_count(warning), str(warning.get("warning_uid"))), reverse=True)
        return window(ranked), len(pool)
    if name == "OracleBlindBindDrift":
        ranked = rank_primary_warnings_oracle_blind(pool)
        return window(ranked), len(ranked)
    if name == "NoRanking":
        ranked = sorted(pool, key=lambda warning: (str(warning.get("pair_id") or ""), str(warning.get("warning_id") or ""), str(warning.get("warning_uid") or "")))
        return window(ranked), len(pool)
    if name == "Random":
        ranked = _random_average_rows(pool, top_k=top_k)
        return ranked, len(pool)
    if name == "NoGraph":
        ranked = sorted(pool, key=lambda warning: (_symbol(warning) or "", str(warning.get("warning_id"))))
        return window(ranked), len(pool)
    if name == "NoImpactGate":
        ranked = sorted(pool, key=lambda warning: (_c_only_score(warning), str(warning.get("warning_uid"))), reverse=True)
        return window(ranked), len(pool)
    return window(warnings), len(warnings)


def _candidate_pool(cfg: Config, warnings: list[dict[str, Any]], run_manifest: str | None) -> list[dict[str, Any]]:
    promoted = _promoted_warnings_path(cfg, run_manifest)
    if promoted and promoted.exists():
        return read_warnings(promoted)
    return warnings


def _refresh_pool_scores(
    pool: list[dict[str, Any]],
    current_warnings: list[dict[str, Any]],
    version_dates: dict[str, str],
    head_date: str | None,
) -> list[dict[str, Any]]:
    current_by_uid = {
        str(warning.get("warning_uid")): warning
        for warning in current_warnings
        if warning.get("warning_uid")
    }
    refreshed: list[dict[str, Any]] = []
    for warning in pool:
        row = dict(warning)
        current = current_by_uid.get(str(row.get("warning_uid")))
        if current:
            row["score_breakdown"] = current.get("score_breakdown", {})
            row["score"] = current.get("score", 0.0)
            row["risk"] = current.get("risk", row.get("risk"))
        else:
            breakdown = ranking_score_breakdown(row, version_dates=version_dates, head_date=head_date)
            row["score_breakdown"] = breakdown
            row["score"] = round(sum(breakdown.values()), 3)
        refreshed.append(row)
    return refreshed


def _promoted_warnings_path(cfg: Config, run_manifest: str | None) -> Path | None:
    if not run_manifest:
        return None
    manifest_path = Path(run_manifest)
    if not manifest_path.exists():
        return None
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    promoted = manifest.get("canonical_promoted_warnings_file")
    if not promoted:
        return None
    return (cfg.repo_root / promoted).resolve() if not Path(promoted).is_absolute() else Path(promoted)


def _c_only_score(warning: dict[str, Any]) -> float:
    c_evidence = 3.0 if warning.get("c_evidence_level") in {"c_source_diff", "c_behavior_indicator"} else 0.0
    confidence = float(warning.get("confidence") or 0.0)
    return c_evidence + confidence + (_change_size(warning) / 1000.0)


def _change_size(warning: dict[str, Any]) -> int:
    c_side = warning.get("c_side") or {}
    return len(str(c_side.get("old", ""))) + len(str(c_side.get("new", "")))


def _rust_use_count(warning: dict[str, Any]) -> int:
    rust_side = warning.get("rust_side") or {}
    return len(rust_side.get("uses") or []) + int((rust_side.get("exposure") or {}).get("edge_count") or 0)


def _random_average_rows(pool: list[dict[str, Any]], trials: int = 10, *, top_k: int | None = TOP_K) -> list[dict[str, Any]]:
    if top_k is None:
        ranked = list(pool)
        random.Random(0).shuffle(ranked)
        return ranked
    if len(pool) <= top_k:
        return list(pool)
    # Represent Random by one deterministic seed in the normal metric columns;
    # per-seed spread is summarized separately by downstream comparison fields.
    rng = random.Random(0)
    return rng.sample(pool, top_k)


def _review_coverage_at_k(warnings: list[dict[str, Any]], labels: dict[str, str], ks: tuple[int, ...] = (10, 50, 100)) -> dict[str, float | None]:
    coverage: dict[str, float | None] = {}
    for k in ks:
        top = warnings[:k]
        coverage[str(k)] = round(sum(1 for warning in top if label_for_warning(labels, warning)) / len(top), 4) if top else None
    return coverage


def _conservative_precision_at_k(warnings: list[dict[str, Any]], labels: dict[str, str], ks: tuple[int, ...] = (10, 50, 100)) -> dict[str, float | None]:
    precision: dict[str, float | None] = {}
    for k in ks:
        top = warnings[:k]
        precision[str(k)] = round(sum(1 for warning in top if label_for_warning(labels, warning) in TRUE_LABELS) / len(top), 4) if top else None
    return precision


def _comparison_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    by_name = {row["variant"]: row for row in rows}
    full = by_name.get("BindDrift", {})
    simple_names = ["BindingDiffOnly", "CSignatureDiffOnly", "CIndicatorOnly", "RustUseOnly", "NoRanking", "Random"]
    simple = [by_name[name] for name in simple_names if name in by_name]
    full_manual = ((full.get("manual_review") or {}).get("precision_at_k") or {})
    full_typed = ((full.get("typed_wrapper_prediction") or {}).get("precision_at_k") or {})
    full_manual_cons = ((full.get("manual_review") or {}).get("conservative_precision_at_k") or {})
    best_simple_manual_50 = max((_metric(row, "manual_review", "precision_at_k", "50") or 0.0) for row in simple) if simple else 0.0
    no_ranking = by_name.get("NoRanking", {})
    full_auxiliary = by_name.get("FullBindDriftWithOracleAuxiliary", {})
    hard_failure = (
        (_metric(no_ranking, "manual_review", "precision_at_k", "10") or 0.0) >= (full_manual.get("10") or 0.0)
        and (_metric(no_ranking, "manual_review", "precision_at_k", "50") or 0.0) >= (full_manual.get("50") or 0.0)
    )
    topk_gate = (full_manual.get("10") or 0.0) >= 0.50
    ranking_claim_supported = (not hard_failure) and topk_gate
    return {
        "binddrift_manual_precision_at_k": full_manual,
        "binddrift_conservative_manual_precision_at_k": full_manual_cons,
        "binddrift_typed_precision_at_k": full_typed,
        "best_simple_manual_p50": round(best_simple_manual_50, 4),
        "binddrift_manual_p10_gt_simple_baselines": all((full_manual.get("10") or 0.0) > (_metric(row, "manual_review", "precision_at_k", "10") or 0.0) for row in simple),
        "binddrift_manual_p50_ge_best_plus_005": (full_manual.get("50") or 0.0) >= best_simple_manual_50 + 0.05,
        "primary_oracle_blind": full.get("oracle_blind") is True,
        "auxiliary_oracle_backed_typed_precision_at_k": ((full_auxiliary.get("typed_wrapper_prediction") or {}).get("precision_at_k") or {}),
        "no_ranking_hard_failure": hard_failure,
        "topk_minimum_gate": topk_gate,
        "ranking_claim_supported": ranking_claim_supported,
        "recommended_claim": "ranking improves prioritization" if ranking_claim_supported else "evidence gate reduces warning volume",
    }


def _metric(row: dict[str, Any], section: str, group: str, key: str) -> float | None:
    value = (((row.get(section) or {}).get(group) or {}).get(key))
    return float(value) if value is not None else None
