# BindDrift: Detecting Cross-Language API and Contract Drift in Rust-for-Linux Safe Abstractions

## Abstract

Rust-for-Linux safe abstractions rely on Linux C APIs whose signatures, layouts,
and behavioral contracts evolve outside Rust's type system. BindDrift is a
static-analysis and empirical-replay artifact for detecting cross-language API
and contract drift from Linux C declarations and helpers to generated Rust
bindings, unsafe Rust call sites, and public safe abstractions. BindDrift builds
a C-to-Rust dependency graph, detects objective API drift and indicator-based
contract drift, and ranks warnings for maintainer review. The artifact now
records a per-version Rust-for-Linux toolchain matrix before replay, so older
kernel releases are built with their required Rust compiler and bindgen versions
instead of the host's current stable toolchain. On the current LLVM 18 host,
BindDrift marks `v6.1` through `v6.5` as binding-build incompatible because
their required bindgen `0.56.0` is known to fail with LLVM 16+ anonymous C item
names; the main replay therefore uses the reproducible `v6.6` through `v7.0`
plus `HEAD` window. The paper claim is evidence-backed warning prioritization,
not soundness proof or automatic bug confirmation.

## 1. Introduction

Rust-for-Linux reduces direct exposure to kernel C APIs by routing most driver
code through Rust abstractions. This architecture improves local safety, but it
also creates a cross-language maintenance problem: a safe Rust API can remain
unchanged while the underlying C API changes its failure convention, refcount
contract, allocation/free pairing, or sleepability constraints.

BindDrift frames this as a software evolution problem. The relevant dependency
chain is:

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

Fourth, detectors produce warnings. Tier 1 detectors compare two versions for
signature, field, layout, macro/constant, and helper drift. Tier 2 detectors
compare C behavior indicators and require Rust-side evidence before emitting
nullability, error, ownership/refcount, allocation/free, or sleepability
warnings.

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

The main experiment replays adjacent Linux mainline releases from `v6.6` through
`v7.0` plus the checked-out `HEAD` on x86_64. The earlier `v6.1` through `v6.5`
tags are retained in the toolchain matrix as documented exclusions on this host:
they require bindgen `0.56.0`, which fails with LLVM/libclang 16+ anonymous C
item names. Each included version is configured with a Rust-enabled kernel
config, built with the versioned Rust and bindgen tools from the matrix, and
required to produce generated binding snapshots before drift detection. The
current main replay completed 15 adjacent pairs, produced 16,973 ranked
warnings, and stores pair-level build status, binding hashes, extraction
summaries, wrapper-fix oracle rows, review CSVs, and evaluation tables under a
replay run directory.

Manual semantic evaluation uses the top 100 ranked warnings plus 100
stratified-by-type warnings. Two reviewers label warnings independently, then an
adjudicator records the final label. The artifact reports precision at k,
symbol-level build/wrapper-fix recall, label distribution, and reviewer
agreement. The aggregate review sheet has been generated for the main replay;
until two independent reviewers and an adjudicator complete it, warning rows
remain review targets rather than confirmed bugs.

Baselines compare BindDrift against bindgen-only drift, C signature drift,
build-only evidence, grep-based Rust usage, no ranking, and Tier-1-only
detection. Ablations remove the graph, Tier 2 detectors, ranking, safety
comments, commit text, or behavior indicators. The paper tables are generated
from artifact outputs, not hand-entered numbers.

## 6. Case Studies

The artifact includes five warning-backed case studies:

- `rb_first`: `NULL_RETURN` evidence reaches Rust rbtree cursor and iterator
  code.
- `auxiliary_device_uninit`: free/release and refcount-put evidence reaches the
  Rust auxiliary device drop path.
- `dma_alloc_attrs`: `NULL_RETURN` evidence reaches Rust DMA allocation
  wrappers.
- `kunit_get_current_test`: `NULL_RETURN` evidence reaches Rust KUnit helpers.
- `auxiliary_device_uninit` allocation/free pairing: release behavior reaches
  Rust cleanup code.

Each case is classified as a review target rather than a confirmed bug. This
matches the artifact's claim boundary and avoids overstating single-version
indicator evidence.

## 7. Threats To Validity

Internal validity threats include regex parser incompleteness, missing generated
binding outputs, and toolchain/config differences. BindDrift mitigates these by
recording extraction diagnostics, environment metadata, and config hashes.

Construct validity threats include the ambiguity of semantic drift labels and
the fact that warnings are not bugs. The manual review guide separates
`TRUE_SEMANTIC_DRIFT`, `BENIGN_DRIFT`, `FALSE_POSITIVE`, and `UNCLEAR`. In this
run, all reviewed warnings are `UNCLEAR` because historical comparison was not
available.

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
prove soundness or claim every warning is a bug.
