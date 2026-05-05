from pathlib import Path
import re


def _section(text: str, start: str, end: str | None = None) -> str:
    start_index = text.index(start)
    end_index = text.index(end, start_index) if end else len(text)
    return text[start_index:end_index]


def test_paper_draft_preserves_claim_boundary() -> None:
    full_text = Path("paper/draft.md").read_text(encoding="utf-8")
    abstract = _section(full_text, "## Abstract", "## 1. Introduction")
    introduction = _section(full_text, "## 1. Introduction", "## 2. Background And Scope")
    evaluation = _section(full_text, "## 5. Evaluation", "## 6. Case Studies")
    text = re.sub(r"\s+", " ", "\n".join([abstract, introduction, evaluation]).lower())
    forbidden = [
        "bug detector",
        "soundness proof",
        "complete detection",
        "guaranteed stale abstraction",
        "proves rust abstraction unsoundness",
        "finds all contract drift",
        "detects real bugs automatically",
        "improves top-k review precision over",
        "ranking improves prioritization",
    ]
    for phrase in forbidden:
        assert phrase not in text

    required = [
        "warning prioritization",
        "review target",
        "evidence chain",
        "cross-version replay",
        "manual adjudication",
    ]
    for phrase in required:
        assert phrase in text

    expected_numbers = [
        "20 adjacent version pairs",
        "21 linux snapshots",
        "17,867 drift facts",
        "331 rust-impact warnings",
        "top 100 warnings",
        "37 adjudicated true-positive",
        "35 `true_wrapper_fix`",
        "2 `true_semantic_drift`",
        "35 `benign_drift`",
        "27 `false_positive`",
        "1 `unclear`",
        "p@10 = 0.30",
        "p@50 = 0.36",
        "p@100 = 0.37",
        "p@20 = 0.20",
        "ndcg@20 = 0.1966",
        "semantic drift result remains exploratory",
        "cohen's kappa = 1.0",
        "eight positive warning-backed case studies",
    ]
    for phrase in expected_numbers:
        assert phrase in text

    assert "evidence gate is supported as the stronger claim" in text
    assert "does not yet support a broad claim" in text
    assert "not every warning is a confirmed bug" in full_text.lower()
    assert "wrapper-fix oracle is auxiliary validation" in full_text.lower()
