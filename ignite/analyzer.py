from pathlib import Path

from ignite.detectors.node_detector import detect_node
from ignite.detectors.python_detector import detect_python
from ignite.gitignore import read_gitignore
from ignite.rules.node import NODE_IGNORE_RULES
from ignite.rules.python import PYTHON_IGNORE_RULES


def analyze_project(project_path: Path) -> dict:
    """
    Analyze a project and determine:

    - detected technologies
    - configured .gitignore rules
    - missing .gitignore rules
    """

    # Read the current .gitignore entries
    existing_rules = read_gitignore(project_path)

    # Technologies detected in this repository
    detected = []

    # Recommended rules that already exist
    configured_rules = []

    # Recommended rules that are missing
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

    # -------------------------
    # Node.js
    # -------------------------
    if detect_node(project_path):
        detected.append("Node.js")

        for rule in NODE_IGNORE_RULES:
            if rule in existing_rules:
                configured_rules.append(rule)
            else:
                missing_rules.append(rule)

    return {
        "detected": detected,
        "configured_rules": configured_rules,
        "missing_rules": missing_rules,
    }