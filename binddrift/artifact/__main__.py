from __future__ import annotations

import argparse
import json

from binddrift.config import Config
from binddrift.artifact.strict_validator import VALIDATION_STAGES, reproduce_artifact, validate_artifact


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="BindDrift artifact reproduction and validation.")
    parser.add_argument("command", choices=["reproduce", "validate"])
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--strict-ccfb", action="store_true", help="Run strict CCF-B consistency checks.")
    parser.add_argument(
        "--stage",
        choices=VALIDATION_STAGES,
        default="final",
        help="Validation stage to enforce. Use final for the full strict CCF-B gate.",
    )
    args = parser.parse_args(argv)
    cfg = Config.from_args(repo_root=args.repo_root)
    if args.command == "reproduce":
        result = reproduce_artifact(cfg)
    else:
        result = validate_artifact(cfg, strict_ccfb=args.strict_ccfb, stage=args.stage)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result.get("passes") else 1


if __name__ == "__main__":
    raise SystemExit(main())
