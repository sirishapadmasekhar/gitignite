# 🔥 GitIgnite

<div align="center">

### Smart Git hygiene for modern projects

Automatically detect missing `.gitignore` rules, audit repository health, and keep repositories clean as they evolve.

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Tests](https://img.shields.io/badge/tests-18%20passing-brightgreen)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-success)
![License](https://img.shields.io/badge/license-MIT-green)

</div>

---

## Why GitIgnite?

Every developer has accidentally committed something they shouldn't have.

* Forgot to ignore `.venv/`
* Accidentally committed `.env`
* Added Docker but never updated `.gitignore`
* Introduced Terraform without excluding state files
* Copied an old `.gitignore` and never looked at it again

Projects evolve.

`.gitignore` files usually don't.

**GitIgnite helps your repository adapt automatically to the technologies you're actually using.**

Instead of asking:

> "Which `.gitignore` template should I use?"

GitIgnite asks:

> "What does this repository need right now?"

---

## ✨ Features

### 🔍 Smart Project Detection

Automatically detects technologies used in your repository and recommends appropriate Git ignore rules.

Supported technologies:

* ✅ Python
* ✅ Node.js
* ✅ VS Code
* ✅ Jupyter Notebooks
* ✅ Docker
* ✅ Terraform

---

### 🛠 Intelligent `.gitignore` Suggestions

Identify missing ignore rules without overwriting your existing configuration.

Example:

```bash
ignite scan
```

Output:

```text
🔥 ignite
Scanning: /path/to/project

Detected:
✓ Python
✓ Docker

Already configured:
✓ .venv/
✓ __pycache__/

Missing ignore rules:
• .env
• *.log
```

---

### 🔧 Automatic Fixes

Apply safe improvements directly to `.gitignore`.

```bash
ignite fix
```

GitIgnite will:

* Add missing rules
* Preserve existing entries
* Avoid duplicates
* Create a backup before modifying files

Example:

```text
The following rules will be added:

+ .terraform/
+ *.tfstate

Backup:
.gitignore.bak

Apply changes? [Y/n]

✓ Created .gitignore.bak
✓ Added 2 rule(s) to .gitignore
```

---

### 🩺 Git Hygiene Doctor

Evaluate repository health and generate a hygiene score.

```bash
ignite doctor
```

Example:

```text
🩺 ignite doctor

Git Hygiene Score: 92/100

Detected:
✓ Python
✓ Terraform

Issues:
⚠ Missing Terraform state ignore rules

Recommendations:
• Add .terraform/
• Ignore *.tfstate files
```

---

### 🤖 CI Integration

Use GitIgnite in automated workflows.

```bash
ignite doctor --ci
```

CI mode:

* Returns exit code `0` when healthy
* Returns non-zero exit code when issues exist

Perfect for GitHub Actions and other CI pipelines.

---

### 🔐 Repository Auditing

Identify potentially risky files that should not be committed.

```bash
ignite audit
```

Example:

```text
🔍 ignite audit

Potential Risks:

⚠ .env file detected

Recommendation:
Add .env to .gitignore immediately.
```

---

## 🚀 Installation

### From Source

Clone the repository:

```bash
git clone https://github.com/sirishapadmasekhar/gitignite.git
cd gitignite
```

Create and activate a virtual environment:

#### macOS/Linux

```bash
python -m venv .venv
source .venv/bin/activate
```

#### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements-dev.txt
pip install -e .
```

Verify installation:

```bash
ignite --help
```

---

## ⚡ Quick Start

Scan your repository:

```bash
ignite scan
```

Apply fixes:

```bash
ignite fix
```

Check repository health:

```bash
ignite doctor
```

Use in CI:

```bash
ignite doctor --ci
```

Audit for risks:

```bash
ignite audit
```

---

## Supported Technologies

| Technology | Detection Method           | Suggested Ignore Rules                              |
| ---------- | -------------------------- | --------------------------------------------------- |
| Python     | Python project files       | `.venv/`, `__pycache__/`, `*.pyc`, `.pytest_cache/` |
| Node.js    | `package.json`             | `node_modules/`                                     |
| VS Code    | `.vscode/` folder          | `.vscode/`                                          |
| Jupyter    | `.ipynb` notebooks         | `.ipynb_checkpoints/`                               |
| Docker     | Dockerfile / Compose files | `.env`, `*.log`                                     |
| Terraform  | `.tf` files                | `.terraform/`, `*.tfstate`, `*.tfstate.*`           |

---

## Example Workflow

```bash
# Analyze repository
ignite scan

# Fix missing ignore rules
ignite fix

# Evaluate hygiene
ignite doctor

# Validate in CI
ignite doctor --ci

# Audit for common risks
ignite audit
```

---

## Development

Set up the development environment:

```bash
git clone https://github.com/sirishapadmasekhar/gitignite.git
cd gitignite

python -m venv .venv
source .venv/bin/activate

pip install -r requirements-dev.txt
pip install -e .
```

Run tests:

```bash
pytest
```

Run GitIgnite locally:

```bash
ignite scan
ignite doctor
ignite fix
ignite audit
```

---

## Continuous Integration

GitIgnite uses GitHub Actions to automatically test against multiple Python versions.

Current CI coverage:

* Python 3.9
* Python 3.10
* Python 3.11

All tests must pass before merging changes.

---

## Project Philosophy

Git hygiene should not depend on memory.

Developers should not have to remember:

* which tools require ignore rules,
* whether secrets are excluded,
* if temporary artifacts are tracked,
* or when project requirements changed.

Repositories evolve.

**GitIgnite helps your Git hygiene evolve with them.**

---

## Roadmap

Future improvements may include:

* Additional technology support
* More repository health checks
* Enhanced auditing capabilities
* Improved reporting
* Package distribution via PyPI

---

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

Before contributing:

```bash
pytest
```

---

## License

This project is licensed under the MIT License.

See the `LICENSE` file for details.

---

<div align="center">

Built with ❤️ to help developers keep repositories clean.

**GitIgnite — Smart Git hygiene for modern projects.**

</div>
