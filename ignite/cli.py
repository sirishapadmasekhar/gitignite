from pathlib import Path

import typer
from rich import print

from ignite.detectors.python_detector import detect_python
from ignite.gitignore import read_gitignore
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

    # Current directory being scanned
    project_path = Path.cwd()

    # Read existing .gitignore entries
    existing_rules = read_gitignore(project_path)

    # Technologies detected in this repository
    detected = []

    # Rules that already exist in .gitignore
    configured_rules = []

    # Rules that should be added
    missing_rules = []

    print("[green]🔥 ignite[/green]")
    print(f"Scanning: {project_path}\n")

    # -------------------------
    # Python Detection
    # -------------------------
    if detect_python(project_path):
        detected.append("Python")

        # Compare recommended Python rules
        # against the existing .gitignore
        for rule in PYTHON_IGNORE_RULES:
            if rule in existing_rules:
                configured_rules.append(rule)
            else:
                missing_rules.append(rule)

    # -------------------------
    # Display Results
    # -------------------------

    if detected:
        print("[bold green]Detected:[/bold green]")

        for tech in detected:
            print(f"✓ {tech}")

    if configured_rules:
        print("\n[bold green]Already configured:[/bold green]")

        for rule in configured_rules:
            print(f"✓ {rule}")

    if missing_rules:
        print("\n[bold yellow]Missing ignore rules:[/bold yellow]")

        for rule in missing_rules:
            print(f"• {rule}")

    if not detected:
        print("[yellow]No technologies detected.[/yellow]")


if __name__ == "__main__":
    app()