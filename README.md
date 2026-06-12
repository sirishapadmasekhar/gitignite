# 🔥 GitIgnite

**Smart Git hygiene for modern projects.**

GitIgnite is a lightweight command-line tool that helps developers maintain clean repositories by detecting common Git hygiene issues, recommending `.gitignore` improvements, identifying risky files, and evaluating repository health.

Whether you're starting a new project or maintaining an existing one, GitIgnite helps you avoid accidentally committing generated files, secrets, caches, and development artifacts.

---

## ✨ Features

* 🔍 **Scan projects automatically**

  * Detects technologies used in your repository.
  * Recommends relevant `.gitignore` rules.

* 🛠️ **Apply fixes**

  * Adds missing `.gitignore` entries automatically.

* 🩺 **Evaluate repository health**

  * Generates a Git Hygiene Score.
  * Highlights potential issues and recommendations.

* 🔐 **Audit risky files**

  * Identifies files that are commonly committed by mistake.

* ⚙️ **CI-friendly**

  * Supports non-zero exit codes for automated workflows.

* 🚀 **Easy installation**

  * Install directly from PyPI.

---

## Supported Technologies

GitIgnite currently supports detection and recommendations for:

| Technology        | Detection | GitIgnore Support |
| ----------------- | --------- | ----------------- |
| Python            | ✅         | ✅                 |
| VS Code           | ✅         | ✅                 |
| Jupyter Notebooks | ✅         | ✅                 |
| Docker            | ✅         | ✅                 |
| Terraform         | ✅         | ✅                 |

More technologies are planned for future releases.

---

## Installation

Install GitIgnite from PyPI:

```bash
pip install gitignite
```

Verify installation:

```bash
ignite --help
```

---

## Quick Start

### Scan a Project

Detect technologies and review current Git hygiene:

```bash
ignite scan
```

Example output:

```text
🔥 ignite
Scanning: /path/to/project

Detected:
✓ Python
✓ VS Code

Already configured:
✓ .venv/
✓ __pycache__/
✓ *.pyc
✓ .vscode/
```

---

### Evaluate Repository Health

Generate a Git Hygiene Score:

```bash
ignite doctor
```

Example:

```text
🩺 ignite doctor

Git Hygiene Score: 100/100

Detected:
✓ Python
✓ VS Code

✓ No issues found.
```

---

### Use in Continuous Integration

Fail builds when hygiene issues are detected:

```bash
ignite doctor --ci
```

Example:

```text
CI check passed.
```

Exit codes:

| Exit Code | Meaning         |
| --------- | --------------- |
| 0         | No issues found |
| 1         | Issues detected |

---

### Automatically Fix Missing Rules

Apply recommended `.gitignore` entries:

```bash
ignite fix
```

GitIgnite updates your `.gitignore` safely by appending missing rules.

---

### Audit Risky Files

Identify files that may expose secrets or unnecessary artifacts:

```bash
ignite audit
```

Example:

```text
🔍 ignite audit

✓ No obvious risks found.
```

---

## Typical Workflow

Use GitIgnite as part of your development process:

```bash
ignite scan
ignite doctor
ignite fix
ignite audit
```

---

## GitHub Actions Example

Integrate GitIgnite into CI pipelines:

```yaml
- name: Check Git hygiene
  run: ignite doctor --ci
```

---

## Why GitIgnite?

Many repositories unintentionally include:

* Virtual environments
* Cache directories
* Notebook checkpoints
* IDE settings
* Log files
* Environment files
* Generated artifacts

These files clutter repositories, increase review noise, and may expose sensitive information.

GitIgnite helps teams establish consistent Git hygiene with minimal effort.

---

## Project Status

GitIgnite is actively maintained and continuously evolving.

Planned improvements include:

* Additional technology detectors
* Custom configuration support
* Expanded auditing capabilities
* Enhanced CI integrations

---

## Contributing

Contributions, suggestions, and bug reports are welcome.

To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Add tests for your changes.
4. Submit a pull request.

Please ensure all tests pass before opening a PR.

---

## Development

Clone the repository:

```bash
git clone https://github.com/sirishapadmasekhar/gitignite.git
cd gitignite
```

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

Run tests:

```bash
pytest
```

---

## License

This project is licensed under the MIT License.

See the `LICENSE` file for details.

---

## Links

* GitHub Repository: https://github.com/sirishapadmasekhar/gitignite
* PyPI Package: https://pypi.org/project/gitignite/

---

Made with ❤️ to help developers keep their repositories clean.
