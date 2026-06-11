from pathlib import Path


def detect_jupyter(project_path: Path) -> bool:
    """
    Detect whether the project contains Jupyter notebooks.
    """

    notebooks = list(project_path.glob("*.ipynb"))

    return len(notebooks) > 0