
"""
Arithmetic Operations Example
=============================

Demonstrates arithmetic operations supported by the
Fraction package.

Run:

    python examples/arithmetic.py
"""

from fraction import fraction


def print_heading(title: str) -> None:
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def show_operation(left, operator: str, right, result) -> None:
    print(f"{left} {operator} {right} = {result}")


def main() -> None:
    print_heading("Fraction Arithmetic Examples")

    a = fraction(1, 2)
    b = fraction(3, 4)
    c = fraction(5, 6)

    print("Operands")
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")

    # -------------------------------------------------
    # Addition
    # -------------------------------------------------
    print_heading("Addition")

    show_operation(a, "+", b, a + b)
    show_operation(b, "+", c, b + c)
    show_operation(a, "+", 2, a + 2)
    show_operation(2, "+", a, 2 + a)

    # -------------------------------------------------
    # Subtraction
    # -------------------------------------------------
    print_heading("Subtraction")

    show_operation(b, "-", a, b - a)
    show_operation(c, "-", b, c - b)
    show_operation(a, "-", 1, a - 1)
    show_operation(1, "-", a, 1 - a)

    # -------------------------------------------------
    # Multiplication
    # -------------------------------------------------
    print_heading("Multiplication")

    show_operation(a, "*", b, a * b)
    show_operation(b, "*", c, b * c)
    show_operation(a, "*", 5, a * 5)
    show_operation(5, "*", a, 5 * a)

    # -------------------------------------------------
    # Division
    # -------------------------------------------------
    print_heading("Division")

    show_operation(a, "/", b, a / b)
    show_operation(c, "/", a, c / a)
    show_operation(a, "/", 2, a / 2)
    show_operation(2, "/", a, 2 / a)

    # -------------------------------------------------
    # Powers
    # -------------------------------------------------
    print_heading("Exponentiation")

    x = fraction(2, 3)

    print(f"{x} ** 2 = {x ** 2}")
    print(f"{x} ** 3 = {x ** 3}")
    print(f"{x} ** 0 = {x ** 0}")
    print(f"{x} ** -1 = {x ** -1}")
    print(f"{x} ** -2 = {x ** -2}")

    # -------------------------------------------------
    # Complex Expressions
    # -------------------------------------------------
    print_heading("Complex Expressions")

    result1 = (a + b) * c
    result2 = a + b * c
    result3 = (a - b) / c
    result4 = (a + c) ** 2

    print(f"(a + b) * c = {result1}")
    print(f"a + b * c = {result2}")
    print(f"(a - b) / c = {result3}")
    print(f"(a + c) ** 2 = {result4}")

    # -------------------------------------------------
    # Mixed Integer Arithmetic
    # -------------------------------------------------
    print_heading("Operations with Integers")

    y = fraction(7, 5)

    print(f"{y} + 10 = {y + 10}")
    print(f"10 + {y} = {10 + y}")

    print(f"{y} - 3 = {y - 3}")
    print(f"3 - {y} = {3 - y}")

    print(f"{y} * 4 = {y * 4}")
    print(f"4 * {y} = {4 * y}")

    print(f"{y} / 2 = {y / 2}")
    print(f"2 / {y} = {2 / y}")

    # -------------------------------------------------
    # Error Handling
    # -------------------------------------------------
    print_heading("Error Handling")

    try:
        print(fraction(1, 2) / fraction(0, 1))
    except ZeroDivisionError as exc:
        print("Division by zero:")
        print(exc)

    try:
        print(fraction(1, 0))
    except ZeroDivisionError as exc:
        print("\nInvalid fraction:")
        print(exc)

    print("\nArithmetic demonstration completed successfully.")


if __name__ == "__main__":
    main()

