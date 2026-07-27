"""
Comparison Operations Example
=============================

Demonstrates comparison operators, hashing, sorting,
and interoperability.

Run:

    python examples/comparison.py
"""

from fractions import Fraction

from fraction import fraction


def heading(title: str) -> None:
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def main() -> None:
    heading("Fraction Comparison Examples")

    a = fraction(1, 2)
    b = fraction(2, 4)
    c = fraction(3, 4)
    d = fraction(5, 6)

    print("Fractions")
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")
    print(f"d = {d}")

    # -------------------------------------------------
    # Equality
    # -------------------------------------------------
    heading("Equality")

    print(f"{a} == {b} -> {a == b}")
    print(f"{a} != {c} -> {a != c}")

    # -------------------------------------------------
    # Ordering
    # -------------------------------------------------
    heading("Ordering")

    print(f"{a} < {c}  -> {a < c}")
    print(f"{d} > {c}  -> {d > c}")
    print(f"{a} <= {b} -> {a <= b}")
    print(f"{d} >= {c} -> {d >= c}")

    # -------------------------------------------------
    # Comparison with Integers
    # -------------------------------------------------
    heading("Comparison with Integers")

    print(f"{a} == 0 -> {a == 0}")
    print(f"{a} < 1  -> {a < 1}")
    print(f"{d} > 0  -> {d > 0}")
    print(f"{c} >= 1 -> {c >= 1}")

    # -------------------------------------------------
    # Comparison with fractions.Fraction
    # -------------------------------------------------
    heading("Comparison with fractions.Fraction")

    std = Fraction(1, 2)

    print(f"{a} == Fraction(1, 2) -> {a == std}")
    print(f"{c} > Fraction(1, 2)  -> {c > std}")

    # -------------------------------------------------
    # Sorting
    # -------------------------------------------------
    heading("Sorting")

    values = [
        fraction(5, 8),
        fraction(1, 3),
        fraction(7, 9),
        fraction(1, 2),
        fraction(3, 5),
    ]

    print("Original:")
    print(values)

    print("\nSorted:")
    print(sorted(values))

    # -------------------------------------------------
    # Minimum / Maximum
    # -------------------------------------------------
    heading("Minimum and Maximum")

    print(f"Minimum: {min(values)}")
    print(f"Maximum: {max(values)}")

    # -------------------------------------------------
    # Hashing
    # -------------------------------------------------
    heading("Hashing")

    print(f"hash({a}) = {hash(a)}")
    print(f"hash({b}) = {hash(b)}")

    print("Equal fractions should have identical hashes:")
    print(hash(a) == hash(b))

    # -------------------------------------------------
    # Set Behaviour
    # -------------------------------------------------
    heading("Set Behaviour")

    numbers = {
        fraction(1, 2),
        fraction(2, 4),
        fraction(3, 4),
        fraction(6, 8),
    }

    print(numbers)
    print(f"Unique values: {len(numbers)}")

    # -------------------------------------------------
    # Dictionary Keys
    # -------------------------------------------------
    heading("Dictionary Keys")

    prices = {
        fraction(1, 2): "Half",
        fraction(3, 4): "Three Quarters",
        fraction(5, 6): "Five Sixths",
    }

    print(prices)

    print("\nLookup using an equivalent fraction:")

    print(prices[fraction(2, 4)])

    # -------------------------------------------------
    # Membership
    # -------------------------------------------------
    heading("Membership")

    print(f"{fraction(3, 4)} in set -> {fraction(3, 4) in numbers}")
    print(f"{fraction(1, 5)} in set -> {fraction(1, 5) in numbers}")

    print("\nComparison demonstration completed successfully.")


if __name__ == "__main__":
    main()
