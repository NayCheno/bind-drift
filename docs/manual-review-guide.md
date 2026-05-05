# BindDrift Manual Review Guide

BindDrift warnings are review targets, not confirmed bugs. Reviewers assign labels from the evidence packet for a warning, and paper metrics use `adjudicated_label` after two independent reviews and adjudication.

## Labels

`TRUE_BUILD_BREAKAGE`: explicit Rust-enabled build-log or build-oracle evidence connects the warning symbol, binding, field, layout, or API drift to a build failure.

`TRUE_WRAPPER_FIX`: a later Rust wrapper/helper/binding change addresses the same warned drift, symbol, contract, or Rust exposure path. Wrapper-fix evidence is auxiliary validation, not the primary ranking score.

`TRUE_SEMANTIC_DRIFT`: real C-side API or contract drift reaches Rust binding/helper/unsafe wrapper/safe abstraction code, and the Rust abstraction or safety assumption plausibly depends on the changed contract.

`BENIGN_DRIFT`: the C-side drift is real, but the evidence shows Rust code is unaffected, robust to both versions, or not dependent on the changed behavior.

`FALSE_POSITIVE`: the warning evidence does not support the claimed drift, such as a wrong symbol, parser artifact, spurious keyword match, unrelated Rust evidence, or no real old/new difference.

`UNCLEAR`: available evidence is insufficient to decide. `UNCLEAR` is not counted as a true positive.

## Review Policy

Each warning must receive independent `reviewer1_label` and `reviewer2_label` values before adjudication. Reviewers should not see each other's notes before submitting their own label.

The adjudicator fills `adjudicated_label` and `adjudication_notes`. Missing adjudication notes above 20% is a paper-build failure condition for strict artifact validation.

`TRUE_WRAPPER_FIX` and `TRUE_SEMANTIC_DRIFT` are reported separately. `TRUE_WRAPPER_FIX` must never be counted as `TRUE_SEMANTIC_DRIFT`.

Wrapper-fix and build oracles are labels and auxiliary validation only. They are not allowed as primary ranking-score inputs.

Prefer `UNCLEAR` over speculation. Prefer `BENIGN_DRIFT` over `TRUE_SEMANTIC_DRIFT` when the C drift is real but Rust impact is not plausible.

## Required CSV Columns

Strict review artifacts must include:

- `warning_uid`
- `pair_id`
- `warning_id`
- `ranker_source`
- `type`
- `symbol`
- `reviewer1_label`
- `reviewer1_notes`
- `reviewer2_label`
- `reviewer2_notes`
- `adjudicated_label`
- `adjudication_notes`

Legacy `label` and `reviewer_notes` columns may remain for compatibility, but main paper metrics must use `adjudicated_label`.
