from pathlib import Path

from binddrift.config import Config
from binddrift.ranking.scorer import score_warning


def test_config_defaults(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    assert cfg.linux_tree == tmp_path / "vendor/linux"
    assert cfg.database.name == "binddrift.sqlite3"


def test_score_contract_warning():
    warning = {
        "type": "NullabilityDrift",
        "confidence": 0.8,
        "rust_side": {"uses": [{"enclosing_unsafe_block": 1}, {"enclosing_unsafe_block": 0}]},
    }
    assert score_warning(warning) > 10
