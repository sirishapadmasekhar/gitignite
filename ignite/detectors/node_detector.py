from pathlib import Path


def detect_node(project_path: Path) -> bool:
    """
    Detect whether a directory appears to be a Node.js project.
    """

    node_markers = [
        "package.json",
        "package-lock.json",
        "yarn.lock",
        "pnpm-lock.yaml",
    ]

    for marker in node_markers:
        if (project_path / marker).exists():
            return True

    return False