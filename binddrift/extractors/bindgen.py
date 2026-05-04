from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from binddrift.config import Config
from binddrift.db import connect, initialize, upsert_many
from binddrift.kernel import default_version_id


EXTERN_FUNCTION_RE = re.compile(
    r"pub\s+fn\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*\((?P<params>.*?)\)\s*(?:->\s*(?P<ret>[^;]+))?;",
    re.DOTALL,
)
STRUCT_RE = re.compile(r"pub\s+struct\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*\{")
FIELD_RE = re.compile(r"pub\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*):\s*(?P<ty>[^,]+),?")
CONST_RE = re.compile(
    r"pub\s+const\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*):\s*(?P<ty>[^=]+)=\s*(?P<value>[^;]+);",
    re.DOTALL,
)
LAYOUT_SIZE_RE = re.compile(r"assert_eq!\s*\(\s*::core::mem::size_of::<(?P<ty>[^>]+)>\(\)\s*,\s*(?P<size>\d+)")
LAYOUT_ALIGN_RE = re.compile(r"assert_eq!\s*\(\s*::core::mem::align_of::<(?P<ty>[^>]+)>\(\)\s*,\s*(?P<align>\d+)")
LAYOUT_OFFSET_RE = re.compile(
    r"assert_eq!\s*\(\s*unsafe\s*\{\s*&\(\*\(0\s+as\s+\*const\s+(?P<ty>[^)]+)\)\)\.(?P<field>[A-Za-z_][A-Za-z0-9_]*)"
    r"\s+as\s+\*const\s+_\s+as\s+usize\s*\}\s*,\s*(?P<offset>\d+)"
)


@dataclass
class BindingFacts:
    functions: list[dict[str, Any]]
    structs: list[dict[str, Any]]
    consts: list[dict[str, Any]]
    layouts: list[dict[str, Any]]
    missing_files: list[str]


def _line_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def _split_top_level(value: str) -> list[str]:
    parts: list[str] = []
    start = 0
    depth = 0
    pairs = {"(": ")", "<": ">", "[": "]"}
    closers = set(pairs.values())
    for idx, char in enumerate(value):
        if char in pairs:
            depth += 1
        elif char in closers and depth:
            depth -= 1
        elif char == "," and depth == 0:
            parts.append(value[start:idx].strip())
            start = idx + 1
    tail = value[start:].strip()
    if tail:
        parts.append(tail)
    return parts


def _parse_params(params: str) -> list[dict[str, str]]:
    out = []
    for raw in _split_top_level(" ".join(params.split())):
        if ":" in raw:
            name, ty = raw.split(":", 1)
            out.append({"name": name.strip(), "type": ty.strip()})
        else:
            out.append({"name": "", "type": raw})
    return out


def _parse_file(path: Path, version_id: str) -> BindingFacts:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    functions: list[dict[str, Any]] = []
    structs: list[dict[str, Any]] = []
    consts: list[dict[str, Any]] = []
    layouts: list[dict[str, Any]] = []
    for match in EXTERN_FUNCTION_RE.finditer(text):
        name = match.group("name")
        functions.append(
            {
                "version_id": version_id,
                "rust_symbol": name,
                "c_symbol": name,
                "params": json.dumps(_parse_params(match.group("params")), sort_keys=True),
                "return_type": " ".join((match.group("ret") or "()").split()),
                "is_unsafe": 1,
                "source_file": str(path),
                "line": _line_for_offset(text, match.start()),
            }
        )
    for match in CONST_RE.finditer(text):
        name = match.group("name")
        consts.append(
            {
                "version_id": version_id,
                "rust_name": name,
                "c_name": name,
                "value": " ".join(match.group("value").split()),
                "source_file": str(path),
                "line": _line_for_offset(text, match.start()),
            }
        )
    i = 0
    while i < len(lines):
        line = lines[i]
        if match := STRUCT_RE.search(line):
            name = match.group("name")
            fields: list[dict[str, str]] = []
            j = i + 1
            depth = line.count("{") - line.count("}")
            while j < len(lines) and depth > 0:
                if field := FIELD_RE.search(lines[j].strip()):
                    fields.append({"name": field.group("name"), "type": field.group("ty").strip()})
                depth += lines[j].count("{") - lines[j].count("}")
                j += 1
            structs.append(
                {
                    "version_id": version_id,
                    "rust_type": name,
                    "c_type": name,
                    "fields": json.dumps(fields, sort_keys=True),
                    "size": None,
                    "align": None,
                    "source_file": str(path),
                    "line": i + 1,
                }
            )
            i = j
        if match := LAYOUT_SIZE_RE.search(line):
            layouts.append(
                {
                    "version_id": version_id,
                    "rust_type": match.group("ty").strip(),
                    "field_name": "",
                    "size": int(match.group("size")),
                    "align": None,
                    "offset": None,
                    "source_file": str(path),
                    "line": i + 1,
                }
            )
        if match := LAYOUT_ALIGN_RE.search(line):
            layouts.append(
                {
                    "version_id": version_id,
                    "rust_type": match.group("ty").strip(),
                    "field_name": "",
                    "size": None,
                    "align": int(match.group("align")),
                    "offset": None,
                    "source_file": str(path),
                    "line": i + 1,
                }
            )
        if match := LAYOUT_OFFSET_RE.search(line):
            layouts.append(
                {
                    "version_id": version_id,
                    "rust_type": match.group("ty").strip(),
                    "field_name": match.group("field"),
                    "size": None,
                    "align": None,
                    "offset": int(match.group("offset")),
                    "source_file": str(path),
                    "line": i + 1,
                }
            )
        i += 1
    return BindingFacts(functions, structs, consts, layouts, [])


def extract_bindings(cfg: Config, objtree: Path | None = None, version_id: str | None = None) -> dict[str, Any]:
    cfg.ensure_dirs()
    vid = version_id or default_version_id(cfg)
    obj = objtree or cfg.build_root / vid
    files = [
        obj / "rust/bindings/bindings_generated.rs",
        obj / "rust/bindings/bindings_helpers_generated.rs",
    ]
    facts = BindingFacts([], [], [], [], [])
    for path in files:
        if not path.exists():
            facts.missing_files.append(str(path))
            continue
        parsed = _parse_file(path, vid)
        facts.functions.extend(parsed.functions)
        facts.structs.extend(parsed.structs)
        facts.consts.extend(parsed.consts)
        facts.layouts.extend(parsed.layouts)
    conn = connect(cfg.database)
    initialize(conn)
    upsert_many(conn, "binding_functions", facts.functions)
    upsert_many(conn, "binding_structs", facts.structs)
    upsert_many(conn, "binding_consts", facts.consts)
    upsert_many(conn, "layout_facts", facts.layouts)
    upsert_many(
        conn,
        "extraction_errors",
        [
            {
                "version_id": vid,
                "stage": "bindings",
                "source": path,
                "message": "generated binding file is missing",
                "severity": "warning",
            }
            for path in facts.missing_files
        ],
    )
    return {
        "database": str(cfg.database),
        "version_id": vid,
        "objtree": str(obj),
        "binding_functions": len(facts.functions),
        "binding_structs": len(facts.structs),
        "binding_consts": len(facts.consts),
        "layout_facts": len(facts.layouts),
        "missing_files": facts.missing_files,
    }
