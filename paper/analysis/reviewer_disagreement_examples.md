# Reviewer Disagreement Examples

Source: `data/replay/latest/pooled_review_labels.csv`

## 1. W-000001 REFCOUNT_INIT

- Pair: `latest-p002-v6.2-to-v6.3`
- Type: `SignatureDrift`
- Reviewer 1: `BENIGN_DRIFT` - C-side drift and Rust exposure exist for REFCOUNT_INIT, but wrapper evidence is broad/not exact and semantic impact is not established.
- Reviewer 2: `UNCLEAR` - Broad-family wrapper evidence plus Rust contract evidence triggers UNCLEAR; direct C evidence is not required to be absent.
- Adjudicated: `BENIGN_DRIFT`
- Adjudication: Reviewer 1 BENIGN_DRIFT vs Reviewer 2 UNCLEAR falls in the broad-family wrapper/Rust-exposure calibration class; real context exists, but no direct same-contract wrapper oracle or semantic-drift rule is satisfied, so BENIGN_DRIFT per v3 policy.

## 2. W-000002 refcount_dec_and_test

- Pair: `latest-p002-v6.2-to-v6.3`
- Type: `SignatureDrift`
- Reviewer 1: `BENIGN_DRIFT` - C-side drift and Rust exposure exist for refcount_dec_and_test, but wrapper evidence is broad/not exact and semantic impact is not established.
- Reviewer 2: `UNCLEAR` - Broad-family wrapper evidence plus Rust contract evidence triggers UNCLEAR; direct C evidence is not required to be absent.
- Adjudicated: `BENIGN_DRIFT`
- Adjudication: Reviewer 1 BENIGN_DRIFT vs Reviewer 2 UNCLEAR falls in the broad-family wrapper/Rust-exposure calibration class; real context exists, but no direct same-contract wrapper oracle or semantic-drift rule is satisfied, so BENIGN_DRIFT per v3 policy.

## 3. W-000003 refcount_inc

- Pair: `latest-p002-v6.2-to-v6.3`
- Type: `SignatureDrift`
- Reviewer 1: `BENIGN_DRIFT` - C-side drift and Rust exposure exist for refcount_inc, but wrapper evidence is broad/not exact and semantic impact is not established.
- Reviewer 2: `UNCLEAR` - Broad-family wrapper evidence plus Rust contract evidence triggers UNCLEAR; direct C evidence is not required to be absent.
- Adjudicated: `BENIGN_DRIFT`
- Adjudication: Reviewer 1 BENIGN_DRIFT vs Reviewer 2 UNCLEAR falls in the broad-family wrapper/Rust-exposure calibration class; real context exists, but no direct same-contract wrapper oracle or semantic-drift rule is satisfied, so BENIGN_DRIFT per v3 policy.

## 4. W-000001 ERR_PTR

- Pair: `latest-p003-v6.3-to-v6.4`
- Type: `SignatureDrift`
- Reviewer 1: `BENIGN_DRIFT` - C-side drift and Rust exposure exist for ERR_PTR, but wrapper evidence is broad/not exact and semantic impact is not established.
- Reviewer 2: `UNCLEAR` - Broad-family wrapper evidence plus Rust contract evidence triggers UNCLEAR; direct C evidence is not required to be absent.
- Adjudicated: `BENIGN_DRIFT`
- Adjudication: Reviewer 1 BENIGN_DRIFT vs Reviewer 2 UNCLEAR falls in the broad-family wrapper/Rust-exposure calibration class; real context exists, but no direct same-contract wrapper oracle or semantic-drift rule is satisfied, so BENIGN_DRIFT per v3 policy.

## 5. W-000002 IS_ERR

- Pair: `latest-p003-v6.3-to-v6.4`
- Type: `SignatureDrift`
- Reviewer 1: `BENIGN_DRIFT` - C-side drift and Rust exposure exist for IS_ERR, but wrapper evidence is broad/not exact and semantic impact is not established.
- Reviewer 2: `UNCLEAR` - Broad-family wrapper evidence plus Rust contract evidence triggers UNCLEAR; direct C evidence is not required to be absent.
- Adjudicated: `BENIGN_DRIFT`
- Adjudication: Reviewer 1 BENIGN_DRIFT vs Reviewer 2 UNCLEAR falls in the broad-family wrapper/Rust-exposure calibration class; real context exists, but no direct same-contract wrapper oracle or semantic-drift rule is satisfied, so BENIGN_DRIFT per v3 policy.

## 6. W-000003 PTR_ERR

- Pair: `latest-p003-v6.3-to-v6.4`
- Type: `SignatureDrift`
- Reviewer 1: `BENIGN_DRIFT` - C-side drift and Rust exposure exist for PTR_ERR, but wrapper evidence is broad/not exact and semantic impact is not established.
- Reviewer 2: `UNCLEAR` - Broad-family wrapper evidence plus Rust contract evidence triggers UNCLEAR; direct C evidence is not required to be absent.
- Adjudicated: `BENIGN_DRIFT`
- Adjudication: Reviewer 1 BENIGN_DRIFT vs Reviewer 2 UNCLEAR falls in the broad-family wrapper/Rust-exposure calibration class; real context exists, but no direct same-contract wrapper oracle or semantic-drift rule is satisfied, so BENIGN_DRIFT per v3 policy.

## 7. W-000004 put_task_struct

- Pair: `latest-p003-v6.3-to-v6.4`
- Type: `SignatureDrift`
- Reviewer 1: `BENIGN_DRIFT` - C-side drift and Rust exposure exist for put_task_struct, but wrapper evidence is broad/not exact and semantic impact is not established.
- Reviewer 2: `UNCLEAR` - Broad-family wrapper evidence plus Rust contract evidence triggers UNCLEAR; direct C evidence is not required to be absent.
- Adjudicated: `BENIGN_DRIFT`
- Adjudication: Reviewer 1 BENIGN_DRIFT vs Reviewer 2 UNCLEAR falls in the broad-family wrapper/Rust-exposure calibration class; real context exists, but no direct same-contract wrapper oracle or semantic-drift rule is satisfied, so BENIGN_DRIFT per v3 policy.

## 8. W-000002 mdiobus_read

- Pair: `latest-p007-v6.7-to-v6.8`
- Type: `SignatureDrift`
- Reviewer 1: `BENIGN_DRIFT` - C-side drift and Rust exposure exist for mdiobus_read, but wrapper evidence is broad/not exact and semantic impact is not established.
- Reviewer 2: `UNCLEAR` - Broad-family wrapper evidence plus Rust contract evidence triggers UNCLEAR; direct C evidence is not required to be absent.
- Adjudicated: `BENIGN_DRIFT`
- Adjudication: Reviewer 1 BENIGN_DRIFT vs Reviewer 2 UNCLEAR falls in the broad-family wrapper/Rust-exposure calibration class; real context exists, but no direct same-contract wrapper oracle or semantic-drift rule is satisfied, so BENIGN_DRIFT per v3 policy.

## 9. W-000003 mdiobus_write

- Pair: `latest-p007-v6.7-to-v6.8`
- Type: `SignatureDrift`
- Reviewer 1: `BENIGN_DRIFT` - C-side drift and Rust exposure exist for mdiobus_write, but wrapper evidence is broad/not exact and semantic impact is not established.
- Reviewer 2: `UNCLEAR` - Broad-family wrapper evidence plus Rust contract evidence triggers UNCLEAR; direct C evidence is not required to be absent.
- Adjudicated: `BENIGN_DRIFT`
- Adjudication: Reviewer 1 BENIGN_DRIFT vs Reviewer 2 UNCLEAR falls in the broad-family wrapper/Rust-exposure calibration class; real context exists, but no direct same-contract wrapper oracle or semantic-drift rule is satisfied, so BENIGN_DRIFT per v3 policy.

## 10. W-000003 device_add_disk

- Pair: `latest-p010-v6.10-to-v6.11`
- Type: `SignatureDrift`
- Reviewer 1: `BENIGN_DRIFT` - C-side drift and Rust exposure exist for device_add_disk, but wrapper evidence is broad/not exact and semantic impact is not established.
- Reviewer 2: `UNCLEAR` - Broad-family wrapper evidence plus Rust contract evidence triggers UNCLEAR; direct C evidence is not required to be absent.
- Adjudicated: `BENIGN_DRIFT`
- Adjudication: Reviewer 1 BENIGN_DRIFT vs Reviewer 2 UNCLEAR falls in the broad-family wrapper/Rust-exposure calibration class; real context exists, but no direct same-contract wrapper oracle or semantic-drift rule is satisfied, so BENIGN_DRIFT per v3 policy.

## 11. W-000004 errno_to_blk_status

- Pair: `latest-p010-v6.10-to-v6.11`
- Type: `SignatureDrift`
- Reviewer 1: `BENIGN_DRIFT` - C-side drift and Rust exposure exist for errno_to_blk_status, but wrapper evidence is broad/not exact and semantic impact is not established.
- Reviewer 2: `UNCLEAR` - Broad-family wrapper evidence plus Rust contract evidence triggers UNCLEAR; direct C evidence is not required to be absent.
- Adjudicated: `BENIGN_DRIFT`
- Adjudication: Reviewer 1 BENIGN_DRIFT vs Reviewer 2 UNCLEAR falls in the broad-family wrapper/Rust-exposure calibration class; real context exists, but no direct same-contract wrapper oracle or semantic-drift rule is satisfied, so BENIGN_DRIFT per v3 policy.

## 12. W-000005 firmware_request_nowarn

- Pair: `latest-p010-v6.10-to-v6.11`
- Type: `SignatureDrift`
- Reviewer 1: `BENIGN_DRIFT` - C-side drift and Rust exposure exist for firmware_request_nowarn, but wrapper evidence is broad/not exact and semantic impact is not established.
- Reviewer 2: `UNCLEAR` - Broad-family wrapper evidence plus Rust contract evidence triggers UNCLEAR; direct C evidence is not required to be absent.
- Adjudicated: `BENIGN_DRIFT`
- Adjudication: Reviewer 1 BENIGN_DRIFT vs Reviewer 2 UNCLEAR falls in the broad-family wrapper/Rust-exposure calibration class; real context exists, but no direct same-contract wrapper oracle or semantic-drift rule is satisfied, so BENIGN_DRIFT per v3 policy.

## 13. W-000007 request_firmware

- Pair: `latest-p010-v6.10-to-v6.11`
- Type: `SignatureDrift`
- Reviewer 1: `BENIGN_DRIFT` - C-side drift and Rust exposure exist for request_firmware, but wrapper evidence is broad/not exact and semantic impact is not established.
- Reviewer 2: `UNCLEAR` - Broad-family wrapper evidence plus Rust contract evidence triggers UNCLEAR; direct C evidence is not required to be absent.
- Adjudicated: `BENIGN_DRIFT`
- Adjudication: Reviewer 1 BENIGN_DRIFT vs Reviewer 2 UNCLEAR falls in the broad-family wrapper/Rust-exposure calibration class; real context exists, but no direct same-contract wrapper oracle or semantic-drift rule is satisfied, so BENIGN_DRIFT per v3 policy.

## 14. W-000001 ERR_PTR

- Pair: `latest-p012-v6.12-to-v6.13`
- Type: `SignatureDrift`
- Reviewer 1: `BENIGN_DRIFT` - C-side drift and Rust exposure exist for ERR_PTR, but wrapper evidence is broad/not exact and semantic impact is not established.
- Reviewer 2: `UNCLEAR` - Broad-family wrapper evidence plus Rust contract evidence triggers UNCLEAR; direct C evidence is not required to be absent.
- Adjudicated: `BENIGN_DRIFT`
- Adjudication: Reviewer 1 BENIGN_DRIFT vs Reviewer 2 UNCLEAR falls in the broad-family wrapper/Rust-exposure calibration class; real context exists, but no direct same-contract wrapper oracle or semantic-drift rule is satisfied, so BENIGN_DRIFT per v3 policy.

## 15. W-000002 IS_ERR

- Pair: `latest-p012-v6.12-to-v6.13`
- Type: `SignatureDrift`
- Reviewer 1: `BENIGN_DRIFT` - C-side drift and Rust exposure exist for IS_ERR, but wrapper evidence is broad/not exact and semantic impact is not established.
- Reviewer 2: `UNCLEAR` - Broad-family wrapper evidence plus Rust contract evidence triggers UNCLEAR; direct C evidence is not required to be absent.
- Adjudicated: `BENIGN_DRIFT`
- Adjudication: Reviewer 1 BENIGN_DRIFT vs Reviewer 2 UNCLEAR falls in the broad-family wrapper/Rust-exposure calibration class; real context exists, but no direct same-contract wrapper oracle or semantic-drift rule is satisfied, so BENIGN_DRIFT per v3 policy.

## 16. W-000003 PTR_ERR

- Pair: `latest-p012-v6.12-to-v6.13`
- Type: `SignatureDrift`
- Reviewer 1: `BENIGN_DRIFT` - C-side drift and Rust exposure exist for PTR_ERR, but wrapper evidence is broad/not exact and semantic impact is not established.
- Reviewer 2: `UNCLEAR` - Broad-family wrapper evidence plus Rust contract evidence triggers UNCLEAR; direct C evidence is not required to be absent.
- Adjudicated: `BENIGN_DRIFT`
- Adjudication: Reviewer 1 BENIGN_DRIFT vs Reviewer 2 UNCLEAR falls in the broad-family wrapper/Rust-exposure calibration class; real context exists, but no direct same-contract wrapper oracle or semantic-drift rule is satisfied, so BENIGN_DRIFT per v3 policy.

## 17. W-000004 REFCOUNT_INIT

- Pair: `latest-p012-v6.12-to-v6.13`
- Type: `SignatureDrift`
- Reviewer 1: `BENIGN_DRIFT` - C-side drift and Rust exposure exist for REFCOUNT_INIT, but wrapper evidence is broad/not exact and semantic impact is not established.
- Reviewer 2: `UNCLEAR` - Broad-family wrapper evidence plus Rust contract evidence triggers UNCLEAR; direct C evidence is not required to be absent.
- Adjudicated: `BENIGN_DRIFT`
- Adjudication: Reviewer 1 BENIGN_DRIFT vs Reviewer 2 UNCLEAR falls in the broad-family wrapper/Rust-exposure calibration class; real context exists, but no direct same-contract wrapper oracle or semantic-drift rule is satisfied, so BENIGN_DRIFT per v3 policy.

## 18. W-000014 current_euid

- Pair: `latest-p012-v6.12-to-v6.13`
- Type: `SignatureDrift`
- Reviewer 1: `BENIGN_DRIFT` - C-side drift and Rust exposure exist for current_euid, but wrapper evidence is broad/not exact and semantic impact is not established.
- Reviewer 2: `UNCLEAR` - Broad-family wrapper evidence plus Rust contract evidence triggers UNCLEAR; direct C evidence is not required to be absent.
- Adjudicated: `BENIGN_DRIFT`
- Adjudication: Reviewer 1 BENIGN_DRIFT vs Reviewer 2 UNCLEAR falls in the broad-family wrapper/Rust-exposure calibration class; real context exists, but no direct same-contract wrapper oracle or semantic-drift rule is satisfied, so BENIGN_DRIFT per v3 policy.

## 19. W-000015 current_user_ns

- Pair: `latest-p012-v6.12-to-v6.13`
- Type: `SignatureDrift`
- Reviewer 1: `BENIGN_DRIFT` - C-side drift and Rust exposure exist for current_user_ns, but wrapper evidence is broad/not exact and semantic impact is not established.
- Reviewer 2: `UNCLEAR` - Broad-family wrapper evidence plus Rust contract evidence triggers UNCLEAR; direct C evidence is not required to be absent.
- Adjudicated: `BENIGN_DRIFT`
- Adjudication: Reviewer 1 BENIGN_DRIFT vs Reviewer 2 UNCLEAR falls in the broad-family wrapper/Rust-exposure calibration class; real context exists, but no direct same-contract wrapper oracle or semantic-drift rule is satisfied, so BENIGN_DRIFT per v3 policy.

## 20. W-000016 device_add_disk

- Pair: `latest-p012-v6.12-to-v6.13`
- Type: `SignatureDrift`
- Reviewer 1: `BENIGN_DRIFT` - C-side drift and Rust exposure exist for device_add_disk, but wrapper evidence is broad/not exact and semantic impact is not established.
- Reviewer 2: `UNCLEAR` - Broad-family wrapper evidence plus Rust contract evidence triggers UNCLEAR; direct C evidence is not required to be absent.
- Adjudicated: `BENIGN_DRIFT`
- Adjudication: Reviewer 1 BENIGN_DRIFT vs Reviewer 2 UNCLEAR falls in the broad-family wrapper/Rust-exposure calibration class; real context exists, but no direct same-contract wrapper oracle or semantic-drift rule is satisfied, so BENIGN_DRIFT per v3 policy.
