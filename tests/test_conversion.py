"""
Tests for conversion methods and constructors.

Coverage:
- from_string()
- from_float()
- from_decimal()
- __str__()
- __repr__()
- __float__()
- __int__()
- __bool__()
- __format__()
- as_tuple()
- to_decimal()
"""

from decimal import Decimal

import pytest

from fraction import fraction


class TestFromString:

    def test_simple_fraction(self):
        assert fraction.from_string("3/4") == fraction(3, 4)

    def test_integer_string(self):
        assert fraction.from_string("5") == fraction(5, 1)

    def test_spaces(self):
        assert fraction.from_string("  6 / 8  ") == fraction(3, 4)

    def test_negative_fraction(self):
        assert fraction.from_string("-4/6") == fraction(-2, 3)

    @pytest.mark.parametrize(
        "value",
        [
            "",
            "   ",
            "1/2/3",
            "abc",
            "/2",
            "2/",
        ],
    )
    def test_invalid_strings(self, value):
        with pytest.raises((ValueError, TypeError)):
            fraction.from_string(value)

    @pytest.mark.parametrize(
        "value",
        [
            123,
            2.5,
            [],
            {},
            None,
        ],
    )
    def test_invalid_type(self, value):
        with pytest.raises(TypeError):
            fraction.from_string(value)


class TestFromFloat:

    def test_simple_float(self):
        assert fraction.from_float(0.5) == fraction(1, 2)

    def test_exact_float(self):
        assert fraction.from_float(0.125) == fraction(1, 8)

    def test_negative_float(self):
        assert fraction.from_float(-0.25) == fraction(-1, 4)

    @pytest.mark.parametrize(
        "value",
        [
            float("nan"),
            float("inf"),
            float("-inf"),
        ],
    )
    def test_invalid_float_values(self, value):
        with pytest.raises(ValueError):
            fraction.from_float(value)

    @pytest.mark.parametrize(
        "value",
        [
            1,
            "0.5",
            [],
            {},
            None,
        ],
    )
    def test_invalid_float_type(self, value):
        with pytest.raises(TypeError):
            fraction.from_float(value)


class TestFromDecimal:

    def test_decimal(self):
        assert fraction.from_decimal(Decimal("0.5")) == fraction(1, 2)

    def test_decimal_integer(self):
        assert fraction.from_decimal(Decimal("5")) == fraction(5, 1)

    def test_negative_decimal(self):
        assert fraction.from_decimal(Decimal("-2.75")) == fraction(-11, 4)

    @pytest.mark.parametrize(
        "value",
        [
            Decimal("NaN"),
            Decimal("Infinity"),
            Decimal("-Infinity"),
        ],
    )
    def test_invalid_decimal(self, value):
        with pytest.raises(ValueError):
            fraction.from_decimal(value)

    @pytest.mark.parametrize(
        "value",
        [
            1,
            2.5,
            "0.5",
            [],
            None,
        ],
    )
    def test_invalid_decimal_type(self, value):
        with pytest.raises(TypeError):
            fraction.from_decimal(value)


class TestConversions:

    def test_float(self):
        assert float(fraction(1, 2)) == 0.5

    def test_int_positive(self):
        assert int(fraction(7, 3)) == 2

    def test_int_negative(self):
        assert int(fraction(-7, 3)) == -2

    def test_bool_false(self):
        assert bool(fraction(0, 5)) is False

    def test_bool_true(self):
        assert bool(fraction(5, 7)) is True


class TestStringRepresentation:

    def test_str_fraction(self):
        assert str(fraction(3, 4)) == "3/4"

    def test_str_integer(self):
        assert str(fraction(5, 1)) == "5"

    def test_repr(self):
        assert repr(fraction(2, 3)) == "fraction(2, 3)"


class TestFormatting:

    def test_default_format(self):
        assert format(fraction(1, 2), "") == "1/2"

    def test_float_format(self):
        assert format(fraction(1, 4), ".2f") == "0.25"


class TestTuple:

    def test_as_tuple(self):
        assert fraction(7, 9).as_tuple() == (7, 9)


class TestToDecimal:

    def test_default_places(self):
        assert fraction(1, 3).to_decimal() == round(1 / 3, 2)

    def test_custom_places(self):
        assert fraction(1, 3).to_decimal(5) == round(1 / 3, 5)

    def test_zero_places(self):
        assert fraction(5, 2).to_decimal(0) == round(2.5, 0)

    def test_negative_places(self):
        with pytest.raises(ValueError):
            fraction(1, 2).to_decimal(-1)
