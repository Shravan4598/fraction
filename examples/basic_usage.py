
"""
Basic Usage Example
===================

This example demonstrates the basic functionality of the
Fraction package.

Run:

    python examples/basic_usage.py
"""

from fraction import fraction


def main() -> None:
    print("=" * 50)
    print("Fraction Package - Basic Usage")
    print("=" * 50)

    # Create fractions
    a = fraction(1, 2)
    b = fraction(3, 4)

    print("\nCreating fractions")
    print("------------------")
    print(f"a = {a}")
    print(f"b = {b}")

    # Automatic simplification
    print("\nAutomatic simplification")
    print("------------------------")
    c = fraction(10, 20)
    print(f"fraction(10, 20) -> {c}")

    # Arithmetic operations
    print("\nArithmetic")
    print("----------")
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")

    # Comparisons
    print("\nComparisons")
    print("-----------")
    print(f"{a} == {b}: {a == b}")
    print(f"{a} < {b}:  {a < b}")
    print(f"{a} <= {b}: {a <= b}")
    print(f"{a} > {b}:  {a > b}")

    # Unary operators
    print("\nUnary operators")
    print("----------------")
    x = fraction(-5, 8)
    print(f"x = {x}")
    print(f"+x = {+x}")
    print(f"-x = {-x}")
    print(f"abs(x) = {abs(x)}")

    # Type conversions
    print("\nConversions")
    print("-----------")
    print(f"float({a}) = {float(a)}")
    print(f"int(fraction(7, 3)) = {int(fraction(7, 3))}")
    print(f"bool(fraction(0, 5)) = {bool(fraction(0, 5))}")
    print(f"bool({a}) = {bool(a)}")

    # Utility methods
    print("\nUtility methods")
    print("----------------")
    y = fraction(7, 3)

    print(f"y = {y}")
    print(f"Reciprocal: {y.reciprocal()}")
    print(f"Tuple: {y.as_tuple()}")
    print(f"Mixed number: {y.mixed()}")

    print("\nDone!")


if __name__ == "__main__":
    main()

