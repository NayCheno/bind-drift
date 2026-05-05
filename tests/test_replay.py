import json
import subprocess
from pathlib import Path

from binddrift import replay as replay_module
from binddrift.config import Config
from binddrift.db import connect, initialize
from binddrift.replay import ReplayStageError, mark_stale_replay_runs, run_version_replay
from binddrift.warnings import read_warnings, write_warnings


def _git(repo: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(repo), *args], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


def _write_linux_snapshot(repo: Path, return_line: str) -> None:
    (repo / "include/linux").mkdir(parents=True, exist_ok=True)
    (repo / "rust/kernel").mkdir(parents=True, exist_ok=True)
    (repo / "scripts").mkdir(parents=True, exist_ok=True)
    (repo / "scripts/min-tool-version.sh").write_text(
        """
case "$1" in
rustc)
	echo 1.78.0
	;;
bindgen)
	echo 0.65.1
	;;
esac
""",
        encoding="utf-8",
    )
    (repo / "include/linux/foo.h").write_text(
        f"""
static inline void *foo_get(void)
{{
    {return_line}
}}
""",
        encoding="utf-8",
    )
    (repo / "rust/kernel/device.rs").write_text(
        """
pub struct Device;
impl Device {
    pub fn get(&self) -> Option<()> {
        // SAFETY: current wrapper treats the pointer as nullable.
        let ptr = unsafe { bindings::foo_get() };
        core::ptr::NonNull::new(ptr).map(|_| ())
    }
}
""",
        encoding="utf-8",
    )


def _make_tagged_linux_repo(root: Path) -> Path:
    repo = root / "vendor/linux"
    repo.mkdir(parents=True)
    subprocess.run(["git", "-C", str(repo), "init"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    _git(repo, "config", "user.email", "binddrift@example.com")
    _git(repo, "config", "user.name", "BindDrift Test")
    _write_linux_snapshot(repo, "return NULL;")
    _git(repo, "add", ".")
    _git(repo, "commit", "-m", "linux v6.1 fixture")
    _git(repo, "tag", "v6.1")
    _write_linux_snapshot(repo, "return ERR_PTR(-ENOMEM);")
    _git(repo, "add", ".")
    _git(repo, "commit", "-m", "linux v6.2 fixture")
    _git(repo, "tag", "v6.2")
    return repo


def test_version_replay_records_pair_outputs(tmp_path: Path):
    _make_tagged_linux_repo(tmp_path)
    cfg = Config.from_args(repo_root=tmp_path)
    stale_dir = tmp_path / "data/replay/latest"
    stale_dir.mkdir(parents=True)
    (stale_dir / "stale.txt").write_text("old replay output\n", encoding="utf-8")
    conn = connect(cfg.database)
    initialize(conn)
    conn.execute(
        """
        INSERT INTO replay_runs(run_id, started_at, status, include_head, build_bindings, configure, jobs, arch, c_roots, refs, summary)
        VALUES('latest', '2026-05-04T00:00:00+00:00', 'completed', 0, 0, 0, 1, 'x86_64', '[]', '[]', '{}')
        """
    )
    conn.execute(
        """
        INSERT INTO replay_pairs(pair_id, run_id, pair_index, old_ref, new_ref, old_version, new_version, started_at, status, extraction_summary, evaluation_summary)
        VALUES('latest-p999-stale', 'latest', 999, 'v6.0', 'v6.1', 'v6.0', 'v6.1', '2026-05-04T00:00:00+00:00', 'completed', '{}', '{}')
        """
    )
    conn.execute(
        """
        INSERT INTO drift_events(event_id, run_id, pair_id, old_version, new_version, drift_type, symbol, evidence)
        VALUES('stale-drift', 'latest', 'latest-p999-stale', 'v6.0', 'v6.1', 'SignatureDrift', 'stale_symbol', '{}')
        """
    )
    conn.execute(
        """
        INSERT INTO build_breakage_events(event_id, run_id, pair_id, build_log, line, symbol, text)
        VALUES('stale-build', 'latest', 'latest-p999-stale', 'old.log', 1, 'stale_symbol', 'old error')
        """
    )
    conn.commit()

    summary = run_version_replay(
        cfg,
        start="v6.1",
        include_head=False,
        roots=["include"],
        build_bindings=False,
        configure=False,
        max_files=10,
    )

    assert summary["pairs"] == 1
    assert summary["completed_pairs"] == 1
    assert summary["warnings"] >= 1
    assert summary["run_id"] == "latest"
    aggregate = Path(summary["aggregate_warnings"])
    assert aggregate.exists()
    assert aggregate.parent == stale_dir
    assert (stale_dir / "evaluation_protocol.json").exists()
    assert (stale_dir / "run_manifest.json").exists()
    assert not (stale_dir / "stale.txt").exists()
    warnings = read_warnings(aggregate)
    assert warnings[0]["run_id"] == summary["run_id"]
    assert warnings[0]["pair_id"]
    assert warnings[0]["pair_id"].startswith("latest-p001-")
    assert warnings[0]["old_version"] == "v6.1"
    assert warnings[0]["new_version"] == "v6.2"

    conn = connect(cfg.database)
    initialize(conn)
    assert conn.execute(
        "SELECT COUNT(*) AS n FROM replay_pairs WHERE pair_id='latest-p999-stale'"
    ).fetchone()["n"] == 0
    assert conn.execute("SELECT COUNT(*) AS n FROM drift_events WHERE event_id='stale-drift'").fetchone()["n"] == 0
    assert conn.execute(
        "SELECT COUNT(*) AS n FROM build_breakage_events WHERE event_id='stale-build'"
    ).fetchone()["n"] == 0
    pair = conn.execute("SELECT * FROM replay_pairs").fetchone()
    assert pair["status"] == "completed"
    assert pair["warning_count"] == len(warnings)
    extraction = json.loads(pair["extraction_summary"])
    assert extraction["tier2"]["new_warnings"] >= 1
    assert extraction["old"]["toolchain"]["required"]["rustc"] == "1.78.0"
    assert (tmp_path / "data/toolchain_matrix.json").exists()


def test_mark_stale_replay_runs_closes_interrupted_rows(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    conn = connect(cfg.database)
    initialize(conn)
    conn.execute(
        """
        INSERT INTO replay_runs(run_id, started_at, status, include_head, build_bindings, configure, jobs, arch, c_roots, refs, summary)
        VALUES('old-run', '2026-05-04T00:00:00+00:00', 'running', 0, 1, 1, 1, 'x86_64', '[]', '[]', '{}')
        """
    )
    conn.execute(
        """
        INSERT INTO replay_pairs(pair_id, run_id, pair_index, old_ref, new_ref, old_version, new_version, started_at, status, extraction_summary, evaluation_summary)
        VALUES('old-pair', 'old-run', 1, 'v6.1', 'v6.2', 'v6.1', 'v6.2', '2026-05-04T00:00:00+00:00', 'running', '{}', '{}')
        """
    )
    conn.commit()

    stale = mark_stale_replay_runs(cfg)

    assert stale == {"runs": 1, "pairs": 1}
    assert conn.execute("SELECT status FROM replay_runs WHERE run_id='old-run'").fetchone()["status"] == "stale"
    assert conn.execute("SELECT status FROM replay_pairs WHERE pair_id='old-pair'").fetchone()["status"] == "stale"


def test_version_replay_reranks_aggregate_for_multi_version_consistency(monkeypatch, tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    (tmp_path / "vendor/linux").mkdir(parents=True)
    versions = [
        {"version_id": "v1", "git_commit": "1" * 40, "tag": "v1", "date": None, "arch": None, "config_hash": None, "rustc_version": None, "clang_version": None, "bindgen_version": None},
        {"version_id": "v2", "git_commit": "2" * 40, "tag": "v2", "date": None, "arch": None, "config_hash": None, "rustc_version": None, "clang_version": None, "bindgen_version": None},
        {"version_id": "v3", "git_commit": "3" * 40, "tag": "v3", "date": None, "arch": None, "config_hash": None, "rustc_version": None, "clang_version": None, "bindgen_version": None},
    ]
    monkeypatch.setattr(replay_module, "select_versions", lambda *args, **kwargs: {"refs": ["v1", "v2", "v3"], "version_rows": versions})
    monkeypatch.setattr(replay_module, "write_toolchain_matrix", lambda *args, **kwargs: {"entries": []})
    monkeypatch.setattr(
        replay_module,
        "_extract_version",
        lambda cfg, version, **kwargs: {"worktree": {"path": str(tmp_path / "vendor/linux")}, "toolchain": {"required": {}}},
    )
    monkeypatch.setattr(
        replay_module,
        "run_tier1_with_context",
        lambda pair_cfg, **kwargs: {"warnings": 0, "warning_file": str(pair_cfg.warnings_jsonl)},
    )

    def write_pair_warning(pair_cfg, old=None, new=None, append=False, run_id=None, pair_id=None):
        write_warnings(
            pair_cfg,
            [
                {
                    "warning_id": "W-000001",
                    "run_id": run_id,
                    "pair_id": pair_id,
                    "old_version": old,
                    "new_version": new,
                    "type": "ErrorDrift",
                    "promotion_status": "promoted",
                    "c_evidence_level": "c_behavior_indicator",
                    "confidence": 0.8,
                    "c_side": {
                        "symbol": "foo_get",
                        "old_indicators": ["NULL_RETURN"],
                        "new_indicators": ["ERROR_CODE"],
                    },
                    "rust_side": {
                        "uses": [
                            {
                                "rust_file": "device.rs",
                                "line": 2,
                                "enclosing_function": "Device::get",
                                "enclosing_unsafe_block": 1,
                            }
                        ],
                    },
                    "evidence_chain": [{"evidence_file": "foo.c", "evidence_line": 1, "evidence_text": "return -EINVAL;"}],
                }
            ],
        )
        return {"warnings": 1, "new_warnings": 1, "warning_file": str(pair_cfg.warnings_jsonl)}

    monkeypatch.setattr(replay_module, "run_tier2_with_context", write_pair_warning)
    monkeypatch.setattr(
        replay_module,
        "run_evaluation",
        lambda pair_cfg, **kwargs: {"summary": {"warnings": len(read_warnings(pair_cfg.warnings_jsonl))}},
    )

    summary = run_version_replay(cfg, start="v1", include_head=False, toolchain="off")
    warnings = read_warnings(Path(summary["aggregate_warnings"]))
    run_dir = Path(summary["run_dir"])

    assert summary["pairs"] == 2
    assert summary["ranking"]["warnings"] == 2
    assert (run_dir / "evaluation_protocol.json").exists()
    assert (run_dir / "run_manifest.json").exists()
    assert all(len(warning["observed_pairs"]) == 2 for warning in warnings)
    assert all(warning["score_breakdown"]["multi_version_consistency"] == 2.0 for warning in warnings)


def test_version_replay_records_classified_stage_failure(monkeypatch, tmp_path: Path):
    _make_tagged_linux_repo(tmp_path)
    cfg = Config.from_args(repo_root=tmp_path)

    def fail_extract(*args, **kwargs):
        raise ReplayStageError("generated bindings missing for v6.1", "failed_missing_bindings", "bindings_missing")

    monkeypatch.setattr(replay_module, "_extract_version", fail_extract)

    summary = run_version_replay(
        cfg,
        start="v6.1",
        include_head=False,
        build_bindings=True,
        configure=True,
    )

    assert summary["completed_pairs"] == 0
    assert summary["failed_pairs"] == 1
    conn = connect(cfg.database)
    initialize(conn)
    pair = conn.execute("SELECT status, build_status, error FROM replay_pairs").fetchone()
    assert pair["status"] == "failed_missing_bindings"
    assert pair["build_status"] == "bindings_missing"
    assert "generated bindings missing" in pair["error"]


def test_version_replay_blocks_known_incompatible_toolchain(monkeypatch, tmp_path: Path):
    _make_tagged_linux_repo(tmp_path)
    cfg = Config.from_args(repo_root=tmp_path)

    def incompatible_matrix(cfg, refs, version_rows):
        return {
            "entries": [
                {
                    "version_id": row["version_id"],
                    "required": {"rustc": "1.62.0", "bindgen": "0.56.0"},
                    "missing": [],
                    "compatibility_issues": [
                        {
                            "kind": "bindgen_0_56_llvm16_anonymous_ident",
                            "severity": "blocking",
                            "detail": "bindgen 0.56.0 is incompatible with LLVM 18",
                        }
                    ],
                }
                for row in version_rows
            ]
        }

    monkeypatch.setattr(replay_module, "write_toolchain_matrix", incompatible_matrix)

    summary = run_version_replay(
        cfg,
        start="v6.1",
        include_head=False,
        build_bindings=True,
        configure=True,
    )

    assert summary["completed_pairs"] == 0
    assert summary["failed_pairs"] == 1
    conn = connect(cfg.database)
    initialize(conn)
    pair = conn.execute("SELECT status, build_status, error FROM replay_pairs").fetchone()
    assert pair["status"] == "failed_toolchain"
    assert pair["build_status"] == "toolchain_incompatible"
    assert "bindgen 0.56.0 is incompatible" in pair["error"]
