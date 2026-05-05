from __future__ import annotations

import json
from typing import Any


WEAK_LIFETIME_NAME_NEEDLES = ("drop", "clone", "inc_ref", "dec_ref", "get", "put", "new", "free", "release")


def _rows(rows) -> list[dict[str, Any]]:
    return [dict(row) for row in rows]


def _json_list_contains(value: str | None, symbol: str) -> bool:
    if not value:
        return False
    try:
        decoded = json.loads(value)
    except json.JSONDecodeError:
        return False
    return any(str(item) == symbol for item in decoded if item is not None)


def _safe_apis(conn, version: str, symbol: str) -> list[dict[str, Any]]:
    rows = conn.execute(
        """
        SELECT rust_file, api_name, receiver_type, visibility, return_type, params, uses_bindings, line
        FROM rust_safe_apis
        WHERE version_id=?
        ORDER BY rust_file, line
        """,
        (version,),
    ).fetchall()
    return [dict(row) for row in rows if _json_list_contains(row["uses_bindings"], symbol)]


def _lifetime_facts(conn, version: str, symbol: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    rows = conn.execute(
        """
        SELECT rust_file, line, fact_type, rust_type, uses_bindings, evidence_text
        FROM rust_lifetime_facts
        WHERE version_id=?
        ORDER BY rust_file, line
        """,
        (version,),
    ).fetchall()
    facts = [dict(row) for row in rows if _json_list_contains(row["uses_bindings"], symbol)]
    weak: list[dict[str, Any]] = []
    if facts:
        return facts, weak
    use_rows = conn.execute(
        """
        SELECT rust_file, line, enclosing_function, enclosing_impl
        FROM rust_binding_uses
        WHERE version_id=? AND binding_symbol=?
        ORDER BY rust_file, line
        LIMIT 20
        """,
        (version, symbol),
    ).fetchall()
    for row in use_rows:
        function = (row["enclosing_function"] or "").lower()
        if any(needle in function for needle in WEAK_LIFETIME_NAME_NEEDLES):
            weak.append(
                {
                    "rust_file": row["rust_file"],
                    "line": row["line"],
                    "fact_type": "LIFETIME_NAMING_PATTERN",
                    "rust_type": row["enclosing_impl"],
                    "evidence_text": row["enclosing_function"],
                    "weak": True,
                }
            )
    return facts, weak


def _wrapper_oracle_hits(conn, symbol: str) -> list[dict[str, Any]]:
    rows = conn.execute(
        """
        SELECT commit_id, date, subject, changed_files, matched_symbols
        FROM wrapper_fix_events
        WHERE likely_wrapper_fix=1
        ORDER BY date
        """,
    ).fetchall()
    hits = []
    for row in rows:
        if _json_list_contains(row["matched_symbols"], symbol):
            hits.append(dict(row))
    return hits


def _unsafe_direct_uses(direct_uses: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [row for row in direct_uses if bool(row.get("enclosing_unsafe_block"))]


def _promoting_direct_uses(direct_uses: list[dict[str, Any]], drift_type: str) -> list[dict[str, Any]]:
    if drift_type == "MacroConstDrift":
        return direct_uses
    return _unsafe_direct_uses(direct_uses)


def compute_rust_impact(conn, version: str, symbol: str, drift_type: str, pair_id: str | None = None) -> dict[str, Any]:
    direct_uses = _rows(
        conn.execute(
            """
            SELECT rust_file, line, enclosing_function, enclosing_impl, enclosing_type, enclosing_unsafe_block
            FROM rust_binding_uses
            WHERE version_id=? AND binding_symbol=?
            ORDER BY rust_file, line
            LIMIT 50
            """,
            (version, symbol),
        ).fetchall()
    )
    safe_apis = _safe_apis(conn, version, symbol)
    safety_comments = _rows(
        conn.execute(
            """
            SELECT rust_file, line, text, nearby_api
            FROM rust_safety_comments
            WHERE version_id=? AND nearby_binding_symbol=?
            ORDER BY rust_file, line
            LIMIT 20
            """,
            (version, symbol),
        ).fetchall()
    )
    error_mappings = _rows(
        conn.execute(
            """
            SELECT rust_file, line, mapping_type, text, nearby_api
            FROM rust_error_mappings
            WHERE version_id=? AND nearby_binding_symbol=?
            ORDER BY rust_file, line
            LIMIT 20
            """,
            (version, symbol),
        ).fetchall()
    )
    lifetime_facts, weak_lifetime_facts = _lifetime_facts(conn, version, symbol)
    build_query = """
        SELECT event_id, run_id, pair_id, build_log, line, symbol, text
        FROM build_breakage_events
        WHERE symbol=?
    """
    build_params: tuple[Any, ...] = (symbol,)
    if pair_id:
        build_query += " AND pair_id=?"
        build_params = (symbol, pair_id)
    build_oracles = _rows(conn.execute(build_query, build_params).fetchall())
    wrapper_oracles = _wrapper_oracle_hits(conn, symbol)
    oracle_hits = [
        {"oracle_type": "build_breakage", **row}
        for row in build_oracles
    ] + [
        {"oracle_type": "wrapper_fix", **row}
        for row in wrapper_oracles
    ]
    unsafe_direct_uses = _unsafe_direct_uses(direct_uses)
    promoting_direct_uses = _promoting_direct_uses(direct_uses, drift_type)

    reasons: list[str] = []
    if promoting_direct_uses:
        reasons.append("direct_binding_use")
    if safe_apis:
        reasons.append("exposes_safe_api")
    if safety_comments:
        reasons.append("has_safety_comment")
    if error_mappings:
        reasons.append("has_error_mapping")
    if lifetime_facts:
        reasons.append("has_lifetime_fact")
    if oracle_hits:
        reasons.append("oracle_hit")

    if oracle_hits:
        impact_level = "oracle_confirmed"
    elif error_mappings or lifetime_facts or safety_comments:
        impact_level = "contract_mapping"
    elif safe_apis:
        impact_level = "safe_api"
    elif unsafe_direct_uses:
        impact_level = "direct_unsafe_call"
    elif promoting_direct_uses:
        impact_level = "generated_binding"
    else:
        impact_level = "none"

    return {
        "eligible": bool(reasons),
        "impact_level": impact_level,
        "direct_uses": direct_uses,
        "unsafe_direct_uses": unsafe_direct_uses,
        "safe_apis": safe_apis,
        "safety_comments": safety_comments,
        "error_mappings": error_mappings,
        "lifetime_facts": lifetime_facts,
        "weak_lifetime_facts": weak_lifetime_facts,
        "oracle_hits": oracle_hits,
        "reasons": reasons,
        "drift_type": drift_type,
        "symbol": symbol,
    }


def apply_impact_to_warning(warning: dict[str, Any], impact: dict[str, Any]) -> dict[str, Any]:
    rust_side = dict(warning.get("rust_side") or {})
    if impact.get("direct_uses"):
        rust_side["uses"] = impact["direct_uses"]
    if impact.get("safe_apis"):
        rust_side["safe_apis"] = impact["safe_apis"]
    if impact.get("safety_comments"):
        rust_side["safety_comments"] = impact["safety_comments"]
    if impact.get("error_mappings"):
        rust_side["error_mappings"] = impact["error_mappings"]
    if impact.get("lifetime_facts"):
        rust_side["lifetime_facts"] = impact["lifetime_facts"]
    if impact.get("weak_lifetime_facts"):
        rust_side["weak_lifetime_facts"] = impact["weak_lifetime_facts"]
    if impact.get("oracle_hits"):
        rust_side["oracle_hits"] = impact["oracle_hits"]
    warning["rust_side"] = rust_side
    warning["rust_impact_level"] = impact.get("impact_level", "none")
    warning["promotion_status"] = "promoted"
    warning["promotion_reasons"] = list(impact.get("reasons") or [])
    warning["demotion_reasons"] = []
    chain = list(warning.get("evidence_chain") or [])
    for key in ("safety_comments", "error_mappings", "lifetime_facts", "oracle_hits"):
        chain.extend(impact.get(key) or [])
    warning["evidence_chain"] = chain
    return warning
