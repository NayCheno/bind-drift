from pathlib import Path

from binddrift.evaluation.evaluator import parse_build_log


def test_parse_build_log_extracts_binding_symbol(tmp_path: Path):
    log = tmp_path / "build.log"
    log.write_text(
        "error[E0425]: cannot find function `foo_get` in module `bindings::foo_get`\n"
        "error: mismatched types\n",
        encoding="utf-8",
    )

    findings = parse_build_log(log)

    assert findings[0]["symbol"] == "foo_get"
    assert len(findings) == 2
