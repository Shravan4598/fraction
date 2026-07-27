"""
Tests for edge cases.

Coverage:
- Zero numerator
- Zero denominator
- Large integers
- Sign normalization
- Invalid constructor arguments
- Interoperability
- Mathematical invariants
"""

from fractions import Fraction

import pytest

from fraction import fraction


class TestConstructorEdgeCases:

    def test_zero_numerator(self):
        assert fraction(0, 5) == fraction(0, 1)

    def test_zero_denominator(self):
        with pytest.raises(ZeroDivisionError):
            fraction(1, 0)

    @pytest.mark.parametrize(
        "num, den",
        [
            (1.5, 2),
            (1, 2.5),
            ("1", 2),
            (1, "2"),
            (None, 1),
            (1, None),
            ([], 2),
            (1, {}),
        ],
    )
    def test_invalid_constructor_types(self, num, den):
        with pytest.raises(TypeError):
            fraction(num, den)


class TestNormalization:

    def test_common_factor(self):
        assert fraction(20, 30) == fraction(2, 3)

    def test_negative_denominator(self):
        assert fraction(1, -2) == fraction(-1, 2)

    def test_both_negative(self):
        assert fraction(-2, -4) == fraction(1, 2)

    def test_zero_negative_denominator(self):
        assert fraction(0, -5) == fraction(0, 1)


class TestLargeIntegers:

    def test_large_fraction(self):
        f = fraction(10**30, 10**25)

        assert f == fraction(100000, 1)

    def test_large_power(self):
        f = fraction(10**20, 10**10)

        assert int(f) == 10**10


class TestInteroperability:

    def test_std_fraction_add(self):
        result = fraction(1, 2) + Fraction(1, 4)

        assert result == fraction(3, 4)

    def test_std_fraction_sub(self):
        result = fraction(3, 4) - Fraction(1, 2)

        assert result == fraction(1, 4)

    def test_std_fraction_mul(self):
        result = fraction(2, 3) * Fraction(3, 5)

        assert result == fraction(2, 5)

    def test_std_fraction_div(self):
        result = fraction(2, 3) / Fraction(4, 5)

        assert result == fraction(5, 6)

    def test_compare_std_fraction(self):
        assert fraction(2, 3) == Fraction(2, 3)


class TestMathematicalProperties:

    def test_additive_identity(self):
        f = fraction(5, 7)

        assert f + fraction(0) == f

    def test_multiplicative_identity(self):
        f = fraction(5, 7)

        assert f * fraction(1) == f

    def test_additive_inverse(self):
        f = fraction(8, 9)

        assert f + (-f) == fraction(0)

    def test_divide_by_self(self):
        f = fraction(9, 11)

        assert f / f == fraction(1)

    def test_reciprocal_identity(self):
        f = fraction(9, 11)

        assert f.reciprocal().reciprocal() == f


class TestBoundaryCases:

    def test_one(self):
        assert fraction(1, 1) == 1

    def test_minus_one(self):
        assert fraction(-1, 1) == -1

    def test_zero(self):
        assert fraction(0, 100) == fraction(0, 1)

    def test_unit_fraction(self):
        assert fraction(1, 999999999) == fraction(1, 999999999)

    def test_negative_unit_fraction(self):
        assert fraction(-1, 999999999) == fraction(-1, 999999999)


class TestUnsupportedOperations:

    @pytest.mark.parametrize(
        "value",
        [
            complex(1, 2),
            object(),
            [],
            {},
            "abc",
        ],
    )
    def test_arithmetic(self, value):
        with pytest.raises(TypeError):
            _ = fraction(1, 2) + value

    @pytest.mark.parametrize(
        "value",
        [
            complex(1, 2),
            object(),
            [],
            {},
            "abc",
        ],
    )
    def test_comparison(self, value):
        with pytest.raises(TypeError):
            _ = fraction(1, 2) < value