# BindDrift: Detecting Cross-Language API and Contract Drift in Rust-for-Linux Safe Abstractions

## Abstract

Rust-for-Linux safe abstractions depend on Linux C APIs whose signatures, layouts, and behavioral contracts evolve over time. BindDrift detects cross-language API and contract drift by connecting C symbols, generated Rust bindings, unsafe Rust call sites, and public safe abstractions. The prototype emits explainable, ranked warnings rather than claiming full soundness proofs.

## 1. Introduction

Rust-for-Linux reduces direct exposure to unsafe C APIs by placing reviewed Rust abstractions between drivers and kernel C functionality. This boundary is only stable if the underlying C API and contract remain compatible with the Rust wrapper's assumptions. Linux C changes can alter signatures, layouts, error conventions, ownership transfer, refcounting, and sleepability without necessarily changing the Rust safe API.

BindDrift studies this as a software evolution problem: C-side API drift can propagate through bindgen output and unsafe Rust wrappers into safe abstractions. The key claim is warning and prioritization, not automated proof of Rust abstraction soundness.

## 2. Background

Rust-for-Linux separates generated bindings from hand-written abstractions. Bindgen exposes selected C declarations to Rust, while helpers wrap inline functions and complex macros that bindgen cannot expose directly. Safe abstractions are expected to encapsulate unsafe calls and document safety requirements.

This structure creates a natural dependency chain from C symbols to generated bindings, unsafe call sites, and public safe Rust APIs. BindDrift makes that chain explicit.

## 3. Motivating Examples

The final paper will include cases for signature drift, layout drift, helper drift, nullability drift, ownership/refcount drift, and sleepability drift. Case skeletons are generated under the paper case-study workflow and are filled from replay warnings plus manual review.

## 4. Problem Definition

BindDrift defines cross-language API and contract drift as a change in a Linux C API surface or behavioral indicator that reaches Rust-for-Linux bindings or safe abstractions. The prototype classifies drift into Tier 1 objective drift and Tier 2 indicator-based contract drift.

Tier 1 includes function signatures, struct fields, layout facts, constants, and helper wrappers. Tier 2 includes nullability, error codes, ownership/refcounting, allocation/free pairing, and sleepability.

## 5. Design

BindDrift has four stages: extraction, graph construction, detection, and ranking.

The extractors collect version metadata, generated binding facts, Rust wrapper usage, C API declarations, and behavior indicators. The graph builder links C functions and macros to Rust bindings, unsafe call sites, safety comments, and public safe APIs. Detectors compare facts across versions or generate indicator-based warnings for contract risks. The ranker scores warnings by drift severity, Rust exposure, unsafe proximity, contract relevance, helper involvement, historical confidence, and build-breakage likelihood.

## 6. Implementation

The artifact is a Python command-line tool backed by SQLite and JSONL. It treats the Linux tree as an input and stores mutable experiment state outside the source tree. Generated Rust bindings are read from the kernel object tree because they are build artifacts.

## 7. Evaluation

The evaluation plan measures drift prevalence, build-breakage prediction, wrapper-fix prediction, semantic warning quality, baselines, and ablations. The current pilot pipeline generates the evaluation table schema and wrapper-fix candidates. Full precision and recall require a replay dataset and manual labels.

## 8. Case Studies

Each case study records the C-side change, Rust dependency, compiler catchability, BindDrift warning, evidence, impact, and general lesson. The paper will include at least five cases, with at least two semantic cases that are not fully caught by compilation.

## 9. Discussion

BindDrift is intentionally conservative. Tier 2 warnings are stale-contract review targets, not confirmed bugs. This framing makes the prototype useful for prioritization while avoiding unsound claims about fully proving Rust abstraction correctness.

## 10. Threats To Validity

Toolchain differences can produce false drift, so the artifact records compiler and bindgen versions. Regex-based fallback parsing is incomplete, so important results require sampling or AST-backed validation. Manual review is subjective, so the intended evaluation uses explicit labels and reviewer notes. The initial scope focuses on Linux mainline, Rust-for-Linux, and x86_64.

## 11. Related Work

The final version will compare BindDrift with API evolution, binding generation, cross-language static analysis, Rust-for-Linux empirical studies, and kernel bug-finding work.

## 12. Conclusion

BindDrift turns Rust-for-Linux cross-language dependencies into an explicit graph and uses that graph to detect and rank API and contract drift. The artifact supports reproducible replay and manual review while keeping the paper claim to warning quality and prioritization.
