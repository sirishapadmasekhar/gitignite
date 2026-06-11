from pathlib import Path

import typer
from rich import print

from ignite.analyzer import analyze_project
from ignite.fixer import backup_gitignore, append_missing_rules

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

    # Display detected technologies
    if detected:
        print("[bold green]Detected:[/bold green]")

        for tech in detected:
            print(f"✓ {tech}")

    # Display rules already present in .gitignore
    if configured_rules:
        print("\n[bold green]Already configured:[/bold green]")

        for rule in configured_rules:
            print(f"✓ {rule}")

    # Display missing rules
    if missing_rules:
        print("\n[bold yellow]Missing ignore rules:[/bold yellow]")

        for rule in missing_rules:
            print(f"• {rule}")

    # If nothing was detected
    if not detected:
        print("[yellow]No technologies detected.[/yellow]")


@app.command()
def fix():
    """
    Apply missing .gitignore recommendations.
    """

    project_path = Path.cwd()

    results = analyze_project(project_path)

    missing_rules = results["missing_rules"]

    if not missing_rules:
        print("[green]✓ No fixes needed.[/green]")
        return

    print("[bold yellow]The following rules will be added:[/bold yellow]\n")

    for rule in missing_rules:
        print(f"+ {rule}")

    print("\nBackup:")
    print(".gitignore.bak")

    apply_changes = typer.confirm(
        "\nApply changes?",
        default=True,
    )

    if not apply_changes:
        print("[yellow]No changes made.[/yellow]")
        return

    # Create backup before modifying .gitignore
    backup_path = backup_gitignore(project_path)

    if backup_path:
        print(f"[green]✓ Created {backup_path.name}[/green]")

    # Append missing rules
    added = append_missing_rules(project_path, missing_rules)

    print(f"[green]✓ Added {added} rule(s) to .gitignore[/green]")


if __name__ == "__main__":
    app()