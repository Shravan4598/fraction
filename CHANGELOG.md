# Changelog

All notable changes to this project will be documented in this file.

The format is based on **Keep a Changelog** and this project adheres to **Semantic Versioning (SemVer)**.

## [Unreleased]

### Added

* Planned support for additional utility methods.
* Planned performance improvements.
* Planned documentation enhancements.
* Planned benchmark suite.
* Planned serialization utilities.
* Planned additional interoperability features.

---

## [1.0.0] - 2026-07-27

### Added

#### Core Features

* Initial public release of the `fraction` package.
* Immutable rational number implementation.
* Automatic fraction simplification.
* Positive denominator normalization.
* Full integration with Python's `numbers.Rational`.

#### Constructors

* Standard constructor.
* `from_string()`
* `from_float()`
* `from_decimal()`

#### Arithmetic

* Addition
* Subtraction
* Multiplication
* Division
* Reverse arithmetic operators
* In-place arithmetic operators
* Integer interoperability
* Float interoperability
* Compatibility with `fractions.Fraction`

#### Comparison

* Equality
* Less than
* Less than or equal
* Greater than
* Greater than or equal

#### Unary Operations

* Unary plus
* Unary minus
* Absolute value

#### Power Operations

* Integer powers
* Negative powers
* Float powers

#### Type Conversion

* `float()`
* `int()`
* `bool()`
* `round()`
* String formatting support

#### Utility Methods

* `reciprocal()`
* `mixed()`
* `to_decimal()`
* `as_tuple()`

#### Python Integration

* Hashable implementation.
* Pickle support.
* Copy support.
* Deep copy support.
* Type annotations (PEP 561).

#### Packaging

* Modern `src/` project layout.
* PEP 517 build system.
* PEP 518 compliance.
* PEP 621 metadata.
* PyPI-ready packaging.
* MkDocs documentation.
* GitHub Actions CI/CD.
* Comprehensive pytest test suite.

---

## Versioning Policy

This project follows **Semantic Versioning (SemVer)**.

* **MAJOR** version when incompatible API changes are introduced.
* **MINOR** version when functionality is added in a backward-compatible manner.
* **PATCH** version when backward-compatible bug fixes are released.

Examples:

* `1.0.0` → Initial stable release
* `1.1.0` → New features
* `1.1.1` → Bug fixes
* `2.0.0` → Breaking changes

---

## Release Process

Each release should include:

* Updated documentation
* Updated tests
* Updated version number
* Git tag
* GitHub Release
* PyPI publication

---

## References

* Keep a Changelog: https://keepachangelog.com/
* Semantic Versioning: https://semver.org/
