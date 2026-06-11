from pathlib import Path

from ignite.detectors.python_detector import detect_python
from ignite.gitignore import read_gitignore
from ignite.rules.python import PYTHON_IGNORE_RULES


def analyze_project(project_path: Path) -> dict:
    """
    Analyze a project and determine:

    - detected technologies
    - configured .gitignore rules
    - missing .gitignore rules
    """

    existing_rules = read_gitignore(project_path)

    detected = []
    configured_rules = []
    missing_rules = []

    # -------------------------
    # Python
    # -------------------------
    if detect_python(project_path):
        detected.append("Python")

        for rule in PYTHON_IGNORE_RULES:
            if rule in existing_rules:
                configured_rules.append(rule)
            else:
                missing_rules.append(rule)

    return {
        "detected": detected,
        "configured_rules": configured_rules,
        "missing_rules": missing_rules,
    }