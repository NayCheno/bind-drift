# Reviewer Disagreement Examples

Source: `data/replay/latest/pooled_review_labels.csv`

## 1. W-000003 refcount_inc

- Pair: `latest-p002-v6.2-to-v6.3`
- Type: `SignatureDrift`
- Reviewer 1: `TRUE_WRAPPER_FIX` - Rust exposure reaches clone, and wrapper-fix evidence points to the same symbol, subsystem, or Rust exposure path. Direct C source is missing, so this is a wrapper-fix finding rather than semantic-drift proof.
- Reviewer 2: `UNCLEAR` - refcount_inc has Rust unsafe_wrapper exposure and broad/plausible context, but lacks direct same-symbol wrapper evidence or complete old/new C/binding proof.
- Adjudicated: `FALSE_POSITIVE`
- Adjudication: refcount_inc: broad-family wrapper evidence is auxiliary only. Without direct same-symbol/same-contract proof or a semantic C-to-Rust contract chain, the warning is unsupported as a Rust-impact target.

## 2. W-000001 ERR_PTR

- Pair: `latest-p003-v6.3-to-v6.4`
- Type: `SignatureDrift`
- Reviewer 1: `TRUE_WRAPPER_FIX` - Rust exposure reaches Error::to_errno, and wrapper-fix evidence points to the same symbol, subsystem, or Rust exposure path. Direct C source is missing, so this is a wrapper-fix finding rather than semantic-drift proof.
- Reviewer 2: `UNCLEAR` - ERR_PTR has Rust safe_api exposure and broad/plausible context, but lacks direct same-symbol wrapper evidence or complete old/new C/binding proof.
- Adjudicated: `FALSE_POSITIVE`
- Adjudication: ERR_PTR: broad-family wrapper evidence is auxiliary only. Without direct same-symbol/same-contract proof or a semantic C-to-Rust contract chain, the warning is unsupported as a Rust-impact target.

## 3. W-000002 IS_ERR

- Pair: `latest-p003-v6.3-to-v6.4`
- Type: `SignatureDrift`
- Reviewer 1: `TRUE_WRAPPER_FIX` - Rust exposure reaches to_result, and wrapper-fix evidence points to the same symbol, subsystem, or Rust exposure path. Direct C source is missing, so this is a wrapper-fix finding rather than semantic-drift proof.
- Reviewer 2: `UNCLEAR` - IS_ERR has Rust safe_api exposure and broad/plausible context, but lacks direct same-symbol wrapper evidence or complete old/new C/binding proof.
- Adjudicated: `FALSE_POSITIVE`
- Adjudication: IS_ERR: broad-family wrapper evidence is auxiliary only. Without direct same-symbol/same-contract proof or a semantic C-to-Rust contract chain, the warning is unsupported as a Rust-impact target.

## 4. W-000001 compat_ptr_ioctl

- Pair: `latest-p006-v6.6-to-v6.7`
- Type: `SignatureDrift`
- Reviewer 1: `FALSE_POSITIVE` - Evidence for compat_ptr_ioctl is generated-binding/layout-only or lacks direct old/new C source, and Rust exposure is only binding_use_only. No build or direct wrapper-fix evidence supports a Rust-impact target.
- Reviewer 2: `TRUE_WRAPPER_FIX` - Direct same-symbol wrapper oracle is present for compat_ptr_ioctl; later Rust wrapper/helper evidence addresses the same warned symbol or contract. Rust exposure level: binding_use_only.
- Adjudicated: `TRUE_WRAPPER_FIX`
- Adjudication: compat_ptr_ioctl: direct same-symbol/same-contract wrapper oracle is present, so the later Rust wrapper/helper/binding change supports the warned drift.

## 5. W-000003 mdiobus_write

- Pair: `latest-p007-v6.7-to-v6.8`
- Type: `SignatureDrift`
- Reviewer 1: `TRUE_WRAPPER_FIX` - Rust exposure reaches Device::write, and wrapper-fix evidence points to the same symbol, subsystem, or Rust exposure path. Direct C source is missing, so this is a wrapper-fix finding rather than semantic-drift proof.
- Reviewer 2: `UNCLEAR` - mdiobus_write has Rust safe_api exposure and broad/plausible context, but lacks direct same-symbol wrapper evidence or complete old/new C/binding proof.
- Adjudicated: `FALSE_POSITIVE`
- Adjudication: mdiobus_write: broad-family wrapper evidence is auxiliary only. Without direct same-symbol/same-contract proof or a semantic C-to-Rust contract chain, the warning is unsupported as a Rust-impact target.

## 6. W-000007 device

- Pair: `latest-p007-v6.7-to-v6.8`
- Type: `FieldDrift`
- Reviewer 1: `FALSE_POSITIVE` - Evidence for device is generated-binding/layout-only or lacks direct old/new C source, and Rust exposure is only binding_use_only. No build or direct wrapper-fix evidence supports a Rust-impact target.
- Reviewer 2: `TRUE_WRAPPER_FIX` - Direct same-symbol wrapper oracle is present for device; later Rust wrapper/helper evidence addresses the same warned symbol or contract. Rust exposure level: binding_use_only.
- Adjudicated: `TRUE_WRAPPER_FIX`
- Adjudication: device: direct same-symbol/same-contract wrapper oracle is present, so the later Rust wrapper/helper/binding change supports the warned drift.

## 7. W-000005 firmware_request_nowarn

- Pair: `latest-p010-v6.10-to-v6.11`
- Type: `SignatureDrift`
- Reviewer 1: `TRUE_WRAPPER_FIX` - Rust exposure reaches request_nowarn, and wrapper-fix evidence points to the same symbol, subsystem, or Rust exposure path. Direct C source is missing, so this is a wrapper-fix finding rather than semantic-drift proof.
- Reviewer 2: `UNCLEAR` - firmware_request_nowarn has Rust unsafe_wrapper exposure and broad/plausible context, but lacks direct same-symbol wrapper evidence or complete old/new C/binding proof.
- Adjudicated: `FALSE_POSITIVE`
- Adjudication: firmware_request_nowarn: broad-family wrapper evidence is auxiliary only. Without direct same-symbol/same-contract proof or a semantic C-to-Rust contract chain, the warning is unsupported as a Rust-impact target.

## 8. W-000002 IS_ERR

- Pair: `latest-p012-v6.12-to-v6.13`
- Type: `SignatureDrift`
- Reviewer 1: `TRUE_WRAPPER_FIX` - Rust exposure reaches to_result, and wrapper-fix evidence points to the same symbol, subsystem, or Rust exposure path. Direct C source is missing, so this is a wrapper-fix finding rather than semantic-drift proof.
- Reviewer 2: `UNCLEAR` - IS_ERR has Rust safe_api exposure and broad/plausible context, but lacks direct same-symbol wrapper evidence or complete old/new C/binding proof.
- Adjudicated: `FALSE_POSITIVE`
- Adjudication: IS_ERR: broad-family wrapper evidence is auxiliary only. Without direct same-symbol/same-contract proof or a semantic C-to-Rust contract chain, the warning is unsupported as a Rust-impact target.

## 9. W-000003 PTR_ERR

- Pair: `latest-p012-v6.12-to-v6.13`
- Type: `SignatureDrift`
- Reviewer 1: `TRUE_WRAPPER_FIX` - Rust exposure reaches to_result, and wrapper-fix evidence points to the same symbol, subsystem, or Rust exposure path. Direct C source is missing, so this is a wrapper-fix finding rather than semantic-drift proof.
- Reviewer 2: `UNCLEAR` - PTR_ERR has Rust safe_api exposure and broad/plausible context, but lacks direct same-symbol wrapper evidence or complete old/new C/binding proof.
- Adjudicated: `FALSE_POSITIVE`
- Adjudication: PTR_ERR: broad-family wrapper evidence is auxiliary only. Without direct same-symbol/same-contract proof or a semantic C-to-Rust contract chain, the warning is unsupported as a Rust-impact target.

## 10. W-000004 REFCOUNT_INIT

- Pair: `latest-p012-v6.12-to-v6.13`
- Type: `SignatureDrift`
- Reviewer 1: `TRUE_WRAPPER_FIX` - Rust exposure reaches Arc<T>::new, and wrapper-fix evidence points to the same symbol, subsystem, or Rust exposure path. Direct C source is missing, so this is a wrapper-fix finding rather than semantic-drift proof.
- Reviewer 2: `UNCLEAR` - REFCOUNT_INIT has Rust safe_api exposure and broad/plausible context, but lacks direct same-symbol wrapper evidence or complete old/new C/binding proof.
- Adjudicated: `FALSE_POSITIVE`
- Adjudication: REFCOUNT_INIT: broad-family wrapper evidence is auxiliary only. Without direct same-symbol/same-contract proof or a semantic C-to-Rust contract chain, the warning is unsupported as a Rust-impact target.
