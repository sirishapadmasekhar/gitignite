import typer
import pytest


def test_typer_exit_code():
    with pytest.raises(typer.Exit) as exc:
        raise typer.Exit(code=1)

    assert exc.value.exit_code == 1