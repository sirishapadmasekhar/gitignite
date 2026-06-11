from ignite.gitignore import read_gitignore


def test_read_gitignore_ignores_comments_and_blank_lines(tmp_path):
    gitignore = tmp_path / ".gitignore"

    gitignore.write_text(
        "# Comment\n"
        "\n"
        ".venv/\n"
        "__pycache__/\n"
    )

    entries = read_gitignore(tmp_path)

    assert entries == {".venv/", "__pycache__/"}


def test_read_gitignore_missing_file(tmp_path):
    entries = read_gitignore(tmp_path)

    assert entries == set()