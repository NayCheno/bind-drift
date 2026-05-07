from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from binddrift.config import Config
from binddrift.db import connect, initialize, upsert_many
from binddrift.kernel import default_version_id


BINDING_RE = re.compile(r"(?:::)?(?:(?:crate|\$crate|super|self|[A-Za-z_][A-Za-z0-9_]*)::)*bindings::(?P<name>[A-Za-z_][A-Za-z0-9_]*)")
PUB_FN_RE = re.compile(
    r"(?P<vis>pub(?:\([^)]*\))?)?\s*(?:unsafe\s+)?fn\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*\((?P<params>[^)]*)\)\s*(?:->\s*(?P<ret>[^{;]+))?"
)
IMPL_RE = re.compile(r"impl\b")
STRUCT_RE = re.compile(r"pub\s+struct\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*)")
ERROR_MAPPING_PATTERNS = {
    "ERR_PTR_MAPPING": "from_err_ptr",
    "TO_RESULT_MAPPING": "to_result",
    "NONNULL_MAPPING": "NonNull::new",
    "IS_ERR_MAPPING": "IS_ERR",
    "PTR_ERR_MAPPING": "PTR_ERR",
}
LIFETIME_PATTERNS = {
    "FROM_RAW": "from_raw",
    "INTO_RAW": "into_raw",
    "AS_PTR": "as_ptr",
    "OPAQUE": "Opaque<",
    "AREF": "ARef<",
    "FOREIGN_OWNABLE": "ForeignOwnable",
    "MANUALLY_DROP": "ManuallyDrop",
    "REFCOUNT_LIKE": "update_refcount",
    "REFCOUNT_INC": "inc_ref",
    "REFCOUNT_INCR": "incr_refcount",
    "REFCOUNT_DEC": "dec_ref",
    "REFCOUNT_DECREF": "decr_refcount",
    "REFCOUNT_WRAPPER": "refcount",
}


@dataclass
class RustLineContext:
    function: str | None = None
    impl_type: str | None = None
    enclosing_type: str | None = None
    unsafe_block: bool = False


@dataclass
class RustSyntax:
    line_context: dict[int, RustLineContext] = field(default_factory=dict)
    apis: list[dict[str, Any]] = field(default_factory=list)
    lifetime_facts: list[dict[str, Any]] = field(default_factory=list)
    binding_uses: list[dict[str, Any]] = field(default_factory=list)


def _brace_delta(line: str) -> int:
    return line.count("{") - line.count("}")


def _nearest_api(apis: list[dict[str, Any]], line_no: int) -> str | None:
    before = [api for api in apis if api["line"] <= line_no]
    if not before:
        return None
    return before[-1]["api_name"]


def _containing_api(apis: list[dict[str, Any]], line_no: int) -> str | None:
    containers = [api for api in apis if api.get("line") <= line_no <= api.get("end_line", api["line"])]
    if containers:
        return containers[-1]["api_name"]
    return _nearest_api(apis, line_no)


def _nearest_binding(
    uses: list[dict[str, Any]],
    line_no: int,
    api_name: str | None = None,
    prefer_following: bool = False,
    allow_cross_api: bool = True,
) -> str | None:
    candidates = [
        use
        for use in uses
        if abs(int(use["line"]) - line_no) <= 5 and (api_name is None or use.get("enclosing_function") == api_name)
    ]
    if not candidates and api_name is not None and allow_cross_api:
        candidates = [use for use in uses if abs(int(use["line"]) - line_no) <= 5]
    if not candidates:
        return None

    def sort_key(use: dict[str, Any]) -> tuple[int, int, int]:
        distance = int(use["line"]) - line_no
        following_rank = 0 if distance >= 0 else 1
        unsafe_rank = 0 if int(use.get("enclosing_unsafe_block") or 0) else 1
        if not prefer_following:
            following_rank = 0
        return (following_rank, abs(distance), unsafe_rank)

    return sorted(candidates, key=sort_key)[0]["binding_symbol"]


def _is_comment_line(stripped: str) -> bool:
    return stripped.startswith(("///", "//!","//", "/*", "*"))


def _is_import_line(stripped: str) -> bool:
    return stripped.startswith("use ") or stripped.startswith("pub use ")


def _return_mapping_type(ret: str | None) -> str | None:
    types = _return_mapping_types(ret)
    return types[0] if types else None


def _return_mapping_types(ret: str | None) -> list[str]:
    if not ret:
        return []
    out: list[str] = []
    if "Result" in ret:
        out.append("RESULT_RETURN")
    if "Option" in ret:
        out.append("OPTION_RETURN")
    return out


def _matching_angle_end(value: str, start: int) -> int | None:
    depth = 0
    for idx in range(start, len(value)):
        char = value[idx]
        if char == "<":
            depth += 1
        elif char == ">":
            depth -= 1
            if depth == 0:
                return idx
    return None


def _parse_impl_type(stripped: str) -> tuple[str, str | None] | None:
    if not stripped.startswith("impl"):
        return None
    rest = stripped[len("impl") :].strip()
    if rest.startswith("<"):
        end = _matching_angle_end(rest, 0)
        if end is None:
            return None
        rest = rest[end + 1 :].strip()
    rest = rest.split("{", 1)[0].strip()
    rest = rest.split(" where ", 1)[0].strip()
    if not rest:
        return None
    trait = None
    ty = rest
    if " for " in rest:
        trait, ty = rest.rsplit(" for ", 1)
        trait = trait.strip()
        ty = ty.strip()
    return ty, trait


def _tree_sitter_parser() -> Any | None:
    try:
        from tree_sitter import Language, Parser
        import tree_sitter_rust
    except Exception:
        return None
    parser = Parser()
    try:
        parser.language = Language(tree_sitter_rust.language())
    except Exception:
        return None
    return parser


def _node_text(node: Any) -> str:
    return node.text.decode("utf-8", errors="replace") if getattr(node, "text", None) is not None else ""


def _line_span(node: Any) -> tuple[int, int]:
    return int(node.start_point.row) + 1, int(node.end_point.row) + 1


def _child_by_type(node: Any, node_type: str) -> Any | None:
    for child in node.children:
        if child.type == node_type:
            return child
    return None


def _has_child_type(node: Any, node_type: str) -> bool:
    return _child_by_type(node, node_type) is not None


def _function_modifiers(node: Any) -> str:
    if modifiers := _child_by_type(node, "function_modifiers"):
        return _node_text(modifiers)
    return ""


def _visibility(node: Any, trait: str | None = None) -> str | None:
    if visibility := _child_by_type(node, "visibility_modifier"):
        return _node_text(visibility)
    if trait:
        return "trait"
    return None


def _function_name(node: Any) -> str | None:
    name = node.child_by_field_name("name")
    return _node_text(name) if name is not None else None


def _function_params(node: Any) -> str:
    params = node.child_by_field_name("parameters")
    if params is None:
        return ""
    value = _node_text(params).strip()
    return value[1:-1].strip() if value.startswith("(") and value.endswith(")") else value


def _function_return_type(node: Any) -> str:
    ret = node.child_by_field_name("return_type")
    return _node_text(ret).strip() if ret is not None else "()"


def _iter_nodes(node: Any) -> list[Any]:
    out: list[Any] = []
    stack = [node]
    while stack:
        current = stack.pop()
        out.append(current)
        stack.extend(reversed(current.children))
    return out


def _binding_symbol_from_node(node: Any) -> str | None:
    if node.type not in {"scoped_identifier", "scoped_type_identifier"}:
        return None
    parts = [part for part in _node_text(node).split("::") if part]
    if "bindings" not in parts:
        return None
    idx = parts.index("bindings")
    if idx + 1 >= len(parts):
        return None
    return parts[idx + 1]


def _line_context(syntax: RustSyntax, line_no: int) -> RustLineContext:
    return syntax.line_context.setdefault(line_no, RustLineContext())


def _apply_span_context(
    syntax: RustSyntax,
    node: Any,
    *,
    function: str | None = None,
    impl_type: str | None = None,
    enclosing_type: str | None = None,
    unsafe_block: bool | None = None,
) -> None:
    start, end = _line_span(node)
    for line_no in range(start, end + 1):
        context = _line_context(syntax, line_no)
        if function:
            context.function = function
        if impl_type:
            context.impl_type = impl_type
        if enclosing_type:
            context.enclosing_type = enclosing_type
        if unsafe_block is not None:
            context.unsafe_block = context.unsafe_block or unsafe_block


def _impl_context(node: Any) -> tuple[str | None, str | None]:
    impl_type = node.child_by_field_name("type")
    trait = node.child_by_field_name("trait")
    return (
        _node_text(impl_type).strip() if impl_type is not None else None,
        _node_text(trait).strip() if trait is not None else None,
    )


def _parse_tree_sitter_syntax(text: str, path: Path, version_id: str) -> RustSyntax | None:
    parser = _tree_sitter_parser()
    if parser is None:
        return None
    tree = parser.parse(text.encode("utf-8", errors="replace"))
    root = tree.root_node
    if root.has_error:
        return None
    rel = str(path)
    syntax = RustSyntax()

    def walk(
        node: Any,
        impl_type: str | None = None,
        trait: str | None = None,
        enclosing_type: str | None = None,
        function_name: str | None = None,
        unsafe_active: bool = False,
        in_use_declaration: bool = False,
    ) -> None:
        local_impl = impl_type
        local_trait = trait
        local_type = enclosing_type
        local_function = function_name
        local_unsafe = unsafe_active
        local_in_use_declaration = in_use_declaration or node.type == "use_declaration"
        if node.type == "struct_item":
            name = node.child_by_field_name("name") or _child_by_type(node, "type_identifier")
            if name is not None:
                local_type = _node_text(name)
                _apply_span_context(syntax, node, enclosing_type=local_type)
        elif node.type == "impl_item":
            local_impl, local_trait = _impl_context(node)
            if local_impl:
                _apply_span_context(syntax, node, impl_type=local_impl, enclosing_type=local_impl)
            if local_trait in {"Drop", "Clone"} and local_impl:
                start, _end = _line_span(node)
                syntax.lifetime_facts.append(
                    {
                        "version_id": version_id,
                        "rust_file": rel,
                        "line": start,
                        "fact_type": f"IMPL_{local_trait.upper()}",
                        "rust_type": local_impl,
                        "uses_bindings": "[]",
                        "evidence_text": _node_text(node).splitlines()[0][:500],
                    }
                )
        elif node.type == "function_item":
            name = _function_name(node)
            if name:
                local_function = f"{local_impl}::{name}" if local_impl else name
                _apply_span_context(
                    syntax,
                    node,
                    function=local_function,
                    impl_type=local_impl,
                    enclosing_type=local_impl or local_type,
                )
                visibility = _visibility(node, local_trait)
                if visibility:
                    start, _end = _line_span(node)
                    ret = _function_return_type(node)
                    syntax.apis.append(
                        {
                            "version_id": version_id,
                            "rust_file": rel,
                            "api_name": local_function,
                            "receiver_type": local_impl,
                            "visibility": visibility,
                            "return_type": ret,
                            "params": json.dumps(_function_params(node)),
                            "uses_bindings": "[]",
                            "line": start,
                            "end_line": _end,
                        }
                    )
        if node.type == "unsafe_block":
            local_unsafe = True
            _apply_span_context(syntax, node, unsafe_block=True)
        if not local_in_use_declaration and (symbol := _binding_symbol_from_node(node)):
            start, _end = _line_span(node)
            syntax.binding_uses.append(
                {
                    "version_id": version_id,
                    "rust_file": rel,
                    "line": start,
                    "column": int(node.start_point.column) + 1,
                    "end_line": _end,
                    "end_column": int(node.end_point.column) + 1,
                    "binding_symbol": symbol,
                    "enclosing_unsafe_block": int(local_unsafe),
                    "enclosing_function": local_function,
                    "enclosing_impl": local_impl,
                    "enclosing_type": local_type or local_impl,
                }
            )
        for child in node.children:
            walk(child, local_impl, local_trait, local_type, local_function, local_unsafe, local_in_use_declaration)

    walk(root)
    return syntax


def _finish_facts(
    uses: list[dict[str, Any]],
    apis: list[dict[str, Any]],
    comments: list[dict[str, Any]],
    lifetime_facts: list[dict[str, Any]],
    error_mappings: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    uses_by_api: dict[str, set[str]] = {}
    for use in uses:
        api = use["enclosing_function"]
        if api:
            uses_by_api.setdefault(api, set()).add(use["binding_symbol"])
    for api in apis:
        api["uses_bindings"] = json.dumps(sorted(uses_by_api.get(api["api_name"], set())))
    for comment in comments:
        nearby_api = _containing_api(apis, comment["line"])
        comment["nearby_api"] = nearby_api
        comment["nearby_binding_symbol"] = _nearest_binding(
            uses,
            comment["line"],
            api_name=nearby_api,
            prefer_following="SAFETY:" in comment["text"],
            allow_cross_api=False,
        )
    for mapping in error_mappings:
        nearby_api = mapping.get("nearby_api") or _containing_api(apis, mapping["line"])
        mapping["nearby_binding_symbol"] = _nearest_binding(
            uses,
            mapping["line"],
            api_name=nearby_api,
            allow_cross_api=False,
        )
        mapping["nearby_api"] = nearby_api
    uses_by_line: dict[int, set[str]] = {}
    for use in uses:
        uses_by_line.setdefault(use["line"], set()).add(use["binding_symbol"])
    for fact in lifetime_facts:
        nearby = set()
        for line_no in range(fact["line"] - 3, fact["line"] + 4):
            nearby.update(uses_by_line.get(line_no, set()))
        fact["uses_bindings"] = json.dumps(sorted(nearby))
    cleaned_uses = [
        {key: value for key, value in use.items() if key not in {"column", "end_line", "end_column"}}
        for use in uses
    ]
    cleaned_apis = [{key: value for key, value in api.items() if key != "end_line"} for api in apis]
    return cleaned_uses, cleaned_apis, comments, lifetime_facts, error_mappings


def _parse_file_with_syntax(
    path: Path,
    version_id: str,
    text: str,
    syntax: RustSyntax,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    rel = str(path)
    lines = text.splitlines()
    uses = list(syntax.binding_uses)
    apis = list(syntax.apis)
    comments: list[dict[str, Any]] = []
    lifetime_facts = list(syntax.lifetime_facts)
    error_mappings: list[dict[str, Any]] = []

    for api in apis:
        for mapping_type in _return_mapping_types(api.get("return_type")):
            error_mappings.append(
                {
                    "version_id": version_id,
                    "rust_file": rel,
                    "line": api["line"],
                    "mapping_type": mapping_type,
                    "text": f"{api['api_name']} -> {api.get('return_type') or '()'}"[:500],
                    "nearby_binding_symbol": None,
                    "nearby_api": api["api_name"],
                }
            )

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        code_line = bool(stripped) and not _is_comment_line(stripped) and not _is_import_line(stripped)
        context = syntax.line_context.get(idx, RustLineContext())
        active_type = context.enclosing_type or context.impl_type

        if code_line:
            for mapping_type, needle in ERROR_MAPPING_PATTERNS.items():
                if needle in stripped:
                    error_mappings.append(
                        {
                            "version_id": version_id,
                            "rust_file": rel,
                            "line": idx,
                            "mapping_type": mapping_type,
                            "text": stripped[:500],
                            "nearby_binding_symbol": None,
                            "nearby_api": context.function,
                        }
                    )
            for fact_type, needle in LIFETIME_PATTERNS.items():
                if needle in stripped and not _is_import_line(stripped):
                    lifetime_facts.append(
                        {
                            "version_id": version_id,
                            "rust_file": rel,
                            "line": idx,
                            "fact_type": fact_type,
                            "rust_type": active_type,
                            "uses_bindings": "[]",
                            "evidence_text": stripped[:500],
                        }
                    )

        if "SAFETY:" in stripped:
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

    return _finish_facts(uses, apis, comments, lifetime_facts, error_mappings)


def _parse_file(
    path: Path, version_id: str
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    rel = str(path)
    text = path.read_text(encoding="utf-8", errors="replace")
    if syntax := _parse_tree_sitter_syntax(text, path, version_id):
        return _parse_file_with_syntax(path, version_id, text, syntax)
    lines = text.splitlines()
    uses: list[dict[str, Any]] = []
    apis: list[dict[str, Any]] = []
    comments: list[dict[str, Any]] = []
    lifetime_facts: list[dict[str, Any]] = []
    error_mappings: list[dict[str, Any]] = []
    unsafe_depth = 0
    impl_stack: list[tuple[str, int]] = []
    struct_stack: list[tuple[str, int]] = []
    pending_impls: list[tuple[str, str | None]] = []
    pending_structs: list[str] = []
    current_fn: tuple[str, int] | None = None

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        code_line = bool(stripped) and not _is_comment_line(stripped) and not _is_import_line(stripped)
        delta = _brace_delta(stripped)
        if match := STRUCT_RE.search(stripped):
            pending_structs.append(match.group("name"))
        if parsed_impl := _parse_impl_type(stripped):
            ty, trait = parsed_impl
            if trait in {"Drop", "Clone"}:
                lifetime_facts.append(
                    {
                        "version_id": version_id,
                        "rust_file": rel,
                        "line": idx,
                        "fact_type": f"IMPL_{trait.upper()}",
                        "rust_type": ty,
                        "uses_bindings": "[]",
                        "evidence_text": stripped[:500],
                    }
                )
            pending_impls.append((ty, trait))
        if "{" in stripped:
            while pending_structs:
                struct_stack.append((pending_structs.pop(), 0))
            while pending_impls:
                ty, _trait = pending_impls.pop()
                impl_stack.append((ty, 0))
        line_starts_unsafe = bool(re.search(r"\bunsafe\s*\{", stripped))
        active_type = impl_stack[-1][0] if impl_stack else (struct_stack[-1][0] if struct_stack else None)

        if match := PUB_FN_RE.search(stripped):
            if match.group("vis"):
                name = match.group("name")
                api_name = f"{impl_stack[-1][0]}::{name}" if impl_stack else name
                current_fn = (api_name, max(1, _brace_delta(stripped)))
                ret = (match.group("ret") or "()").strip()
                apis.append(
                    {
                        "version_id": version_id,
                        "rust_file": rel,
                        "api_name": api_name,
                        "receiver_type": impl_stack[-1][0] if impl_stack else None,
                        "visibility": match.group("vis"),
                        "return_type": ret,
                        "params": json.dumps(match.group("params").strip()),
                        "uses_bindings": "[]",
                        "line": idx,
                    }
                )
                for mapping_type in _return_mapping_types(ret) if code_line else []:
                    error_mappings.append(
                        {
                            "version_id": version_id,
                            "rust_file": rel,
                            "line": idx,
                            "mapping_type": mapping_type,
                            "text": stripped[:500],
                            "nearby_binding_symbol": None,
                            "nearby_api": api_name,
                        }
                    )
            else:
                current_fn = (match.group("name"), max(1, _brace_delta(stripped)))

        for match in BINDING_RE.finditer(line if code_line else ""):
            uses.append(
                {
                    "version_id": version_id,
                    "rust_file": rel,
                    "line": idx,
                    "binding_symbol": match.group("name"),
                    "enclosing_unsafe_block": int(unsafe_depth > 0 or line_starts_unsafe),
                    "enclosing_function": current_fn[0] if current_fn else None,
                    "enclosing_impl": impl_stack[-1][0] if impl_stack else None,
                    "enclosing_type": active_type,
                }
            )

        for mapping_type, needle in ERROR_MAPPING_PATTERNS.items():
            if needle in stripped:
                if code_line:
                    error_mappings.append(
                        {
                            "version_id": version_id,
                            "rust_file": rel,
                            "line": idx,
                            "mapping_type": mapping_type,
                            "text": stripped[:500],
                            "nearby_binding_symbol": None,
                            "nearby_api": current_fn[0] if current_fn else None,
                        }
                    )
        for fact_type, needle in LIFETIME_PATTERNS.items():
            if needle in stripped and not _is_import_line(stripped):
                lifetime_facts.append(
                    {
                        "version_id": version_id,
                        "rust_file": rel,
                        "line": idx,
                        "fact_type": fact_type,
                        "rust_type": active_type,
                        "uses_bindings": "[]",
                        "evidence_text": stripped[:500],
                    }
                )

        if "SAFETY:" in stripped:
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
        if struct_stack:
            ty, depth = struct_stack[-1]
            depth += delta
            if depth <= 0:
                struct_stack.pop()
            else:
                struct_stack[-1] = (ty, depth)
        if line_starts_unsafe:
            unsafe_depth = max(0, unsafe_depth + delta)
        elif unsafe_depth:
            unsafe_depth = max(0, unsafe_depth + delta)

    return _finish_facts(uses, apis, comments, lifetime_facts, error_mappings)


def extract_rust_usage(cfg: Config, version_id: str | None = None) -> dict[str, Any]:
    cfg.ensure_dirs()
    vid = version_id or default_version_id(cfg)
    root = cfg.linux_tree / "rust/kernel"
    all_uses: list[dict[str, Any]] = []
    all_apis: list[dict[str, Any]] = []
    all_comments: list[dict[str, Any]] = []
    all_lifetime_facts: list[dict[str, Any]] = []
    all_error_mappings: list[dict[str, Any]] = []
    for path in sorted(root.rglob("*.rs")):
        uses, apis, comments, lifetime_facts, error_mappings = _parse_file(path, vid)
        all_uses.extend(uses)
        all_apis.extend(apis)
        all_comments.extend(comments)
        all_lifetime_facts.extend(lifetime_facts)
        all_error_mappings.extend(error_mappings)
    conn = connect(cfg.database)
    initialize(conn)
    for table in ("rust_binding_uses", "rust_safe_apis", "rust_safety_comments", "rust_lifetime_facts", "rust_error_mappings"):
        conn.execute(f"DELETE FROM {table} WHERE version_id=?", (vid,))
    conn.commit()
    upsert_many(conn, "rust_binding_uses", all_uses)
    upsert_many(conn, "rust_safe_apis", all_apis)
    upsert_many(conn, "rust_safety_comments", all_comments)
    upsert_many(conn, "rust_lifetime_facts", all_lifetime_facts)
    upsert_many(conn, "rust_error_mappings", all_error_mappings)
    return {
        "database": str(cfg.database),
        "version_id": vid,
        "rust_files": len(list(root.rglob("*.rs"))) if root.exists() else 0,
        "binding_uses": len(all_uses),
        "safe_apis": len(all_apis),
        "safety_comments": len(all_comments),
        "lifetime_facts": len(all_lifetime_facts),
        "error_mappings": len(all_error_mappings),
    }
