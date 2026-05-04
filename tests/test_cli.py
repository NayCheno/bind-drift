from binddrift.cli import main


def test_help_runs(capsys):
    try:
        main(["--help"])
    except SystemExit as exc:
        assert exc.code == 0
    assert "BindDrift research artifact CLI" in capsys.readouterr().out
