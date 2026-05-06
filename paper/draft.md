# BindDrift: Evidence-Backed Warning Prioritization for Rust-for-Linux API and Contract Drift

## Abstract

Rust-for-Linux safe abstractions rely on Linux C APIs whose signatures, layouts,
and behavioral contracts evolve outside Rust's type system. BindDrift is a
static-analysis and cross-version replay artifact for evidence-backed warning
prioritization, not automatic bug confirmation. BindDrift separates low-level
cross-version drift facts from promoted Rust-impact warnings, then attaches an
evidence chain from Linux C declarations or helpers through generated Rust
bindings, unsafe Rust call sites, wrapper code, safety comments, or public safe
abstractions. Each emitted warning is a review target for maintainers. The
current canonical replay spans 21 Linux snapshots from `v6.1` through `v7.0`
plus `HEAD`, covers 20 adjacent version pairs, records 17,867 drift facts,
promotes 331 Rust-impact warnings, and sends the top 100 warnings through
double review and manual adjudication. The resulting paper-top-100 review has
37 adjudicated true-positive review targets, 35 benign drifts, 27 false
positives, and one unclear warning.

## 1. Introduction

Rust-for-Linux reduces direct exposure to kernel C APIs by routing most driver
code through Rust abstractions. This architecture improves local safety, but it
also creates a cross-language maintenance problem: a safe Rust API can remain
unchanged while the underlying C API changes its failure convention, refcount
contract, allocation/free pairing, or sleepability constraints.

BindDrift frames this as a software evolution problem. The relevant dependency
chain is an evidence chain:

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
2 warnings are review targets and are explicitly marked as indicator-based.

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

Fifth, the ranker scores warnings by drift severity, Rust exposure, unsafe
proximity, safe API relevance, helper involvement, confidence, build-breakage
likelihood, and evidence-chain richness.

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

The CCF-B-strength evaluation is organized around one main release-tag replay
and one small external-validity slice.

The main experiment replays 20 adjacent Linux mainline pairs across 21 version
snapshots from `v6.1` through `v7.0` plus the checked-out `HEAD` on x86_64. Each
included version is configured with a Rust-enabled kernel config, built with
versioned Rust and bindgen tools from the matrix, and required to produce
generated binding snapshots before drift detection. The canonical `latest`
manifest fixes the files used by all paper tables: 17,867 drift facts, 331
promoted Rust-impact warnings, and a paper top-100 warning set.

Manual semantic evaluation uses the paper top-100 warnings. Two reviewers label
warnings independently, then an adjudicator records the final label; this manual
adjudication is the only source of semantic precision claims. All 100 paper
warnings are double-labeled with agreement rate 1.0. The final labels are
35 `TRUE_WRAPPER_FIX`, 2 `TRUE_SEMANTIC_DRIFT`, 35 `BENIGN_DRIFT`,
27 `FALSE_POSITIVE`, and 1 `UNCLEAR`. Manual precision is 0.37 overall, with
P@10 = 0.30, P@50 = 0.36, and P@100 = 0.37. These labels support a claim that
BindDrift surfaces useful review targets, not a claim that every warning is a
confirmed defect.

Baselines compare BindDrift against binding-diff, C-signature, C-indicator,
Rust-use, oracle-blind, no-ranking, and random variants. In the current tables,
the evidence gate is supported as the stronger claim: BindDrift reduces the
warning volume to a reviewed Rust-impact set, but the ranking comparison does
not yet support a broad claim that BindDrift beats every simple baseline on
top-K manual precision. The strict pooled ranking table reports oracle-blind
P@10 = 0.30, P@20 = 0.20, P@50 = 0.08, P@100 = 0.04, and NDCG@20 = 0.1966, so
the ranking result is downgraded to evidence-gate support only. The wrapper-fix oracle is auxiliary validation, while symbol-level wrapper matching is treated as an upper bound. The paper tables are generated from artifact outputs, not hand-entered numbers.

The targeted semantic review pass samples 100 adjudicated semantic target rows
across nullability, ownership/refcount, allocation/free, sleepability/context,
and layout/field categories. It finds 2 `TRUE_SEMANTIC_DRIFT` rows, 54
`TRUE_WRAPPER_FIX` rows, 2 build-breakage rows, and several benign, unclear, or
false-positive rows. Because the semantic gate requires at least 8 semantic true positives and at least 3 semantic drift types, the semantic drift result remains exploratory.

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

The artifact also includes eight positive warning-backed case studies selected
from adjudicated true positives.

## 6. Case Studies

The artifact includes eight positive warning-backed case studies generated only
from adjudicated true positives:

- `security_secid_to_secctx`: nullability/error semantic drift reaches
  `SecurityCtx::from_secid`.
- `security_release_secctx`: allocation/free semantic drift reaches the Rust
  security context drop path.
- `mdiobus_write`: wrapper-fix-backed nullability/error drift reaches Rust PHY
  register write code.
- `refcount_set`: ownership/refcount wrapper-fix evidence reaches Rust wrapper
  paths.
- `gpu_buddy_free_list`: allocation/free wrapper-fix evidence reaches Rust GPU
  helper code.
- `fsleep`: sleepability/context wrapper-fix evidence reaches Rust-visible helper
  code.
- `queue_limits`: layout/field wrapper-fix evidence reaches Rust block wrapper
  paths.
- `__mutex_init`: build-breakage-backed sleepability/context evidence reaches
  Rust synchronization helper code.

The suite also includes one negative/failure-analysis case for `PTR_ERR`, whose
adjudicated label is `FALSE_POSITIVE`.

Each case is classified as a review target rather than a confirmed defect. No
positive case study is unlabeled, false positive, benign drift, or
single-version-only. The positive case set covers five drift target categories,
contains 2 semantic true cases and 5 wrapper-fix-backed cases, and has no local
absolute paths in the generated case artifacts.

## 7. Threats To Validity

Internal validity threats include regex parser incompleteness, missing generated
binding outputs, and toolchain/config differences. BindDrift mitigates these by
recording extraction diagnostics, environment metadata, and config hashes.

Construct validity threats include the ambiguity of semantic drift labels and
the fact that warnings are review targets rather than confirmed defects. The
manual review guide separates `TRUE_SEMANTIC_DRIFT`, `TRUE_WRAPPER_FIX`,
`BENIGN_DRIFT`, `FALSE_POSITIVE`, and `UNCLEAR`, and the evaluation uses the
adjudicated label for paper metrics. Not every warning is a confirmed bug.
Wrapper-fix-backed labels and semantic labels are reported separately, and
`TRUE_WRAPPER_FIX` is not counted as `TRUE_SEMANTIC_DRIFT`. The current semantic
target review is underpowered for a strong semantic-discovery claim, so semantic
drift is presented as exploratory.

External validity threats include focusing on Linux/Rust-for-Linux and x86_64.
Future work should evaluate additional architectures, rust-next branches, and
complete release-tag histories once full binding generation is available.

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
