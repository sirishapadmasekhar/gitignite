from pathlib import Path


def read_gitignore(project_path: Path) -> set[str]:
    """
    Read .gitignore and return its entries as a set.

    Ignores:
    - Empty lines
    - Comments
    """

    gitignore_path = project_path / ".gitignore"

    if not gitignore_path.exists():
        return set()

    entries = set()

    with open(gitignore_path, "r") as file:
        for line in file:
            line = line.strip()

            # Skip blank lines
            if not line:
                continue

            # Skip comments
            if line.startswith("#"):
                continue

            entries.add(line)

    return entries