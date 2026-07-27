# Contributing to Fraction

First of all, thank you for your interest in contributing to **Fraction**!

Whether you're fixing a bug, improving documentation, adding a new feature, or improving the test suite, your contributions are greatly appreciated.

Please read this guide before contributing.

---

# Table of Contents

* Code of Conduct
* Ways to Contribute
* Development Setup
* Project Structure
* Coding Standards
* Running Tests
* Code Formatting
* Type Checking
* Commit Message Guidelines
* Pull Request Process
* Reporting Issues
* Feature Requests
* Release Process
* Community

---

# Code of Conduct

This project follows the **Contributor Covenant Code of Conduct**.

By participating in this project, you agree to abide by the rules described in:

> **CODE_OF_CONDUCT.md**

Please be respectful and constructive in all interactions.

---

# Ways to Contribute

You can contribute by:

* Fixing bugs
* Improving documentation
* Adding examples
* Writing tests
* Improving performance
* Refactoring code
* Adding new mathematical utilities
* Improving CI/CD
* Reviewing pull requests
* Reporting bugs
* Suggesting new features

Every contribution, no matter how small, is welcome.

---

# Development Setup

## 1. Fork the repository

Click the **Fork** button on GitHub.

---

## 2. Clone your fork

```bash
git clone https://github.com/YOUR_USERNAME/fraction.git

cd fraction
```

---

## 3. Create a virtual environment

### Linux/macOS

```bash
python -m venv .venv

source .venv/bin/activate
```

### Windows

```powershell
python -m venv .venv

.venv\Scripts\activate
```

---

## 4. Install development dependencies

```bash
pip install -r requirements-dev.txt
```

Install the package in editable mode:

```bash
pip install -e .
```

---

# Project Structure

```text
fraction/
│
├── src/
│   └── fraction/
│
├── tests/
│
├── docs/
│
├── examples/
│
├── .github/
│
├── pyproject.toml
├── README.md
└── ...
```

---

# Coding Standards

Please follow these guidelines:

* Follow PEP 8.
* Keep functions focused and readable.
* Write meaningful variable names.
* Prefer descriptive docstrings.
* Add type hints to all public APIs.
* Maintain backwards compatibility whenever possible.
* Do not introduce unnecessary dependencies.

---

# Formatting

Before opening a pull request, run:

```bash
black .
```

Then check style:

```bash
ruff check .
```

---

# Type Checking

Run:

```bash
mypy src
```

No type errors should remain.

---

# Running Tests

Run the full test suite:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=fraction
```

The project aims for **95% or higher** test coverage.

Every new feature should include appropriate tests.

---

# Writing Tests

Please:

* Test normal behaviour.
* Test edge cases.
* Test invalid input.
* Test exceptions.
* Test interoperability.
* Test regression scenarios for fixed bugs.

Use descriptive test names, for example:

```python
def test_addition_with_integer():
    ...
```

---

# Commit Message Guidelines

Use clear, descriptive commit messages.

Recommended format:

```text
type(scope): short description
```

Examples:

```text
feat: add reciprocal method

fix: correct negative denominator handling

docs: improve installation guide

test: add edge case coverage

refactor: simplify comparison logic

ci: update GitHub Actions workflow
```

Common commit types:

* feat
* fix
* docs
* style
* refactor
* test
* chore
* ci

---

# Pull Request Process

Before submitting a pull request:

* Ensure all tests pass.
* Run Ruff.
* Run Black.
* Run MyPy.
* Update documentation if needed.
* Add tests for new functionality.
* Update the changelog when appropriate.

Your pull request description should include:

* Summary of the change
* Motivation
* Testing performed
* Related issue(s), if applicable

Small, focused pull requests are preferred over large ones.

---

# Reporting Bugs

When opening a bug report, include:

* Python version
* Operating system
* Package version
* Minimal reproducible example
* Expected behaviour
* Actual behaviour
* Full traceback (if any)

A clear bug report helps us resolve issues faster.

---

# Feature Requests

Feature requests are welcome.

Please explain:

* The problem you're trying to solve.
* Your proposed solution.
* Possible alternatives.
* Any additional context or examples.

---

# Documentation Contributions

Documentation improvements are always appreciated.

Examples include:

* Fixing typos
* Improving explanations
* Adding examples
* Clarifying APIs
* Updating installation instructions

---

# Release Process

Maintainers typically follow these steps:

1. Update version number.
2. Update `CHANGELOG.md`.
3. Run the complete test suite.
4. Build the package.

```bash
python -m build
```

5. Verify the distribution.

```bash
twine check dist/*
```

6. Create a Git tag.

```bash
git tag v1.0.0
git push origin v1.0.0
```

7. Publish to PyPI.

---

# Getting Help

If you have questions:

* Open a GitHub Discussion (if enabled).
* Open an Issue for bugs or feature requests.
* Review the project documentation.

---

# Thank You

Thank you for helping make **Fraction** better.

Every contribution—whether it's code, documentation, tests, or ideas—helps improve the project for the entire Python community.
