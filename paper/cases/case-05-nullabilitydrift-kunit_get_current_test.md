# NullabilityDrift Case Study

## One-Line Summary

`kunit_get_current_test` produced `W-000039` because C-side contract evidence reaches Rust-for-Linux wrapper code.

## C-Side Change

BindDrift observed `NullabilityDrift` evidence for `kunit_get_current_test`.

- Old indicators/value: `[]`
- New indicators/value: `['NULL_RETURN']`
- `/home/nya/workspace/bind-drift/vendor/linux/include/kunit/test-bug.h:44`: `return NULL;`
- `/home/nya/workspace/bind-drift/vendor/linux/include/kunit/test-bug.h:65`: `static inline struct kunit *kunit_get_current_test(void) { return NULL; }`

## Rust-Side Dependency

The symbol is used through Rust binding calls or nearby wrapper code.

- `/home/nya/workspace/bind-drift/vendor/linux/rust/kernel/kunit.rs:73` in `info`
- `/home/nya/workspace/bind-drift/vendor/linux/rust/kernel/kunit.rs:329` in `TestResult::in_kunit_test`
- `/home/nya/workspace/bind-drift/vendor/linux/rust/kernel/kunit.rs:72`: `// SAFETY: FFI call without safety requirements.`
- `/home/nya/workspace/bind-drift/vendor/linux/rust/kernel/kunit.rs:324`: `/// assert_eq!(mock_res, 100);`
- `/home/nya/workspace/bind-drift/vendor/linux/rust/kernel/kunit.rs:325`: `/// ````

## Why The Compiler Cannot Fully Catch It

This case is treated as a contract-review target. The type checker can validate the current call shape, but it does not verify that Rust wrapper assumptions about nullability, error representation, ownership, or context remain synchronized with C-side behavior.

## BindDrift Warning

- Warning: `W-000039`
- Drift type: `NullabilityDrift`
- C symbol: `kunit_get_current_test`
- Risk: `High`
- Score: `13.7`

## Evidence

The evidence above is copied from the ranked BindDrift warning report. The current artifact keeps this case within the warning/prioritization claim boundary.

## Impact

Single-version review candidate: no historical baseline was available for this warning, so the artifact does not claim a confirmed drift bug.

## Lesson

Safe Rust APIs can depend on C-side contracts that are not represented in the Rust function signature. BindDrift makes that dependency explicit so maintainers can prioritize review.
