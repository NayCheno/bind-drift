from pathlib import Path

from binddrift.config import Config
from binddrift.extractors.c_api import binding_closure_roots


def test_binding_closure_roots_uses_bindings_helper_surface(tmp_path: Path):
    linux = tmp_path / "vendor/linux"
    (linux / "rust/bindings").mkdir(parents=True)
    (linux / "rust/helpers").mkdir(parents=True)
    (linux / "include/linux").mkdir(parents=True)
    (linux / "drivers/base").mkdir(parents=True)
    (linux / "rust/bindings/bindings_helper.h").write_text(
        """
#include <linux/slab.h>
#include <../../drivers/base/base.h>
""",
        encoding="utf-8",
    )
    (linux / "include/linux/slab.h").write_text("void *kmalloc(void);\n", encoding="utf-8")
    (linux / "drivers/base/base.h").write_text("struct device_private;\n", encoding="utf-8")
    (linux / "rust/helpers/helpers.c").write_text("void rust_helper_foo(void) {}\n", encoding="utf-8")
    cfg = Config.from_args(repo_root=tmp_path)

    roots = binding_closure_roots(cfg)

    assert "include/linux/slab.h" in roots
    assert "drivers/base/base.h" in roots
    assert "rust/helpers" in roots
