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

Start with the ranked Markdown report, then record labels in the generated review CSV. Inspect the C evidence, Rust call site, safe API exposure, and any nearby safety comments. For semantic warnings, do not require proof of a concrete bug; judge whether the warning is a valid stale-contract review target.

## Reviewer Notes

Use notes to explain why the label was chosen. For wrapper fixes, include the relevant commit hash. For unclear cases, state which evidence is missing.
