"""
Tests for arithmetic operators.

Coverage:
- Addition
- Subtraction
- Multiplication
- Division
- Reverse operators
- Operations with int
- Operations with fractions.Fraction
- Simplification
- Zero division
"""

from fractions import Fraction

import pytest

from fraction import fraction


class TestAddition:

    def test_fraction_plus_fraction(self):
        assert fraction(1, 2) + fraction(1, 3) == fraction(5, 6)

    def test_fraction_plus_int(self):
        assert fraction(3, 2) + 2 == fraction(7, 2)

    def test_int_plus_fraction(self):
        assert 2 + fraction(3, 2) == fraction(7, 2)

    def test_fraction_plus_std_fraction(self):
        result = fraction(1, 2) + Fraction(1, 3)
        assert result == fraction(5, 6)

    def test_addition_simplifies(self):
        assert fraction(1, 6) + fraction(2, 6) == fraction(1, 2)


class TestSubtraction:

    def test_fraction_minus_fraction(self):
        assert fraction(3, 4) - fraction(1, 4) == fraction(1, 2)

    def test_fraction_minus_int(self):
        assert fraction(5, 2) - 2 == fraction(1, 2)

    def test_int_minus_fraction(self):
        assert 3 - fraction(1, 2) == fraction(5, 2)

    def test_fraction_minus_std_fraction(self):
        result = fraction(3, 4) - Fraction(1, 4)
        assert result == fraction(1, 2)


class TestMultiplication:

    def test_fraction_times_fraction(self):
        assert fraction(2, 3) * fraction(3, 5) == fraction(2, 5)

    def test_fraction_times_int(self):
        assert fraction(2, 3) * 3 == fraction(2, 1)

    def test_int_times_fraction(self):
        assert 3 * fraction(2, 3) == fraction(2, 1)

    def test_fraction_times_std_fraction(self):
        result = fraction(2, 3) * Fraction(3, 5)
        assert result == fraction(2, 5)


class TestDivision:

    def test_fraction_div_fraction(self):
        assert fraction(2, 3) / fraction(4, 5) == fraction(5, 6)

    def test_fraction_div_int(self):
        assert fraction(3, 4) / 2 == fraction(3, 8)

    def test_int_div_fraction(self):
        assert 2 / fraction(3, 4) == fraction(8, 3)

    def test_fraction_div_std_fraction(self):
        result = fraction(2, 3) / Fraction(4, 5)
        assert result == fraction(5, 6)


class TestZeroDivision:

    def test_divide_by_zero_int(self):
        with pytest.raises(ZeroDivisionError):
            fraction(1, 2) / 0

    def test_divide_by_zero_fraction(self):
        with pytest.raises(ZeroDivisionError):
            fraction(1, 2) / fraction(0, 1)

    def test_reverse_division_zero(self):
        with pytest.raises(ZeroDivisionError):
            5 / fraction(0, 1)


class TestSimplification:

    def test_result_is_reduced(self):
        assert fraction(2, 4) + fraction(2, 4) == fraction(1, 1)

    def test_negative_result(self):
        assert fraction(1, 3) - fraction(2, 3) == fraction(-1, 3)

    def test_zero_result(self):
        assert fraction(5, 7) - fraction(5, 7) == fraction(0, 1)


class TestUnsupportedTypes:

    @pytest.mark.parametrize(
        "value",
        [
            "abc",
            2.5,
            complex(1, 2),
            object(),
            [],
            {},
        ],
    )
    def test_add_not_supported(self, value):
        with pytest.raises(TypeError):
            _ = fraction(1, 2) + value

    @pytest.mark.parametrize(
        "value",
        [
            "abc",
            2.5,
            complex(1, 2),
            object(),
            [],
            {},
        ],
    )
    def test_sub_not_supported(self, value):
        with pytest.raises(TypeError):
            _ = fraction(1, 2) - value

    @pytest.mark.parametrize(
        "value",
        [
            "abc",
            2.5,
            complex(1, 2),
            object(),
            [],
            {},
        ],
    )
    def test_mul_not_supported(self, value):
        with pytest.raises(TypeError):
            _ = fraction(1, 2) * value

    @pytest.mark.parametrize(
        "value",
        [
            "abc",
            2.5,
            complex(1, 2),
            object(),
            [],
            {},
        ],
    )
    def test_div_not_supported(self, value):
        with pytest.raises(TypeError):
            _ = fraction(1, 2) / value
