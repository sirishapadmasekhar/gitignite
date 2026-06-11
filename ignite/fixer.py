import shutil
from pathlib import Path
from typing import Optional


def backup_gitignore(project_path: Path) -> Optional[Path]:
    """
    Create a backup of .gitignore.

    Returns:
        Path to backup file, or None if .gitignore doesn't exist.
    """

    gitignore_path = project_path / ".gitignore"

    if not gitignore_path.exists():
        return None

    backup_path = project_path / ".gitignore.bak"

    shutil.copy2(gitignore_path, backup_path)

    return backup_path


def append_missing_rules(project_path: Path, rules: list[str]) -> int:
    """
    Append missing rules to .gitignore.

    Returns:
        Number of rules added.
    """

    if not rules:
        return 0

    gitignore_path = project_path / ".gitignore"

    with open(gitignore_path, "a") as file:
        file.write("\n")
        file.write("# Added by ignite\n")

        for rule in rules:
            file.write(f"{rule}\n")

    return len(rules)