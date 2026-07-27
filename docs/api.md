# API Reference

This page documents the public API of the **Fraction** package.

The package provides a single public class:

```python
from fraction import fraction
```

---

# Class Overview

```python
class fraction(numbers.Rational)
```

A lightweight, immutable implementation of a rational number.

The class automatically:

* Simplifies fractions
* Normalises negative denominators
* Supports Python's numeric protocols
* Implements arithmetic operators
* Implements comparison operators
* Supports hashing
* Supports pickling
* Provides rich type conversions

---

# Constructors

## Standard Constructor

```python
fraction(numerator: int, denominator: int = 1)
```

Creates a new fraction.

### Example

```python
from fraction import fraction

fraction(3, 4)

fraction(10)

fraction(-5, 8)
```

---

## from_string()

```python
fraction.from_string(value: str)
```

Creates a fraction from a string.

Examples

```python
fraction.from_string("3/4")

fraction.from_string("25")
```

---

## from_float()

```python
fraction.from_float(value: float)
```

Creates an exact fraction from a floating-point value.

Example

```python
fraction.from_float(0.125)
```

---

## from_decimal()

```python
fraction.from_decimal(value: Decimal)
```

Creates an exact fraction from a `Decimal`.

Example

```python
from decimal import Decimal

fraction.from_decimal(Decimal("1.25"))
```

---

# Properties

## numerator

```python
fraction.numerator
```

Returns the simplified numerator.

Example

```python
f = fraction(6, 8)

print(f.numerator)
```

---

## denominator

```python
fraction.denominator
```

Returns the positive denominator.

Example

```python
print(f.denominator)
```

---

# Arithmetic Operators

The following operators are supported.

| Operator | Description    |
| -------- | -------------- |
| `+`      | Addition       |
| `-`      | Subtraction    |
| `*`      | Multiplication |
| `/`      | Division       |
| `**`     | Exponentiation |

Example

```python
a = fraction(1, 2)
b = fraction(3, 5)

a + b
a - b
a * b
a / b
a ** 2
```

---

# Comparison Operators

Supported comparisons:

* `==`
* `!=`
* `<`
* `<=`
* `>`
* `>=`

Example

```python
fraction(1, 2) == fraction(2, 4)

fraction(3, 4) > fraction(1, 2)
```

---

# Unary Operators

Supported unary operations:

```python
+x

-x

abs(x)
```

Example

```python
x = fraction(-3, 4)

abs(x)

-x

+x
```

---

# Type Conversions

The class integrates naturally with Python.

Supported conversions:

```python
float(x)

int(x)

bool(x)

round(x)
```

Example

```python
x = fraction(7, 3)

float(x)

int(x)

bool(x)

round(x, 2)
```

---

# Utility Methods

## reciprocal()

Returns the reciprocal.

```python
fraction(3, 4).reciprocal()
```

Raises:

* `ZeroDivisionError`

---

## to_decimal()

Returns a rounded decimal representation.

```python
fraction(1, 3).to_decimal(4)
```

---

## as_tuple()

Returns

```python
(numerator, denominator)
```

Example

```python
fraction(5, 7).as_tuple()
```

---

## mixed()

Returns a mixed-number representation.

Example

```python
whole, remainder = fraction(7, 3).mixed()
```

Returns

```python
(2, fraction(1, 3))
```

---

# Python Protocol Support

The class implements:

* String representation
* Developer representation
* Hashing
* Copy
* Deep copy
* Pickling
* Formatting
* Boolean conversion

making it suitable for use with:

* dictionaries
* sets
* caching
* serialization
* standard Python collections

---

# Exceptions

The following exceptions may be raised.

## ZeroDivisionError

Raised when:

* denominator is zero
* reciprocal of zero is requested
* division by zero occurs
* negative powers are applied to zero

---

## TypeError

Raised when:

* numerator is not an integer
* denominator is not an integer

---

# Interoperability

The package interoperates with:

* `int`
* `float`
* `fractions.Fraction`
* `decimal.Decimal` (via `from_decimal()`)

Example

```python
from fractions import Fraction

fraction(1, 2) + Fraction(1, 3)

fraction(1, 2) + 5

fraction(3, 4) * 2
```

---

# Automatic API Documentation

The section below is generated automatically from the source code using **mkdocstrings**.

As the code evolves, this documentation will stay up to date without requiring manual edits.
