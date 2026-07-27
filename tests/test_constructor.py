"""
Tests for fraction constructor and initialization.
"""

import pytest

from fraction import fraction


class TestConstructor:
    """Tests related to object construction."""

    def test_create_positive_fraction(self):
        f = fraction(1, 2)

        assert f.num == 1
        assert f.den == 2

    def test_create_negative_numerator(self):
        f = fraction(-3, 5)

        assert f.num == -3
        assert f.den == 5

    def test_create_negative_denominator(self):
        f = fraction(3, -5)

        # denominator should always be positive
        assert f.num == -3
        assert f.den == 5

    def test_both_negative(self):
        f = fraction(-3, -5)

        assert f.num == 3
        assert f.den == 5

    def test_zero_numerator(self):
        f = fraction(0, 5)

        assert f.num == 0
        assert f.den == 1

    def test_fraction_is_simplified(self):
        f = fraction(20, 40)

        assert f.num == 1
        assert f.den == 2

    def test_large_values(self):
        f = fraction(1000000, 500000)

        assert f.num == 2
        assert f.den == 1

    def test_zero_denominator(self):
        with pytest.raises(ZeroDivisionError):
            fraction(1, 0)

    @pytest.mark.parametrize(
        "numerator, denominator",
        [
            ("1", 2),
            (1, "2"),
            (1.5, 2),
            (1, 2.5),
            (None, 2),
            (1, None),
            ([], 2),
            ({}, 2),
        ],
    )
    def test_invalid_types(self, numerator, denominator):
        with pytest.raises(TypeError):
            fraction(numerator, denominator)


class TestStringRepresentation:
    """Tests for __str__ and __repr__."""

    def test_str(self):
        assert str(fraction(1, 2)) == "1/2"

    def test_repr(self):
        assert repr(fraction(3, 4)) == "fraction(3, 4)"


class TestNormalization:
    """Tests for normalization rules."""

    @pytest.mark.parametrize(
        "n,d,expected",
        [
            (2, 4, "1/2"),
            (10, 100, "1/10"),
            (-2, 4, "-1/2"),
            (2, -4, "-1/2"),
            (-2, -4, "1/2"),
            (0, 10, "0/1"),
        ],
    )
    def test_normalization(self, n, d, expected):
        assert str(fraction(n, d)) == expected
