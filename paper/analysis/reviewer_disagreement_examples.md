# Reviewer Disagreement Examples

Source: `data/replay/latest/pooled_review_labels.csv`

## 1. W-000004 put_task_struct

- Pair: `latest-p003-v6.3-to-v6.4`
- Type: `SignatureDrift`
- Reviewer 1: `TRUE_WRAPPER_FIX` - put_task_struct is binding-only but reaches a Rust unsafe decrement path with refcount/lifetime evidence, and the later task/Kuid wrapper commit directly matches put_task_struct in task helper files.
- Reviewer 2: `UNCLEAR` - Rust refcount teardown reaches put_task_struct, but the cited later Kuid/task commit adds task UID helpers and does not show a change to the put_task_struct ownership path. Binding-only C evidence is insufficient for TRUE_* here.
- Adjudicated: `UNCLEAR`
- Adjudication: put_task_struct reaches a Rust unsafe refcount/lifetime path, but the cited later Kuid/task commit is not shown to change the put_task_struct ownership path. With only binding-level C drift and an indirect wrapper hit, the evidence is insufficient for TRUE_WRAPPER_FIX.

## 2. W-000002 kunit_case

- Pair: `latest-p006-v6.6-to-v6.7`
- Type: `FieldDrift`
- Reviewer 1: `TRUE_WRAPPER_FIX` - kunit_case field evidence shows log type changed, and commit be97f3c82021 removes explicit kunit_case null-field initialization in favor of zeroed(). That directly addresses the struct-initialization exposure.
- Reviewer 2: `BENIGN_DRIFT` - The packet shows a kunit_case field type change, but no Rust call site or safe API exposure is listed. Later KUnit hits are documentation or null-value cleanup, not evidence of stale Rust contract dependence.
- Adjudicated: `BENIGN_DRIFT`
- Adjudication: The kunit_case log field type appears to change, but the packet lists no Rust call site or safe API exposure. The later KUnit hits are documentation or zeroed-initialization cleanup and do not clearly fix the changed log-field contract, so no harmful Rust impact is supported.

## 3. W-000007 device

- Pair: `latest-p007-v6.7-to-v6.8`
- Type: `FieldDrift`
- Reviewer 1: `UNCLEAR` - The packet only shows binding-level struct device addition and no Rust call site or safe API exposure. Later oracle hits are broad device-related fixes, but the evidence does not tie them to this FieldDrift contract.
- Reviewer 2: `FALSE_POSITIVE` - The device field warning is based on binding-level old=[] versus a full new field list, with no Rust exposure. That looks like missing/generated binding data rather than supported C field drift.
- Adjudicated: `FALSE_POSITIVE`
- Adjudication: The device field warning shows old=[] and a full new struct list, no Rust exposure, and broad device oracle hits unrelated to a specific field. This looks like missing/generated binding data rather than supported field drift.

## 4. W-000008 request_firmware_direct

- Pair: `latest-p010-v6.10-to-v6.11`
- Type: `SignatureDrift`
- Reviewer 1: `UNCLEAR` - request_firmware_direct is binding-only with only a weak line-level Rust use. The firmware_loader fix mentions related functions but the packet does not show a direct wrapper path or fix for request_firmware_direct.
- Reviewer 2: `FALSE_POSITIVE` - The only Rust evidence for request_firmware_direct is a listed line in the FwFunc documentation/comment area, and the later soundness diff does not add a code path for it. This is not a supported Rust exposure.
- Adjudicated: `FALSE_POSITIVE`
- Adjudication: request_firmware_direct has only a weak listed Rust line with no real call path or safe API. The firmware_loader soundness fix mentions related functions but is not shown to add or fix a request_firmware_direct wrapper path.

## 5. W-000001 __mutex_init

- Pair: `latest-p011-v6.11-to-v6.12`
- Type: `SignatureDrift`
- Reviewer 1: `TRUE_WRAPPER_FIX` - __mutex_init has a parameter-name binding drift and reaches Rust mutex initialization. Commit d065cc76054d directly adds rust_helper___mutex_init for PREEMPT_RT, matching the symbol and helper path.
- Reviewer 2: `TRUE_BUILD_BREAKAGE` - The later mutex helper commit includes an explicit PREEMPT_RT build error for bindings::__mutex_init and adds rust_helper___mutex_init. That connects the warning symbol to objective build breakage.
- Adjudicated: `TRUE_BUILD_BREAKAGE`
- Adjudication: Reviewer 2 cites explicit E0425 build-error evidence for bindings::__mutex_init in rust/kernel/sync/lock/mutex.rs, and the packet has the same-symbol PREEMPT_RT helper fix in rust/helpers/mutex.c. Build breakage takes priority over the wrapper-fix label.
