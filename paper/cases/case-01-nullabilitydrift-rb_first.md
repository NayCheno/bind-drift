# NullabilityDrift Case Study

## One-Line Summary

`rb_first` produced `W-000053` because C-side contract evidence reaches Rust-for-Linux wrapper code.

## C-Side Change

BindDrift observed `NullabilityDrift` evidence for `rb_first`.

- Old indicators/value: `[]`
- New indicators/value: `['NULL_RETURN']`
- `/home/nya/workspace/bind-drift/vendor/linux/include/linux/rbtree.h:61`: `return NULL;`

## Rust-Side Dependency

The symbol is used through Rust binding calls or nearby wrapper code.

- `/home/nya/workspace/bind-drift/vendor/linux/rust/kernel/rbtree.rs:206` in `RBTree<K::iter`
- `/home/nya/workspace/bind-drift/vendor/linux/rust/kernel/rbtree.rs:209` in `RBTree<K::iter`
- `/home/nya/workspace/bind-drift/vendor/linux/rust/kernel/rbtree.rs:221` in `RBTree<K::iter_mut`
- `/home/nya/workspace/bind-drift/vendor/linux/rust/kernel/rbtree.rs:224` in `RBTree<K::iter_mut`
- `/home/nya/workspace/bind-drift/vendor/linux/rust/kernel/rbtree.rs:249` in `RBTree<K::cursor_front_mut`
- `/home/nya/workspace/bind-drift/vendor/linux/rust/kernel/rbtree.rs:208`: `// SAFETY: by the invariants, all pointers are valid.`
- `/home/nya/workspace/bind-drift/vendor/linux/rust/kernel/rbtree.rs:223`: `// SAFETY: by the invariants, all pointers are valid.`
- `/home/nya/workspace/bind-drift/vendor/linux/rust/kernel/rbtree.rs:245`: `/// Returns a cursor over the tree nodes, starting with the smallest key.`

## Why The Compiler Cannot Fully Catch It

This case is treated as a contract-review target. The type checker can validate the current call shape, but it does not verify that Rust wrapper assumptions about nullability, error representation, ownership, or context remain synchronized with C-side behavior.

## BindDrift Warning

- Warning: `W-000053`
- Drift type: `NullabilityDrift`
- C symbol: `rb_first`
- Risk: `High`
- Score: `15.7`

## Evidence

The evidence above is copied from the ranked BindDrift warning report. The current artifact keeps this case within the warning/prioritization claim boundary.

## Impact

Single-version review candidate: no historical baseline was available for this warning, so the artifact does not claim a confirmed drift bug.

## Lesson

Safe Rust APIs can depend on C-side contracts that are not represented in the Rust function signature. BindDrift makes that dependency explicit so maintainers can prioritize review.
