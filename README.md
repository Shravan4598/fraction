# Fraction

<div align="center">

A modern, lightweight, immutable, and fully type-annotated rational number library for Python.

Designed to integrate seamlessly with Python's numeric ecosystem while providing a clean, intuitive API for fraction arithmetic, comparison, conversion, and interoperability.

[![PyPI Version](https://img.shields.io/pypi/v/fraction.svg)](https://pypi.org/project/fraction/)
[![Python Versions](https://img.shields.io/pypi/pyversions/fraction.svg)](https://pypi.org/project/fraction/)
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

- Python **3.12+**
- Pure Python
- No runtime dependencies
- Cross-platform
- Fully typed

---

# Installation

## Install from PyPI

```bash
pip install fraction-py
