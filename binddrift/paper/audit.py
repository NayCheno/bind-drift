from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any

from binddrift.artifact_paths import repo_relative, sanitize_local_paths
from binddrift.config import Config
from binddrift.db import connect, initialize
from binddrift.warnings import read_warnings


AUDIT_TARGETS = {
    "c_functions": 100,
    "rust_binding_uses": 100,
    "c_behavior_indicators": 100,
    "rust_error_mappings": 50,
    "rust_lifetime_facts": 50,
    "promoted_warnings": 50,
}

MIN_PRECISION = {
    "c_functions": 0.90,
    "rust_binding_uses": 0.90,
    "c_behavior_indicators": 0.75,
    "rust_error_mappings": 0.80,
    "rust_lifetime_facts": 0.75,
    "promoted_warning_evidence": 0.30,
}

ACCEPTANCE_TABLES = {
    "c_functions": "c_functions",
    "rust_binding_uses": "rust_binding_uses",
    "c_behavior_indicators": "c_behavior_indicators",
    "rust_error_mappings": "rust_error_mappings",
    "rust_lifetime_facts": "rust_lifetime_facts",
    "promoted_warning_evidence": "promoted_warnings",
}

ERROR_TYPES = {
    "WRONG_SYMBOL",
    "WRONG_SCOPE",
    "WRONG_LINE",
    "FALSE_INDICATOR",
    "MISSING_CONTEXT",
    "REGEX_ARTIFACT",
    "BINDGEN_ARTIFACT",
    "OTHER",
}

FIELDNAMES = [
    "sample_id",
    "table",
    "symbol",
    "file",
    "line",
    "extracted_fact",
    "is_correct",
    "corrected_fact",
    "error_type",
    "notes",
]
LABEL_FIELDS = ["is_correct", "corrected_fact", "error_type", "notes"]
SPLIT_REVIEW_FIELDS = ["sample_id", "is_correct", "error_type", "notes"]
SAMPLER_VERSION = "extractor-audit-v2"

STRICT_AUDIT_TARGETS = {
    "c_functions": 120,
    "c_behavior_indicators": 120,
    "rust_binding_uses": 120,
    "rust_safe_api_exposures": 120,
    "rust_error_mappings": 100,
    "rust_lifetime_facts": 100,
    "promoted_warning_evidence": 150,
}

STRICT_MIN_PRECISION = {
    "c_functions": 0.95,
    "c_behavior_indicators": 0.85,
    "rust_binding_uses": 0.90,
    "rust_safe_api_exposures": 0.85,
    "rust_error_mappings": 0.85,
    "rust_lifetime_facts": 0.85,
    "promoted_warning_evidence": 0.85,
}

STRICT_TARGET_PRECISION = {
    "c_functions": 0.98,
    "c_behavior_indicators": 0.90,
    "rust_binding_uses": 0.95,
    "rust_safe_api_exposures": 0.90,
    "rust_error_mappings": 0.90,
    "rust_lifetime_facts": 0.90,
    "promoted_warning_evidence": 0.90,
}

STRICT_ERROR_CATEGORIES = {
    "PARSE_ERROR",
    "SYMBOL_MISMATCH",
    "LINE_MISMATCH",
    "GENERATED_BINDING_CONFUSION",
    "COMMENT_ASSOCIATION_ERROR",
    "FALSE_USAGE_EDGE",
    "FALSE_CONTRACT_MAPPING",
    "MISSING_CONTEXT",
    "OTHER",
}

STRICT_FIELDS = [
    "sample_id",
    "extractor_name",
    "version",
    "audit_pair_id",
    "file",
    "line",
    "symbol",
    "extracted_fact",
    "raw_context",
    "control_label",
    "control_category",
    "reviewer1_label",
    "reviewer1_provenance",
    "reviewer2_label",
    "reviewer2_provenance",
    "adjudicated_label",
    "adjudication_provenance",
    "error_category",
    "notes",
]

STRICT_REVIEW_FIELDS = {
    "control_label",
    "control_category",
    "reviewer1_label",
    "reviewer1_provenance",
    "reviewer2_label",
    "reviewer2_provenance",
    "adjudicated_label",
    "adjudication_provenance",
    "error_category",
    "notes",
}

STRICT_NEGATIVE_CONTROL_MINIMUM = 1
STRICT_MIN_VERSION_COVERAGE = 10
STRICT_MIN_PAIR_COVERAGE = 10

STRICT_PARSER_LIMITATIONS = [
    {
        "extractor_name": "c_functions",
        "limitation": "Header declarations and inline signatures are sampled as C API facts; the extractor does not prove body-level behavior or all call-site contracts.",
    },
    {
        "extractor_name": "c_behavior_indicators",
        "limitation": "Behavior indicators are lexical or local-context signals and must be reviewed with surrounding C code before being treated as semantic contract drift.",
    },
    {
        "extractor_name": "rust_binding_uses",
        "limitation": "A Rust binding reference establishes reachability evidence, not that the surrounding safe abstraction depends on the changed C contract.",
    },
    {
        "extractor_name": "rust_safe_api_exposures",
        "limitation": "Safe API exposure extraction is signature-oriented and can miss contracts expressed outside the function body or module-local helper path.",
    },
    {
        "extractor_name": "rust_error_mappings",
        "limitation": "Error and nullability mappings are proximity facts; nearby C bindings are hints, not proof of an exact return-convention dependency.",
    },
    {
        "extractor_name": "rust_lifetime_facts",
        "limitation": "Lifetime and ownership facts identify Rust-side patterns but do not prove that a specific C-side refcount or allocation rule changed.",
    },
    {
        "extractor_name": "promoted_warning_evidence",
        "limitation": "Promoted warning evidence is sufficient for prioritization, but file-level or oracle-only context is reported as a limitation and not as a confirmed bug.",
    },
]

M2_GOLD_SCHEMA_VERSION = "extractor-precision-recall-gold-v1"
M2_PRECISION_RECALL_SCHEMA_VERSION = "extractor-precision-recall-v1"
M2_MIN_OVERALL_PRECISION = 0.95
M2_MIN_OVERALL_RECALL = 0.88
M2_MIN_KAPPA = 0.80
M2_MIN_NEGATIVE_CONTROLS_PER_EXTRACTOR = 30
M2_GOLD_TARGETS = {
    "c_function_signatures": {
        "target_positive": 300,
        "minimum_precision": 0.98,
        "minimum_recall": 0.92,
    },
    "c_struct_fields": {
        "target_positive": 200,
        "minimum_precision": 0.95,
        "minimum_recall": 0.90,
    },
    "c_behavior_indicators": {
        "target_positive": 300,
        "minimum_precision": 0.90,
        "minimum_recall": 0.78,
    },
    "rust_binding_uses": {
        "target_positive": 300,
        "minimum_precision": 0.95,
        "minimum_recall": 0.93,
    },
    "rust_safe_api_exposures": {
        "target_positive": 250,
        "minimum_precision": 0.90,
        "minimum_recall": 0.88,
    },
    "rust_safety_comments": {
        "target_positive": 200,
        "minimum_precision": 0.90,
        "minimum_recall": 0.85,
    },
    "rust_error_lifetime_mappings": {
        "target_positive": 200,
        "minimum_precision": 0.90,
        "minimum_recall": 0.88,
    },
    "generated_binding_facts": {
        "target_positive": 300,
        "minimum_precision": 0.98,
        "minimum_recall": 0.95,
    },
}

M2_GOLD_FIELDS = [
    "gold_id",
    "extractor_name",
    "gold_kind",
    "source_table",
    "version",
    "audit_pair_id",
    "file",
    "line",
    "symbol",
    "expected_present",
    "expected_fact",
    "match_key",
    "reviewer1_label",
    "reviewer1_notes",
    "reviewer2_label",
    "reviewer2_notes",
    "adjudicated_label",
    "adjudication_notes",
]

M2_PRECISION_REVIEW_FIELDS = [
    "precision_id",
    "extractor_name",
    "source_table",
    "version",
    "file",
    "line",
    "symbol",
    "extracted_fact",
    "reviewer1_label",
    "reviewer1_notes",
    "reviewer2_label",
    "reviewer2_notes",
    "adjudicated_label",
    "adjudication_notes",
    "error_category",
]

M2_POSITIVE_LABEL = "SHOULD_EXTRACT"
M2_NEGATIVE_LABEL = "SHOULD_NOT_EXTRACT"
M2_LABELS = {"", M2_POSITIVE_LABEL, M2_NEGATIVE_LABEL}
M2_PRECISION_LABELS = {"", "CORRECT", "INCORRECT"}

M2_LIMITATION_EXAMPLES = {
    "c_function_signatures": [
        "Macro-expanded static inline wrappers can hide the declaration shape that reviewers expect to audit.",
        "Architecture-specific preprocessor branches may expose different signatures under non-main replay configs.",
        "Function-pointer typedefs are intentionally separated from ordinary function declarations.",
        "Out-of-tree helper prototypes are outside the Linux mainline Rust-facing surface unless replay roots include them.",
        "A header declaration does not prove that all body-level error or sleepability contracts were extracted.",
    ],
    "c_struct_fields": [
        "Anonymous unions can preserve layout while obscuring the reviewer-facing field name.",
        "Nested structs are represented as field facts, not as a full semantic layout proof.",
        "Bitfields are audit facts, but C compiler packing rules remain toolchain-dependent.",
        "Conditional fields under preprocessor guards are only covered for the replayed config.",
        "Flexible arrays are retained as fields but require manual review before layout-impact claims.",
    ],
    "c_behavior_indicators": [
        "Keyword indicators such as GFP_KERNEL are local evidence and do not prove the full call-chain context.",
        "Error-return macros inside helper macros can be missed when the expanded source is unavailable.",
        "Refcount naming conventions are hints and can over- or under-approximate custom ownership APIs.",
        "Allocation/free pairs may span functions, so local extraction can miss cross-function obligations.",
        "Atomic-context indicators document potential context constraints, not confirmed unsafe Rust impact.",
    ],
    "rust_binding_uses": [
        "A binding path proves reachability evidence but not that a safe abstraction depends on the changed C contract.",
        "Macro-generated Rust binding uses are only audited when the generated token stream is checked in or expanded.",
        "Re-exported bindings can require graph reachability rather than direct textual matching.",
        "Line mapping can drift when rustfmt or generated comments change between versions.",
        "Unsafe block membership is lexical evidence and does not prove the safety invariant itself.",
    ],
    "rust_safe_api_exposures": [
        "Public trait methods are treated as exposure facts even when the concrete implementation is elsewhere.",
        "Module visibility such as pub(crate) is preserved, but downstream reachability still needs review.",
        "Generic impl blocks can obscure the receiver type that maintainers use in prose.",
        "Contracts expressed only in docs are not equivalent to extracted type signatures.",
        "A public function without a direct binding edge can still be relevant through helper layers.",
    ],
    "rust_safety_comments": [
        "SAFETY comments are proximity evidence, not proof that the comment justifies the nearest binding call.",
        "Multi-line comments can split one rationale across several audited rows.",
        "Doc comments with a Safety section describe caller obligations rather than a specific unsafe block.",
        "Nearby binding association is line-window based and can be ambiguous in dense wrappers.",
        "Safety rationale can become stale without any syntactic change in the comment text.",
    ],
    "rust_error_lifetime_mappings": [
        "Result and Option return types document Rust-side handling but not the complete C error convention.",
        "from_raw and into_raw are ownership markers, not proof of a changed C lifetime contract.",
        "Nearby binding symbols can be absent when an error helper is factored through a wrapper function.",
        "Refcount-like names can identify patterns without proving which C-side counter is affected.",
        "Drop and Clone evidence must be reviewed with the corresponding allocation or get/put path.",
    ],
    "generated_binding_facts": [
        "Generated bindings are build artifacts and require a matching kernel object tree for full coverage.",
        "Bindgen output can omit unsupported macros while still emitting related constants.",
        "repr(C) structs preserve field facts but do not by themselves explain semantic contracts.",
        "Layout assertions can be absent when bindgen or kernel config suppresses a type.",
        "Missing generated files are artifact warnings and must not be treated as successful extraction.",
    ],
}


def generate_extractor_precision_recall_audit(cfg: Config, manifest: dict[str, Any] | None = None) -> dict[str, Any]:
    gold_path = cfg.data_dir / "audit/extractor_gold_labels.csv"
    precision_review_path = cfg.data_dir / "audit/extractor_precision_review.csv"
    audit_manifest_path = cfg.data_dir / "audit/extractor_audit_manifest.json"
    precision_recall_path = cfg.repo_root / "paper/tables/extractor_precision_recall.json"
    confusion_path = cfg.repo_root / "paper/tables/extractor_confusion_matrix.json"
    limitations_path = cfg.repo_root / "paper/analysis/extractor_limitations.md"
    false_negatives_path = cfg.repo_root / "paper/analysis/extractor_false_negatives.md"

    if gold_path.exists():
        rows = _read_m2_gold_csv(gold_path)
    else:
        rows = []
        gold_path.parent.mkdir(parents=True, exist_ok=True)
        _write_m2_gold_csv(gold_path, rows)

    rows = [sanitize_local_paths(row, cfg) for row in rows]
    _write_m2_gold_csv(gold_path, rows)

    summary, confusion = _m2_precision_recall_summary(cfg, rows)
    audit_manifest = _m2_audit_manifest(cfg, manifest, rows, summary)
    summary.update(
        {
            "schema_version": M2_PRECISION_RECALL_SCHEMA_VERSION,
            "gold_labels_csv": repo_relative(cfg, gold_path),
            "precision_review_csv": repo_relative(cfg, precision_review_path),
            "audit_manifest": repo_relative(cfg, audit_manifest_path),
            "confusion_matrix": repo_relative(cfg, confusion_path),
            "limitations": repo_relative(cfg, limitations_path),
            "false_negative_analysis": repo_relative(cfg, false_negatives_path),
            "gold_schema_version": M2_GOLD_SCHEMA_VERSION,
            "review_method": (
                "Extractor recall gold rows use two reviewer fields plus adjudication fields. "
                "Rows are rank/score/ranker blind and are evaluated only against extracted fact identity."
            ),
        }
    )
    confusion.update(
        {
            "schema_version": "extractor-confusion-matrix-v1",
            "gold_labels_csv": repo_relative(cfg, gold_path),
        }
    )

    for path, payload in (
        (precision_recall_path, summary),
        (confusion_path, confusion),
        (audit_manifest_path, audit_manifest),
    ):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(sanitize_local_paths(payload, cfg), indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    limitations_path.parent.mkdir(parents=True, exist_ok=True)
    limitations_path.write_text(_m2_limitations_markdown(summary), encoding="utf-8")
    false_negatives_path.write_text(_m2_false_negatives_markdown(summary, confusion), encoding="utf-8")
    return {
        "extractor_precision_recall": repo_relative(cfg, precision_recall_path),
        "extractor_confusion_matrix": repo_relative(cfg, confusion_path),
        "extractor_limitations": repo_relative(cfg, limitations_path),
        "extractor_false_negatives": repo_relative(cfg, false_negatives_path),
        "extractor_gold_labels": repo_relative(cfg, gold_path),
        "extractor_precision_review": repo_relative(cfg, precision_review_path),
        "extractor_audit_manifest": repo_relative(cfg, audit_manifest_path),
    }


def _read_m2_gold_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames is None:
            return []
        missing = [field for field in M2_GOLD_FIELDS if field not in reader.fieldnames]
        if missing:
            raise RuntimeError(f"extractor gold labels CSV is missing required fields: {', '.join(missing)}")
        rows = [{field: str(row.get(field, "") or "") for field in M2_GOLD_FIELDS} for row in reader]
    _validate_m2_gold_rows(rows)
    return rows


def _write_m2_gold_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=M2_GOLD_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in M2_GOLD_FIELDS} for row in rows)


def _validate_m2_gold_rows(rows: list[dict[str, str]]) -> None:
    seen: set[str] = set()
    for row in rows:
        gold_id = row.get("gold_id", "")
        if not gold_id:
            raise RuntimeError("extractor gold row is missing gold_id")
        if gold_id in seen:
            raise RuntimeError(f"duplicate extractor gold_id: {gold_id}")
        seen.add(gold_id)
        expected = row.get("expected_present", "").strip().lower()
        if expected not in {"true", "false"}:
            raise RuntimeError(f"invalid expected_present value for {gold_id}: {row.get('expected_present')}")
        for field in ("reviewer1_label", "reviewer2_label", "adjudicated_label"):
            if row.get(field, "") not in M2_LABELS:
                raise RuntimeError(f"invalid {field} for {gold_id}: {row.get(field)}")
        if not row.get("match_key"):
            raise RuntimeError(f"extractor gold row is missing match_key: {gold_id}")


def _read_m2_precision_review_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames is None:
            return []
        missing = [field for field in M2_PRECISION_REVIEW_FIELDS if field not in reader.fieldnames]
        if missing:
            raise RuntimeError(f"extractor precision review CSV is missing required fields: {', '.join(missing)}")
        rows = [{field: str(row.get(field, "") or "") for field in M2_PRECISION_REVIEW_FIELDS} for row in reader]
    seen: set[str] = set()
    for row in rows:
        precision_id = row.get("precision_id", "")
        if not precision_id:
            raise RuntimeError("extractor precision review row is missing precision_id")
        if precision_id in seen:
            raise RuntimeError(f"duplicate extractor precision_id: {precision_id}")
        seen.add(precision_id)
        for field in ("reviewer1_label", "reviewer2_label", "adjudicated_label"):
            if row.get(field, "") not in M2_PRECISION_LABELS:
                raise RuntimeError(f"invalid {field} for {precision_id}: {row.get(field)}")
    return rows


def _m2_candidates_from_rows(
    cfg: Config,
    rows: list[dict[str, Any]],
    extractor_name: str,
    gold_kind: str,
    source_table: str,
    symbol_col: str,
    file_col: str,
    line_col: str,
    pair_strata: list[dict[str, str]],
) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    for row in rows:
        symbol = str(row.get(symbol_col) or "")
        file = str(row.get(file_col) or row.get("header_file") or "")
        line = str(row.get(line_col) or "")
        fact = dict(row)
        out.append(_m2_candidate(cfg, extractor_name, gold_kind, source_table, row, symbol, file, line, fact, pair_strata))
    return out


def _m2_candidate(
    cfg: Config,
    extractor_name: str,
    gold_kind: str,
    source_table: str,
    db_row: dict[str, Any],
    symbol: str,
    file: str,
    line: str,
    fact: dict[str, Any],
    pair_strata: list[dict[str, str]],
) -> dict[str, str]:
    version = str(db_row.get("version_id") or "")
    sanitized_fact = sanitize_local_paths(fact, cfg)
    sanitized_file = str(sanitize_local_paths(file, cfg))
    payload = _m2_match_payload(extractor_name, gold_kind, source_table, version, symbol, sanitized_file, str(line))
    return {
        "extractor_name": extractor_name,
        "gold_kind": gold_kind,
        "source_table": source_table,
        "version": version,
        "audit_pair_id": _pair_for_version(pair_strata, version) if pair_strata else "",
        "file": sanitized_file,
        "line": str(line),
        "symbol": symbol,
        "expected_fact": json.dumps(sanitized_fact, sort_keys=True),
        "match_key": _m2_match_key(payload),
    }


def _m2_match_payload(
    extractor_name: str,
    gold_kind: str,
    source_table: str,
    version: str,
    symbol: str,
    file: str,
    line: str,
) -> dict[str, str]:
    return {
        "extractor_name": extractor_name,
        "gold_kind": gold_kind.removesuffix("_negative_control"),
        "source_table": source_table,
        "version": version,
        "symbol": symbol,
        "file": file,
        "line": line,
    }


def _m2_match_key(payload: dict[str, Any]) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str)
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def _load_json(value: str | None, default: Any) -> Any:
    if value is None or value == "":
        return default
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return default


def _m2_precision_recall_summary(cfg: Config, rows: list[dict[str, str]]) -> tuple[dict[str, Any], dict[str, Any]]:
    conn = connect(cfg.database)
    initialize(conn)
    precision_sources = _m2_precision_sources(cfg, rows)
    by_extractor: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        by_extractor.setdefault(row["extractor_name"], []).append(row)

    extractors: dict[str, Any] = {}
    confusion_extractors: dict[str, Any] = {}
    reviewer_pairs: list[tuple[str, str]] = []
    false_negative_examples: list[dict[str, str]] = []
    negative_control_hit_examples: list[dict[str, str]] = []
    totals = Counter()
    for extractor_name in M2_GOLD_TARGETS:
        sample = by_extractor.get(extractor_name, [])
        positives = [row for row in sample if row["expected_present"].lower() == "true"]
        negatives = [row for row in sample if row["expected_present"].lower() == "false"]
        reviewer_pairs.extend((row.get("reviewer1_label", ""), row.get("reviewer2_label", "")) for row in sample)
        recall_tp = control_fp = control_tn = recall_fn = 0
        fn_examples: list[dict[str, str]] = []
        control_hit_examples: list[dict[str, str]] = []
        by_kind: dict[str, Counter[str]] = {}
        for row in sample:
            present = _m2_gold_row_present(conn, cfg, row)
            expected_present = row["expected_present"].lower() == "true"
            if expected_present and present:
                outcome = "tp"
                recall_tp += 1
            elif expected_present:
                outcome = "fn"
                recall_fn += 1
                example = _m2_example(row)
                fn_examples.append(example)
                false_negative_examples.append(example)
            elif present:
                outcome = "fp"
                control_fp += 1
                example = _m2_example(row)
                control_hit_examples.append(example)
                negative_control_hit_examples.append(example)
            else:
                outcome = "tn"
                control_tn += 1
            by_kind.setdefault(row.get("gold_kind", ""), Counter())[outcome] += 1
        precision_source = precision_sources.get(extractor_name, {})
        precision_correct = int(precision_source.get("correct") or 0)
        precision_incorrect = int(precision_source.get("incorrect") or 0)
        precision_reviewed = int(precision_source.get("reviewed") or 0)
        precision = round(precision_correct / precision_reviewed, 4) if precision_reviewed else None
        recall = round(recall_tp / (recall_tp + recall_fn), 4) if recall_tp + recall_fn else None
        f1 = round((2 * precision * recall) / (precision + recall), 4) if precision and recall else None
        target = M2_GOLD_TARGETS[extractor_name]
        versions = sorted({row["version"] for row in sample if row.get("version")})
        pair_ids = sorted({row["audit_pair_id"] for row in sample if row.get("audit_pair_id")})
        file_types = Counter(_m2_file_type(row.get("file", "")) for row in sample)
        passes = bool(
            len(positives) >= int(target["target_positive"])
            and len(negatives) >= M2_MIN_NEGATIVE_CONTROLS_PER_EXTRACTOR
            and (precision or 0.0) >= float(target["minimum_precision"])
            and (recall or 0.0) >= float(target["minimum_recall"])
        )
        extractors[extractor_name] = {
            "positive_gold_samples": len(positives),
            "negative_controls": len(negatives),
            "target_positive": target["target_positive"],
            "minimum_negative_controls": M2_MIN_NEGATIVE_CONTROLS_PER_EXTRACTOR,
            "tp": recall_tp,
            "fp": precision_incorrect + control_fp,
            "fn": recall_fn,
            "tn": control_tn,
            "recall_tp": recall_tp,
            "recall_fn": recall_fn,
            "precision_reviewed": precision_reviewed,
            "precision_correct": precision_correct,
            "precision_incorrect": precision_incorrect,
            "precision_source": precision_source.get("source"),
            "negative_control_fp": control_fp,
            "negative_control_tn": control_tn,
            "precision": precision,
            "recall": recall,
            "f1": f1,
            "minimum_precision": target["minimum_precision"],
            "minimum_recall": target["minimum_recall"],
            "passes": passes,
            "version_count": len(versions),
            "pair_count": len(pair_ids),
            "file_type_distribution": dict(sorted(file_types.items())),
            "false_negative_examples": fn_examples[:5],
            "negative_control_hit_examples": control_hit_examples[:5],
        }
        confusion_extractors[extractor_name] = {
            "tp": recall_tp,
            "fp": precision_incorrect + control_fp,
            "fn": recall_fn,
            "tn": control_tn,
            "recall_tp": recall_tp,
            "recall_fn": recall_fn,
            "precision_correct": precision_correct,
            "precision_incorrect": precision_incorrect,
            "negative_control_fp": control_fp,
            "negative_control_tn": control_tn,
            "by_gold_kind": {kind: dict(counts) for kind, counts in sorted(by_kind.items())},
        }
        totals.update(
            {
                "tp": recall_tp,
                "fp": precision_incorrect + control_fp,
                "fn": recall_fn,
                "tn": control_tn,
                "precision_correct": precision_correct,
                "precision_incorrect": precision_incorrect,
                "precision_reviewed": precision_reviewed,
                "negative_control_fp": control_fp,
                "negative_control_tn": control_tn,
                "positives": len(positives),
                "negatives": len(negatives),
            }
        )

    overall_precision = (
        round(totals["precision_correct"] / totals["precision_reviewed"], 4)
        if totals["precision_reviewed"]
        else None
    )
    overall_recall = round(totals["tp"] / (totals["tp"] + totals["fn"]), 4) if totals["tp"] + totals["fn"] else None
    agreement = _agreement(reviewer_pairs)
    sample_hash = _m2_gold_sample_hash(rows)
    overall = {
        "positive_gold_samples": totals["positives"],
        "negative_controls": totals["negatives"],
        "target_positive_gold_samples": sum(int(item["target_positive"]) for item in M2_GOLD_TARGETS.values()),
        "tp": totals["tp"],
        "fp": totals["fp"],
        "fn": totals["fn"],
        "tn": totals["tn"],
        "precision_reviewed": totals["precision_reviewed"],
        "precision_correct": totals["precision_correct"],
        "precision_incorrect": totals["precision_incorrect"],
        "negative_control_fp": totals["negative_control_fp"],
        "negative_control_tn": totals["negative_control_tn"],
        "precision": overall_precision,
        "recall": overall_recall,
        "minimum_precision": M2_MIN_OVERALL_PRECISION,
        "minimum_recall": M2_MIN_OVERALL_RECALL,
        "agreement": agreement,
        "sample_hash": sample_hash,
    }
    acceptance = {
        "overall_precision": (overall_precision or 0.0) >= M2_MIN_OVERALL_PRECISION,
        "overall_recall": (overall_recall or 0.0) >= M2_MIN_OVERALL_RECALL,
        "gold_sample_size": totals["positives"] >= overall["target_positive_gold_samples"],
        "negative_controls": all(item["negative_controls"] >= M2_MIN_NEGATIVE_CONTROLS_PER_EXTRACTOR for item in extractors.values()),
        "double_review_complete": all(row.get("reviewer1_label") and row.get("reviewer2_label") and row.get("adjudicated_label") for row in rows),
        "cohen_kappa": (agreement.get("cohen_kappa") or 0.0) >= M2_MIN_KAPPA,
        "per_extractor_thresholds": all(item["passes"] for item in extractors.values()),
    }
    summary = {
        "overall": overall,
        "extractors": extractors,
        "acceptance": {**acceptance, "passes": all(acceptance.values())},
        "false_negative_count": len(false_negative_examples),
        "negative_control_hit_count": len(negative_control_hit_examples),
        "false_negative_examples": false_negative_examples[:20],
    }
    confusion = {
        "overall": {key: totals[key] for key in ("tp", "fp", "fn", "tn", "precision_correct", "precision_incorrect", "negative_control_fp", "negative_control_tn")},
        "extractors": confusion_extractors,
        "false_negative_examples": false_negative_examples[:20],
        "negative_control_hit_examples": negative_control_hit_examples[:20],
    }
    return summary, confusion


def _m2_precision_sources(cfg: Config, rows: list[dict[str, str]]) -> dict[str, dict[str, Any]]:
    strict_path = cfg.repo_root / "paper/tables/strict_extractor_audit.json"
    strict = _load_json(strict_path.read_text(encoding="utf-8") if strict_path.exists() else None, {})
    strict_extractors = strict.get("extractors") or {}
    precision_review_path = cfg.data_dir / "audit/extractor_precision_review.csv"
    precision_review_rows = _read_m2_precision_review_csv(precision_review_path)
    mapped = {
        "c_function_signatures": ["c_functions"],
        "c_behavior_indicators": ["c_behavior_indicators"],
        "rust_binding_uses": ["rust_binding_uses"],
        "rust_safe_api_exposures": ["rust_safe_api_exposures"],
        "rust_error_lifetime_mappings": ["rust_error_mappings", "rust_lifetime_facts"],
    }
    out: dict[str, dict[str, Any]] = {}
    for extractor_name, strict_names in mapped.items():
        reviewed = sum(int((strict_extractors.get(name) or {}).get("reviewed") or 0) for name in strict_names)
        correct = sum(int((strict_extractors.get(name) or {}).get("correct") or 0) for name in strict_names)
        out[extractor_name] = {
            "source": f"paper/tables/strict_extractor_audit.json:{','.join(strict_names)}",
            "reviewed": reviewed,
            "correct": correct,
            "incorrect": max(0, reviewed - correct),
        }
    for extractor_name in M2_GOLD_TARGETS:
        if extractor_name in out and out[extractor_name]["reviewed"]:
            continue
        reviewed_rows = [
            row
            for row in precision_review_rows
            if row.get("extractor_name") == extractor_name
            and row.get("adjudicated_label") in {"CORRECT", "INCORRECT"}
        ]
        out[extractor_name] = {
            "source": "data/audit/extractor_precision_review.csv",
            "reviewed": len(reviewed_rows),
            "correct": sum(1 for row in reviewed_rows if row.get("adjudicated_label") == "CORRECT"),
            "incorrect": sum(1 for row in reviewed_rows if row.get("adjudicated_label") == "INCORRECT"),
        }
    return out


def _m2_gold_row_present(conn, cfg: Config, row: dict[str, str]) -> bool:
    if row.get("adjudicated_label") not in {M2_POSITIVE_LABEL, M2_NEGATIVE_LABEL}:
        return False
    for candidate in _m2_candidate_rows_for_gold(conn, cfg, row):
        if candidate.get("match_key") == row.get("match_key"):
            return True
    return False


def _m2_candidate_rows_for_gold(conn, cfg: Config, gold: dict[str, str]) -> list[dict[str, str]]:
    table = gold.get("source_table", "")
    if table not in {
        "binding_consts",
        "binding_functions",
        "binding_structs",
        "c_behavior_indicators",
        "c_functions",
        "c_structs",
        "rust_binding_uses",
        "rust_error_mappings",
        "rust_lifetime_facts",
        "rust_safe_apis",
        "rust_safety_comments",
    }:
        return []
    expected = _load_json(gold.get("expected_fact"), {})
    version = gold.get("version", "")
    line = str(gold.get("line", ""))
    pair = [{"pair_id": gold.get("audit_pair_id", ""), "old_version": version, "new_version": version}]
    rows: list[dict[str, Any]] = []
    if table == "c_structs":
        source_fields = expected.get("source_fields") if isinstance(expected.get("source_fields"), dict) else {}
        c_type = expected.get("c_type") or source_fields.get("c_type") or gold.get("symbol", "").split(".", 1)[0]
        rows = [
            dict(row)
            for row in conn.execute(
                "SELECT * FROM c_structs WHERE version_id=? AND c_type=? AND line=?",
                (version, c_type, line or 0),
            )
        ]
        return [
            candidate
            for candidate in _m2_c_struct_rows_to_candidates(cfg, rows, pair)
            if candidate["symbol"] == gold.get("symbol")
        ]
    symbol_col = {
        "binding_consts": "c_name",
        "binding_functions": "c_symbol",
        "binding_structs": "c_type",
        "c_behavior_indicators": "c_symbol",
        "c_functions": "c_symbol",
        "rust_binding_uses": "binding_symbol",
        "rust_error_mappings": "mapping_type",
        "rust_lifetime_facts": "fact_type",
        "rust_safe_apis": "api_name",
        "rust_safety_comments": "nearby_binding_symbol",
    }[table]
    file_col = {
        "binding_consts": "source_file",
        "binding_functions": "source_file",
        "binding_structs": "source_file",
        "c_behavior_indicators": "evidence_file",
        "c_functions": "definition_file",
        "rust_binding_uses": "rust_file",
        "rust_error_mappings": "rust_file",
        "rust_lifetime_facts": "rust_file",
        "rust_safe_apis": "rust_file",
        "rust_safety_comments": "rust_file",
    }[table]
    line_col = "evidence_line" if table == "c_behavior_indicators" else "line"
    symbol = gold.get("symbol", "")
    if symbol:
        query = f"SELECT * FROM {table} WHERE version_id=? AND {symbol_col}=? AND {line_col}=?"
        params = (version, symbol, line or 0)
    else:
        query = f"SELECT * FROM {table} WHERE version_id=? AND ({symbol_col} IS NULL OR {symbol_col}='') AND {line_col}=?"
        params = (version, line or 0)
    rows = [dict(row) for row in conn.execute(query, params)]
    extractor_name = gold.get("extractor_name", "")
    gold_kind = gold.get("gold_kind", "").removesuffix("_negative_control")
    return _m2_candidates_from_rows(cfg, rows, extractor_name, gold_kind, table, symbol_col, file_col, line_col, pair)


def _m2_c_struct_rows_to_candidates(cfg: Config, rows: list[dict[str, Any]], pair_strata: list[dict[str, str]]) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    for row in rows:
        try:
            fields = json.loads(row.get("fields") or "[]")
        except json.JSONDecodeError:
            fields = []
        for field in fields:
            if not isinstance(field, dict) or not field.get("name"):
                continue
            fact = {**row, "field_name": field.get("name"), "field_type": field.get("type", "")}
            out.append(
                _m2_candidate(
                    cfg,
                    "c_struct_fields",
                    "struct_field",
                    "c_structs",
                    row,
                    f"{row.get('c_type')}.{field.get('name')}",
                    str(row.get("header_file") or ""),
                    str(row.get("line") or ""),
                    fact,
                    pair_strata,
                )
            )
    return out


def _m2_example(row: dict[str, str]) -> dict[str, str]:
    return {
        "gold_id": row.get("gold_id", ""),
        "extractor_name": row.get("extractor_name", ""),
        "gold_kind": row.get("gold_kind", ""),
        "version": row.get("version", ""),
        "file": row.get("file", ""),
        "line": row.get("line", ""),
        "symbol": row.get("symbol", ""),
    }


def _m2_file_type(path: str) -> str:
    suffix = Path(path).suffix
    if path.endswith("bindings_generated.rs"):
        return "generated_rs"
    if suffix in {".h", ".c", ".rs"}:
        return suffix.lstrip(".")
    return "unknown"


def _m2_gold_sample_hash(rows: list[dict[str, str]]) -> str:
    payload = [
        {
            "gold_id": row.get("gold_id", ""),
            "extractor_name": row.get("extractor_name", ""),
            "expected_present": row.get("expected_present", ""),
            "match_key": row.get("match_key", ""),
            "adjudicated_label": row.get("adjudicated_label", ""),
        }
        for row in rows
    ]
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def _m2_audit_manifest(
    cfg: Config,
    manifest: dict[str, Any] | None,
    rows: list[dict[str, str]],
    summary: dict[str, Any],
) -> dict[str, Any]:
    versions = sorted({row["version"] for row in rows if row.get("version")})
    pair_ids = sorted({row["audit_pair_id"] for row in rows if row.get("audit_pair_id")})
    file_types = Counter(_m2_file_type(row.get("file", "")) for row in rows)
    warning_types = Counter(_m2_warning_type(row) for row in rows if row.get("expected_present") == "true")
    difficulty = Counter(_m2_difficulty(row) for row in rows if row.get("expected_present") == "true")
    by_extractor = Counter(row["extractor_name"] for row in rows)
    positive_by_extractor = Counter(row["extractor_name"] for row in rows if row.get("expected_present") == "true")
    negative_by_extractor = Counter(row["extractor_name"] for row in rows if row.get("expected_present") == "false")
    return {
        "schema_version": "extractor-audit-manifest-v1",
        "gold_schema_version": M2_GOLD_SCHEMA_VERSION,
        "sampler": "deterministic stratified DB fact sampler with checked-in adjudicated gold expectations",
        "sample_hash": _m2_gold_sample_hash(rows),
        "database_path": repo_relative(cfg, cfg.database),
        "manifest_run_id": str(manifest.get("run_id")) if manifest else None,
        "manifest_sha256": (manifest or {}).get("sha256", {}),
        "reviewer_protocol": {
            "role_separation": True,
            "rank_score_ranker_blind": True,
            "generator_creates_review_labels": False,
            "missing_gold_csv_behavior": "write an empty skeleton; acceptance fails until reviewed gold labels are supplied",
            "precision_review_source": "strict extractor audit or data/audit/extractor_precision_review.csv; recall gold labels are never used as precision labels",
            "reviewer1_field": "reviewer1_label",
            "reviewer2_field": "reviewer2_label",
            "adjudication_field": "adjudicated_label",
            "cohen_kappa": (summary.get("overall") or {}).get("agreement", {}).get("cohen_kappa"),
        },
        "targets": M2_GOLD_TARGETS,
        "counts": {
            "rows": len(rows),
            "positive_gold_samples": sum(positive_by_extractor.values()),
            "negative_controls": sum(negative_by_extractor.values()),
            "by_extractor": dict(sorted(by_extractor.items())),
            "positive_by_extractor": dict(sorted(positive_by_extractor.items())),
            "negative_by_extractor": dict(sorted(negative_by_extractor.items())),
            "precision_reviewed_by_extractor": {
                name: item.get("precision_reviewed", 0)
                for name, item in sorted((summary.get("extractors") or {}).items())
            },
            "precision_source_by_extractor": {
                name: item.get("precision_source", "")
                for name, item in sorted((summary.get("extractors") or {}).items())
            },
        },
        "stratification": {
            "version_count": len(versions),
            "versions": versions,
            "pair_count": len(pair_ids),
            "pair_ids": pair_ids,
            "file_type_distribution": dict(sorted(file_types.items())),
            "warning_type_distribution": dict(sorted(warning_types.items())),
            "difficulty_distribution": dict(sorted(difficulty.items())),
            "required_file_types": ["h", "c", "rs", "generated_rs"],
            "required_warning_types": [
                "Signature",
                "Field/Layout",
                "MacroConst",
                "Nullability/Error",
                "Refcount/Ownership",
                "Sleepability",
            ],
            "required_difficulties": [
                "header declaration",
                "helper C source",
                "struct field",
                "generated binding",
                "unsafe wrapper",
                "safe API surface",
                "safety comment proximity",
                "error mapping",
                "lifetime or ownership marker",
            ],
        },
        "acceptance": summary.get("acceptance", {}),
    }


def _m2_warning_type(row: dict[str, str]) -> str:
    extractor_name = row.get("extractor_name", "")
    gold_kind = row.get("gold_kind", "")
    symbol = row.get("symbol", "").lower()
    expected = _load_json(row.get("expected_fact"), {})
    indicator = str(expected.get("indicator_type") or "").upper()
    if extractor_name == "c_function_signatures":
        return "Signature"
    if extractor_name == "c_struct_fields":
        return "Field/Layout"
    if extractor_name == "c_behavior_indicators":
        if indicator in {"MAY_SLEEP", "ATOMIC_CONTEXT"} or "sleep" in symbol or "wait" in symbol or "mutex" in symbol:
            return "Sleepability"
        if indicator in {"REFCOUNT_GET", "REFCOUNT_PUT"} or "ref" in symbol or "kref" in symbol:
            return "Refcount/Ownership"
        if indicator in {"NULL_RETURN", "ERR_PTR_RETURN", "IS_ERR_CHECK", "ERROR_CODE"} or "err" in symbol or "null" in symbol:
            return "Nullability/Error"
        return "MacroConst"
    if extractor_name == "rust_error_lifetime_mappings":
        return "Refcount/Ownership" if "lifetime" in gold_kind else "Nullability/Error"
    if extractor_name == "generated_binding_facts" and gold_kind == "const":
        return "MacroConst"
    if extractor_name == "generated_binding_facts":
        return "Field/Layout" if "struct" in gold_kind else "Signature"
    if extractor_name in {"rust_binding_uses", "rust_safe_api_exposures", "rust_safety_comments"}:
        return "Nullability/Error"
    return "Other"


def _m2_difficulty(row: dict[str, str]) -> str:
    extractor_name = row.get("extractor_name", "")
    gold_kind = row.get("gold_kind", "")
    file_type = _m2_file_type(row.get("file", ""))
    if extractor_name == "c_function_signatures":
        return "helper C source" if file_type == "c" else "header declaration"
    if extractor_name == "c_struct_fields":
        return "struct field"
    if extractor_name == "generated_binding_facts":
        return "generated binding"
    if extractor_name == "rust_binding_uses":
        return "unsafe wrapper"
    if extractor_name == "rust_safe_api_exposures":
        return "safe API surface"
    if extractor_name == "rust_safety_comments":
        return "safety comment proximity"
    if extractor_name == "rust_error_lifetime_mappings":
        return "lifetime or ownership marker" if "lifetime" in gold_kind else "error mapping"
    if extractor_name == "c_behavior_indicators":
        return "helper C source" if file_type == "c" else "header declaration"
    return "other"


def _m2_limitations_markdown(summary: dict[str, Any]) -> str:
    lines = [
        "# Extractor Limitations",
        "",
        "The precision/recall audit treats extracted facts as review-target evidence, not as proof of complete semantic analysis.",
        "",
        "## Summary",
        "",
        f"- Positive gold facts: `{(summary.get('overall') or {}).get('positive_gold_samples')}`",
        f"- Negative controls: `{(summary.get('overall') or {}).get('negative_controls')}`",
        f"- Overall precision: `{(summary.get('overall') or {}).get('precision')}`",
        f"- Overall recall: `{(summary.get('overall') or {}).get('recall')}`",
        "",
    ]
    for extractor_name in M2_GOLD_TARGETS:
        extractor = (summary.get("extractors") or {}).get(extractor_name) or {}
        lines.extend(
            [
                f"## {extractor_name}",
                "",
                f"- Positive gold facts: `{extractor.get('positive_gold_samples')}`",
                f"- Negative controls: `{extractor.get('negative_controls')}`",
                f"- Precision: `{extractor.get('precision')}`",
                f"- Recall: `{extractor.get('recall')}`",
                "",
            ]
        )
        for example in M2_LIMITATION_EXAMPLES.get(extractor_name, []):
            lines.append(f"- {example}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _m2_false_negatives_markdown(summary: dict[str, Any], confusion: dict[str, Any]) -> str:
    lines = [
        "# Extractor False Negatives",
        "",
        "False negatives are gold facts with `expected_present=true` whose exact extracted-fact identity is missing from the current database.",
        "",
        "## Overall",
        "",
        f"- False negatives: `{summary.get('false_negative_count')}`",
        f"- Negative-control lookup hits: `{summary.get('negative_control_hit_count')}`",
        f"- Overall recall: `{(summary.get('overall') or {}).get('recall')}`",
        "",
        "## Taxonomy",
        "",
        "- Parser coverage gap: the source fact is present in the gold set but absent from the extractor table.",
        "- Line or symbol drift: the source fact exists but no longer matches the adjudicated identity.",
        "- Generated artifact gap: expected bindgen output is missing from the object-tree snapshot.",
        "- Proximity association gap: Rust comments, unsafe calls, or binding uses moved outside the extractor window.",
        "- Configuration gap: the replay config no longer exposes the expected C or generated Rust fact.",
        "",
        "## Observed Examples",
        "",
    ]
    examples = confusion.get("false_negative_examples") or []
    if not examples:
        lines.append("- No false negatives were observed in the checked-in gold set.")
    else:
        for example in examples:
            lines.append(
                f"- `{example.get('gold_id')}` `{example.get('extractor_name')}` `{example.get('symbol')}` "
                f"at `{example.get('file')}:{example.get('line')}`"
            )
    lines.append("")
    lines.append("## Per Extractor")
    lines.append("")
    for extractor_name in M2_GOLD_TARGETS:
        matrix = ((confusion.get("extractors") or {}).get(extractor_name) or {})
        lines.append(f"- `{extractor_name}`: FN `{matrix.get('fn', 0)}`, TP `{matrix.get('tp', 0)}`")
    return "\n".join(lines).rstrip() + "\n"


def generate_extractor_audit(cfg: Config, manifest: dict[str, Any] | None = None) -> dict[str, Any]:
    sample_path = cfg.data_dir / "audit/extractor_sample.csv"
    rows, provenance = _ensure_sample_csv(cfg, manifest, sample_path)

    summary = {
        "sample_csv": repo_relative(cfg, sample_path),
        "tables": _summaries(rows),
        "metrics": {},
        "acceptance": {},
        "provenance": provenance,
        "error_types": sorted(ERROR_TYPES),
        "note": (
            "Extractor audit samples are deterministic and unfiltered. Precision is computed only from "
            "reviewed CSV rows with explicit is_correct labels; pending rows are not counted as passing."
        ),
    }
    summary["metrics"] = _precision_metrics(summary["tables"])
    summary["acceptance"] = {
        metric: {
            "minimum_precision": minimum,
            "observed_precision": summary["metrics"].get(f"{metric}_precision"),
            "target_sample": AUDIT_TARGETS.get(ACCEPTANCE_TABLES[metric]),
            "sampled": summary["tables"].get(ACCEPTANCE_TABLES[metric], {}).get("sampled"),
            "reviewed": summary["tables"].get(ACCEPTANCE_TABLES[metric], {}).get("reviewed"),
            "pending": summary["tables"].get(ACCEPTANCE_TABLES[metric], {}).get("pending"),
            "sample_size_passes": summary["tables"].get(ACCEPTANCE_TABLES[metric], {}).get("sampled")
            == AUDIT_TARGETS.get(ACCEPTANCE_TABLES[metric]),
            "review_complete": summary["tables"].get(ACCEPTANCE_TABLES[metric], {}).get("pending") == 0,
            "passes": (summary["metrics"].get(f"{metric}_precision") or 0.0) >= minimum,
        }
        for metric, minimum in MIN_PRECISION.items()
    }
    for item in summary["acceptance"].values():
        item["passes"] = bool(item["passes"] and item["sample_size_passes"] and item["review_complete"])
    summary["all_minimums_pass"] = all(item["passes"] for item in summary["acceptance"].values())
    path = cfg.repo_root / "paper/tables/extractor_audit.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(sanitize_local_paths(summary, cfg), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return {"extractor_audit": repo_relative(cfg, path), "sample_csv": repo_relative(cfg, sample_path)}


def _ensure_sample_csv(
    cfg: Config,
    manifest: dict[str, Any] | None,
    sample_path: Path,
) -> tuple[list[dict[str, str]], dict[str, Any]]:
    previous_rows = _read_sample_csv(sample_path) if sample_path.exists() else []
    rows = _sample_rows(cfg, manifest)
    rows = [sanitize_local_paths(row, cfg) for row in rows]
    review_sources = _merge_review_labels(cfg, rows, previous_rows)
    sample_path.parent.mkdir(parents=True, exist_ok=True)
    with sample_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDNAMES, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return rows, _sample_provenance(cfg, manifest, rows, review_sources)


def _read_sample_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames is None:
            return []
        missing = [field for field in FIELDNAMES if field not in reader.fieldnames]
        if missing:
            raise RuntimeError(f"extractor audit CSV is missing required fields: {', '.join(missing)}")
        rows = [{field: str(row.get(field, "") or "") for field in FIELDNAMES} for row in reader]
    _validate_review_rows(rows)
    return rows


def _validate_review_rows(rows: list[dict[str, str]]) -> None:
    valid_labels = {"", "true", "false"}
    for row in rows:
        _validate_label_fields(row, row.get("sample_id", ""), valid_labels=valid_labels)


def _validate_label_fields(row: dict[str, str], sample_id: str, *, valid_labels: set[str] | None = None) -> None:
    valid = valid_labels or {"", "true", "false"}
    label = row.get("is_correct", "").strip().lower()
    if label not in valid:
        raise RuntimeError(f"invalid is_correct value for {sample_id}: {row.get('is_correct')}")
    error_type = row.get("error_type", "").strip()
    if label == "false":
        if error_type not in ERROR_TYPES:
            raise RuntimeError(f"invalid error_type for {sample_id}: {error_type}")
    elif error_type and error_type not in ERROR_TYPES:
        raise RuntimeError(f"invalid error_type for {sample_id}: {error_type}")


def _merge_review_labels(
    cfg: Config,
    current_rows: list[dict[str, str]],
    previous_rows: list[dict[str, str]],
) -> dict[str, Any]:
    previous_by_id = {row["sample_id"]: row for row in previous_rows}
    split_labels, split_sources = _read_split_review_labels(cfg)
    stats = {
        "previous_sample_rows": len(previous_rows),
        "previous_sample_labels_transferred": 0,
        "split_review_labels_transferred": 0,
        "stale_or_unmatched_previous_rows": 0,
        "stale_or_unmatched_split_rows": 0,
        "split_sources": split_sources,
    }
    current_ids = {row["sample_id"] for row in current_rows}
    for sample_id in set(previous_by_id) - current_ids:
        if previous_by_id[sample_id].get("is_correct", "").strip():
            stats["stale_or_unmatched_previous_rows"] += 1
    for sample_id, label in split_labels.items():
        if label.get("is_correct", "").strip() and sample_id not in current_ids:
            stats["stale_or_unmatched_split_rows"] += 1

    for row in current_rows:
        sample_id = row["sample_id"]
        previous = previous_by_id.get(sample_id)
        if not previous or _row_fingerprint(previous) != _row_fingerprint(row):
            if previous and previous.get("is_correct", "").strip():
                stats["stale_or_unmatched_previous_rows"] += 1
            if split_labels.get(sample_id, {}).get("is_correct", "").strip():
                stats["stale_or_unmatched_split_rows"] += 1
            continue
        split_label = split_labels.get(sample_id)
        if split_label and split_label.get("is_correct", "").strip():
            _copy_label_fields(row, split_label)
            stats["split_review_labels_transferred"] += 1
        elif previous.get("is_correct", "").strip():
            _copy_label_fields(row, previous)
            stats["previous_sample_labels_transferred"] += 1
    return stats


def _copy_label_fields(target: dict[str, str], source: dict[str, str]) -> None:
    for field in LABEL_FIELDS:
        target[field] = str(source.get(field, "") or "")


def _read_split_review_labels(cfg: Config) -> tuple[dict[str, dict[str, str]], list[dict[str, Any]]]:
    review_dir = cfg.data_dir / "audit/reviews"
    labels: dict[str, dict[str, str]] = {}
    sources: list[dict[str, Any]] = []
    if not review_dir.exists():
        return labels, sources
    for table in AUDIT_TARGETS:
        path = review_dir / f"{table}_review.csv"
        if not path.exists():
            continue
        with path.open(newline="", encoding="utf-8") as fh:
            reader = csv.DictReader(fh)
            if reader.fieldnames is None:
                rows: list[dict[str, str]] = []
            else:
                missing = [field for field in SPLIT_REVIEW_FIELDS if field not in reader.fieldnames]
                if missing:
                    raise RuntimeError(f"extractor audit review CSV {path} is missing required fields: {', '.join(missing)}")
                rows = [{field: str(row.get(field, "") or "") for field in SPLIT_REVIEW_FIELDS} for row in reader]
        seen: set[str] = set()
        for row in rows:
            sample_id = row["sample_id"]
            if sample_id in seen or sample_id in labels:
                raise RuntimeError(f"duplicate extractor audit review sample_id: {sample_id}")
            seen.add(sample_id)
            if not sample_id.startswith(f"{table}-"):
                raise RuntimeError(f"review row {sample_id} does not belong to {table}")
            label = {
                "is_correct": row.get("is_correct", ""),
                "corrected_fact": "",
                "error_type": row.get("error_type", ""),
                "notes": row.get("notes", ""),
            }
            _validate_label_fields(label, sample_id)
            labels[sample_id] = label
        sources.append(
            {
                "path": str(path),
                "table": table,
                "rows": len(rows),
                "target_rows": AUDIT_TARGETS[table],
                "target_count_present": len(rows) == AUDIT_TARGETS[table],
            }
        )
    return labels, sources


def _row_fingerprint(row: dict[str, str]) -> str:
    if row.get("table") == "promoted_warnings":
        payload = {
            "sample_id": row.get("sample_id", ""),
            "table": row.get("table", ""),
            "symbol": row.get("symbol", ""),
            "extracted_fact": _normalized_promoted_warning_fact(row.get("extracted_fact", "")),
        }
    else:
        payload = {field: row.get(field, "") for field in ("sample_id", "table", "symbol", "file", "line", "extracted_fact")}
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def _normalized_promoted_warning_fact(raw: str) -> str:
    try:
        fact = json.loads(raw or "{}")
    except json.JSONDecodeError:
        return raw
    if isinstance(fact, dict):
        fact.pop("evidence_location", None)
        return json.dumps(fact, sort_keys=True, separators=(",", ":"))
    return raw


def _sample_provenance(
    cfg: Config,
    manifest: dict[str, Any] | None,
    rows: list[dict[str, str]],
    review_sources: dict[str, Any],
) -> dict[str, Any]:
    payload = [_row_fingerprint(row) for row in rows]
    sample_hash = hashlib.sha256(json.dumps(payload, separators=(",", ":")).encode("utf-8")).hexdigest()
    manifest_sha = manifest.get("sha256", {}) if manifest else {}
    return {
        "sampler_version": SAMPLER_VERSION,
        "sample_hash": sample_hash,
        "sampled_rows": len(rows),
        "manifest_run_id": str(manifest.get("run_id")) if manifest else None,
        "manifest_artifact_sha256": manifest_sha,
        "database_path": repo_relative(cfg, cfg.database),
        "review_label_sources": review_sources,
    }


def _sample_rows(cfg: Config, manifest: dict[str, Any] | None) -> list[dict[str, str]]:
    conn = connect(cfg.database)
    initialize(conn)
    version_ids = _audit_version_ids(conn, manifest)
    rows: list[dict[str, str]] = []
    rows.extend(_db_rows(conn, "c_functions", AUDIT_TARGETS["c_functions"], "c_symbol", "definition_file", "line", version_ids=version_ids))
    rows.extend(_db_rows(conn, "rust_binding_uses", AUDIT_TARGETS["rust_binding_uses"], "binding_symbol", "rust_file", "line", version_ids=version_ids))
    rows.extend(_db_rows(conn, "c_behavior_indicators", AUDIT_TARGETS["c_behavior_indicators"], "c_symbol", "evidence_file", "evidence_line", version_ids=version_ids))
    rows.extend(_db_rows(conn, "rust_error_mappings", AUDIT_TARGETS["rust_error_mappings"], "mapping_type", "rust_file", "line", version_ids=version_ids))
    rows.extend(_db_rows(conn, "rust_lifetime_facts", AUDIT_TARGETS["rust_lifetime_facts"], "fact_type", "rust_file", "line", version_ids=version_ids))
    rows.extend(_promoted_warning_rows(cfg, manifest, AUDIT_TARGETS["promoted_warnings"]))
    return rows


def _audit_version_ids(conn, manifest: dict[str, Any] | None) -> list[str]:
    if not manifest:
        return []
    versions: set[str] = set()
    for row in conn.execute(
        "SELECT old_version, new_version FROM replay_pairs WHERE run_id=? AND status='completed'",
        (manifest["run_id"],),
    ):
        if row["old_version"]:
            versions.add(str(row["old_version"]))
        if row["new_version"]:
            versions.add(str(row["new_version"]))
    return sorted(versions)


def _audit_pairs(conn, manifest: dict[str, Any] | None) -> list[dict[str, str]]:
    if not manifest:
        return []
    return [
        {"pair_id": str(row["pair_id"]), "old_version": str(row["old_version"]), "new_version": str(row["new_version"])}
        for row in conn.execute(
            "SELECT pair_id, old_version, new_version FROM replay_pairs WHERE run_id=? AND status='completed' ORDER BY pair_id",
            (manifest["run_id"],),
        )
    ]


def _db_rows(
    conn,
    table: str,
    limit: int,
    symbol_col: str,
    file_col: str,
    line_col: str,
    *,
    version_ids: list[str] | None = None,
) -> list[dict[str, str]]:
    selected: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str, str]] = set()
    if version_ids:
        placeholders = ",".join("?" for _ in version_ids)
        query = f"SELECT * FROM {table} WHERE version_id IN ({placeholders})"
        db_rows = conn.execute(query, version_ids)
    else:
        db_rows = conn.execute(f"SELECT * FROM {table}")
    candidates = sorted((dict(row) for row in db_rows), key=lambda item: _sample_key(table, item))
    for item in candidates:
        symbol = str(item.get(symbol_col) or item.get("c_symbol") or item.get("binding_symbol") or "")
        file = str(item.get(file_col) or item.get("header_file") or "")
        line = str(item.get(line_col) or "")
        fact = json.dumps(item, sort_keys=True)
        key = (symbol, file, line, fact)
        if key in seen:
            continue
        seen.add(key)
        selected.append(item)
        if len(selected) >= limit:
            break
    rows: list[dict[str, str]] = []
    for idx, item in enumerate(selected, start=1):
        symbol = str(item.get(symbol_col) or item.get("c_symbol") or item.get("binding_symbol") or "")
        file = str(item.get(file_col) or item.get("header_file") or "")
        line = str(item.get(line_col) or "")
        rows.append(
            {
                "sample_id": f"{table}-{idx:03d}",
                "table": table,
                "symbol": symbol,
                "file": file,
                "line": line,
                "extracted_fact": json.dumps(item, sort_keys=True),
                "is_correct": "",
                "corrected_fact": "",
                "error_type": "",
                "notes": "",
            }
        )
    return rows


def _sample_key(table: str, item: dict[str, Any]) -> str:
    payload = json.dumps(item, sort_keys=True, default=str, separators=(",", ":"))
    return hashlib.sha256(f"{table}|{payload}".encode("utf-8")).hexdigest()


def _promoted_warning_rows(cfg: Config, manifest: dict[str, Any] | None, limit: int) -> list[dict[str, str]]:
    warning_path = Path(manifest["resolved_paths"]["promoted_warnings"]) if manifest else cfg.warnings_jsonl
    warnings = sorted(read_warnings(warning_path), key=lambda warning: _sample_key("promoted_warnings", warning))[:limit]
    rows: list[dict[str, str]] = []
    for idx, warning in enumerate(warnings, start=1):
        c_side = warning.get("c_side") or {}
        rust_side = warning.get("rust_side") or {}
        location = _warning_location(warning)
        notes = "" if location["file"] and location["line"] else "missing concrete evidence line"
        rows.append(
            {
                "sample_id": f"promoted_warnings-{idx:03d}",
                "table": "promoted_warnings",
                "symbol": str(c_side.get("symbol") or warning.get("symbol") or ""),
                "file": location["file"],
                "line": location["line"],
                "extracted_fact": json.dumps(
                    {
                        "warning_uid": warning.get("warning_uid"),
                        "warning_id": warning.get("warning_id"),
                        "pair_id": warning.get("pair_id"),
                        "type": warning.get("type"),
                        "c_evidence": c_side.get("evidence"),
                        "rust_side": rust_side,
                        "promotion_reasons": warning.get("promotion_reasons"),
                        "evidence_chain": warning.get("evidence_chain"),
                        "evidence_location": location,
                        "score": warning.get("score"),
                    },
                    sort_keys=True,
                ),
                "is_correct": "",
                "corrected_fact": "",
                "error_type": "",
                "notes": notes,
            }
        )
    return rows


def _warning_location(warning: dict[str, Any]) -> dict[str, str]:
    c_side = warning.get("c_side") or {}
    rust_side = warning.get("rust_side") or {}
    for item in _iter_evidence_items(c_side.get("evidence")):
        if location := _location_from_item(item):
            return location
    for item in _iter_evidence_items(warning.get("evidence_chain")):
        if location := _location_from_item(item):
            return location
    for key in ("uses", "safety_comments", "lifetime_facts", "error_mappings"):
        for item in _iter_evidence_items(rust_side.get(key)):
            if location := _location_from_item(item):
                return location
    for item in _iter_evidence_items(warning.get("oracle_hits")):
        if location := _location_from_changed_files(item):
            return location
    for item in _iter_evidence_items(warning.get("evidence_chain")):
        if location := _location_from_changed_files(item):
            return location
    return {"file": "", "line": "", "source": "missing"}


def _iter_evidence_items(value: Any) -> list[dict[str, Any]]:
    if isinstance(value, list):
        return [item for item in value if isinstance(item, dict)]
    if isinstance(value, dict):
        return [value]
    return []


def _location_from_item(item: dict[str, Any]) -> dict[str, str] | None:
    file = item.get("evidence_file") or item.get("rust_file") or item.get("file")
    if not file:
        return None
    line = item.get("evidence_line") or item.get("line") or ""
    return {"file": str(file), "line": str(line), "source": "evidence"}


def _location_from_changed_files(item: dict[str, Any]) -> dict[str, str] | None:
    changed_files = item.get("changed_files")
    if isinstance(changed_files, str):
        try:
            changed_files = json.loads(changed_files)
        except json.JSONDecodeError:
            changed_files = [changed_files]
    if isinstance(changed_files, list) and changed_files:
        return {"file": str(changed_files[0]), "line": "", "source": "changed_files"}
    return None


def _summaries(rows: list[dict[str, str]]) -> dict[str, dict[str, Any]]:
    tables = sorted({row["table"] for row in rows})
    out: dict[str, dict[str, Any]] = {}
    for table in tables:
        sample = [row for row in rows if row["table"] == table]
        reviewed = [row for row in sample if row["is_correct"].strip().lower() in {"true", "false"}]
        correct = sum(1 for row in reviewed if row["is_correct"].strip().lower() == "true")
        errors: dict[str, int] = {}
        for row in reviewed:
            if row["is_correct"].strip().lower() != "false":
                continue
            error_type = row.get("error_type", "").strip() or "OTHER"
            errors[error_type] = errors.get(error_type, 0) + 1
        out[table] = {
            "sampled": len(sample),
            "reviewed": len(reviewed),
            "pending": len(sample) - len(reviewed),
            "correct": correct,
            "precision": round(correct / len(reviewed), 4) if reviewed else None,
            "target_sample": AUDIT_TARGETS.get(table),
            "error_type_distribution": errors,
        }
    return out


def _precision_metrics(tables: dict[str, dict[str, Any]]) -> dict[str, float | None]:
    metrics: dict[str, float | None] = {}
    for table, summary in tables.items():
        metrics[f"{table}_precision"] = summary.get("precision")
    metrics["promoted_warning_evidence_precision"] = tables.get("promoted_warnings", {}).get("precision")
    return metrics


def generate_strict_extractor_audit(cfg: Config, manifest: dict[str, Any] | None = None) -> dict[str, Any]:
    sample_path = cfg.data_dir / "audit/strict_extractor_sample.csv"
    review_path = cfg.data_dir / "audit/strict_extractor_review.csv"
    previous_review_rows = _read_strict_review_csv(review_path) if review_path.exists() else []
    rows = _strict_sample_rows(cfg, manifest)
    rows = [sanitize_local_paths(row, cfg) for row in rows]
    review_provenance = _merge_strict_review_labels(rows, previous_review_rows)
    sample_path.parent.mkdir(parents=True, exist_ok=True)
    _write_strict_csv(sample_path, rows, review_fields=False)
    _write_strict_csv(review_path, rows, review_fields=True)

    summary = _strict_summary(rows)
    summary["negative_samples"] = _strict_negative_samples(rows)
    summary["cross_version_sampling"] = _strict_cross_version_sampling(rows)
    summary["parser_limitations"] = STRICT_PARSER_LIMITATIONS
    summary.update(
        {
            "sample_csv": repo_relative(cfg, sample_path),
            "review_csv": repo_relative(cfg, review_path),
            "sampler_version": "strict-extractor-audit-v2",
            "error_categories": sorted(STRICT_ERROR_CATEGORIES),
            "review_method": (
                "strict audit labels are transferred only from matching reviewed rows with explicit "
                "reviewer/adjudication provenance; unreviewed strict-only rows remain pending"
            ),
            "review_provenance": review_provenance,
        }
    )
    summary["acceptance"] = _strict_acceptance(summary)
    summary["all_minimums_pass"] = all(item["passes"] for item in summary["acceptance"].values())
    out = cfg.repo_root / "paper/tables/strict_extractor_audit.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    taxonomy = cfg.repo_root / "paper/analysis/extractor_error_taxonomy.md"
    taxonomy.parent.mkdir(parents=True, exist_ok=True)
    taxonomy.write_text(_strict_error_taxonomy(summary), encoding="utf-8")
    return {
        "strict_extractor_sample": repo_relative(cfg, sample_path),
        "strict_extractor_review": repo_relative(cfg, review_path),
        "strict_extractor_audit": repo_relative(cfg, out),
        "extractor_error_taxonomy": repo_relative(cfg, taxonomy),
    }


def _strict_sample_rows(cfg: Config, manifest: dict[str, Any] | None) -> list[dict[str, str]]:
    conn = connect(cfg.database)
    initialize(conn)
    version_ids = _audit_version_ids(conn, manifest)
    pair_strata = _audit_pairs(conn, manifest)
    split_labels, _ = _read_split_review_labels(cfg)
    rows: list[dict[str, str]] = []
    rows.extend(
        _strict_db_rows(
            conn,
            "c_functions",
            STRICT_AUDIT_TARGETS["c_functions"],
            "c_functions",
            "c_symbol",
            "definition_file",
            "line",
            split_labels=split_labels,
            version_ids=version_ids,
            pair_strata=pair_strata,
        )
    )
    rows.extend(
        _strict_db_rows(
            conn,
            "c_behavior_indicators",
            STRICT_AUDIT_TARGETS["c_behavior_indicators"],
            "c_behavior_indicators",
            "c_symbol",
            "evidence_file",
            "evidence_line",
            split_labels=split_labels,
            version_ids=version_ids,
            pair_strata=pair_strata,
        )
    )
    rows.extend(
        _strict_db_rows(
            conn,
            "rust_binding_uses",
            STRICT_AUDIT_TARGETS["rust_binding_uses"],
            "rust_binding_uses",
            "binding_symbol",
            "rust_file",
            "line",
            split_labels=split_labels,
            version_ids=version_ids,
            pair_strata=pair_strata,
        )
    )
    rows.extend(
        _strict_db_rows(
            conn,
            "rust_safe_apis",
            STRICT_AUDIT_TARGETS["rust_safe_api_exposures"],
            "rust_safe_api_exposures",
            "api_name",
            "rust_file",
            "line",
            split_labels=split_labels,
            version_ids=version_ids,
            pair_strata=pair_strata,
        )
    )
    rows.extend(
        _strict_db_rows(
            conn,
            "rust_error_mappings",
            STRICT_AUDIT_TARGETS["rust_error_mappings"],
            "rust_error_mappings",
            "mapping_type",
            "rust_file",
            "line",
            split_labels=split_labels,
            version_ids=version_ids,
            pair_strata=pair_strata,
        )
    )
    rows.extend(
        _strict_db_rows(
            conn,
            "rust_lifetime_facts",
            STRICT_AUDIT_TARGETS["rust_lifetime_facts"],
            "rust_lifetime_facts",
            "fact_type",
            "rust_file",
            "line",
            split_labels=split_labels,
            version_ids=version_ids,
            pair_strata=pair_strata,
        )
    )
    rows.extend(_strict_promoted_warning_rows(cfg, manifest, STRICT_AUDIT_TARGETS["promoted_warning_evidence"]))
    return rows


def _strict_db_rows(
    conn,
    table: str,
    limit: int,
    extractor_name: str,
    symbol_col: str,
    file_col: str,
    line_col: str,
    *,
    split_labels: dict[str, dict[str, str]],
    version_ids: list[str] | None,
    pair_strata: list[dict[str, str]] | None,
) -> list[dict[str, str]]:
    base_rows = _strict_db_rows_by_pair(
        conn,
        table,
        limit,
        symbol_col,
        file_col,
        line_col,
        version_ids=version_ids,
        pair_strata=pair_strata,
    )
    out: list[dict[str, str]] = []
    for row in base_rows:
        fact = json.loads(row["extracted_fact"] or "{}")
        control_category = _strict_negative_control_category(extractor_name, fact)
        notes = _strict_limitation_note(extractor_name, fact) or "pending strict audit review"
        out.append(
            {
                "sample_id": row["sample_id"].replace(table, extractor_name, 1),
                "extractor_name": extractor_name,
                "version": str(fact.get("version_id", "")),
                "audit_pair_id": row.get("audit_pair_id", ""),
                "file": row["file"],
                "line": row["line"],
                "symbol": row["symbol"],
                "extracted_fact": row["extracted_fact"],
                "raw_context": _raw_context(fact),
                "control_label": "NEGATIVE_CONTROL" if control_category else "",
                "control_category": control_category,
                "reviewer1_label": "",
                "reviewer1_provenance": "",
                "reviewer2_label": "",
                "reviewer2_provenance": "",
                "adjudicated_label": "",
                "adjudication_provenance": "",
                "error_category": "",
                "notes": notes,
            }
        )
    return out


def _strict_db_rows_by_pair(
    conn,
    table: str,
    limit: int,
    symbol_col: str,
    file_col: str,
    line_col: str,
    *,
    version_ids: list[str] | None,
    pair_strata: list[dict[str, str]] | None,
) -> list[dict[str, str]]:
    rows = _db_rows(conn, table, 10_000_000, symbol_col, file_col, line_col, version_ids=version_ids)
    if not pair_strata:
        return rows[:limit]
    by_version: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        try:
            fact = json.loads(row["extracted_fact"] or "{}")
        except json.JSONDecodeError:
            continue
        by_version.setdefault(str(fact.get("version_id") or ""), []).append(row)

    selected: list[dict[str, str]] = []
    seen: set[str] = set()
    while len(selected) < limit:
        made_progress = False
        for pair in pair_strata:
            if len(selected) >= limit:
                break
            candidates = by_version.get(pair["old_version"], []) + by_version.get(pair["new_version"], [])
            for row in candidates:
                key = _strict_candidate_key(row)
                if key in seen:
                    continue
                item = dict(row)
                item["audit_pair_id"] = pair["pair_id"]
                selected.append(item)
                seen.add(key)
                made_progress = True
                break
        if not made_progress:
            break
    if len(selected) < limit:
        for row in rows:
            if len(selected) >= limit:
                break
            key = _strict_candidate_key(row)
            if key in seen:
                continue
            item = dict(row)
            item["audit_pair_id"] = _pair_for_version(pair_strata, _version_from_row(row))
            selected.append(item)
            seen.add(key)
    return selected


def _strict_candidate_key(row: dict[str, str]) -> str:
    payload = {field: row.get(field, "") for field in ("table", "symbol", "file", "line", "extracted_fact")}
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def _version_from_row(row: dict[str, str]) -> str:
    try:
        fact = json.loads(row.get("extracted_fact") or "{}")
    except json.JSONDecodeError:
        return ""
    return str(fact.get("version_id") or "")


def _pair_for_version(pair_strata: list[dict[str, str]], version: str) -> str:
    for pair in pair_strata:
        if version in {pair["old_version"], pair["new_version"]}:
            return pair["pair_id"]
    return ""


def _strict_review_from_split(sample_id: str, label: dict[str, str], extractor_name: str) -> dict[str, str]:
    if label.get("is_correct", "").strip().lower() == "false":
        mapped = _map_strict_error(label.get("error_type", "OTHER"), extractor_name)
        return {
            "reviewer1_label": "INCORRECT",
            "reviewer2_label": "INCORRECT",
            "adjudicated_label": "INCORRECT",
            "error_category": mapped,
            "notes": label.get("notes", "imported split review false label"),
        }
    return {
        "reviewer1_label": "CORRECT",
        "reviewer2_label": "CORRECT",
        "adjudicated_label": "CORRECT",
        "error_category": "",
        "notes": "imported split review true label" if label else "strict audit deterministic provenance review",
    }


def _map_strict_error(error_type: str, extractor_name: str) -> str:
    if error_type in {"WRONG_SYMBOL"}:
        return "SYMBOL_MISMATCH"
    if error_type in {"WRONG_LINE"}:
        return "LINE_MISMATCH"
    if error_type in {"BINDGEN_ARTIFACT"}:
        return "GENERATED_BINDING_CONFUSION"
    if error_type in {"FALSE_INDICATOR"}:
        return "FALSE_CONTRACT_MAPPING" if "behavior" in extractor_name or "error" in extractor_name else "PARSE_ERROR"
    if error_type in {"REGEX_ARTIFACT"}:
        return "PARSE_ERROR"
    if error_type in {"WRONG_SCOPE"}:
        return "FALSE_USAGE_EDGE"
    if error_type in {"MISSING_CONTEXT"}:
        return "MISSING_CONTEXT"
    return "OTHER"


def _strict_negative_control_category(extractor_name: str, fact: dict[str, Any]) -> str:
    if extractor_name == "c_functions" and not str(fact.get("definition_file") or "").strip():
        return "HEADER_DECLARATION_WITHOUT_BODY"
    if extractor_name == "c_behavior_indicators" and float(fact.get("confidence") or 1.0) < 0.9:
        return "LOCAL_KEYWORD_INDICATOR"
    if extractor_name == "rust_binding_uses" and int(fact.get("enclosing_unsafe_block") or 0) == 0:
        return "BINDING_USE_OUTSIDE_UNSAFE_BLOCK"
    if extractor_name == "rust_safe_api_exposures" and _empty_json_list(fact.get("uses_bindings")):
        return "SAFE_API_WITHOUT_BINDING_EDGE"
    if extractor_name == "rust_error_mappings" and not str(fact.get("nearby_binding_symbol") or "").strip():
        return "ERROR_MAPPING_WITHOUT_NEARBY_BINDING"
    if extractor_name == "rust_lifetime_facts" and _empty_json_list(fact.get("uses_bindings")):
        return "LIFETIME_FACT_WITHOUT_BINDING_EDGE"
    if extractor_name == "promoted_warning_evidence":
        location = fact.get("evidence_location") if isinstance(fact.get("evidence_location"), dict) else {}
        reasons = set(fact.get("promotion_reasons") or [])
        if location.get("source") == "changed_files" or not str(location.get("line") or "").strip():
            if reasons == {"oracle_hit"}:
                return "FILE_LEVEL_ORACLE_ONLY_CONTEXT"
            return "FILE_LEVEL_EVIDENCE_CONTEXT"
    return ""


def _empty_json_list(value: Any) -> bool:
    if value in (None, "", []):
        return True
    if isinstance(value, list):
        return len(value) == 0
    if isinstance(value, str):
        stripped = value.strip()
        if stripped == "[]":
            return True
        try:
            parsed = json.loads(stripped)
        except json.JSONDecodeError:
            return False
        return isinstance(parsed, list) and len(parsed) == 0
    return False


def _strict_limitation_note(extractor_name: str, fact: dict[str, Any]) -> str:
    category = _strict_negative_control_category(extractor_name, fact)
    if not category:
        return ""
    return (
        f"negative-control:{category}; adjudicated extractor fact is correct, "
        "but this row documents a boundary where the parser should not be treated as completeness evidence"
    )


def _strict_promoted_warning_rows(cfg: Config, manifest: dict[str, Any] | None, limit: int) -> list[dict[str, str]]:
    warning_path = Path(manifest["resolved_paths"]["promoted_warnings"]) if manifest else cfg.warnings_jsonl
    warnings = [
        warning
        for warning in read_warnings(warning_path)
        if warning.get("c_evidence_level") in {"c_source_diff", "c_behavior_indicator", "binding_only"}
        and ((warning.get("rust_side") or {}).get("uses") or (warning.get("rust_side") or {}).get("safe_apis") or (warning.get("rust_side") or {}).get("oracle_hits"))
    ]
    warnings = sorted(warnings, key=lambda warning: (0 if warning.get("c_evidence_level") != "binding_only" else 1, -float(warning.get("score") or 0.0), str(warning.get("warning_uid") or "")))[:limit]
    out: list[dict[str, str]] = []
    for idx, warning in enumerate(warnings, start=1):
        location = _warning_location(warning)
        fact = {
            "warning_uid": warning.get("warning_uid"),
            "warning_id": warning.get("warning_id"),
            "pair_id": warning.get("pair_id"),
            "type": warning.get("type"),
            "c_evidence_level": warning.get("c_evidence_level"),
            "promotion_reasons": warning.get("promotion_reasons"),
            "rust_impact_level": warning.get("rust_impact_level"),
            "evidence_location": location,
        }
        control_category = _strict_negative_control_category("promoted_warning_evidence", fact)
        notes = _strict_limitation_note("promoted_warning_evidence", fact)
        out.append(
            {
                "sample_id": f"promoted_warning_evidence-{idx:03d}",
                "extractor_name": "promoted_warning_evidence",
                "version": str(warning.get("new_version") or ""),
                "audit_pair_id": str(warning.get("pair_id") or ""),
                "file": location["file"],
                "line": location["line"],
                "symbol": str((warning.get("c_side") or {}).get("symbol") or ""),
                "extracted_fact": json.dumps(fact, sort_keys=True),
                "raw_context": json.dumps({"c_side": warning.get("c_side"), "rust_side_keys": sorted((warning.get("rust_side") or {}).keys())}, sort_keys=True),
                "control_label": "NEGATIVE_CONTROL" if control_category else "",
                "control_category": control_category,
                "reviewer1_label": "",
                "reviewer1_provenance": "",
                "reviewer2_label": "",
                "reviewer2_provenance": "",
                "adjudicated_label": "",
                "adjudication_provenance": "",
                "error_category": "",
                "notes": notes or "strict audit evidence-chain sample selected for concrete Rust/C reachability",
            }
        )
    return out


def _raw_context(fact: dict[str, Any]) -> str:
    for key in ("evidence_text", "text", "params", "return_type", "uses_bindings", "api_name"):
        if fact.get(key):
            return str(fact.get(key))
    return json.dumps(fact, sort_keys=True)[:300]


def _write_strict_csv(path: Path, rows: list[dict[str, str]], *, review_fields: bool) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=STRICT_FIELDS, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            if review_fields:
                writer.writerow({field: row.get(field, "") for field in STRICT_FIELDS})
            else:
                writer.writerow({field: ("" if field in STRICT_REVIEW_FIELDS else row.get(field, "")) for field in STRICT_FIELDS})


def _read_strict_review_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        fieldnames = set(reader.fieldnames or [])
        if not set(STRICT_FIELDS).issubset(fieldnames):
            return []
        return [{field: str(row.get(field, "") or "") for field in STRICT_FIELDS} for row in reader]


def _merge_strict_review_labels(
    rows: list[dict[str, str]],
    previous_rows: list[dict[str, str]],
) -> dict[str, Any]:
    previous_by_fingerprint = {
        _strict_row_fingerprint(row): row
        for row in previous_rows
        if _strict_review_has_provenance(row)
    }
    transferred = 0
    current_fingerprints = {_strict_row_fingerprint(current) for current in rows}
    for row in rows:
        previous = previous_by_fingerprint.get(_strict_row_fingerprint(row))
        if not previous:
            continue
        for field in STRICT_REVIEW_FIELDS:
            row[field] = previous.get(field, "")
        transferred += 1
    stale_reviewed_rows = sum(
        1
        for row in previous_rows
        if _strict_review_has_provenance(row) and _strict_row_fingerprint(row) not in current_fingerprints
    )
    missing = [
        row["sample_id"]
        for row in rows
        if not row.get("reviewer1_label") or not row.get("reviewer2_label") or not row.get("adjudicated_label")
    ]
    return {
        "source": "data/audit/strict_extractor_review.csv",
        "previous_rows": len(previous_rows),
        "review_labels_transferred": transferred,
        "pending_rows": len(missing),
        "pending_sample_ids": missing[:20],
        "stale_reviewed_rows": stale_reviewed_rows,
        "requires_explicit_provenance": True,
        "generated_default_labels": 0,
    }


def _strict_review_has_provenance(row: dict[str, str]) -> bool:
    return bool(
        row.get("reviewer1_label", "").strip()
        and row.get("reviewer2_label", "").strip()
        and row.get("adjudicated_label", "").strip()
        and row.get("reviewer1_provenance", "").strip()
        and row.get("reviewer2_provenance", "").strip()
        and row.get("adjudication_provenance", "").strip()
    )


def _strict_row_fingerprint(row: dict[str, str]) -> str:
    payload = {
        field: row.get(field, "")
        for field in (
            "extractor_name",
            "version",
            "audit_pair_id",
            "file",
            "line",
            "symbol",
            "extracted_fact",
            "raw_context",
        )
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def _strict_summary(rows: list[dict[str, str]]) -> dict[str, Any]:
    by_extractor: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        by_extractor.setdefault(row["extractor_name"], []).append(row)
    extractors: dict[str, Any] = {}
    reviewer_pairs: list[tuple[str, str]] = []
    for name, sample in sorted(by_extractor.items()):
        reviewed = [row for row in sample if row.get("adjudicated_label") in {"CORRECT", "INCORRECT"}]
        correct = sum(1 for row in reviewed if row.get("adjudicated_label") == "CORRECT")
        reviewer_pairs.extend((row.get("reviewer1_label", ""), row.get("reviewer2_label", "")) for row in reviewed)
        errors = Counter(row.get("error_category") or "NONE" for row in reviewed if row.get("adjudicated_label") == "INCORRECT")
        versions = sorted({row.get("version", "") for row in sample if row.get("version")})
        pair_ids = sorted({row.get("audit_pair_id", "") for row in sample if row.get("audit_pair_id")})
        extractors[name] = {
            "sampled": len(sample),
            "reviewed": len(reviewed),
            "pending": len(sample) - len(reviewed),
            "correct": correct,
            "precision": round(correct / len(reviewed), 4) if reviewed else None,
            "minimum_precision": STRICT_MIN_PRECISION.get(name),
            "target_precision": STRICT_TARGET_PRECISION.get(name),
            "version_count": len(versions),
            "versions": versions,
            "pair_count": len(pair_ids),
            "pair_ids": pair_ids,
            "error_category_distribution": dict(errors),
        }
    agreement = _agreement(reviewer_pairs)
    return {
        "total_samples": len(rows),
        "extractors": extractors,
        "agreement": agreement,
    }


def _strict_negative_samples(rows: list[dict[str, str]]) -> dict[str, Any]:
    by_extractor: dict[str, dict[str, Any]] = {
        name: {"count": 0, "categories": {}, "examples": []}
        for name in STRICT_AUDIT_TARGETS
    }
    for row in rows:
        extractor_name = row["extractor_name"]
        if row.get("control_label") != "NEGATIVE_CONTROL" or not _strict_review_has_provenance(row):
            continue
        try:
            fact = json.loads(row.get("extracted_fact") or "{}")
        except json.JSONDecodeError:
            fact = {}
        category = row.get("control_category") or _strict_negative_control_category(extractor_name, fact)
        if not category:
            continue
        summary = by_extractor.setdefault(extractor_name, {"count": 0, "categories": {}, "examples": []})
        summary["count"] += 1
        summary["categories"][category] = summary["categories"].get(category, 0) + 1
        if len(summary["examples"]) < 3:
            summary["examples"].append(
                {
                    "sample_id": row.get("sample_id"),
                    "symbol": row.get("symbol"),
                    "category": category,
                    "note": row.get("notes"),
                }
            )
    missing = [
        name
        for name, summary in sorted(by_extractor.items())
        if summary["count"] < STRICT_NEGATIVE_CONTROL_MINIMUM
    ]
    return {
        "description": (
            "Negative controls are limitation-focused reviewed rows. They keep the extracted fact label "
            "separate from completeness claims and document where downstream review must inspect context."
        ),
        "minimum_per_extractor": STRICT_NEGATIVE_CONTROL_MINIMUM,
        "passes": not missing,
        "missing_extractors": missing,
        "total": sum(summary["count"] for summary in by_extractor.values()),
        "extractors": by_extractor,
    }


def _strict_cross_version_sampling(rows: list[dict[str, str]]) -> dict[str, Any]:
    coverage: dict[str, Any] = {}
    for name in sorted(STRICT_AUDIT_TARGETS):
        versions = sorted({row.get("version", "") for row in rows if row["extractor_name"] == name and row.get("version")})
        pair_ids = sorted({row.get("audit_pair_id", "") for row in rows if row["extractor_name"] == name and row.get("audit_pair_id")})
        coverage[name] = {"version_count": len(versions), "versions": versions, "pair_count": len(pair_ids), "pair_ids": pair_ids}
    missing = [
        name
        for name, item in coverage.items()
        if item["version_count"] < STRICT_MIN_VERSION_COVERAGE or item["pair_count"] < STRICT_MIN_PAIR_COVERAGE
    ]
    return {
        "minimum_versions_per_extractor": STRICT_MIN_VERSION_COVERAGE,
        "minimum_pairs_per_extractor": STRICT_MIN_PAIR_COVERAGE,
        "passes": not missing,
        "missing_extractors": missing,
        "extractors": coverage,
    }


def _strict_acceptance(summary: dict[str, Any]) -> dict[str, Any]:
    acceptance: dict[str, Any] = {}
    for name, minimum in STRICT_MIN_PRECISION.items():
        extractor = summary["extractors"].get(name, {})
        target_precision = STRICT_TARGET_PRECISION.get(name, minimum)
        observed_precision = extractor.get("precision") or 0.0
        sampled = extractor.get("sampled", 0)
        pending = extractor.get("pending", 0)
        minimum_passes = bool(
            sampled == STRICT_AUDIT_TARGETS[name]
            and pending == 0
            and observed_precision >= minimum
        )
        target_passes = bool(observed_precision >= target_precision)
        acceptance[name] = {
            "minimum_precision": minimum,
            "target_precision": target_precision,
            "observed_precision": extractor.get("precision"),
            "sampled": sampled,
            "target_sample": STRICT_AUDIT_TARGETS[name],
            "reviewed": extractor.get("reviewed", 0),
            "pending": pending,
            "minimum_passes": minimum_passes,
            "target_passes": target_passes,
            "passes": bool(minimum_passes and target_passes),
        }
    agreement = summary["agreement"]
    negative_samples = summary.get("negative_samples") or {}
    cross_version_sampling = summary.get("cross_version_sampling") or {}
    review_provenance = summary.get("review_provenance") or {}
    acceptance["overall"] = {
        "total_samples": summary["total_samples"],
        "minimum_samples": 800,
        "target_total_samples": 800,
        "cohen_kappa": agreement["cohen_kappa"],
        "minimum_kappa": 0.70,
        "target_kappa": 0.80,
        "negative_samples_pass": negative_samples.get("passes") is True,
        "cross_version_sampling_pass": cross_version_sampling.get("passes") is True,
        "parser_limitations_reported": bool(summary.get("parser_limitations")),
        "review_provenance_pass": review_provenance.get("pending_rows") == 0
        and review_provenance.get("generated_default_labels") == 0
        and review_provenance.get("review_labels_transferred") == summary["total_samples"],
        "passes": bool(
            summary["total_samples"] >= 800
            and (agreement["cohen_kappa"] or 0.0) >= 0.80
            and negative_samples.get("passes") is True
            and cross_version_sampling.get("passes") is True
            and bool(summary.get("parser_limitations"))
            and review_provenance.get("pending_rows") == 0
            and review_provenance.get("generated_default_labels") == 0
            and review_provenance.get("review_labels_transferred") == summary["total_samples"]
        ),
    }
    return acceptance


def _agreement(pairs: list[tuple[str, str]]) -> dict[str, Any]:
    if not pairs:
        return {"reviewed_pairs": 0, "agreement_rate": None, "cohen_kappa": None}
    agreements = sum(1 for left, right in pairs if left == right)
    labels = sorted({label for pair in pairs for label in pair if label})
    total = len(pairs)
    observed = agreements / total
    left_counts = Counter(left for left, _ in pairs)
    right_counts = Counter(right for _, right in pairs)
    expected = sum((left_counts[label] / total) * (right_counts[label] / total) for label in labels)
    if expected == 1.0:
        kappa = 1.0 if observed == 1.0 else 0.0
    else:
        kappa = (observed - expected) / (1 - expected)
    return {"reviewed_pairs": total, "agreement_rate": round(observed, 4), "cohen_kappa": round(kappa, 4)}


def _strict_error_taxonomy(summary: dict[str, Any]) -> str:
    lines = [
        "# Extractor Failure And Limitation Taxonomy",
        "",
        "Strict extractor audit error categories are reported per extractor. Limitation-focused negative controls are reviewed rows that keep the extracted fact separate from any completeness or confirmed-bug claim.",
        "",
        "## Overall",
        "",
        f"- Total strict samples: `{summary.get('total_samples')}`",
        f"- Promoted warning evidence samples: `{(summary.get('extractors') or {}).get('promoted_warning_evidence', {}).get('sampled')}`",
        f"- Cohen's kappa: `{(summary.get('agreement') or {}).get('cohen_kappa')}`",
        f"- Negative-control rows: `{(summary.get('negative_samples') or {}).get('total')}`",
        "",
        "## Parser Limitations",
        "",
    ]
    for item in summary.get("parser_limitations") or []:
        lines.append(f"- `{item['extractor_name']}`: {item['limitation']}")
    lines.append("")
    lines.append("## Negative Controls")
    lines.append("")
    negative = summary.get("negative_samples") or {}
    negative_by_extractor = negative.get("extractors") or {}
    for name in sorted(summary["extractors"]):
        item = negative_by_extractor.get(name) or {}
        categories = item.get("categories") or {}
        lines.append(f"### {name}")
        lines.append("")
        lines.append(f"- Count: `{item.get('count', 0)}`")
        if categories:
            for category, count in sorted(categories.items()):
                lines.append(f"- `{category}`: {count}")
        else:
            lines.append("- No limitation-focused negative-control row selected.")
        for example in (item.get("examples") or [])[:2]:
            lines.append(f"- Example `{example.get('sample_id')}` `{example.get('symbol')}`: `{example.get('category')}`")
        lines.append("")
    lines.append("## Observed Incorrect Rows")
    lines.append("")
    for name, extractor in sorted(summary["extractors"].items()):
        lines.append(f"### {name}")
        lines.append("")
        lines.append(f"- Precision: `{extractor.get('precision')}`")
        lines.append(f"- Versions sampled: `{extractor.get('version_count')}`")
        errors = extractor.get("error_category_distribution") or {}
        if not errors:
            lines.append("- Main errors: none in reviewed strict sample.")
        else:
            for category, count in sorted(errors.items()):
                lines.append(f"- `{category}`: {count}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"
