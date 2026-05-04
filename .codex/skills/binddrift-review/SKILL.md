---
name: binddrift-review
description: Review BindDrift manual_review.csv warnings using an LLM-assisted evidence-collector, two independent reviewer roles, adjudication, and CSV backfill. Use when Codex needs to label BindDrift warnings, prepare evidence packets for warnings.jsonl/warnings.md/manual_review.csv rows, run sub-agent review of Rust-for-Linux API or contract drift warnings, or enforce the repository review-guide labels and claim boundary.
---

# BindDrift Review

## Claim Boundary

Treat BindDrift output as warnings, not proven bugs. Do not describe an all-LLM process as "human manual review" or "manual review by human experts" in paper text. Use wording such as "LLM-assisted review", "independent LLM review", or "LLM-assisted review with human spot-checking" unless actual human expert review happened.

The repository review guide uses two independent reviewers plus an adjudicator. Evaluation prefers `adjudicated_label`; legacy `label` exists for compatibility. Tier 2 semantic findings are review targets, not confirmed bugs.

## Workflow

1. Locate review artifacts: `manual_review.csv`, ranked `warnings.md`, `warnings.jsonl`, build-oracle rows, wrapper-fix candidates, binding diffs, source snippets, and any replay run directory relevant to the warning IDs.
2. For each warning, prepare an evidence packet before assigning labels. Prefer concrete old/new C evidence, generated binding evidence, Rust exposure, safety comments, build logs, and wrapper-fix diffs over keyword matches.
3. Review roles must be performed by sub-agents: use one sub-agent per role. The role dependency graph is strict: Evidence Collector must finish first; Reviewer 1 and Reviewer 2 each receive only the evidence packet and may run in parallel after collection; Adjudicator runs only after both reviewers finish and receives the evidence packet plus both review outputs; CSV Merger runs only after adjudication.
4. Keep Reviewer 1 and Reviewer 2 independent: do not pass either reviewer's output, notes, or label to the other reviewer. If sub-agents are unavailable, stop and state that the required one-role-per-sub-agent review cannot be completed in this session.
5. Backfill only `reviewer1_label`, `reviewer1_notes`, `reviewer2_label`, `reviewer2_notes`, `adjudicated_label`, and `adjudication_notes`. Keep `warning_id`, `type`, `risk`, `score`, and `symbol` unchanged. Leave legacy `label` and `reviewer_notes` empty unless the user explicitly asks otherwise.

## Labels

Use exactly one of:

- `TRUE_BUILD_BREAKAGE`
- `TRUE_WRAPPER_FIX`
- `TRUE_SEMANTIC_DRIFT`
- `BENIGN_DRIFT`
- `FALSE_POSITIVE`
- `UNCLEAR`

Use the detailed label definitions in [review-prompts.md](references/review-prompts.md) whenever generating role prompts or reviewing a warning.

## Evidence Standard

Prefer `UNCLEAR` over speculation. Prefer `BENIGN_DRIFT` over `TRUE_SEMANTIC_DRIFT` when the C drift is real but Rust impact is not plausible. Do not upgrade a warning based only on BindDrift score, symbol names, commit-subject keywords, or repeated terms.

Require:

- `TRUE_BUILD_BREAKAGE`: explicit build-log or build-oracle evidence connected to the warning symbol, binding, field, layout, or API drift.
- `TRUE_WRAPPER_FIX`: a later Rust wrapper/helper/binding commit or diff that addresses the same warned drift, symbol, contract, or Rust exposure path.
- `TRUE_SEMANTIC_DRIFT`: real C-side drift, reachable Rust exposure, and a Rust abstraction/unsafe boundary/safety assumption that plausibly depends on the changed contract.
- `BENIGN_DRIFT`: real C-side drift, but evidence shows Rust code is unaffected or robust.
- `FALSE_POSITIVE`: unsupported, wrong, parser-created, unrelated, or mismapped warning evidence.
- `UNCLEAR`: missing old/new C evidence, Rust exposure, binding diff, build log, wrapper-fix diff, or other information needed to decide.

## Prompt Reference

Open [review-prompts.md](references/review-prompts.md) when you need any of these reusable prompts:

- Global label definition prompt for all review roles.
- Evidence Collector sub-agent prompt.
- Reviewer 1 prompt.
- Reviewer 2 prompt.
- Adjudicator prompt.
- Batch review prompt.
- CSV backfill prompt.
- Single-warning input template.

Use the prompts verbatim where possible, adding only the specific warning evidence packet or batch input.
