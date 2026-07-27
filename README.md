# Fraction

<div align="center">

A modern, lightweight, immutable, and fully type-annotated rational number library for Python.

Designed to integrate seamlessly with Python's numeric ecosystem while providing a clean, intuitive API for fraction arithmetic, comparison, conversion, and interoperability.

[![PyPI Version](https://img.shields.io/pypi/v/fraction-py.svg)](https://pypi.org/project/fraction-py/)
[![Python Versions](https://img.shields.io/pypi/pyversions/fraction-py.svg)](https://pypi.org/project/fraction-py/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Tests](https://github.com/Shravan4598/fraction/actions/workflows/tests.yml/badge.svg)](https://github.com/Shravan4598/fraction/actions)
[![Code Coverage](https://img.shields.io/badge/Coverage-95%25-brightgreen.svg)](https://github.com/Shravan4598/fraction)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/badge/linter-ruff-blue.svg)](https://github.com/astral-sh/ruff)
[![Type Checked](https://img.shields.io/badge/type--checked-mypy-blue.svg)](https://mypy-lang.org/)

</div>

---

# Why Fraction?

Python already provides `fractions.Fraction`, but this library focuses on simplicity, readability, modern packaging, and developer experience.

It provides a clean immutable implementation that behaves naturally with Python's numeric types while remaining easy to understand, extend, and use in educational, scientific, and production projects.

Highlights include:

- Automatic simplification
- Immutable objects
- Rich operator overloading
- Strong type hints
- Modern Python packaging
- Comprehensive test suite
- Excellent interoperability

---

# Table of Contents

- Features
- Requirements
- Installation
- Quick Start
- Creating Fractions
- Arithmetic
- Comparisons
- Type Conversions
- Utility Methods
- Interoperability
- API Overview
- Project Structure
- Development
- Testing
- Documentation
- Roadmap
- Contributing
- License
- Author

---

# Features

## Core Features

- Pure Python implementation
- Automatic reduction to lowest terms
- Immutable design
- Memory-efficient (`__slots__`)
- Fully type annotated
- PEP 561 compatible
- Pickle support
- Hashable objects

---

## Supported Arithmetic

- Addition
- Subtraction
- Multiplication
- Division
- Power operator
- Unary operators
- Reciprocal

---

## Comparisons

- Equality
- Less than
- Less than or equal
- Greater than
- Greater than or equal

---

## Type Conversions

Supports conversion to

- `int`
- `float`
- `bool`
- `round()`

Alternative constructors

- `from_string()`
- `from_float()`
- `from_decimal()`

---

## Utility Methods

- `reciprocal()`
- `mixed()`
- `to_decimal()`
- `as_tuple()`

---

## Interoperability

Works naturally with

- `int`
- `float`
- `fractions.Fraction`
- Python's `numbers.Rational`

---

# Requirements

- Python **3.10+**
- Pure Python
- No runtime dependencies
- Cross-platform
- Fully typed

---

# Installation

## Install from PyPI

```bash
pip install fraction-py
```

---

## Install from source

```bash
git clone https://github.com/Shravan4598/fraction.git

cd fraction

pip install -e .
```

---

## Install development dependencies

```bash
pip install -r requirements-dev.txt
```

---

# Verify Installation

```python
>>> from fraction import fraction

>>> fraction(2, 4)
fraction(1, 2)

>>> fraction(5)
fraction(5, 1)

>>> fraction.from_string("3/9")
fraction(1, 3)
```

---

# Quick Start

```python
from fraction import fraction

a = fraction(1, 2)
b = fraction(3, 4)

print("a =", a)
print("b =", b)

print("Addition      :", a + b)
print("Subtraction   :", a - b)
print("Multiplication:", a * b)
print("Division      :", a / b)

print("Power         :", a ** 3)

print("Reciprocal    :", a.reciprocal())

print("Mixed Number  :", fraction(7, 3).mixed())
```

Output

```text
a = 1/2
b = 3/4

Addition      : 5/4
Subtraction   : -1/4
Multiplication: 3/8
Division      : 2/3

Power         : 1/8

Reciprocal    : 2

Mixed Number  : (2, fraction(1, 3))
```

---

# Design Goals

This project aims to provide a fraction implementation that is:

- Easy to learn
- Easy to read
- Fully immutable
- Type-safe
- Fast enough for everyday use
- Suitable for education
- Suitable for production projects
- Compatible with modern Python tooling

---
# Creating Fractions

Fractions can be created in several ways depending on your data source.

## Using the Constructor

```python
from fraction import fraction

a = fraction(3, 4)
b = fraction(5)
c = fraction(-7, 9)

print(a)
print(b)
print(c)
```

Output

```text
3/4
5
-7/9
```

---

## Automatic Simplification

Fractions are always stored in their simplest form.

```python
fraction(10, 20)
```

Output

```text
fraction(1, 2)
```

```python
fraction(-15, -30)
```

Output

```text
fraction(1, 2)
```

---

## Negative Denominator

The denominator is always kept positive.

```python
fraction(2, -5)
```

Output

```text
fraction(-2, 5)
```

---

## Creating from Strings

```python
fraction.from_string("7/9")

fraction.from_string("12")

fraction.from_string("-15/20")
```

Output

```text
fraction(7, 9)

fraction(12, 1)

fraction(-3, 4)
```

---

## Creating from Floats

```python
fraction.from_float(0.75)

fraction.from_float(1.25)
```

Output

```text
fraction(3, 4)

fraction(5, 4)
```

---

## Creating from Decimal

```python
from decimal import Decimal

fraction.from_decimal(
    Decimal("3.125")
)
```

Output

```text
fraction(25, 8)
```

---

# Arithmetic Operations

The class fully supports Python arithmetic operators.

## Addition

```python
a = fraction(1, 2)
b = fraction(2, 3)

print(a + b)
```

Output

```text
7/6
```

---

## Subtraction

```python
print(
    fraction(5, 6) -
    fraction(1, 3)
)
```

Output

```text
1/2
```

---

## Multiplication

```python
print(
    fraction(4, 5) *
    fraction(3, 7)
)
```

Output

```text
12/35
```

---

## Division

```python
print(
    fraction(3, 5) /
    fraction(9, 10)
)
```

Output

```text
2/3
```

---

## Powers

```python
x = fraction(2, 3)

print(x ** 2)

print(x ** 3)

print(x ** -2)
```

Output

```text
4/9

8/27

9/4
```

---

## Unary Operators

```python
x = fraction(-2, 5)

print(+x)

print(-x)

print(abs(x))
```

Output

```text
-2/5

2/5

2/5
```

---

# Operations with Integers

Fractions work naturally with integers.

```python
x = fraction(3, 4)

print(x + 2)

print(2 + x)

print(x - 1)

print(5 - x)

print(x * 4)

print(4 * x)

print(x / 2)

print(2 / x)
```

---

# Comparison Operations

Fractions support all rich comparison operators.

```python
fraction(1, 2) == fraction(2, 4)

fraction(3, 5) != fraction(4, 5)

fraction(1, 2) < fraction(2, 3)

fraction(7, 8) > fraction(5, 8)

fraction(4, 5) >= fraction(4, 5)

fraction(2, 3) <= fraction(5, 6)
```

---

## Comparison with Integers

```python
fraction(5, 2) > 2

fraction(1, 3) < 1

fraction(6, 2) == 3
```

---

## Comparison with Float

```python
fraction(1, 2) == 0.5

fraction(1, 4) < 0.5

fraction(7, 4) > 1.5
```

---

# Type Conversions

The class integrates naturally with Python conversion functions.

## Convert to Float

```python
float(fraction(3, 8))
```

Output

```text
0.375
```

---

## Convert to Integer

Integer conversion truncates toward zero.

```python
int(fraction(7, 3))

int(fraction(-7, 3))
```

Output

```text
2

-2
```

---

## Boolean Conversion

```python
bool(fraction(1, 5))

bool(fraction(0, 9))
```

Output

```text
True

False
```

---

## Rounding

```python
round(fraction(1, 3), 2)

round(fraction(5, 2))
```

---

## Formatting

```python
f = fraction(1, 3)

print(format(f, ".2f"))

print(format(f, ".5f"))
```

---

# Utility Methods

## Reciprocal

```python
fraction(2, 5).reciprocal()
```

Output

```text
fraction(5, 2)
```

---

## Mixed Number

```python
fraction(7, 3).mixed()

fraction(-7, 3).mixed()

fraction(-1, 3).mixed()
```

Output

```text
(2, fraction(1, 3))

(-2, fraction(1, 3))

(0, fraction(-1, 3))
```

---

## Decimal Representation

```python
fraction(1, 3).to_decimal()

fraction(1, 3).to_decimal(5)
```

Output

```text
0.33

0.33333
```

---

## Tuple Representation

```python
fraction(5, 8).as_tuple()
```

Output

```text
(5, 8)
```

---

# Interoperability

One of the design goals of this project is smooth interoperability with Python's built-in numeric types.

## Built-in Fraction

```python
from fractions import Fraction

a = fraction(2, 3)

b = Fraction(5, 7)

print(a + b)

print(a - b)

print(a * b)

print(a / b)
```

---

## Integers

```python
a = fraction(3, 4)

print(a + 5)

print(5 + a)

print(a * 10)

print(10 * a)

print(a / 2)

print(2 / a)
```

---

## Hashability

Fractions are immutable and hashable, making them suitable as dictionary keys and set elements.

```python
d = {
    fraction(1, 2): "half",
    fraction(2, 3): "two thirds",
}

print(d[fraction(2, 4)])
```

Output

```text
half
```

---

## Copy Support

Because fractions are immutable, copying returns the same object.

```python
import copy

f = fraction(3, 4)

assert copy.copy(f) is f

assert copy.deepcopy(f) is f
```

---
# API Reference

## Constructor

### `fraction(numerator, denominator=1)`

Creates a new immutable fraction.

```python
fraction(3, 4)

fraction(10)

fraction(-5, 8)
```

---

# Alternative Constructors

## `fraction.from_string()`

Construct a fraction from a string.

```python
fraction.from_string("5/8")

fraction.from_string("42")
```

---

## `fraction.from_float()`

Construct from a floating-point number.

```python
fraction.from_float(0.125)
```

---

## `fraction.from_decimal()`

Construct from a Decimal.

```python
from decimal import Decimal

fraction.from_decimal(
    Decimal("2.75")
)
```

---

# Properties

## `numerator`

Returns the numerator.

```python
f = fraction(5, 8)

print(f.numerator)
```

Output

```text
5
```

---

## `denominator`

Returns the denominator.

```python
f = fraction(5, 8)

print(f.denominator)
```

Output

```text
8
```

---

# Supported Operators

## Arithmetic

| Operator | Description |
|----------|-------------|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `**` | Exponentiation |

---

## Comparison

| Operator | Description |
|----------|-------------|
| `==` | Equality |
| `!=` | Not Equal |
| `<` | Less Than |
| `<=` | Less Than or Equal |
| `>` | Greater Than |
| `>=` | Greater Than or Equal |

---

## Unary

| Operator | Description |
|----------|-------------|
| `+` | Unary Plus |
| `-` | Unary Minus |
| `abs()` | Absolute Value |

---

## Conversion Functions

| Function | Description |
|----------|-------------|
| `int()` | Convert to integer |
| `float()` | Convert to float |
| `bool()` | Truth value |
| `round()` | Rounded value |
| `format()` | String formatting |

---

# Utility Methods

| Method | Description |
|---------|-------------|
| `reciprocal()` | Returns reciprocal |
| `mixed()` | Returns mixed number |
| `to_decimal()` | Rounded decimal representation |
| `as_tuple()` | Returns `(numerator, denominator)` |

---

# Design Principles

The library follows several important design goals.

- Immutable objects
- Automatic normalization
- Consistent hashing
- Strong type hints
- Pythonic API
- Interoperability with built-in numeric types
- Memory efficiency using `__slots__`
- Safe arithmetic
- Production-ready packaging

---

# Project Structure

```text
fraction/
│
├── src/
│   └── fraction/
│       ├── __init__.py
│       ├── fraction.py
│       └── py.typed
│
├── tests/
│   ├── test_constructor.py
│   ├── test_arithmetic.py
│   ├── test_comparison.py
│   ├── test_conversion.py
│   ├── test_unary.py
│   ├── test_power.py
│   ├── test_utilities.py
│   ├── test_edge_cases.py
│   └── test_hash.py
│
├── examples/
│   ├── basic_usage.py
│   ├── arithmetic.py
│   ├── comparison.py
│   └── interoperability.py
│
├── docs/
│
├── .github/
│   └── workflows/
│
├── pyproject.toml
├── README.md
├── LICENSE
└── ...
```

---

# Testing

The project uses **pytest** for testing.

Run all tests

```bash
pytest
```

---

Run with verbose output

```bash
pytest -v
```

---

Run a single file

```bash
pytest tests/test_arithmetic.py
```

---

Run a single test

```bash
pytest -k reciprocal
```

---

Generate coverage

```bash
pytest --cov=fraction
```

---

Generate HTML coverage report

```bash
pytest --cov=fraction --cov-report=html
```

The report will be available in

```text
htmlcov/index.html
```

---

# Code Quality

The project follows modern Python development practices.

## Ruff

Run Ruff

```bash
ruff check .
```

Automatically fix issues

```bash
ruff check . --fix
```

---

## Black

Format all files

```bash
black .
```

Check formatting

```bash
black . --check
```

---

## MyPy

Run static type checking

```bash
mypy src
```

---

## Pre-commit

Install hooks

```bash
pre-commit install
```

Run manually

```bash
pre-commit run --all-files
```

---

# Development

Clone the repository

```bash
git clone https://github.com/Shravan4598/fraction.git
```

Move into the project

```bash
cd fraction
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements-dev.txt
```

Install the package in editable mode

```bash
pip install -e .
```

---

# Building the Package

Build a source distribution and wheel

```bash
python -m build
```

Generated files

```text
dist/

fraction-x.x.x.tar.gz

fraction-x.x.x-py3-none-any.whl
```

---

# Publishing to PyPI

Upload using Twine

```bash
twine upload dist/*
```

If Trusted Publishing is configured, GitHub Actions can publish automatically when a release is created.

---

# Continuous Integration

GitHub Actions automatically performs:

- Code formatting checks
- Ruff linting
- MyPy type checking
- Unit testing
- Coverage generation
- Package building
- Distribution validation

Every pull request and push is validated before merging.

---

# Documentation

Documentation is generated using **MkDocs Material**.

Serve locally

```bash
mkdocs serve
```

Build the documentation

```bash
mkdocs build
```

Deploy to GitHub Pages

```bash
mkdocs gh-deploy
```

The documentation includes:

- Installation Guide
- API Reference
- Examples
- Changelog
- Development Guide

---

# Performance

The `fraction` package is designed to be lightweight, efficient, and predictable.

## Characteristics

- Immutable objects
- Hashable
- Automatic normalization using `math.gcd()`
- Memory efficient (`__slots__`)
- Fully type annotated
- Pure Python
- No runtime dependencies

Most arithmetic operations execute in constant time apart from the cost of integer arithmetic and the GCD calculation required for normalization.

---

# FAQ

## Why not use `fractions.Fraction`?

Python's built-in `fractions.Fraction` is an excellent implementation.

This project is intended to provide:

- A clean educational implementation
- Modern project structure
- Strong typing
- Easy-to-read source code
- Examples for learning operator overloading
- A reusable open-source package

---

## Is the class immutable?

Yes.

After construction, neither the numerator nor denominator can be modified.

---

## Are fractions automatically simplified?

Yes.

```python
fraction(20, 60)
```

becomes

```text
fraction(1, 3)
```

---

## Can I use fractions as dictionary keys?

Yes.

```python
prices = {
    fraction(1, 2): "Half",
    fraction(1, 4): "Quarter",
}

print(prices[fraction(2, 4)])
```

Output

```text
Half
```

---

## Does it support negative fractions?

Yes.

```python
fraction(-2, 5)

fraction(2, -5)

fraction(-2, -5)
```

All signs are normalized automatically.

---

## Does it support Decimal?

Yes.

```python
from decimal import Decimal

fraction.from_decimal(
    Decimal("3.125")
)
```

---

## Does it work with Python integers?

Yes.

```python
fraction(1, 2) + 5

5 + fraction(1, 2)

fraction(3, 4) * 8

8 / fraction(3, 4)
```

---

## Is the project thread-safe?

Yes.

Because the objects are immutable, they can safely be shared across threads.

---

# Roadmap

The following features are planned for future releases.

## Version 1.x

- Additional constructors
- Better formatting options
- JSON serialization helpers
- More mathematical utilities
- Improved interoperability

---

## Version 2.x

- Performance benchmarking
- NumPy interoperability
- SymPy interoperability
- Optional C extension
- Rich string formatting

---

## Long-term Goals

- Stable public API
- 100% documentation coverage
- 100% test coverage
- Continuous benchmarking
- Community contributions
- Educational examples
- Interactive documentation

---

# Contributing

Contributions are welcome and greatly appreciated.

You can contribute by

- Reporting bugs
- Suggesting features
- Improving documentation
- Writing tests
- Improving examples
- Optimising performance

Please read

- CONTRIBUTING.md
- CODE_OF_CONDUCT.md

before opening a pull request.

---

# Reporting Issues

If you discover a bug, please create a GitHub Issue including

- Python version
- Operating system
- Package version
- Minimal reproducible example
- Expected behaviour
- Actual behaviour

This helps us resolve issues more quickly.

---

# Security

If you discover a security vulnerability, please **do not** open a public issue.

Instead, follow the instructions in **SECURITY.md**.

We appreciate responsible disclosure.

---

# Versioning

This project follows **Semantic Versioning (SemVer)**.

Version numbers follow the format

```text
MAJOR.MINOR.PATCH
```

Example

```text
1.0.0
```

---

# Changelog

Release history is maintained in

```text
CHANGELOG.md
```

---

# License

This project is distributed under the **MIT License**.

You are free to

- Use
- Modify
- Distribute
- Include in commercial projects

subject to the terms of the MIT License.

See the LICENSE file for complete details.

---

# Acknowledgements

This project is inspired by

- Python's `fractions` module
- The Python Standard Library
- PEP 3141 — Numeric Tower
- The open-source Python community

Special thanks to all contributors and users who help improve this project.

---

# Author

## Shravan Kumar Pandey

**Computer Science & Engineering (Data Science)**

GitHub

https://github.com/Shravan4598


---

# Citation

If you use this project in research, teaching, or publications, please consider citing it.

BibTeX support may be added in future releases.

---

# Support the Project

If you find this project useful, you can help by

- ⭐ Starring the repository
- 🐛 Reporting issues
- 💡 Suggesting new features
- 📖 Improving documentation
- 🧪 Writing tests
- 🔀 Submitting pull requests

Every contribution, no matter how small, is appreciated.

---

# Maintainer

**Shravan Kumar Pandey**

GitHub: https://github.com/Shravan4598

---

<div align="center">

## ⭐ If you find this project useful, please consider giving it a star on GitHub!

Made with ❤️ using Python.

</div>
