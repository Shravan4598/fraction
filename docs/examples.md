# Examples

This page demonstrates common ways to use the **Fraction** package.

---

# Basic Usage

Create fraction objects and print them.

```python
from fraction import fraction

a = fraction(1, 2)
b = fraction(3, 4)

print(a)
print(b)
```

Output

```text
1/2
3/4
```

---

# Automatic Simplification

Fractions are automatically reduced.

```python
from fraction import fraction

print(fraction(6, 8))
print(fraction(20, 100))
```

Output

```text
3/4
1/5
```

---

# Negative Denominators

Negative denominators are normalised.

```python
from fraction import fraction

print(fraction(3, -5))
print(fraction(-3, -5))
```

Output

```text
-3/5
3/5
```

---

# Arithmetic

```python
from fraction import fraction

a = fraction(2, 3)
b = fraction(5, 6)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

Output

```text
3/2
-1/6
5/9
4/5
```

---

# Working with Integers

Fractions work naturally with integers.

```python
from fraction import fraction

x = fraction(3, 4)

print(x + 2)

print(2 + x)

print(x * 5)

print(5 * x)
```

---

# Working with Python's Fraction

```python
from fractions import Fraction
from fraction import fraction

a = fraction(2, 3)
b = Fraction(5, 7)

print(a + b)

print(a * b)
```

---

# Comparison Operators

```python
from fraction import fraction

print(fraction(1, 2) == fraction(2, 4))

print(fraction(3, 4) > fraction(2, 3))

print(fraction(1, 5) < 1)

print(fraction(7, 3) >= 2)
```

---

# Unary Operators

```python
from fraction import fraction

x = fraction(-7, 5)

print(+x)

print(-x)

print(abs(x))
```

---

# Powers

```python
from fraction import fraction

x = fraction(2, 3)

print(x ** 2)

print(x ** -2)

print(x ** 0)
```

---

# Float Conversion

```python
from fraction import fraction

x = fraction(1, 8)

print(float(x))
```

Output

```text
0.125
```

---

# Integer Conversion

```python
from fraction import fraction

print(int(fraction(7, 3)))
```

Output

```text
2
```

---

# Boolean Conversion

```python
from fraction import fraction

print(bool(fraction(0, 5)))

print(bool(fraction(2, 7)))
```

Output

```text
False
True
```

---

# Alternative Constructors

## From String

```python
from fraction import fraction

print(fraction.from_string("7/9"))

print(fraction.from_string("15"))
```

---

## From Float

```python
from fraction import fraction

print(fraction.from_float(0.125))
```

---

## From Decimal

```python
from decimal import Decimal
from fraction import fraction

print(fraction.from_decimal(Decimal("2.75")))
```

---

# Utility Methods

## Reciprocal

```python
from fraction import fraction

x = fraction(5, 8)

print(x.reciprocal())
```

---

## Decimal Representation

```python
from fraction import fraction

print(fraction(1, 3).to_decimal())

print(fraction(1, 3).to_decimal(5))
```

---

## Tuple Representation

```python
from fraction import fraction

print(fraction(9, 10).as_tuple())
```

Output

```text
(9, 10)
```

---

## Mixed Numbers

```python
from fraction import fraction

whole, remainder = fraction(17, 5).mixed()

print(whole)

print(remainder)
```

Output

```text
3
2/5
```

---

# Formatting

```python
from fraction import fraction

x = fraction(1, 8)

print(format(x, ".2f"))

print(f"{x:.4f}")
```

---

# Hashing

Fraction objects are hashable and can be used in sets or dictionaries.

```python
from fraction import fraction

numbers = {
    fraction(1, 2),
    fraction(2, 4),
    fraction(3, 4),
}

print(numbers)
```

---

# Exception Handling

```python
from fraction import fraction

try:
    fraction(1, 0)
except ZeroDivisionError as exc:
    print(exc)
```

---

# Best Practices

* Prefer immutable fraction objects instead of modifying existing ones.
* Use `from_string()` when reading fractions from text files or user input.
* Use `from_decimal()` when exact decimal precision is required.
* Use `fractions.Fraction` interoperability when integrating with the Python standard library.
* Keep arithmetic in the `fraction` type instead of converting to `float` unless floating-point behaviour is specifically needed.

---

# Next Steps

After exploring these examples:

* Read the **API Reference** for detailed documentation.
* Review the **Installation Guide** for development setup.
* Visit the project repository to contribute or report issues.
