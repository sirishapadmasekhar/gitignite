from pathlib import Path


def detect_python(project_path: Path) -> bool:
    """
    Detect whether a directory appears to be a Python project.

    Returns:
        True if Python-related files are found.
        False otherwise.
    """

    python_markers = [
        "requirements.txt",
        "pyproject.toml",
        "setup.py",
        "Pipfile",
        "poetry.lock",
    ]

    for marker in python_markers:
        if (project_path / marker).exists():
            return True

    return False