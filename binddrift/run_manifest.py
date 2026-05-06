from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
from typing import Any

from binddrift.config import Config
from binddrift.artifact_paths import repo_relative, sanitize_local_paths
from binddrift.warnings import eligible_for_main_warning, read_warnings


MANIFEST_NAME = "run_manifest.json"
REPLAY_RUN_ID = "latest"


class ArtifactConsistencyError(RuntimeError):
    pass


def canonical_run_dir(cfg: Config, run_id: str = REPLAY_RUN_ID) -> Path:
    if cfg.data_dir.name == run_id and cfg.data_dir.parent.name == "replay":
        return cfg.data_dir
    return cfg.data_dir / "replay" / run_id


def run_manifest_path(cfg: Config, run_id: str = REPLAY_RUN_ID) -> Path:
    return canonical_run_dir(cfg, run_id) / MANIFEST_NAME


def count_jsonl(path: Path) -> int:
    if not path.exists():
        return 0
    with path.open(encoding="utf-8") as fh:
        return sum(1 for line in fh if line.strip())


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_json(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def count_csv_rows(path: Path) -> int:
    if not path.exists():
        return 0
    with path.open(newline="", encoding="utf-8") as fh:
        return sum(1 for _ in csv.DictReader(fh))


def resolve_manifest_path(cfg: Config, value: str) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path
    return (cfg.repo_root / path).resolve()


def aggregate_pair_jsonl(run_dir: Path, filename: str, output: Path, *, cfg: Config | None = None) -> int:
    rows = 0
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as out:
        for pair_dir in sorted(path for path in run_dir.iterdir() if path.is_dir()):
            source = pair_dir / filename
            if not source.exists():
                continue
            with source.open(encoding="utf-8") as fh:
                for line in fh:
                    if not line.strip():
                        continue
                    if cfg is not None:
                        try:
                            row = sanitize_local_paths(json.loads(line), cfg)
                            line = json.dumps(row, sort_keys=True)
                        except json.JSONDecodeError:
                            line = sanitize_local_paths(line.rstrip("\n"), cfg)
                    out.write(line if line.endswith("\n") else line + "\n")
                    rows += 1
    return rows


def load_summary(run_dir: Path) -> dict[str, Any]:
    summary_path = run_dir / "summary.json"
    if not summary_path.exists():
        return {}
    return json.loads(summary_path.read_text(encoding="utf-8"))


def build_run_manifest(cfg: Config, run_id: str = REPLAY_RUN_ID) -> dict[str, Any]:
    run_dir = canonical_run_dir(cfg, run_id)
    warnings_path = run_dir / "warnings.jsonl"
    promoted_path = run_dir / "promoted_warnings.jsonl"
    review_path = run_dir / "manual_review.csv"
    drift_facts_path = run_dir / "drift_facts.jsonl"
    single_version_path = run_dir / "single_version_review_targets.jsonl"
    protocol_path = run_dir / "evaluation_protocol.json"
    pooled_set_path = run_dir / "pooled_review_set.jsonl"
    pooled_labels_path = run_dir / "pooled_review_labels.csv"
    pooled_manifest_path = run_dir / "pooled_review_manifest.json"
    summary = load_summary(run_dir)

    if not warnings_path.exists():
        raise ArtifactConsistencyError(f"missing canonical warning file: {warnings_path}")
    if not promoted_path.exists():
        raise ArtifactConsistencyError(f"missing canonical promoted warning file: {promoted_path}")
    if not review_path.exists():
        raise ArtifactConsistencyError(f"missing canonical review file: {review_path}")
    if not drift_facts_path.exists():
        raise ArtifactConsistencyError(f"missing canonical drift facts file: {drift_facts_path}")
    if not single_version_path.exists():
        raise ArtifactConsistencyError(f"missing canonical single-version target file: {single_version_path}")
    if not protocol_path.exists():
        raise ArtifactConsistencyError(f"missing canonical evaluation protocol file: {protocol_path}")

    warnings = read_warnings(warnings_path)
    promoted_warnings = read_warnings(promoted_path)
    _validate_evaluation_protocol_splits(protocol_path, promoted_warnings)
    protocol = json.loads(protocol_path.read_text(encoding="utf-8"))
    split_hash = evaluation_protocol_split_hash(protocol)
    ineligible = [warning for warning in warnings + promoted_warnings if not eligible_for_main_warning(warning)]
    if ineligible:
        raise ArtifactConsistencyError(f"canonical warning file contains non-main warnings: {len(ineligible)}")
    warning_count = len(warnings)
    if warning_count == 0:
        raise ArtifactConsistencyError("canonical warning file is empty")
    drift_fact_count = count_jsonl(drift_facts_path)
    single_version_count = count_jsonl(single_version_path)
    reviewed_warning_count = count_csv_rows(review_path)
    if reviewed_warning_count > warning_count:
        raise ArtifactConsistencyError(f"reviewed_warning_count {reviewed_warning_count}>{warning_count}")
    promoted_warning_count = len(promoted_warnings)
    if warning_count > promoted_warning_count:
        raise ArtifactConsistencyError(f"paper_topk {warning_count}>{promoted_warning_count}")
    version_ids = sorted(
        {
            str(value)
            for warning in warnings
            for value in (warning.get("old_version"), warning.get("new_version"))
            if value
        }
    )
    pair_ids = sorted({str(warning.get("pair_id")) for warning in warnings if warning.get("pair_id")})
    manifest = {
        "run_id": run_id,
        "run_dir": repo_relative(cfg, run_dir),
        "canonical_warning_file": repo_relative(cfg, warnings_path),
        "canonical_promoted_warnings_file": repo_relative(cfg, promoted_path),
        "canonical_review_file": repo_relative(cfg, review_path),
        "canonical_drift_facts_file": repo_relative(cfg, drift_facts_path),
        "canonical_single_version_review_targets_file": repo_relative(cfg, single_version_path),
        "canonical_evaluation_protocol_file": repo_relative(cfg, protocol_path),
        "canonical_database": repo_relative(cfg, cfg.database),
        "locked_split_hash": split_hash,
        "warning_count": warning_count,
        "promoted_warning_count": promoted_warning_count,
        "paper_topk": warning_count,
        "drift_fact_count": drift_fact_count,
        "reviewed_warning_count": reviewed_warning_count,
        "single_version_review_targets": single_version_count,
        "pair_count": int(summary.get("pairs") or len(pair_ids)),
        "version_count": int(summary.get("versions") or len(version_ids)),
        "sha256": {
            "warnings.jsonl": sha256_file(warnings_path),
            "promoted_warnings.jsonl": sha256_file(promoted_path),
            "manual_review.csv": sha256_file(review_path),
            "drift_facts.jsonl": sha256_file(drift_facts_path),
            "single_version_review_targets.jsonl": sha256_file(single_version_path),
            "evaluation_protocol.json": sha256_file(protocol_path),
        },
    }
    pooled_paths = [pooled_set_path, pooled_labels_path, pooled_manifest_path]
    if any(path.exists() for path in pooled_paths):
        missing = [str(path) for path in pooled_paths if not path.exists()]
        if missing:
            raise ArtifactConsistencyError("missing pooled review files: " + ", ".join(missing))
        manifest.update(
            {
                "canonical_pooled_review_set_file": repo_relative(cfg, pooled_set_path),
                "canonical_pooled_review_labels_file": repo_relative(cfg, pooled_labels_path),
                "canonical_pooled_review_manifest_file": repo_relative(cfg, pooled_manifest_path),
                "pooled_review_set_count": count_jsonl(pooled_set_path),
                "pooled_review_label_count": count_csv_rows(pooled_labels_path),
            }
        )
        manifest["sha256"].update(
            {
                "pooled_review_set.jsonl": sha256_file(pooled_set_path),
                "pooled_review_labels.csv": sha256_file(pooled_labels_path),
                "pooled_review_manifest.json": sha256_file(pooled_manifest_path),
            }
        )
    return manifest


def write_run_manifest(cfg: Config, run_id: str = REPLAY_RUN_ID) -> dict[str, Any]:
    manifest = build_run_manifest(cfg, run_id=run_id)
    path = run_manifest_path(cfg, run_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return manifest


def load_run_manifest(cfg: Config, run_id: str = REPLAY_RUN_ID) -> dict[str, Any]:
    path = run_manifest_path(cfg, run_id)
    if not path.exists():
        raise ArtifactConsistencyError(f"missing run manifest: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def validate_run_manifest(cfg: Config, manifest: dict[str, Any] | None = None) -> dict[str, Any]:
    manifest = manifest or load_run_manifest(cfg)
    warnings_path = resolve_manifest_path(cfg, manifest["canonical_warning_file"])
    promoted_path = resolve_manifest_path(cfg, manifest["canonical_promoted_warnings_file"])
    review_path = resolve_manifest_path(cfg, manifest["canonical_review_file"])
    drift_facts_path = resolve_manifest_path(cfg, manifest["canonical_drift_facts_file"])
    single_version_path = resolve_manifest_path(cfg, manifest.get("canonical_single_version_review_targets_file", "data/replay/latest/single_version_review_targets.jsonl"))
    protocol_path = resolve_manifest_path(cfg, manifest.get("canonical_evaluation_protocol_file", "data/replay/latest/evaluation_protocol.json"))
    database_path = resolve_manifest_path(cfg, manifest["canonical_database"])
    if database_path != cfg.database.resolve():
        raise ArtifactConsistencyError(f"canonical_database {database_path} != configured database {cfg.database.resolve()}")
    required = {
        "warnings.jsonl": warnings_path,
        "promoted_warnings.jsonl": promoted_path,
        "manual_review.csv": review_path,
        "drift_facts.jsonl": drift_facts_path,
        "single_version_review_targets.jsonl": single_version_path,
        "evaluation_protocol.json": protocol_path,
    }
    optional_resolved: dict[str, Path] = {}
    optional_manifest_keys = {
        "pooled_review_set.jsonl": "canonical_pooled_review_set_file",
        "pooled_review_labels.csv": "canonical_pooled_review_labels_file",
        "pooled_review_manifest.json": "canonical_pooled_review_manifest_file",
    }
    present_optional_keys = [key for key in optional_manifest_keys.values() if key in manifest]
    if present_optional_keys:
        missing_keys = [key for key in optional_manifest_keys.values() if key not in manifest]
        if missing_keys:
            raise ArtifactConsistencyError("manifest has incomplete pooled review files: " + ", ".join(missing_keys))
        optional_resolved = {
            name: resolve_manifest_path(cfg, manifest[key])
            for name, key in optional_manifest_keys.items()
        }
        required.update(optional_resolved)
    missing = [str(path) for path in required.values() if not path.exists()]
    if missing:
        raise ArtifactConsistencyError("missing canonical files: " + ", ".join(missing))

    warning_count = count_jsonl(warnings_path)
    promoted_warning_count = count_jsonl(promoted_path)
    drift_fact_count = count_jsonl(drift_facts_path)
    single_version_count = count_jsonl(single_version_path)
    reviewed_warning_count = count_csv_rows(review_path)
    pooled_set_count = count_jsonl(optional_resolved["pooled_review_set.jsonl"]) if optional_resolved else None
    pooled_label_count = count_csv_rows(optional_resolved["pooled_review_labels.csv"]) if optional_resolved else None
    checks = [
        (warning_count > 0, "canonical warning file is empty"),
        (warning_count == manifest.get("warning_count"), f"warning_count {warning_count}!={manifest.get('warning_count')}"),
        (
            promoted_warning_count == manifest.get("promoted_warning_count"),
            f"promoted_warning_count {promoted_warning_count}!={manifest.get('promoted_warning_count')}",
        ),
        (
            warning_count == manifest.get("paper_topk"),
            f"paper_topk {warning_count}!={manifest.get('paper_topk')}",
        ),
        (warning_count <= promoted_warning_count, f"paper_topk {warning_count}>{promoted_warning_count}"),
        (drift_fact_count == manifest.get("drift_fact_count"), f"drift_fact_count {drift_fact_count}!={manifest.get('drift_fact_count')}"),
        (reviewed_warning_count == manifest.get("reviewed_warning_count"), f"reviewed_warning_count {reviewed_warning_count}!={manifest.get('reviewed_warning_count')}"),
        (reviewed_warning_count <= warning_count, f"reviewed_warning_count {reviewed_warning_count}>{warning_count}"),
        (
            single_version_count == manifest.get("single_version_review_targets", 0),
            f"single_version_review_targets {single_version_count}!={manifest.get('single_version_review_targets', 0)}",
        ),
    ]
    if optional_resolved:
        checks.extend(
            [
                (
                    pooled_set_count == manifest.get("pooled_review_set_count"),
                    f"pooled_review_set_count {pooled_set_count}!={manifest.get('pooled_review_set_count')}",
                ),
                (
                    pooled_label_count == manifest.get("pooled_review_label_count"),
                    f"pooled_review_label_count {pooled_label_count}!={manifest.get('pooled_review_label_count')}",
                ),
            ]
        )
    for name, path in required.items():
        expected = (manifest.get("sha256") or {}).get(name)
        actual = sha256_file(path)
        checks.append((actual == expected, f"{name} sha256 {actual}!={expected}"))
    warnings = read_warnings(warnings_path) + read_warnings(promoted_path)
    _validate_evaluation_protocol_splits(protocol_path, read_warnings(promoted_path))
    protocol = json.loads(protocol_path.read_text(encoding="utf-8"))
    expected_split_hash = evaluation_protocol_split_hash(protocol)
    checks.append(
        (
            manifest.get("locked_split_hash") == expected_split_hash,
            f"locked_split_hash {manifest.get('locked_split_hash')}!={expected_split_hash}",
        )
    )
    checks.append(
        (
            all(eligible_for_main_warning(warning) for warning in warnings),
            "canonical warning file contains non-main warnings",
        )
    )
    failures = [message for passed, message in checks if not passed]
    if failures:
        raise ArtifactConsistencyError("; ".join(failures))
    return {
        **manifest,
        "resolved_paths": {
            "warnings": str(warnings_path),
            "promoted_warnings": str(promoted_path),
            "manual_review": str(review_path),
            "drift_facts": str(drift_facts_path),
            "single_version_review_targets": str(single_version_path),
            "evaluation_protocol": str(protocol_path),
            **(
                {
                    "pooled_review_set": str(optional_resolved["pooled_review_set.jsonl"]),
                    "pooled_review_labels": str(optional_resolved["pooled_review_labels.csv"]),
                    "pooled_review_manifest": str(optional_resolved["pooled_review_manifest.json"]),
                }
                if optional_resolved
                else {}
            ),
        },
    }


def manifest_exists(cfg: Config, run_id: str = REPLAY_RUN_ID) -> bool:
    return run_manifest_path(cfg, run_id).exists()


def _validate_evaluation_protocol_splits(protocol_path: Path, promoted_warnings: list[dict[str, Any]]) -> None:
    protocol = json.loads(protocol_path.read_text(encoding="utf-8"))
    expected = {str(warning.get("pair_id")) for warning in promoted_warnings if warning.get("pair_id")}
    if not expected:
        return
    splits = protocol.get("splits") or {}
    actual = {
        str(pair_id)
        for key in ("dev_pairs", "validation_pairs", "locked_test_pairs")
        for pair_id in (splits.get(key) or [])
    }
    if actual != expected:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        raise ArtifactConsistencyError(
            "evaluation_protocol split pair_ids do not match canonical warning pairs"
            f"; missing={missing[:5]} extra={extra[:5]}"
        )


def evaluation_protocol_split_hash(protocol: dict[str, Any]) -> str:
    splits = protocol.get("splits") or {}
    locked_policy = protocol.get("locked_split_policy") or {}
    payload = {
        "splits": {
            key: list(splits.get(key) or [])
            for key in ("dev_pairs", "validation_pairs", "locked_test_pairs")
        },
        "locked_split_policy": locked_policy,
    }
    return sha256_json(payload)
