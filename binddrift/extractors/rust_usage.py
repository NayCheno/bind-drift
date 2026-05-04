from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from binddrift.config import Config
from binddrift.db import connect, initialize, upsert_many
from binddrift.kernel import default_version_id


BINDING_RE = re.compile(r"(?:crate::|\$crate::)?bindings::(?P<name>[A-Za-z_][A-Za-z0-9_]*)")
PUB_FN_RE = re.compile(
    r"(?P<vis>pub(?:\([^)]*\))?)?\s*(?:unsafe\s+)?fn\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*\((?P<params>[^)]*)\)\s*(?:->\s*(?P<ret>[^{;]+))?"
)
IMPL_RE = re.compile(r"impl(?:<[^>]+>)?\s+(?:(?P<trait>Drop|Clone)\s+for\s+)?(?P<ty>[A-Za-z_][A-Za-z0-9_:<>]*)")
STRUCT_RE = re.compile(r"pub\s+struct\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*)")


def _brace_delta(line: str) -> int:
    return line.count("{") - line.count("}")


def _nearest_api(apis: list[dict[str, Any]], line_no: int) -> str | None:
    before = [api for api in apis if api["line"] <= line_no]
    if not before:
        return None
    return before[-1]["api_name"]


def _nearest_binding(uses: list[dict[str, Any]], line_no: int) -> str | None:
    near = [use for use in uses if abs(use["line"] - line_no) <= 5]
    return near[-1]["binding_symbol"] if near else None


def _parse_file(path: Path, version_id: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    rel = str(path)
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    uses: list[dict[str, Any]] = []
    apis: list[dict[str, Any]] = []
    comments: list[dict[str, Any]] = []
    unsafe_depth = 0
    impl_stack: list[tuple[str, int]] = []
    current_fn: tuple[str, int] | None = None
    current_type: str | None = None

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if match := STRUCT_RE.search(stripped):
            current_type = match.group("name")
        if match := IMPL_RE.match(stripped):
            ty = match.group("ty")
            if match.group("trait"):
                ty = f"{match.group('trait')} for {ty}"
            impl_stack.append((ty, max(1, _brace_delta(stripped))))
            current_type = ty
        if "unsafe" in stripped and "{" in stripped:
            unsafe_depth += stripped.count("{")

        for match in BINDING_RE.finditer(line):
            uses.append(
                {
                    "version_id": version_id,
                    "rust_file": rel,
                    "line": idx,
                    "binding_symbol": match.group("name"),
                    "enclosing_unsafe_block": int(unsafe_depth > 0 or "unsafe {" in stripped),
                    "enclosing_function": current_fn[0] if current_fn else None,
                    "enclosing_impl": impl_stack[-1][0] if impl_stack else None,
                    "enclosing_type": current_type,
                }
            )

        if "SAFETY:" in stripped or stripped.startswith("///") or stripped.startswith("//!"):
            comments.append(
                {
                    "version_id": version_id,
                    "rust_file": rel,
                    "line": idx,
                    "text": stripped,
                    "nearby_binding_symbol": None,
                    "nearby_api": None,
                }
            )

        if match := PUB_FN_RE.search(stripped):
            if match.group("vis"):
                name = match.group("name")
                api_name = f"{impl_stack[-1][0]}::{name}" if impl_stack else name
                current_fn = (api_name, max(1, _brace_delta(stripped)))
                apis.append(
                    {
                        "version_id": version_id,
                        "rust_file": rel,
                        "api_name": api_name,
                        "receiver_type": impl_stack[-1][0] if impl_stack else None,
                        "visibility": match.group("vis"),
                        "return_type": (match.group("ret") or "()").strip(),
                        "params": json.dumps(match.group("params").strip()),
                        "uses_bindings": "[]",
                        "line": idx,
                    }
                )
            else:
                current_fn = (match.group("name"), max(1, _brace_delta(stripped)))

        delta = _brace_delta(stripped)
        if current_fn:
            current_fn = (current_fn[0], current_fn[1] + delta)
            if current_fn[1] <= 0:
                current_fn = None
        if impl_stack:
            ty, depth = impl_stack[-1]
            depth += delta
            if depth <= 0:
                impl_stack.pop()
            else:
                impl_stack[-1] = (ty, depth)
        if unsafe_depth:
            unsafe_depth = max(0, unsafe_depth + delta)

    uses_by_api: dict[str, set[str]] = {}
    for use in uses:
        api = use["enclosing_function"]
        if api:
            uses_by_api.setdefault(api, set()).add(use["binding_symbol"])
    for api in apis:
        api["uses_bindings"] = json.dumps(sorted(uses_by_api.get(api["api_name"], set())))
    for comment in comments:
        comment["nearby_binding_symbol"] = _nearest_binding(uses, comment["line"])
        comment["nearby_api"] = _nearest_api(apis, comment["line"])
    return uses, apis, comments


def extract_rust_usage(cfg: Config, version_id: str | None = None) -> dict[str, Any]:
    cfg.ensure_dirs()
    vid = version_id or default_version_id(cfg)
    root = cfg.linux_tree / "rust/kernel"
    all_uses: list[dict[str, Any]] = []
    all_apis: list[dict[str, Any]] = []
    all_comments: list[dict[str, Any]] = []
    for path in sorted(root.rglob("*.rs")):
        uses, apis, comments = _parse_file(path, vid)
        all_uses.extend(uses)
        all_apis.extend(apis)
        all_comments.extend(comments)
    conn = connect(cfg.database)
    initialize(conn)
    upsert_many(conn, "rust_binding_uses", all_uses)
    upsert_many(conn, "rust_safe_apis", all_apis)
    upsert_many(conn, "rust_safety_comments", all_comments)
    return {
        "database": str(cfg.database),
        "version_id": vid,
        "rust_files": len(list(root.rglob("*.rs"))) if root.exists() else 0,
        "binding_uses": len(all_uses),
        "safe_apis": len(all_apis),
        "safety_comments": len(all_comments),
    }
