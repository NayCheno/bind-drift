import json
from pathlib import Path
import re


def _section(text: str, start: str, end: str | None = None) -> str:
    start_index = text.index(start)
    end_index = text.index(end, start_index) if end else len(text)
    return text[start_index:end_index]


def test_paper_draft_preserves_claim_boundary() -> None:
    full_text = Path("paper/draft.md").read_text(encoding="utf-8")
    manifest = json.loads(Path("data/replay/latest/run_manifest.json").read_text(encoding="utf-8"))
    ranking = json.loads(Path("paper/tables/ranking_pooled_evaluation.json").read_text(encoding="utf-8"))
    manual = json.loads(Path("paper/tables/manual_review_quality.json").read_text(encoding="utf-8"))
    semantic = json.loads(Path("paper/tables/semantic_drift_review_summary.json").read_text(encoding="utf-8"))
    cases = json.loads(Path("paper/tables/case_study_summary.json").read_text(encoding="utf-8"))
    primary = next(row for row in ranking["rankers"] if row["ranker"] == "binddrift_oracle_blind")
    deltas = ranking["comparison_against_best_simple_baseline"]["deltas"]
    abstract = _section(full_text, "## Abstract", "## 1. Introduction")
    introduction = _section(full_text, "## 1. Introduction", "## 2. Background And Scope")
    evaluation = _section(full_text, "## 5. Evaluation", "## 6. Case Studies")
    full_normalized = re.sub(r"\s+", " ", full_text.lower())
    text = re.sub(r"\s+", " ", "\n".join([abstract, introduction, evaluation]).lower())
    forbidden = [
        "bug detector",
        "soundness proof",
        "complete detection",
        "guaranteed stale abstraction",
        "proves rust abstraction unsoundness",
        "finds all contract drift",
        "detects real bugs automatically",
        "ranking improves prioritization",
        "outperforms all baselines",
        "many semantic bugs",
    ]
    for phrase in forbidden:
        assert phrase not in text

    required = [
        "binddrift prioritizes review targets for rust-for-linux cross-language api and contract drift",
        "`binddrift-oracle-blind`",
        "warning prioritization",
        "review target",
        "evidence chain",
        "detection-time features",
        "auxiliary validation oracles",
        "evaluation and validation",
        "neither oracle has a data path",
        "cross-version replay",
        "manual adjudication",
        "strict ranking gate passes",
        "semantic gate passes",
    ]
    for phrase in required:
        assert phrase in text

    expected_numbers = [
        "20 adjacent version pairs",
        "21 linux snapshots",
        f"{manifest['drift_fact_count']:,} drift facts",
        f"{manifest['promoted_warning_count']:,} rust-impact warnings",
        f"{manual['reviewed_warnings']}-item pooled review set",
        "47 adjudicated true-positive",
        f"{manual['true_wrapper_fix_count']} `true_wrapper_fix`",
        f"{manual['true_semantic_drift_count']} `true_semantic_drift`",
        f"{manual['label_distribution']['BENIGN_DRIFT']} `benign_drift`",
        f"{manual['label_distribution']['FALSE_POSITIVE']} `false_positive`",
        f"{manual['label_distribution']['UNCLEAR']} `unclear`",
        f"p@10 = {primary['p_at_10']:.2f}",
        f"p@20 = {primary['p_at_20']:.2f}",
        f"p@50 = {primary['p_at_50']:.2f}",
        f"p@100 = {primary['p_at_100']:.2f}",
        f"ndcg@20 = {primary['ndcg_at_20']:.2f}",
        f"{deltas['p_at_20']:.2f} p@20",
        f"{deltas['p_at_50']:.2f} p@50",
        f"{deltas['ndcg_at_20']:.4f} ndcg@20",
        f"{semantic['true_semantic_drift_count']} `true_semantic_drift` rows",
        f"{semantic['non_wrapper_semantic_true_positives']} non-wrapper semantic true positives",
        f"{semantic['semantic_drift_type_count']} semantic drift types",
        "cohen's kappa = 1.0",
        f"{cases['positive_case_studies']} positive warning-backed case studies",
        f"{cases['negative_case_studies']} negative/failure-analysis cases",
    ]
    for phrase in expected_numbers:
        assert phrase in text

    assert "evidence gate is supported as the stronger claim" not in text
    assert "does not yet support a broad claim" not in text
    assert "semantic drift result remains exploratory" not in text
    assert "does not prove rust safe abstraction soundness" in full_normalized
    assert "does not automatically detect bugs" in full_normalized
    assert "tier 2 semantic findings are review targets" in full_normalized
    assert "`true_wrapper_fix` is not counted as `true_semantic_drift`" in full_normalized
    assert "not every warning is a confirmed bug" in full_normalized
    assert "wrapper-fix oracle is auxiliary validation" in full_normalized
    assert "build-breakage oracle and wrapper-fix oracle are auxiliary validation only" in full_normalized
    assert "oracleblindbinddrift" not in full_normalized
    assert "binddrift_oracle_blind" not in full_normalized
    assert Path("paper/figures/ranking-dataflow.md").exists()


def test_table_index_records_sha256_provenance() -> None:
    index = json.loads(Path("paper/tables/table_index.json").read_text(encoding="utf-8"))
    assert index
    for name, entry in index.items():
        assert entry["available"] is True, name
        assert re.fullmatch(r"[0-9a-f]{64}", entry.get("sha256", "")), name
