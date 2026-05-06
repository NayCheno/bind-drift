# Reviewer Disagreement Examples

Source: `data/replay/latest/pooled_review_labels.csv`

## 1. W-000001 compat_ptr_ioctl

- Pair: `latest-p006-v6.6-to-v6.7`
- Type: `SignatureDrift`
- Reviewer 1: `BENIGN_DRIFT` - Generated bindings show the symbol appearing, but Rust exposure is only a generated binding edge and build breakage is absent. The wrapper oracle is not enough by itself to show a same-contract fix.
- Reviewer 2: `FALSE_POSITIVE` - The packet supports only an added generated binding with no old C evidence and no Rust exposure beyond the binding edge. The wrapper oracle is undiffed and not enough for a TRUE label.
- Adjudicated: `FALSE_POSITIVE`
- Adjudication: The packet supports only generated binding/layout evidence for `compat_ptr_ioctl` with binding-only Rust exposure. There is no direct old/new C source diff, no build evidence, and the wrapper oracle is weak or broad.

## 2. W-000002 kunit_case

- Pair: `latest-p006-v6.6-to-v6.7`
- Type: `FieldDrift`
- Reviewer 1: `BENIGN_DRIFT` - Generated binding/layout evidence shows drift, but Rust exposure is only generated bindings and build breakage is absent. Without direct Rust use or a specific fix diff, the observed impact looks harmless.
- Reviewer 2: `FALSE_POSITIVE` - The old/new evidence is generated-binding-only and appears to be ffi namespace or type-rendering churn, not a concrete C API drift. Wrapper oracle text is not enough to rescue the warning without a matching diff.
- Adjudicated: `FALSE_POSITIVE`
- Adjudication: Old/new evidence for `kunit_case` is generated Rust type spelling churn, mainly `core::ffi` to `ffi`, not a supported C contract drift. Wrapper oracle text and absent build evidence do not rescue the warning.

## 3. W-000001 get_device

- Pair: `latest-p007-v6.7-to-v6.8`
- Type: `SignatureDrift`
- Reviewer 1: `BENIGN_DRIFT` - Generated bindings show the symbol appearing, but Rust exposure is only a generated binding edge and build breakage is absent. The wrapper oracle is not enough by itself to show a same-contract fix.
- Reviewer 2: `FALSE_POSITIVE` - The packet supports only an added generated binding with no old C evidence and no Rust exposure beyond the binding edge. The wrapper oracle is undiffed and not enough for a TRUE label.
- Adjudicated: `FALSE_POSITIVE`
- Adjudication: The packet supports only generated binding/layout evidence for `get_device` with binding-only Rust exposure. There is no direct old/new C source diff, no build evidence, and the wrapper oracle is weak or broad.

## 4. W-000004 phy_read_mmd

- Pair: `latest-p007-v6.7-to-v6.8`
- Type: `SignatureDrift`
- Reviewer 1: `BENIGN_DRIFT` - Generated bindings show the symbol appearing, but Rust exposure is only a generated binding edge and build breakage is absent. The wrapper oracle is not enough by itself to show a same-contract fix.
- Reviewer 2: `FALSE_POSITIVE` - The packet supports only an added generated binding with no old C evidence and no Rust exposure beyond the binding edge. The wrapper oracle is undiffed and not enough for a TRUE label.
- Adjudicated: `FALSE_POSITIVE`
- Adjudication: The packet supports only generated binding/layout evidence for `phy_read_mmd` with binding-only Rust exposure. There is no direct old/new C source diff, no build evidence, and the wrapper oracle is weak or broad.

## 5. W-000005 phy_write_mmd

- Pair: `latest-p007-v6.7-to-v6.8`
- Type: `SignatureDrift`
- Reviewer 1: `BENIGN_DRIFT` - Generated bindings show the symbol appearing, but Rust exposure is only a generated binding edge and build breakage is absent. The wrapper oracle is not enough by itself to show a same-contract fix.
- Reviewer 2: `FALSE_POSITIVE` - The packet supports only an added generated binding with no old C evidence and no Rust exposure beyond the binding edge. The wrapper oracle is undiffed and not enough for a TRUE label.
- Adjudicated: `FALSE_POSITIVE`
- Adjudication: The packet supports only generated binding/layout evidence for `phy_write_mmd` with binding-only Rust exposure. There is no direct old/new C source diff, no build evidence, and the wrapper oracle is weak or broad.
