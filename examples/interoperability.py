
"""
Interoperability Example
========================

Demonstrates interoperability between the custom Fraction
class and Python's built-in numeric types.

Run:

    python examples/interoperability.py
"""

from decimal import Decimal
from fractions import Fraction
import pickle

from fraction import fraction


def heading(title: str) -> None:
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def main() -> None:
    heading("Interoperability Examples")

    x = fraction(3, 4)

    print(f"Custom fraction: {x}")

    # -------------------------------------------------
    # Integer Interoperability
    # -------------------------------------------------
    heading("Integers")

    print(f"{x} + 2 = {x + 2}")
    print(f"2 + {x} = {2 + x}")

    print(f"{x} - 2 = {x - 2}")
    print(f"2 - {x} = {2 - x}")

    print(f"{x} * 2 = {x * 2}")
    print(f"2 * {x} = {2 * x}")

    print(f"{x} / 2 = {x / 2}")
    print(f"2 / {x} = {2 / x}")

    # -------------------------------------------------
    # Python fractions.Fraction
    # -------------------------------------------------
    heading("fractions.Fraction")

    std = Fraction(2, 5)

    print(f"Standard Fraction: {std}")

    print(f"{x} + {std} = {x + std}")
    print(f"{x} - {std} = {x - std}")
    print(f"{x} * {std} = {x * std}")
    print(f"{x} / {std} = {x / std}")

    # -------------------------------------------------
    # Float Conversion
    # -------------------------------------------------
    heading("Float Conversion")

    print(f"float({x}) = {float(x)}")

    y = fraction.from_float(0.125)

    print(f"fraction.from_float(0.125) = {y}")

    # -------------------------------------------------
    # Decimal Conversion
    # -------------------------------------------------
    heading("Decimal Conversion")

    d = Decimal("2.75")

    z = fraction.from_decimal(d)

    print(f"Decimal value: {d}")
    print(f"Converted: {z}")

    # -------------------------------------------------
    # String Conversion
    # -------------------------------------------------
    heading("String Conversion")

    print(str(x))
    print(repr(x))

    s = "15/20"

    print(f"Input string: {s}")
    print(f"Parsed: {fraction.from_string(s)}")

    # -------------------------------------------------
    # Boolean Conversion
    # -------------------------------------------------
    heading("Boolean Conversion")

    print(bool(fraction(0, 3)))
    print(bool(fraction(5, 7)))

    # -------------------------------------------------
    # Integer Conversion
    # -------------------------------------------------
    heading("Integer Conversion")

    print(int(fraction(7, 3)))
    print(int(fraction(9, 2)))

    # -------------------------------------------------
    # Hashing
    # -------------------------------------------------
    heading("Hashing")

    numbers = {
        fraction(1, 2),
        fraction(2, 4),
        fraction(3, 4),
    }

    print(numbers)

    # -------------------------------------------------
    # Sorting
    # -------------------------------------------------
    heading("Sorting")

    values = [
        fraction(5, 7),
        fraction(1, 3),
        fraction(9, 10),
        fraction(2, 5),
    ]

    print(sorted(values))

    # -------------------------------------------------
    # Dictionary Keys
    # -------------------------------------------------
    heading("Dictionary Usage")

    mapping = {
        fraction(1, 2): "Half",
        fraction(1, 3): "One Third",
        fraction(3, 4): "Three Quarters",
    }

    print(mapping)

    print(mapping[fraction(2, 4)])

    # -------------------------------------------------
    # Pickle Support
    # -------------------------------------------------
    heading("Pickle Serialization")

    data = pickle.dumps(x)

    restored = pickle.loads(data)

    print(restored)

    print(restored == x)

    # -------------------------------------------------
    # Tuple Representation
    # -------------------------------------------------
    heading("Tuple Representation")

    print(x.as_tuple())

    print("\nInteroperability demonstration completed successfully.")


if __name__ == "__main__":
    main()

