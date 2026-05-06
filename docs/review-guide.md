# BindDrift Manual Review Guide

## Reader And Goal

This guide is for reviewers labeling BindDrift warnings. After reading it, they should be able to assign consistent labels for evaluation.

## Labels

Use one label per warning:

- `TRUE_BUILD_BREAKAGE`: the warning corresponds to a Rust-enabled build failure.
- `TRUE_WRAPPER_FIX`: a later Rust wrapper/helper/binding fix addresses the warned drift.
- `TRUE_SEMANTIC_DRIFT`: the warning identifies a real contract drift that can stale a safe abstraction, even if no build failure is visible.
- `BENIGN_DRIFT`: the drift is real but harmless for the Rust abstraction.
- `FALSE_POSITIVE`: the warning evidence does not support the claimed drift.
- `UNCLEAR`: available evidence is insufficient.

## Review Procedure

Start with the binddrift-review evidence packet for each warning, then record
labels in the generated review CSV. Reviewer role inputs should omit ranker
name, rank, score, and the other reviewer's notes. The CCF-B-strength workflow
uses two independent reviewers:

1. Reviewer 1 fills `reviewer1_label` and `reviewer1_notes`.
2. Reviewer 2 fills `reviewer2_label` and `reviewer2_notes` without looking at reviewer 1's notes.
3. The adjudicator fills `adjudicated_label` and `adjudication_notes`.

Inspect the C evidence, Rust call site, safe API exposure, generated binding
facts when available, build-breakage rows, wrapper-fix candidates, and nearby
safety comments. Reviewers are therefore not blind to build/wrapper evidence
when those sources are part of the label evidence, but that evidence remains
labels and auxiliary validation only, not a primary ranking input. For semantic
warnings, do not require proof of a concrete bug;
judge whether the warning is a valid stale-contract review target. The legacy
`label` column remains for compatibility; evaluation prefers
`adjudicated_label` when it is present.

Repository role artifacts are LLM-assisted binddrift-review outputs. Do not
call them human expert manual labels unless a separate human review record is
present.

## Reviewer Notes

Use notes to explain why the label was chosen. For wrapper fixes, include the relevant commit hash. For unclear cases, state which evidence is missing.
