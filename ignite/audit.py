from pathlib import Path

from ignite.gitignore import read_gitignore


RISK_FILES = [
    ".env",
    ".env.local",
    "credentials.json",
    "service-account.json",
    "local.db",
]


def generate_audit_report(project_path: Path) -> dict:
    existing_rules = read_gitignore(project_path)

    risks = []

    for filename in RISK_FILES:
        file_path = project_path / filename

        if file_path.exists() and filename not in existing_rules:
            risks.append(
                f"{filename} exists but is not ignored"
            )

    return {
        "risks": risks,
    }