# Extractor Failure And Limitation Taxonomy

Strict extractor audit error categories are reported per extractor. Limitation-focused negative controls are reviewed rows that keep the extracted fact separate from any completeness or confirmed-bug claim.

## Overall

- Total strict samples: `830`
- Promoted warning evidence samples: `150`
- Cohen's kappa: `1.0`
- Negative-control rows: `484`

## Parser Limitations

- `c_functions`: Header declarations and inline signatures are sampled as C API facts; the extractor does not prove body-level behavior or all call-site contracts.
- `c_behavior_indicators`: Behavior indicators are lexical or local-context signals and must be reviewed with surrounding C code before being treated as semantic contract drift.
- `rust_binding_uses`: A Rust binding reference establishes reachability evidence, not that the surrounding safe abstraction depends on the changed C contract.
- `rust_safe_api_exposures`: Safe API exposure extraction is signature-oriented and can miss contracts expressed outside the function body or module-local helper path.
- `rust_error_mappings`: Error and nullability mappings are proximity facts; nearby C bindings are hints, not proof of an exact return-convention dependency.
- `rust_lifetime_facts`: Lifetime and ownership facts identify Rust-side patterns but do not prove that a specific C-side refcount or allocation rule changed.
- `promoted_warning_evidence`: Promoted warning evidence is sufficient for prioritization, but file-level or oracle-only context is reported as a limitation and not as a confirmed bug.

## Negative Controls

### c_behavior_indicators

- Count: `120`
- `LOCAL_KEYWORD_INDICATOR`: 120
- Example `c_behavior_indicators-906` `__kmalloc_index`: `LOCAL_KEYWORD_INDICATOR`
- Example `c_behavior_indicators-072` `__kmalloc_index`: `LOCAL_KEYWORD_INDICATOR`

### c_functions

- Count: `70`
- `HEADER_DECLARATION_WITHOUT_BODY`: 70
- Example `c_functions-050` `prepare_to_wait`: `HEADER_DECLARATION_WITHOUT_BODY`
- Example `c_functions-233` `kunit_suite_has_succeeded`: `HEADER_DECLARATION_WITHOUT_BODY`

### promoted_warning_evidence

- Count: `31`
- `FILE_LEVEL_ORACLE_ONLY_CONTEXT`: 31
- Example `promoted_warning_evidence-109` `device`: `FILE_LEVEL_ORACLE_ONLY_CONTEXT`
- Example `promoted_warning_evidence-116` `_find_last_bit`: `FILE_LEVEL_ORACLE_ONLY_CONTEXT`

### rust_binding_uses

- Count: `52`
- `BINDING_USE_OUTSIDE_UNSAFE_BLOCK`: 52
- Example `rust_binding_uses-054` `KERN_CONT`: `BINDING_USE_OUTSIDE_UNSAFE_BLOCK`
- Example `rust_binding_uses-025` `KERN_CONT`: `BINDING_USE_OUTSIDE_UNSAFE_BLOCK`

### rust_error_mappings

- Count: `51`
- `ERROR_MAPPING_WITHOUT_NEARBY_BINDING`: 51
- Example `rust_error_mappings-669` `RESULT_RETURN`: `ERROR_MAPPING_WITHOUT_NEARBY_BINDING`
- Example `rust_error_mappings-1847` `RESULT_RETURN`: `ERROR_MAPPING_WITHOUT_NEARBY_BINDING`

### rust_lifetime_facts

- Count: `71`
- `LIFETIME_FACT_WITHOUT_BINDING_EDGE`: 71
- Example `rust_lifetime_facts-180` `AS_PTR`: `LIFETIME_FACT_WITHOUT_BINDING_EDGE`
- Example `rust_lifetime_facts-076` `AS_PTR`: `LIFETIME_FACT_WITHOUT_BINDING_EDGE`

### rust_safe_api_exposures

- Count: `89`
- `SAFE_API_WITHOUT_BINDING_EDGE`: 89
- Example `rust_safe_api_exposures-805` `Error::to_kernel_errno`: `SAFE_API_WITHOUT_BINDING_EDGE`
- Example `rust_safe_api_exposures-476` `CStr::to_str`: `SAFE_API_WITHOUT_BINDING_EDGE`

## Observed Incorrect Rows

### c_behavior_indicators

- Precision: `1.0`
- Versions sampled: `20`
- Main errors: none in reviewed strict sample.

### c_functions

- Precision: `1.0`
- Versions sampled: `20`
- Main errors: none in reviewed strict sample.

### promoted_warning_evidence

- Precision: `1.0`
- Versions sampled: `16`
- Main errors: none in reviewed strict sample.

### rust_binding_uses

- Precision: `1.0`
- Versions sampled: `20`
- Main errors: none in reviewed strict sample.

### rust_error_mappings

- Precision: `1.0`
- Versions sampled: `19`
- Main errors: none in reviewed strict sample.

### rust_lifetime_facts

- Precision: `1.0`
- Versions sampled: `20`
- Main errors: none in reviewed strict sample.

### rust_safe_api_exposures

- Precision: `1.0`
- Versions sampled: `20`
- Main errors: none in reviewed strict sample.
