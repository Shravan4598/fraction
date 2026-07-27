# Fraction

Welcome to the official documentation for **Fraction**, a modern, lightweight, pure-Python implementation of a mathematical **Fraction** data type.

Fraction provides a clean, intuitive, and fully type-annotated API for working with rational numbers while integrating naturally with Python's numeric ecosystem.

---

# Why Fraction?

Python already includes `fractions.Fraction`, but this project was built as an educational and open-source implementation demonstrating how a production-quality numeric data type can be designed and packaged.

The project focuses on:

* Clean and readable implementation
* Modern Python packaging standards
* Rich operator overloading
* Full type annotations
* Comprehensive testing
* Professional documentation
* PyPI-ready distribution

Whether you're learning object-oriented programming, operator overloading, or building mathematical software, **Fraction** provides an approachable and practical reference implementation.

---

# Features

* Immutable fraction objects
* Automatic simplification
* Positive denominator normalization
* Arithmetic operators
* Comparison operators
* Unary operators
* Integer, float, and `Decimal` conversions
* Reciprocal calculation
* Mixed number conversion
* Alternative constructors
* Interoperability with:

  * Python integers
  * `float`
  * `fractions.Fraction`
* Type hints (PEP 561)
* Compatible with Python's `numbers.Rational`
* Modern `src/` package layout
* Comprehensive pytest test suite
* Continuous Integration with GitHub Actions

---

# Installation

Install the latest release from PyPI:

```bash
pip install fraction
```

Or install from source:

```bash
git clone https://github.com/Shravan4598/fraction.git

cd fraction

pip install -e .
```

---

# Quick Start

```python
from fraction import fraction

a = fraction(1, 2)
b = fraction(3, 4)

print(a)
print(b)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

Output:

```text
1/2
3/4
5/4
-1/4
3/8
2/3
```

---

# Example Operations

```python
from fraction import fraction

x = fraction(7, 3)

print(x.reciprocal())

print(x.mixed())

print(float(x))

print(int(x))

print(abs(-x))
```

---

# Documentation Guide

The documentation is organised into the following sections:

## Installation

Complete installation instructions and development setup.

## API Reference

Detailed documentation for every public class, property, method, and operator.

## Examples

Practical examples demonstrating common use cases and interoperability with Python's standard library.

## Changelog

A record of notable changes between releases.

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
├── examples/
│
├── docs/
│
├── .github/
│
├── pyproject.toml
└── README.md
```

---

# Contributing

Contributions of all kinds are welcome.

You can help by:

* Reporting bugs
* Improving documentation
* Writing tests
* Adding examples
* Suggesting features
* Improving performance

Please read **CONTRIBUTING.md** before submitting a pull request.

---

# Roadmap

Future releases are expected to include:

* Additional mathematical utilities
* Performance improvements
* Serialization helpers
* Expanded interoperability
* More examples
* Benchmark suite
* Enhanced documentation

---

# License

Fraction is released under the **MIT License**.

See the project's `LICENSE` file for complete details.

---

# Author

**Shravan Kumar Pandey**

* GitHub: https://github.com/Shravan4598
* Repository: https://github.com/Shravan4598/fraction

---

Thank you for using **Fraction**!

We hope this project serves as both a useful Python library and an educational resource for learning modern Python development and package design.
