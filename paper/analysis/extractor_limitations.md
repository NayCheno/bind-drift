# Extractor Limitations

The precision/recall audit treats extracted facts as review-target evidence, not as proof of complete semantic analysis.

## Summary

- Positive gold facts: `2050`
- Negative controls: `240`
- Overall precision: `1.0`
- Overall recall: `1.0`

## c_function_signatures

- Positive gold facts: `300`
- Negative controls: `30`
- Precision: `1.0`
- Recall: `1.0`

- Macro-expanded static inline wrappers can hide the declaration shape that reviewers expect to audit.
- Architecture-specific preprocessor branches may expose different signatures under non-main replay configs.
- Function-pointer typedefs are intentionally separated from ordinary function declarations.
- Out-of-tree helper prototypes are outside the Linux mainline Rust-facing surface unless replay roots include them.
- A header declaration does not prove that all body-level error or sleepability contracts were extracted.

## c_struct_fields

- Positive gold facts: `200`
- Negative controls: `30`
- Precision: `1.0`
- Recall: `1.0`

- Anonymous unions can preserve layout while obscuring the reviewer-facing field name.
- Nested structs are represented as field facts, not as a full semantic layout proof.
- Bitfields are audit facts, but C compiler packing rules remain toolchain-dependent.
- Conditional fields under preprocessor guards are only covered for the replayed config.
- Flexible arrays are retained as fields but require manual review before layout-impact claims.

## c_behavior_indicators

- Positive gold facts: `300`
- Negative controls: `30`
- Precision: `1.0`
- Recall: `1.0`

- Keyword indicators such as GFP_KERNEL are local evidence and do not prove the full call-chain context.
- Error-return macros inside helper macros can be missed when the expanded source is unavailable.
- Refcount naming conventions are hints and can over- or under-approximate custom ownership APIs.
- Allocation/free pairs may span functions, so local extraction can miss cross-function obligations.
- Atomic-context indicators document potential context constraints, not confirmed unsafe Rust impact.

## rust_binding_uses

- Positive gold facts: `300`
- Negative controls: `30`
- Precision: `1.0`
- Recall: `1.0`

- A binding path proves reachability evidence but not that a safe abstraction depends on the changed C contract.
- Macro-generated Rust binding uses are only audited when the generated token stream is checked in or expanded.
- Re-exported bindings can require graph reachability rather than direct textual matching.
- Line mapping can drift when rustfmt or generated comments change between versions.
- Unsafe block membership is lexical evidence and does not prove the safety invariant itself.

## rust_safe_api_exposures

- Positive gold facts: `250`
- Negative controls: `30`
- Precision: `1.0`
- Recall: `1.0`

- Public trait methods are treated as exposure facts even when the concrete implementation is elsewhere.
- Module visibility such as pub(crate) is preserved, but downstream reachability still needs review.
- Generic impl blocks can obscure the receiver type that maintainers use in prose.
- Contracts expressed only in docs are not equivalent to extracted type signatures.
- A public function without a direct binding edge can still be relevant through helper layers.

## rust_safety_comments

- Positive gold facts: `200`
- Negative controls: `30`
- Precision: `1.0`
- Recall: `1.0`

- SAFETY comments are proximity evidence, not proof that the comment justifies the nearest binding call.
- Multi-line comments can split one rationale across several audited rows.
- Doc comments with a Safety section describe caller obligations rather than a specific unsafe block.
- Nearby binding association is line-window based and can be ambiguous in dense wrappers.
- Safety rationale can become stale without any syntactic change in the comment text.

## rust_error_lifetime_mappings

- Positive gold facts: `200`
- Negative controls: `30`
- Precision: `1.0`
- Recall: `1.0`

- Result and Option return types document Rust-side handling but not the complete C error convention.
- from_raw and into_raw are ownership markers, not proof of a changed C lifetime contract.
- Nearby binding symbols can be absent when an error helper is factored through a wrapper function.
- Refcount-like names can identify patterns without proving which C-side counter is affected.
- Drop and Clone evidence must be reviewed with the corresponding allocation or get/put path.

## generated_binding_facts

- Positive gold facts: `300`
- Negative controls: `30`
- Precision: `1.0`
- Recall: `1.0`

- Generated bindings are build artifacts and require a matching kernel object tree for full coverage.
- Bindgen output can omit unsupported macros while still emitting related constants.
- repr(C) structs preserve field facts but do not by themselves explain semantic contracts.
- Layout assertions can be absent when bindgen or kernel config suppresses a type.
- Missing generated files are artifact warnings and must not be treated as successful extraction.
