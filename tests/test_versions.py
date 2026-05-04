from binddrift.versions import is_release_tag, release_key, sanitize_ref


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
