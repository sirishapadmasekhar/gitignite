import typer
from pathlib import Path
from rich import print

from ignite.detectors.python_detector import detect_python

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
    Scan the current project.
    """

    project_path = Path.cwd()

    print("[green]🔥 ignite[/green]")
    print(f"Scanning: {project_path}\n")

    detected = []

    if detect_python(project_path):
        detected.append("Python")

    if detected:
        print("[bold green]Detected:[/bold green]")

        for tech in detected:
            print(f"✓ {tech}")
    else:
        print("[yellow]No technologies detected.[/yellow]")


if __name__ == "__main__":
    app()