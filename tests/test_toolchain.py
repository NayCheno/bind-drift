from binddrift.toolchain import recommendations, rustavailable_recommendations


def test_recommendations_include_bindgen_install():
    recs = recommendations(["bindgen"])
    assert any("cargo install --locked bindgen-cli" in item for item in recs)


def test_recommendations_are_empty_when_complete():
    assert recommendations([]) == []


def test_rustavailable_recommends_rust_src():
    recs = rustavailable_recommendations("Source code for the 'core' standard library could not be found")
    assert any("rustup component add rust-src" in item for item in recs)
