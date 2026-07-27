# Installation

This guide explains how to install **Fraction** for both regular use and development.

---

# Requirements

Fraction supports:

* Python 3.10+
* Windows
* macOS
* Linux

Verify your Python version:

```bash
python --version
```

---

# Install from PyPI

The recommended way to install the latest stable release is:

```bash
pip install fraction
```

Verify the installation:

```bash
python -c "from fraction import fraction; print(fraction(1, 2))"
```

Expected output:

```text
1/2
```

---

# Upgrade to the Latest Version

Upgrade an existing installation:

```bash
pip install --upgrade fraction
```

---

# Install from Source

Clone the repository:

```bash
git clone https://github.com/Shravan4598/fraction.git
```

Move into the project directory:

```bash
cd fraction
```

Install the package:

```bash
pip install .
```

---

# Editable Installation (Recommended for Development)

Editable mode allows changes made to the source code to be reflected immediately without reinstalling the package.

```bash
pip install -e .
```

---

# Install Development Dependencies

To contribute to the project, install all development tools:

```bash
pip install -r requirements-dev.txt
```

This installs:

* pytest
* Ruff
* Black
* MyPy
* Coverage
* MkDocs
* Pre-commit
* Build tools
* Twine
* Tox

---

# Create a Virtual Environment

Using a virtual environment is strongly recommended.

## Windows

```powershell
python -m venv .venv

.venv\Scripts\activate
```

---

## macOS / Linux

```bash
python -m venv .venv

source .venv/bin/activate
```

After activation:

```bash
pip install --upgrade pip
```

---

# Verify the Installation

Create a file named `example.py`:

```python
from fraction import fraction

a = fraction(2, 3)
b = fraction(5, 6)

print(a + b)
```

Run it:

```bash
python example.py
```

Expected output:

```text
3/2
```

---

# Running Tests

Run the complete test suite:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=fraction
```

---

# Code Formatting

Format the project:

```bash
black .
```

Check formatting only:

```bash
black --check .
```

---

# Linting

Run Ruff:

```bash
ruff check .
```

Automatically fix issues where possible:

```bash
ruff check . --fix
```

---

# Type Checking

Run MyPy:

```bash
mypy src
```

---

# Building the Package

Build both the source distribution and wheel:

```bash
python -m build
```

The generated files will appear in:

```text
dist/
```

---

# Verify the Distribution

Before publishing, validate the generated packages:

```bash
twine check dist/*
```

---

# Publishing to PyPI

Upload the distributions:

```bash
twine upload dist/*
```

Alternatively, configure GitHub Actions with **Trusted Publishing** to publish automatically from tagged releases.

---

# Common Installation Issues

## `pip` not found

Try:

```bash
python -m pip install fraction
```

---

## Wrong Python Version

Check your interpreter:

```bash
python --version
```

Ensure it is Python **3.10** or newer.

---

## Virtual Environment Not Activated

If packages appear to install but cannot be imported, verify your virtual environment is active before installing dependencies.

---

## Permission Errors

Avoid using administrator/root privileges unless necessary.

Using a virtual environment generally resolves permission-related issues.

---

# Uninstall

Remove the package:

```bash
pip uninstall fraction
```

---

# Next Steps

Now that Fraction is installed, continue with:

* **API Reference** — Learn about every class and method.
* **Examples** — Explore common usage patterns.
* **Contributing Guide** — Set up a development environment and contribute to the project.

Happy coding!
