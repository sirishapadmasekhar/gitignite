from pathlib import Path

from ignite.analyzer import analyze_project


def test_detects_terraform(tmp_path: Path):
    """
    Terraform projects should be detected
    when .tf files exist.
    """
    (tmp_path / "main.tf").touch()

    report = analyze_project(tmp_path)

    assert "Terraform" in report["detected"]


def test_suggests_terraform_gitignore_rules(tmp_path: Path):
    """
    Terraform projects should suggest
    Terraform-related ignore rules.
    """
    (tmp_path / "main.tf").touch()

    report = analyze_project(tmp_path)

    rules = (
        report["configured_rules"]
        + report["missing_rules"]
    )

    assert ".terraform/" in rules
    assert "*.tfstate" in rules
    assert "*.tfstate.*" in rules