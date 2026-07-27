from __future__ import annotations

import math
import numbers
import types
from fractions import Fraction
from decimal import Decimal
from typing import Self, Any


class fraction(numbers.Rational):
    """
    Represents a mathematical fraction (Rational number).

    The fraction is strictly immutable and automatically reduced to its simplest form.
    It integrates seamlessly with Python's numeric tower.
    """

    __slots__ = ("_num", "_den")

    def __init__(self, numerator: int, denominator: int = 1) -> None:
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator must be integers.")

        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        g = math.gcd(numerator, denominator)
        
        self._num: int = numerator // g
        self._den: int = denominator // g

    @property
    def numerator(self) -> int:
        return self._num

    @property
    def denominator(self) -> int:
        return self._den

    # =====================================================
    # Alternative Constructors
    # =====================================================

    @classmethod
    def from_string(cls, s: str) -> Self:
        if not isinstance(s, str):
            raise TypeError(f"Argument must be a string, got {type(s).__name__}.")
            
        if not s or not s.strip():
            raise ValueError("String cannot be empty.")
            
        parts = s.split("/")
        if len(parts) == 1:
            return cls(int(parts[0].strip()), 1)
        if len(parts) == 2:
            return cls(int(parts[0].strip()), int(parts[1].strip()))
            
        raise ValueError(f"Invalid fraction string format: {s}")

    @classmethod
    def from_float(cls, f: float) -> Self:
        if not isinstance(f, float):
            raise TypeError(f"Argument must be a float, got {type(f).__name__}.")
            
        if math.isnan(f) or math.isinf(f):
            raise ValueError("Cannot convert NaN or Infinity to fraction.")
            
        n, d = f.as_integer_ratio()
        return cls(n, d)

    @classmethod
    def from_decimal(cls, dec: Decimal) -> Self:
        if not isinstance(dec, Decimal):
            raise TypeError(f"Argument must be a Decimal, got {type(dec).__name__}.")
            
        if not dec.is_finite():
            raise ValueError("Cannot convert NaN or Infinity to fraction.")
            
        n, d = dec.as_integer_ratio()
        return cls(n, d)

    # =====================================================
    # Magic Methods: Lifecycle & Representation
    # =====================================================

    def __str__(self) -> str:
        if self._den == 1:
            return str(self._num)
        return f"{self._num}/{self._den}"

    def __repr__(self) -> str:
        return f"fraction({self._num}, {self._den})"

    def __hash__(self) -> int:
        return hash(Fraction(self._num, self._den))

    def __bool__(self) -> bool:
        return self._num != 0

    def __reduce__(self) -> tuple[type, tuple[int, int]]:
        return self.__class__, (self._num, self._den)

    def __copy__(self) -> Self:
        return self

    def __deepcopy__(self, memo: dict[Any, Any]) -> Self:
        return self

    # =====================================================
    # Arithmetic Operators
    # =====================================================

    def __add__(self, other: Any) -> Self | Any:
        if isinstance(other, int):
            return self.__class__(self._num + other * self._den, self._den)
        if isinstance(other, (Fraction, fraction)):
            n = self._num * other.denominator + other.numerator * self._den
            d = self._den * other.denominator
            return self.__class__(n, d)
        return NotImplemented

    def __radd__(self, other: Any) -> Self | Any:
        return self + other

    def __sub__(self, other: Any) -> Self | Any:
        if isinstance(other, int):
            return self.__class__(self._num - other * self._den, self._den)
        if isinstance(other, (Fraction, fraction)):
            n = self._num * other.denominator - other.numerator * self._den
            d = self._den * other.denominator
            return self.__class__(n, d)
        return NotImplemented

    def __rsub__(self, other: Any) -> Self | Any:
        if isinstance(other, int):
            return self.__class__(other * self._den - self._num, self._den)
        return NotImplemented

    def __mul__(self, other: Any) -> Self | Any:
        if isinstance(other, int):
            return self.__class__(self._num * other, self._den)
        if isinstance(other, (Fraction, fraction)):
            return self.__class__(self._num * other.numerator, self._den * other.denominator)
        return NotImplemented

    def __rmul__(self, other: Any) -> Self | Any:
        return self * other

    def __truediv__(self, other: Any) -> Self | Any:
        if isinstance(other, int):
            if other == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return self.__class__(self._num, self._den * other)
        if isinstance(other, (Fraction, fraction)):
            if other.numerator == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return self.__class__(self._num * other.denominator, self._den * other.numerator)
        return NotImplemented

    def __rtruediv__(self, other: Any) -> Self | Any:
        if self._num == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        if isinstance(other, int):
            return self.__class__(other * self._den, self._num)
        return NotImplemented

    # =====================================================
    # Comparison Operators
    # =====================================================

    def __eq__(self, other: object) -> bool | types.NotImplementedType:
        if isinstance(other, int):
            return self._den == 1 and self._num == other
        if isinstance(other, (Fraction, fraction)):
            return self._num == other.numerator and self._den == other.denominator
        if isinstance(other, float):
            return float(self) == other
        return NotImplemented

    def __lt__(self, other: Any) -> bool | types.NotImplementedType:
        if isinstance(other, int):
            return self._num < other * self._den
        if isinstance(other, (Fraction, fraction)):
            return self._num * other.denominator < other.numerator * self._den
        if isinstance(other, float):
            return float(self) < other
        return NotImplemented

    def __le__(self, other: Any) -> bool | types.NotImplementedType:
        if isinstance(other, int):
            return self._num <= other * self._den
        if isinstance(other, (Fraction, fraction)):
            return self._num * other.denominator <= other.numerator * self._den
        if isinstance(other, float):
            return float(self) <= other
        return NotImplemented

    def __gt__(self, other: Any) -> bool | types.NotImplementedType:
        if isinstance(other, int):
            return self._num > other * self._den
        if isinstance(other, (Fraction, fraction)):
            return self._num * other.denominator > other.numerator * self._den
        if isinstance(other, float):
            return float(self) > other
        return NotImplemented

    def __ge__(self, other: Any) -> bool | types.NotImplementedType:
        if isinstance(other, int):
            return self._num >= other * self._den
        if isinstance(other, (Fraction, fraction)):
            return self._num * other.denominator >= other.numerator * self._den
        if isinstance(other, float):
            return float(self) >= other
        return NotImplemented

    # =====================================================
    # Unary & Power Operators
    # =====================================================

    def __abs__(self) -> Self:
        return self.__class__(abs(self._num), self._den)

    def __neg__(self) -> Self:
        return self.__class__(-self._num, self._den)

    def __pos__(self) -> Self:
        return self.__class__(self._num, self._den)

    def __pow__(self, power: Any) -> Self | Any:
        if not isinstance(power, int):
            return NotImplemented
            
        if power == 0:
            return self.__class__(1, 1)
        if power > 0:
            return self.__class__(self._num ** power, self._den ** power)
        
        if self._num == 0:
            raise ZeroDivisionError("Cannot raise zero fraction to a negative power.")
        
        abs_p = abs(power)
        return self.__class__(self._den ** abs_p, self._num ** abs_p)

    # =====================================================
    # Type Conversions & Formatting
    # =====================================================

    def __float__(self) -> float:
        return self._num / self._den

    def __int__(self) -> int:
        """Returns the integer part EXACTLY (truncating towards zero) avoiding floats."""
        res = abs(self._num) // self._den
        return res if self._num >= 0 else -res

    def __round__(self, ndigits: int | None = None) -> int | Self:
        res = round(Fraction(self._num, self._den), ndigits)
        if ndigits is None:
            return res
        return self.__class__(res.numerator, res.denominator)

    def __format__(self, format_spec: str) -> str:
        return format(Fraction(self._num, self._den), format_spec)

    # =====================================================
    # Utility Methods
    # =====================================================

    def reciprocal(self) -> Self:
        if self._num == 0:
            raise ZeroDivisionError("Zero has no reciprocal.")
        return self.__class__(self._den, self._num)

    def to_decimal(self, places: int = 2) -> float:
        if places < 0:
            raise ValueError("Places must be non-negative.")
        return round(float(self), places)
        
    def as_tuple(self) -> tuple[int, int]:
        return self._num, self._den

    def mixed(self) -> tuple[int, Self]:
        """
        Convert an improper fraction into a mixed number.
        
        For negative fractions where the whole part is non-zero, 
        the whole part carries the sign and the fractional part is positive 
        (e.g., -7/3 -> -2, 1/3). 
        If the whole part is zero, the fractional part carries the sign 
        (e.g., -1/3 -> 0, -1/3).
        """
        whole = abs(self._num) // self._den
        remainder = abs(self._num) % self._den
        
        if self._num < 0:
            if whole != 0:
                whole = -whole
            else:
                remainder = -remainder
                
        return whole, self.__class__(remainder, self._den)