from pathlib import Path

import typer
from rich import print

from ignite.analyzer import analyze_project

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

    project_path = Path.cwd()

    results = analyze_project(project_path)

    detected = results["detected"]
    configured_rules = results["configured_rules"]
    missing_rules = results["missing_rules"]

    print("[green]🔥 ignite[/green]")
    print(f"Scanning: {project_path}\n")

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