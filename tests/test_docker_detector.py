from pathlib import Path

from ignite.analyzer import analyze_project


def test_detects_docker(tmp_path: Path):
    """
    Docker projects should be detected
    when a Dockerfile exists.
    """
    (tmp_path / "Dockerfile").touch()

    report = analyze_project(tmp_path)

    assert "Docker" in report["detected"]


def test_suggests_docker_gitignore_rules(tmp_path: Path):
    """
    Docker projects should suggest
    Docker-related ignore rules.
    """
    (tmp_path / "Dockerfile").touch()

    report = analyze_project(tmp_path)

    assert ".env" in (
        report["configured_rules"] + report["missing_rules"]
    )

    assert "*.log" in (
        report["configured_rules"] + report["missing_rules"]
    )