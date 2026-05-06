# BindDrift: Prioritizing Review Targets for Rust-for-Linux Cross-Language API and Contract Drift

## Abstract

Rust-for-Linux safe abstractions rely on Linux C APIs whose signatures, layouts,
and behavioral contracts evolve outside Rust's type system. BindDrift
prioritizes review targets for Rust-for-Linux cross-language API and contract
drift. It is a static-analysis and cross-version replay artifact for
evidence-backed warning prioritization, not automatic bug confirmation:
BindDrift does not prove Rust safe abstraction soundness and does not
automatically detect bugs. BindDrift separates low-level cross-version drift
facts from promoted Rust-impact warnings, then attaches an evidence chain from
Linux C declarations or helpers through generated Rust bindings, unsafe Rust
call sites, wrapper code, safety comments, or public safe abstractions. Each
emitted warning is a review target for maintainers. The current canonical
replay spans 21 Linux snapshots from `v6.1` through `v7.0` plus `HEAD`, covers
20 adjacent version pairs, records 16,757 drift facts, and promotes 320
Rust-impact warnings. A 500-item pooled review set is double-reviewed and
adjudicated. The strict oracle-blind ranking gate reports
P@10 = 1.00, P@20 = 1.00, P@50 = 0.86, P@100 = 0.43, and NDCG@20 = 1.00,
improving P@20 by 0.60, P@50 by 0.64, and NDCG@20 by 0.5394 over the
strongest simple baseline in the shared pooled-label evaluation. The final
pooled labels contain 47 adjudicated true-positive review targets, including
29 `TRUE_SEMANTIC_DRIFT` rows and 17 `TRUE_WRAPPER_FIX` rows.

## 1. Introduction

Rust-for-Linux reduces direct exposure to kernel C APIs by routing most driver
code through Rust abstractions. This architecture improves local safety, but it
also creates a cross-language maintenance problem: a safe Rust API can remain
unchanged while the underlying C API changes its failure convention, refcount
contract, allocation/free pairing, or sleepability constraints.

BindDrift prioritizes review targets for Rust-for-Linux cross-language API and
contract drift. It frames this as a software evolution problem. The relevant
dependency chain is an evidence chain:

```text
Linux C function/type/macro/helper
-> bindgen-generated Rust binding or Rust helper
-> unsafe Rust call site
-> public safe abstraction
```

The key observation is that Rust type checking sees only part of this chain.
Type-visible signature or layout changes can break builds, but semantic changes
such as `NULL` versus `ERR_PTR`, owned versus borrowed references, or new
blocking behavior may still require human review.

This paper therefore makes a warning prioritization claim: BindDrift identifies
cross-version drift facts, filters them through Rust-impact evidence, and ranks
the resulting warnings as review targets. It does not certify Rust abstraction
correctness or automatically confirm a concrete runtime defect.

## 2. Background And Scope

Rust-for-Linux separates generated bindings from hand-written abstractions.
Bindings expose selected C declarations to Rust. Helpers expose C inline
functions and complex macros that bindgen cannot directly represent. Safe
abstractions then encapsulate unsafe calls and document the invariants callers
must rely on.

BindDrift targets Linux mainline, x86_64, Rust-enabled builds when the local
toolchain can produce them, and the `rust/bindings`, `rust/helpers`, and
`rust/kernel` surfaces. It does not prove Rust safe abstraction soundness. Tier
2 semantic findings are review targets and are explicitly marked as
indicator-based. They are not confirmed defects.

## 3. Design

BindDrift has five stages.

First, it captures environment metadata: kernel commit, config hash, tool
versions, and kernel Rust availability. For historical replay, BindDrift parses
each selected kernel release's minimum-tool script and writes a toolchain matrix
containing the Rust compiler, rust-src path, rustfmt, clippy-driver, and bindgen
binary used for that release. The matrix also records `LIBCLANG_PATH`,
`LLVM_CONFIG_PATH`, libclang probe output, and blocking compatibility issues.
This avoids a known validity threat: newer Rust compilers or mismatched
libclang versions can break older kernel Rust build rules even when the
kernel's own minimum supported Rust version is lower.

Second, extractors collect C facts, Rust facts, and generated binding facts when
available. C extraction defaults to the Rust-facing C surface: direct includes
from the kernel binding helper plus Rust helper sources. It records functions,
structs, macros, and behavior indicators such as `NULL_RETURN`,
`ERR_PTR_RETURN`, `ERROR_CODE`, `REFCOUNT_GET`, `REFCOUNT_PUT`, `ALLOC`,
`FREE`, and `MAY_SLEEP`. Rust extraction records binding uses, unsafe scopes,
public APIs, safety comments, Drop/Clone/lifetime patterns, and Option/Result
or error mappings.

Third, BindDrift builds a C-to-Rust dependency graph. Nodes include C functions,
C structs, macros, behavior indicators, Rust bindings, unsafe call sites, safe
APIs, safety comments, error mappings, and lifetime facts. Edges capture
generation, binding calls, safe API exposure, contract comments, error mapping,
and lifetime relevance.

Fourth, detectors produce two layers of output. Drift facts record low-level
cross-version changes in signatures, fields, layouts, macro/constants, helpers,
and behavior indicators. Promoted warnings are the subset with Rust-impact
evidence, such as direct binding use, safe API exposure, safety comments,
error/lifetime mappings, or wrapper-fix evidence.

Fifth, the primary oracle-blind ranker scores warnings with detection-time
features: C-side drift strength, Rust exposure, unsafe proximity, safe API
relevance, contract evidence, fanout penalties, repeated occurrence, and
evidence-chain richness. Build-breakage and wrapper-fix oracles are retained
only for auxiliary validation and are not inputs to the primary score.

## 4. Implementation

The artifact is a Python command-line tool backed by SQLite and JSONL reports.
It treats `vendor/linux` as an input repository and uses managed worktrees under
`.binddrift` for historical replay. The CLI supports toolchain checks, version
selection, kernel object-tree preparation, binding extraction, Rust extraction,
C extraction, graph construction, detection, ranking, evaluation, and paper
artifact generation.

The schema stores version metadata, commits, binding facts, Rust facts, C facts,
graph nodes and edges, extraction diagnostics, drift events, build-breakage
events, wrapper-fix candidates, manual labels, and generated table provenance.

## 5. Evaluation

The CCF-B-strength evaluation is organized around five research questions:

- RQ1: Can BindDrift extract reliable cross-language drift facts?
- RQ2: Does evidence gating reduce review volume while preserving useful
  review targets?
- RQ3: Does oracle-blind ranking improve top-K review yield over strong
  baselines?
- RQ4: What semantic drift patterns appear in adjudicated cases?
- RQ5: How reproducible is the artifact across versioned toolchains?

The main experiment replays 20 adjacent Linux mainline pairs across 21 version
snapshots from `v6.1` through `v7.0` plus the checked-out `HEAD` on x86_64. Each
included version is configured with a Rust-enabled kernel config, built with
versioned Rust and bindgen tools from the matrix, and required to produce
generated binding snapshots before drift detection. The canonical `latest`
manifest fixes the files used by all paper tables: 16,757 drift facts, 320
promoted Rust-impact warnings, the 500-row pooled review set, the 304 reviewed
semantic targets, and the generated case-study suite. `paper/tables/table_index.json`
records sha256 provenance for every generated main table.

An arm64 external-validity slice replays 8 release tags from `v6.13` through
`v7.0`, covering 7 adjacent pairs with Rust-enabled arm64 binding generation.
All 7 pairs complete, so there are 0 failed pairs; failed pairs would be
reported with pair status, build status, and error text rather than silently
skipped. The slice records 7,086 drift facts and 248 promoted Rust-impact
warnings. Warning overlap with the x86_64 replay is high: 236 warning
type/symbol keys are shared, 4 are arm64-only, and 47 are x86_64-only. The
architecture delta is concentrated in `SignatureDrift`, where arm64 reports
209 warnings versus 269 on x86_64; `MacroConstDrift` is unchanged at 26 on both
architectures, and `FieldDrift` drops from 25 on x86_64 to 13 on arm64. This
slice supports external validity for the replay and prioritization pipeline,
while the main pooled-label claims remain anchored to the canonical x86_64
review set.

Manual semantic evaluation uses a blind pooled review set. Two reviewers label
warnings independently, then an adjudicator records the final label; this manual
adjudication is the only source of semantic precision claims. All 500 pooled
warnings are double-labeled and adjudicated, with Cohen's kappa = 0.8118 and
agreement rate 0.922. The final pooled labels are 1 `TRUE_BUILD_BREAKAGE`,
17 `TRUE_WRAPPER_FIX`, 29 `TRUE_SEMANTIC_DRIFT`, 3 `BENIGN_DRIFT`,
450 `FALSE_POSITIVE`, and 0 `UNCLEAR`. These labels support a claim that
BindDrift surfaces useful review targets, not a claim that every warning is a
confirmed defect.

Baselines compare BindDrift against binding-diff, C-signature, C-indicator,
Rust-use, no-ranking, ablated variants, and random variants on the same pooled
label set. The strict pooled ranking table reports oracle-blind P@10 = 1.00,
P@20 = 1.00, P@50 = 0.86, P@100 = 0.43, NDCG@20 = 1.00, and AUPRC = 0.9444.
The strongest simple baseline is `rust_use`, with P@20 = 0.40, P@50 = 0.22,
and NDCG@20 = 0.4606. The strict ranking gate passes: BindDrift improves
oracle-blind top-K review yield over the strongest simple baseline by 0.60
P@20, 0.64 P@50, and 0.5394 NDCG@20 in the shared pooled-label evaluation.
The wrapper-fix oracle is auxiliary validation, while symbol-level wrapper
matching is treated as an upper bound. The paper tables are generated from
artifact outputs, not hand-entered numbers.

The targeted semantic review pass samples 400 semantic target candidates and
reviews 304 adjudicated rows
across nullability, ownership/refcount, allocation/free, sleepability/context,
and layout/field categories. It finds 29 `TRUE_SEMANTIC_DRIFT` rows, 17
`TRUE_WRAPPER_FIX` rows, 1 build-breakage row, 3 benign rows, and 255
false-positive rows, with no unclear rows. The semantic gate passes with 29
non-wrapper semantic true positives and 4 semantic drift types, so semantic
review targets may be reported as a secondary contribution while preserving the
claim boundary that they remain review targets rather than confirmed runtime
bugs.

The strict extractor audit samples 830 facts across C functions, C behavior
indicators, Rust binding uses, Rust safe API exposures, Rust error mappings,
Rust lifetime facts, and 150 promoted warning evidence chains. The audit reports
Cohen's kappa = 1.0 and `all_minimums_pass = true`, including promoted warning
evidence precision above the 0.85 gate. Review labels are transferred only from
rows with explicit reviewer/adjudication provenance; generated strict-only rows
remain pending until that provenance is present. The generated failure taxonomy
also reports limitation-focused negative controls for every extractor; these
controls document parser boundaries and should not be read as completeness or
bug confirmation evidence.

The artifact also includes 8 positive warning-backed case studies and 2
negative/failure-analysis cases selected from adjudicated labels.

## 6. Case Studies

The artifact includes 8 positive warning-backed case studies generated only
from adjudicated true positives:

- `security_secid_to_secctx`: nullability/error semantic drift reaches
  `SecurityCtx::from_secid`.
- `init_wait`: sleepability/context semantic drift reaches `CondVar::new`.
- `errname`: wrapper-fix-backed nullability/error drift reaches `Error::name`.
- `__mutex_init`: wrapper-fix-backed sleepability/context drift reaches Rust
  synchronization helper code.
- `errname`: an earlier wrapper-fix-backed nullability/error drift reaches
  `Error::name`.
- `dma_free_attrs`: allocation/free semantic drift reaches the Rust DMA drop
  path.
- `security_release_secctx`: allocation/free semantic drift reaches the Rust
  security context drop path.
- `__mutex_init`: another wrapper-fix-backed sleepability/context drift reaches
  Rust synchronization helper code.

The suite also includes 2 negative/failure-analysis cases:

- `refcount_set`: ownership/refcount evidence is rejected because broad-family
  wrapper evidence is auxiliary only.
- `kunit_case`: layout/field evidence is rejected because the case lacks a
  direct same-contract Rust-impact chain.

Each case is classified as a review target rather than a confirmed defect. No
positive case study is unlabeled, false positive, benign drift, or
single-version-only. The full case suite covers five drift target categories,
contains 4 semantic true cases, 4 non-wrapper semantic cases, 4 wrapper-fix-backed
cases, and has no local absolute paths in the generated case artifacts.

## 7. Threats To Validity

Internal validity threats include regex parser incompleteness, missing generated
binding outputs, toolchain/config differences, and oracle limitations. BindDrift
mitigates these by recording extraction diagnostics, environment metadata,
config hashes, and explicit separation between primary oracle-blind ranking and
auxiliary build/wrapper evidence.

Construct validity threats include the ambiguity of semantic drift labels and
the fact that warnings are review targets rather than confirmed defects. The
manual review guide separates `TRUE_SEMANTIC_DRIFT`, `TRUE_WRAPPER_FIX`,
`BENIGN_DRIFT`, `FALSE_POSITIVE`, and `UNCLEAR`, and the evaluation uses the
adjudicated label for paper metrics. Not every warning is a confirmed bug.
Wrapper-fix-backed labels and semantic labels are reported separately, and
`TRUE_WRAPPER_FIX` is not counted as `TRUE_SEMANTIC_DRIFT`. Label ambiguity
remains a threat even with double review and adjudication, so the paper reports
semantic labels as stale-contract review targets rather than confirmed bugs.

External validity threats include focusing on Linux/Rust-for-Linux and using
x86_64 as the main labeled evaluation architecture. The arm64 external-validity
slice reduces this threat by showing that the replay and warning-prioritization
pipeline runs across 8 arm64 release tags with 7 completed pairs, explicit
failed-pair reporting, and warning overlap/type-delta analysis. It does not
remove the threat entirely: arm64 is still Linux mainline, uses the same
Rust-for-Linux surfaces, and does not add independent manual labels. Future
work should evaluate rust-next branches, additional architectures, and complete
release-tag histories once full binding generation is available.

## 8. Related Work

BindDrift is related to API evolution, cross-language binding generation,
software maintenance mining, static bug finding for systems software, and
Rust-for-Linux empirical studies. Its distinguishing focus is the
cross-language path from evolving C APIs through generated bindings and unsafe
Rust wrappers into safe abstraction contracts.

## 9. Conclusion

BindDrift makes Rust-for-Linux cross-language dependencies explicit and ranks
API/contract drift warnings for review. The current artifact implements the full
pipeline and reports measured pilot results while preserving the central claim
boundary: BindDrift prioritizes evidence-backed review targets; it does not
certify correctness or claim every warning is a confirmed defect.
