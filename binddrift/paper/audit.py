from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
from typing import Any

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


def generate_extractor_audit(cfg: Config, manifest: dict[str, Any] | None = None) -> dict[str, Any]:
    sample_path = cfg.data_dir / "audit/extractor_sample.csv"
    rows, provenance = _ensure_sample_csv(cfg, manifest, sample_path)

    summary = {
        "sample_csv": str(sample_path),
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
    path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return {"extractor_audit": str(path), "sample_csv": str(sample_path)}


def _ensure_sample_csv(
    cfg: Config,
    manifest: dict[str, Any] | None,
    sample_path: Path,
) -> tuple[list[dict[str, str]], dict[str, Any]]:
    previous_rows = _read_sample_csv(sample_path) if sample_path.exists() else []
    rows = _sample_rows(cfg, manifest)
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
        "database_path": str(cfg.database),
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
