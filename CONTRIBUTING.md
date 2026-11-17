# Contributing to Handwritten Digits

Thank you for contributing to the **Handwritten Digits** project. This document describes the development workflow, coding standards, pre-commit configuration, testing requirements, and Git processes used in this repository.

---

## 1. Development Workflow

All development must be conducted using feature branches based on `develop`. Direct commits to `main` are prohibited.

### Git Branching Model
```
main  <--  develop  <--  feature/*
```

### Typical Workflow:
```bash
# 1. Update local develop branch
git checkout develop
git pull origin develop

# 2. Create a new feature branch
git checkout -b feature/my-new-feature
```

---

## 2. Environment & Dependency Setup

This project uses **`uv`** for ultra-fast Python package and environment management.

### Project Installation:
```bash
# Clone the repository
git clone <repository-url>
cd handwritten_digits

# Create virtual environment and install all dependencies (including dev groups)
uv sync --all-groups

# Activate virtual environment
source .venv/bin/activate  # Linux / macOS
# .venv\Scripts\activate   # Windows
```

---

## 3. Pre-Commit Hooks & Quality Assurance

This repository uses **`pre-commit`** configured via `.pre-commit-config.yaml` to automatically enforce code quality and hygiene before every Git commit.

### Initializing Pre-Commit Hooks
After installing project dependencies, you **must** install the Git pre-commit hooks:

```bash
uv run pre-commit install
```

### Pre-Commit Configuration (`.pre-commit-config.yaml`)
The project enforces the following automated checks:

1. **File Structure & Hygiene (`pre-commit-hooks`)**:
   - `trailing-whitespace`: Removes unnecessary trailing spaces.
   - `end-of-file-fixer`: Ensures files end with a single newline.
   - `check-yaml`, `check-toml`, `check-json`: Validates syntax of configuration files.
   - `check-added-large-files`: Prevents accidental commits of large binary files (> 1 MB).

2. **Linting & Formatting (`ruff-pre-commit`)**:
   - `ruff`: Lints Python files with automated fixing (`--fix`).
   - `ruff-format`: Formats Python code according to project conventions (replacing Black).

### Running Pre-Commit Manually
To test all files against pre-commit hooks at any time:

```bash
uv run pre-commit run --all-files
```

---

## 4. Code Quality & Formatting

We use **Ruff** for both linting and formatting as configured in `pyproject.toml`.

### Manual Quality Checks:
```bash
# Run linter
uv run ruff check .

# Apply automatic linter fixes
uv run ruff check . --fix

# Check formatting
uv run ruff format --check .

# Apply automatic formatting
uv run ruff format .
```

---

## 5. Running the Application & Tests

### Running the Flask Web Application
```bash
uv run python app/app.py
```

### Running Tests & Coverage
All code changes must be accompanied by relevant unit or integration tests.

```bash
# Run all pytest tests
uv run pytest

# Run tests with coverage report
uv run pytest --cov=src --cov-report=term-missing
```

### Test Directory Structure
```
tests/
├── unit/         # Test isolated functions and logic
├── integration/  # Test interactions between modules (e.g. Flask endpoints)
└── smoke/        # Basic import and application startup checks
```

---

## 6. Pull Request & Commit Guidelines

Before submitting a Pull Request (PR) from `feature/*` into `develop`:

1. All unit and integration tests must pass (`uv run pytest`).
2. All pre-commit hooks must pass (`uv run pre-commit run --all-files`).
3. Code coverage must meet or exceed the project threshold (50%+).
4. Direct pushes to `main` and `develop` are protected; merge via PR only.