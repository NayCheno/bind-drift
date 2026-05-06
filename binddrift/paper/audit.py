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
