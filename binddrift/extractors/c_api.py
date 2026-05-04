from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from binddrift.config import Config
from binddrift.db import connect, initialize, upsert_many
from binddrift.kernel import default_version_id


FUNC_RE = re.compile(
    r"^\s*(?P<ret>(?:(?:static|extern|inline|const|struct|enum|unsigned|signed|long|short|void|int|char|bool|"
    r"[A-Za-z_][A-Za-z0-9_]*)[\s\*]+)+?)"
    r"(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*\((?P<params>[^;{}]*)\)\s*(?P<end>[;{])",
    re.DOTALL | re.MULTILINE,
)
STRUCT_RE = re.compile(r"^\s*struct\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*\{")
FIELD_RE = re.compile(r"^\s*(?P<ty>[A-Za-z_][A-Za-z0-9_\s\*\[\]]+)\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*)(?:\[[^]]+\])?;")
MACRO_RE = re.compile(r"^\s*#\s*define\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*)(?:\([^)]*\))?\s*(?P<value>.*)$")
CONTROL_NAMES = {"if", "for", "while", "switch", "return", "sizeof"}

INDICATORS: dict[str, list[str]] = {
    "NULL_RETURN": ["return NULL"],
    "ERR_PTR_RETURN": ["ERR_PTR(", "return ERR_CAST"],
    "IS_ERR_CHECK": ["IS_ERR(", "PTR_ERR("],
    "ERROR_CODE": ["-ENOMEM", "-EINVAL", "-EAGAIN", "-EBUSY", "-ENODEV", "-ENOENT", "-EPERM", "-EFAULT"],
    "REFCOUNT_GET": ["kref_get", "refcount_inc", "get_device", "_get("],
    "REFCOUNT_PUT": ["kref_put", "refcount_dec", "put_device", "_put("],
    "ALLOC": ["kmalloc", "kzalloc", "vmalloc", "_alloc(", "_create(", "_new("],
    "FREE": ["kfree", "vfree", "_free(", "_destroy(", "_release("],
    "MAY_SLEEP": ["might_sleep", "mutex_lock", "wait_event", "schedule(", "GFP_KERNEL", "down_read", "down_write"],
    "ATOMIC_CONTEXT": ["spin_lock", "rcu_read_lock", "GFP_ATOMIC"],
}


def _paths(cfg: Config, roots: list[str]) -> list[Path]:
    files: list[Path] = []
    for root in roots:
        base = cfg.linux_tree / root
        if base.is_file():
            files.append(base)
        elif base.exists():
            files.extend(path for path in base.rglob("*") if path.suffix in {".h", ".c"})
    return sorted(set(files))


def _line_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def _split_top_level(value: str) -> list[str]:
    parts: list[str] = []
    depth = 0
    start = 0
    for idx, char in enumerate(value):
        if char in "([{":
            depth += 1
        elif char in ")]}" and depth:
            depth -= 1
        elif char == "," and depth == 0:
            parts.append(value[start:idx].strip())
            start = idx + 1
    tail = value[start:].strip()
    if tail and tail != "void":
        parts.append(tail)
    return parts


def _parse_params(params: str) -> list[str]:
    return [" ".join(part.split()) for part in _split_top_level(params)]


def _parse_file(path: Path, version_id: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    functions: list[dict[str, Any]] = []
    structs: list[dict[str, Any]] = []
    macros: list[dict[str, Any]] = []
    indicators: list[dict[str, Any]] = []
    current_function: tuple[str, int] | None = None
    body_start_by_line: dict[int, str] = {}

    for match in FUNC_RE.finditer(text):
        name = match.group("name")
        if name in CONTROL_NAMES:
            continue
        start_line = _line_for_offset(text, match.start())
        row = {
            "version_id": version_id,
            "c_symbol": name,
            "return_type": " ".join(match.group("ret").split()),
            "params": json.dumps(_parse_params(match.group("params")), sort_keys=True),
            "header_file": str(path) if path.suffix == ".h" else "",
            "definition_file": str(path) if path.suffix == ".c" or match.group("end") == "{" else "",
            "line": start_line,
        }
        functions.append(row)
        if match.group("end") == "{":
            body_start_by_line[_line_for_offset(text, match.end() - 1)] = name

    for idx, raw in enumerate(lines, start=1):
        line = raw.strip()
        if not line or line.startswith("*"):
            continue
        if idx in body_start_by_line:
            current_function = (body_start_by_line[idx], 0)
        if match := FUNC_RE.match(raw):
            name = match.group("name")
            if name not in CONTROL_NAMES and match.group("end") == "{":
                current_function = (name, 0)
        if match := MACRO_RE.match(raw):
            macros.append(
                {
                    "version_id": version_id,
                    "name": match.group("name"),
                    "value": match.group("value").strip(),
                    "source_file": str(path),
                    "line": idx,
                }
            )
        if match := STRUCT_RE.match(raw):
            name = match.group("name")
            fields: list[dict[str, str]] = []
            j = idx
            while j < len(lines) and "};" not in lines[j]:
                if field := FIELD_RE.match(lines[j]):
                    fields.append({"name": field.group("name"), "type": " ".join(field.group("ty").split())})
                j += 1
            structs.append(
                {
                    "version_id": version_id,
                    "c_type": name,
                    "fields": json.dumps(fields, sort_keys=True),
                    "size": None,
                    "align": None,
                    "header_file": str(path),
                    "line": idx,
                }
            )
        symbol = current_function[0] if current_function else "<file>"
        for indicator_type, needles in INDICATORS.items():
            if any(needle in raw for needle in needles):
                indicators.append(
                    {
                        "version_id": version_id,
                        "c_symbol": symbol,
                        "indicator_type": indicator_type,
                        "evidence_file": str(path),
                        "evidence_line": idx,
                        "evidence_text": raw.strip()[:500],
                        "confidence": 0.7 if symbol != "<file>" else 0.4,
                    }
                )
        if current_function:
            depth = current_function[1] + raw.count("{") - raw.count("}")
            current_function = (current_function[0], depth) if depth > 0 else None
    return functions, structs, macros, indicators


def extract_c_api(cfg: Config, roots: list[str] | None = None, version_id: str | None = None, max_files: int | None = None) -> dict[str, Any]:
    cfg.ensure_dirs()
    vid = version_id or default_version_id(cfg)
    selected_roots = roots or ["include", "rust/helpers"]
    files = _paths(cfg, selected_roots)
    if max_files:
        files = files[:max_files]
    all_functions: list[dict[str, Any]] = []
    all_structs: list[dict[str, Any]] = []
    all_macros: list[dict[str, Any]] = []
    all_indicators: list[dict[str, Any]] = []
    for path in files:
        functions, structs, macros, indicators = _parse_file(path, vid)
        all_functions.extend(functions)
        all_structs.extend(structs)
        all_macros.extend(macros)
        all_indicators.extend(indicators)
    conn = connect(cfg.database)
    initialize(conn)
    upsert_many(conn, "c_functions", all_functions)
    upsert_many(conn, "c_structs", all_structs)
    upsert_many(conn, "c_macros", all_macros)
    upsert_many(conn, "c_behavior_indicators", all_indicators)
    return {
        "database": str(cfg.database),
        "version_id": vid,
        "roots": selected_roots,
        "files": len(files),
        "c_functions": len(all_functions),
        "c_structs": len(all_structs),
        "c_macros": len(all_macros),
        "c_behavior_indicators": len(all_indicators),
    }
