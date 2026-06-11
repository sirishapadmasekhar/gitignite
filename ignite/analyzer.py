from ignite.gitignore import read_gitignore
from ignite.registry import TECHNOLOGIES


def analyze_project(project_path):
    existing_rules = read_gitignore(project_path)

    detected = []
    configured_rules = []
    missing_rules = []

    for tech in TECHNOLOGIES:
        if tech["detector"](project_path):
            detected.append(tech["name"])

            for rule in tech["rules"]:
                if rule in existing_rules:
                    configured_rules.append(rule)
                else:
                    missing_rules.append(rule)

    return {
        "detected": detected,
        "configured_rules": configured_rules,
        "missing_rules": missing_rules,
    }