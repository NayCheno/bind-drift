from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path
from typing import Any

from .config import Config
from .environment import capture_environment


REQUIRED_TOOLS = ("make", "clang", "rustc", "rustfmt", "bindgen")


def _run(command: list[str], cwd: Path | None = None, timeout: int = 120) -> dict[str, Any]:
    try:
        proc = subprocess.run(
            command,
            cwd=cwd,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
            timeout=timeout,
        )
        return {
            "command": command,
            "returncode": proc.returncode,
            "output": proc.stdout[-12000:],
        }
    except subprocess.TimeoutExpired as exc:
        return {
            "command": command,
            "returncode": 124,
            "output": (exc.stdout or "")[-12000:] if isinstance(exc.stdout, str) else "",
            "timed_out": True,
        }


def check_toolchain(cfg: Config, run_rustavailable: bool = False) -> dict[str, Any]:
    cfg.ensure_dirs()
    env = capture_environment(cfg)
    tools = env["tools"]
    missing = [name for name in REQUIRED_TOOLS if not tools.get(name, {}).get("available")]
    result: dict[str, Any] = {
        "status": "ok" if not missing else "missing_tools",
        "missing": missing,
        "tools": {name: tools.get(name, {"available": False}) for name in REQUIRED_TOOLS},
        "linux_commit": env["linux_commit"],
        "linux_describe": env["linux_describe"],
        "rustavailable": None,
        "recommendations": recommendations(missing),
    }
    if run_rustavailable:
        rustavailable = _run(["make", "LLVM=1", "rustavailable"], cwd=cfg.linux_tree)
        result["rustavailable"] = rustavailable
        if rustavailable["returncode"] != 0:
            result["status"] = "rustavailable_failed"
            result["recommendations"].extend(rustavailable_recommendations(rustavailable["output"]))
    path = cfg.data_dir / "toolchain.json"
    path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    result["written_to"] = str(path)
    return result


def bootstrap_toolchain(cfg: Config, install_bindgen: bool = False, install_rust_src: bool = False) -> dict[str, Any]:
    cfg.ensure_dirs()
    before = check_toolchain(cfg, run_rustavailable=False)
    actions: list[dict[str, Any]] = []
    if install_bindgen and not shutil.which("bindgen"):
        actions.append(_run(["cargo", "install", "--locked", "bindgen-cli"], timeout=1800))
    if install_rust_src:
        actions.append(_run(["rustup", "component", "add", "rust-src"], timeout=600))
    after = check_toolchain(cfg, run_rustavailable=False)
    return {
        "before": before,
        "actions": actions,
        "after": after,
        "next_step": "Run `uv run binddrift toolchain check --run-rustavailable` to verify kernel Rust detection.",
    }


def recommendations(missing: list[str]) -> list[str]:
    out: list[str] = []
    if "bindgen" in missing:
        out.append("Install bindgen with `cargo install --locked bindgen-cli` or a distro package.")
    if "rustc" in missing:
        out.append("Install a Rust compiler supported by the checked-out kernel.")
    if "rustfmt" in missing:
        out.append("Install rustfmt through rustup or the distribution Rust package.")
    if "clang" in missing:
        out.append("Install LLVM/Clang and libclang for bindgen.")
    if "make" in missing:
        out.append("Install GNU make.")
    return out


def rustavailable_recommendations(output: str) -> list[str]:
    lowered = output.lower()
    out: list[str] = []
    if "core' standard library could not be found" in lowered or "rust-src" in lowered:
        out.append("Install Rust standard library sources with `rustup component add rust-src`.")
    if "bindgen" in lowered and "could not be found" in lowered:
        out.append("Install bindgen with `cargo install --locked bindgen-cli` or a distro package.")
    if "libclang" in lowered:
        out.append("Install libclang or set LIBCLANG_PATH so bindgen can load it.")
    return out
