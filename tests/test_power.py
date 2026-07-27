"""
Tests for exponentiation.

Coverage:
- Positive powers
- Negative powers
- Zero power
- Zero fraction
- Invalid exponents
"""

import pytest

from fraction import fraction


class TestPositivePower:

    def test_power_one(self):
        assert fraction(2, 3) ** 1 == fraction(2, 3)

    def test_power_two(self):
        assert fraction(2, 3) ** 2 == fraction(4, 9)

    def test_power_three(self):
        assert fraction(2, 3) ** 3 == fraction(8, 27)

    def test_negative_fraction_even_power(self):
        assert fraction(-2, 3) ** 2 == fraction(4, 9)

    def test_negative_fraction_odd_power(self):
        assert fraction(-2, 3) ** 3 == fraction(-8, 27)

    def test_integer_fraction(self):
        assert fraction(5, 1) ** 2 == fraction(25, 1)


class TestZeroPower:

    def test_fraction_zero_power(self):
        assert fraction(2, 3) ** 0 == fraction(1, 1)

    def test_negative_fraction_zero_power(self):
        assert fraction(-5, 7) ** 0 == fraction(1, 1)

    def test_zero_fraction_zero_power(self):
        assert fraction(0, 1) ** 0 == fraction(1, 1)


class TestNegativePower:

    def test_negative_one(self):
        assert fraction(2, 3) ** -1 == fraction(3, 2)

    def test_negative_two(self):
        assert fraction(2, 3) ** -2 == fraction(9, 4)

    def test_negative_fraction(self):
        assert fraction(-2, 3) ** -1 == fraction(-3, 2)

    def test_negative_fraction_even(self):
        assert fraction(-2, 3) ** -2 == fraction(9, 4)

    def test_integer_fraction(self):
        assert fraction(5, 1) ** -1 == fraction(1, 5)


class TestZeroFraction:

    def test_zero_positive_power(self):
        assert fraction(0, 1) ** 5 == fraction(0, 1)

    def test_zero_negative_power(self):
        with pytest.raises(ZeroDivisionError):
            fraction(0, 1) ** -1


class TestLargePowers:

    def test_large_positive_power(self):
        assert fraction(2, 5) ** 6 == fraction(64, 15625)

    def test_large_negative_power(self):
        assert fraction(2, 5) ** -3 == fraction(125, 8)


class TestInvalidPower:

    @pytest.mark.parametrize(
        "value",
        [
            2.5,
            "2",
            None,
            object(),
            [],
            {},
            complex(2, 0),
        ],
    )
    def test_invalid_exponent(self, value):
        with pytest.raises(TypeError):
            fraction(2, 3) ** value


class TestPowerIdentity:

    def test_power_then_inverse(self):
        f = fraction(3, 5)

        assert (f**2) ** -1 == fraction(25, 9)

    def test_inverse_then_power(self):
        f = fraction(3, 5)

        assert (f**-1) ** 2 == fraction(25, 9)

    def test_power_preserves_type(self):
        result = fraction(4, 7) ** 3

        assert isinstance(result, fraction)

    def test_negative_power_preserves_type(self):
        result = fraction(4, 7) ** -3

        assert isinstance(result, fraction)


class TestPowerEdgeCases:

    def test_one_power_large(self):
        assert fraction(1, 1) ** 100 == fraction(1, 1)

    def test_minus_one_even(self):
        assert fraction(-1, 1) ** 100 == fraction(1, 1)

    def test_minus_one_odd(self):
        assert fraction(-1, 1) ** 101 == fraction(-1, 1)

    def test_denominator_growth(self):
        result = fraction(1, 2) ** 10

        assert result == fraction(1, 1024)
