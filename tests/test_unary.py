"""
Tests for unary operators.

Coverage:
- __abs__
- __neg__
- __pos__
- reciprocal()
"""

import pytest

from fraction import fraction


class TestAbsolute:

    def test_positive_fraction(self):
        assert abs(fraction(3, 4)) == fraction(3, 4)

    def test_negative_fraction(self):
        assert abs(fraction(-3, 4)) == fraction(3, 4)

    def test_zero_fraction(self):
        assert abs(fraction(0, 5)) == fraction(0, 1)


class TestNegation:

    def test_positive_fraction(self):
        assert -fraction(3, 4) == fraction(-3, 4)

    def test_negative_fraction(self):
        assert -fraction(-3, 4) == fraction(3, 4)

    def test_zero_fraction(self):
        assert -fraction(0, 5) == fraction(0, 1)


class TestUnaryPlus:

    def test_positive_fraction(self):
        f = fraction(3, 4)
        assert +f == fraction(3, 4)

    def test_negative_fraction(self):
        f = fraction(-3, 4)
        assert +f == fraction(-3, 4)

    def test_returns_new_equal_object(self):
        f = fraction(5, 7)

        result = +f

        assert result == f
        assert result is not f


class TestReciprocal:

    def test_positive_fraction(self):
        assert fraction(2, 3).reciprocal() == fraction(3, 2)

    def test_negative_fraction(self):
        assert fraction(-2, 3).reciprocal() == fraction(-3, 2)

    def test_integer_fraction(self):
        assert fraction(5, 1).reciprocal() == fraction(1, 5)

    def test_fraction_one(self):
        assert fraction(1, 1).reciprocal() == fraction(1, 1)

    def test_reciprocal_twice(self):
        f = fraction(7, 9)

        assert f.reciprocal().reciprocal() == f

    def test_zero_fraction(self):
        with pytest.raises(ZeroDivisionError):
            fraction(0, 1).reciprocal()


class TestUnaryComposition:

    def test_abs_after_neg(self):
        assert abs(-fraction(5, 8)) == fraction(5, 8)

    def test_neg_after_abs(self):
        assert -abs(fraction(-5, 8)) == fraction(-5, 8)

    def test_pos_after_neg(self):
        assert +(-fraction(2, 3)) == fraction(-2, 3)

    def test_double_negative(self):
        assert -(-fraction(4, 9)) == fraction(4, 9)

    def test_positive_of_positive(self):
        assert +(+fraction(4, 9)) == fraction(4, 9)


class TestUnaryIdentity:

    def test_abs_is_positive(self):
        result = abs(fraction(-9, 10))

        assert result.numerator > 0
        assert result.denominator > 0

    def test_neg_preserves_denominator(self):
        f = fraction(7, 11)

        result = -f

        assert result.denominator == 11

    def test_pos_preserves_value(self):
        f = fraction(-8, 13)

        assert (+f).numerator == f.numerator
        assert (+f).denominator == f.denominator


class TestEdgeCases:

    def test_reciprocal_of_negative_one(self):
        assert fraction(-1, 1).reciprocal() == fraction(-1, 1)

    def test_abs_of_integer_fraction(self):
        assert abs(fraction(-7, 1)) == fraction(7, 1)

    def test_neg_zero(self):
        assert -fraction(0, 1) == fraction(0, 1)

    def test_pos_zero(self):
        assert +fraction(0, 1) == fraction(0, 1)