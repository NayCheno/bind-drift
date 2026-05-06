# Failure Analysis: LayoutFieldDrift for `kunit_case`

## Summary

`kunit_case` produced `W-000178` and is included as a negative/failure-analysis case with adjudicated label `FALSE_POSITIVE`.

## Old Version Evidence

- Version: `v6.17`
- Old value or indicators: `[{'name': 'run_case', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit)>'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'generate_params', 'type': '::core::option::Option<'}, {'name': 'attr', 'type': 'kunit_attributes'}, {'name': 'status', 'type': 'kunit_status'}, {'name': 'module_name', 'type': '*mut ffi::c_char'}, {'name': 'log', 'type': '*mut string_stream'}]`

## New Version Evidence

- Version: `v6.18`
- New value or indicators: `[{'name': 'run_case', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit)>'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'generate_params', 'type': '::core::option::Option<'}, {'name': 'attr', 'type': 'kunit_attributes'}, {'name': 'param_init', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit) -> ffi::c_int>'}, {'name': 'param_exit', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit)>'}, {'name': 'status', 'type': 'kunit_status'}, {'name': 'module_name', 'type': '*mut ffi::c_char'}, {'name': 'log', 'type': '*mut string_stream'}]`

## C-Side Diff

- Old indicators/value: `[{'name': 'run_case', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit)>'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'generate_params', 'type': '::core::option::Option<'}, {'name': 'attr', 'type': 'kunit_attributes'}, {'name': 'status', 'type': 'kunit_status'}, {'name': 'module_name', 'type': '*mut ffi::c_char'}, {'name': 'log', 'type': '*mut string_stream'}]`
- New indicators/value: `[{'name': 'run_case', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit)>'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'generate_params', 'type': '::core::option::Option<'}, {'name': 'attr', 'type': 'kunit_attributes'}, {'name': 'param_init', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit) -> ffi::c_int>'}, {'name': 'param_exit', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit)>'}, {'name': 'status', 'type': 'kunit_status'}, {'name': 'module_name', 'type': '*mut ffi::c_char'}, {'name': 'log', 'type': '*mut string_stream'}]`

## Rust-Side Dependency

- exposure `GENERATED_FROM`: `CStruct:kunit_case` -> `RustBindingStruct:kunit_case`
- exposure `HAS_SAFETY_COMMENT`: `RustBindingFunction:kunit_case` -> `RustSafetyComment:.binddrift/worktrees/v6.18/rust/kernel/kunit.rs:197`
- exposure `HAS_SAFETY_COMMENT`: `RustBindingFunction:kunit_case` -> `RustSafetyComment:.binddrift/worktrees/v6.18/rust/kernel/kunit.rs:218`
- exposure `HAS_SAFETY_COMMENT`: `RustBindingFunction:kunit_case` -> `RustSafetyComment:.binddrift/worktrees/v6.18/rust/kernel/kunit.rs:219`
- exposure `HAS_SAFETY_COMMENT`: `RustBindingFunction:kunit_case` -> `RustSafetyComment:.binddrift/worktrees/v6.18/rust/kernel/kunit.rs:220`
- `.binddrift/worktrees/v6.18/rust/kernel/kunit.rs:296` in `test_fn` (unsafe block)
- `.binddrift/worktrees/v6.18/rust/kernel/kunit.rs:202` in `is_test_result_ok`
- `.binddrift/worktrees/v6.18/rust/kernel/kunit.rs:203` in `is_test_result_ok`
- `.binddrift/worktrees/v6.18/rust/kernel/kunit.rs:223` in `kunit_case_null`
- `.binddrift/worktrees/v6.18/rust/kernel/kunit.rs:224` in `kunit_case_null`
- safe API `is_test_result_ok`
- `.binddrift/worktrees/v6.18/rust/kernel/kunit.rs:197`: `/// Use [`kunit_case_null`] to generate such a delimiter.`
- `.binddrift/worktrees/v6.18/rust/kernel/kunit.rs:218`: `/// Represents the NULL test case delimiter.`
- `.binddrift/worktrees/v6.18/rust/kernel/kunit.rs:219`: `///`
- wrapper_fix: `7f87c7a003125d5af5ec7abbbc0ac21b4a4661ae`
- wrapper_fix: `be97f3c82021239476ce32cddde32948c597753e`

## Safe API / Contract Assumption

The warning reaches a public safe Rust API, so the maintainer review question is whether that API's documented contract remains synchronized with the C-side behavior.

## Manual Review Label

- Adjudicated label: `FALSE_POSITIVE`
- Reviewer 1: `UNCLEAR` -- kunit_case reaches Rust safe or unsafe code, but the wrapper oracle is broad-family only and the packet lacks exact same-symbol/direct contract proof. This is plausible but not enough for TRUE_WRAPPER_FIX or semantic drift.
- Reviewer 2: `UNCLEAR` -- kunit_case has Rust safe_api exposure and broad/plausible context, but lacks direct same-symbol wrapper evidence or complete old/new C/binding proof.
- Adjudication: kunit_case: broad-family wrapper evidence is auxiliary only. Without direct same-symbol/same-contract proof or a semantic C-to-Rust contract chain, the warning is unsupported as a Rust-impact target.

## Why This Is Not Generated-Binding-Only

The case has Rust reachability or contract/oracle evidence beyond a generated binding delta; generated-binding-only rows are excluded from positive case selection.

## Why Compiler Alone Does Not Catch It

The compiler checks the current Rust/C binding shape. This case is about whether a Rust abstraction, helper, or safety invariant remains synchronized with an evolving C-side contract across versions.

## Alternative Explanation Considered

Review considered whether the warning should be promoted, but adjudication found the evidence benign, unsupported, or incomplete.

## Maintainer Review Implication

This case documents why similar high-scoring warnings need manual review before being counted as true positives.

## Reproduction Pointers

- Warning: `W-000178`
- Warning UID: `c6fedd40f4293a2cf97cd21b46968e2da0844c4ef8fcd202fe3a2c9a3cc04e23`
- Replay pair: `latest-p017-v6.17-to-v6.18`
- Drift type: `LayoutFieldDrift`
- C symbol: `kunit_case`
- Risk: `Medium`
- Score: `8.0`
