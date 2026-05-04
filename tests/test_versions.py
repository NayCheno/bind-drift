import subprocess
from pathlib import Path

from binddrift.versions import is_release_tag, release_key, sanitize_ref, version_row


def test_release_key_sorts_linux_minor_versions():
    assert release_key("v6.10") > release_key("v6.9")
    assert release_key("v7.0") > release_key("v6.99")


def test_is_release_tag_filters_rcs_and_old_tags():
    assert is_release_tag("v6.1")
    assert is_release_tag("v6.10")
    assert not is_release_tag("v6.1-rc1")
    assert not is_release_tag("v5.19")


def test_sanitize_ref_is_path_safe():
    assert sanitize_ref("HEAD:6d35786de281") == "HEAD_6d35786de281"


def test_version_row_peels_annotated_tags(tmp_path: Path):
    repo = tmp_path / "repo"
    repo.mkdir()
    subprocess.run(["git", "-C", str(repo), "init"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    subprocess.run(["git", "-C", str(repo), "config", "user.email", "binddrift@example.com"], check=True)
    subprocess.run(["git", "-C", str(repo), "config", "user.name", "BindDrift Test"], check=True)
    (repo / "README").write_text("test\n", encoding="utf-8")
    subprocess.run(["git", "-C", str(repo), "add", "README"], check=True)
    subprocess.run(["git", "-C", str(repo), "commit", "-m", "initial"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    commit = subprocess.run(["git", "-C", str(repo), "rev-parse", "HEAD"], check=True, stdout=subprocess.PIPE, text=True).stdout.strip()
    subprocess.run(["git", "-C", str(repo), "tag", "-a", "v6.1", "-m", "Linux 6.1"], check=True)
    tag_object = subprocess.run(["git", "-C", str(repo), "rev-parse", "v6.1"], check=True, stdout=subprocess.PIPE, text=True).stdout.strip()

    row = version_row(repo, "v6.1")

    assert tag_object != commit
    assert row["git_commit"] == commit
