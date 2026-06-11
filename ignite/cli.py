from pathlib import Path

import typer
from rich import print

from ignite.detectors.python_detector import detect_python
from ignite.rules.python import PYTHON_IGNORE_RULES

app = typer.Typer()


@app.callback()
def main():
    """
    ignite - Smart Git hygiene for modern projects.
    """
    pass


@app.command()
def scan():
    """
    Scan the current project and suggest .gitignore improvements.
    """

    # Get the directory where the command is being executed.
    # Example:
    # If you're inside ~/Desktop/gitignite,
    # project_path becomes that directory.
    project_path = Path.cwd()

    # Store detected technologies.
    detected = []

    # Store recommended .gitignore entries.
    suggestions = []

    print("[green]🔥 ignite[/green]")
    print(f"Scanning: {project_path}\n")

    # -------------------------
    # Python Detection
    # -------------------------
    if detect_python(project_path):
        detected.append("Python")

        # Add Python ignore recommendations.
        suggestions.extend(PYTHON_IGNORE_RULES)

    # -------------------------
    # Display Results
    # -------------------------

    if detected:
        print("[bold green]Detected:[/bold green]")

        for tech in detected:
            print(f"✓ {tech}")

    if suggestions:
        print("\n[bold cyan]Suggested additions:[/bold cyan]")

        for rule in suggestions:
            print(f"• {rule}")

    if not detected:
        print("[yellow]No technologies detected.[/yellow]")


if __name__ == "__main__":
    app()
