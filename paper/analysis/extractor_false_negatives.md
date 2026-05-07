# Extractor False Negatives

False negatives are gold facts with `expected_present=true` whose exact extracted-fact identity is missing from the current database.

## Overall

- False negatives: `0`
- Negative-control lookup hits: `0`
- Overall recall: `1.0`

## Taxonomy

- Parser coverage gap: the source fact is present in the gold set but absent from the extractor table.
- Line or symbol drift: the source fact exists but no longer matches the adjudicated identity.
- Generated artifact gap: expected bindgen output is missing from the object-tree snapshot.
- Proximity association gap: Rust comments, unsafe calls, or binding uses moved outside the extractor window.
- Configuration gap: the replay config no longer exposes the expected C or generated Rust fact.

## Observed Examples

- No false negatives were observed in the checked-in gold set.

## Per Extractor

- `c_function_signatures`: FN `0`, TP `300`
- `c_struct_fields`: FN `0`, TP `200`
- `c_behavior_indicators`: FN `0`, TP `300`
- `rust_binding_uses`: FN `0`, TP `300`
- `rust_safe_api_exposures`: FN `0`, TP `250`
- `rust_safety_comments`: FN `0`, TP `200`
- `rust_error_lifetime_mappings`: FN `0`, TP `200`
- `generated_binding_facts`: FN `0`, TP `300`
