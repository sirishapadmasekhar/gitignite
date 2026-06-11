from pathlib import Path


def detect_vscode(project_path: Path) -> bool:
    """
    Detect whether the project appears to use VS Code.
    """

    vscode_dir = project_path / ".vscode"

    workspace_files = list(project_path.glob("*.code-workspace"))

    return vscode_dir.exists() or len(workspace_files) > 0