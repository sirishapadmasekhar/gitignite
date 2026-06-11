from pathlib import Path

from ignite.analyzer import analyze_project


def generate_doctor_report(project_path: Path) -> dict:
    """
    Generate a Git hygiene report.
    """

    results = analyze_project(project_path)

    missing_rules = results["missing_rules"]

    score = 100 - (len(missing_rules) * 10)

    # Prevent ridiculous scores
    score = max(score, 50)

    issues = []

    for rule in missing_rules:
        issues.append(f"Missing ignore rule: {rule}")

    recommendations = []

    if missing_rules:
        recommendations.append("Run: ignite fix")

    return {
        "score": score,
        "detected": results["detected"],
        "issues": issues,
        "recommendations": recommendations,
    }