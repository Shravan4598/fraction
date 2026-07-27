"""
Tests for comparison operators.

Coverage:
- ==
- !=
- <
- <=
- >
- >=
- Comparisons with int
- Comparisons with float
- Comparisons with fractions.Fraction
- Sorting
"""

from fractions import Fraction

import pytest

from fraction import fraction


class TestEquality:

    def test_equal_fraction(self):
        assert fraction(1, 2) == fraction(2, 4)

    def test_not_equal_fraction(self):
        assert fraction(1, 2) != fraction(3, 4)

    def test_equal_integer(self):
        assert fraction(5, 1) == 5

    def test_not_equal_integer(self):
        assert fraction(5, 2) != 2

    def test_equal_float(self):
        assert fraction(1, 2) == 0.5

    def test_not_equal_float(self):
        assert fraction(1, 2) != 0.75

    def test_equal_std_fraction(self):
        assert fraction(2, 3) == Fraction(2, 3)

    def test_not_equal_std_fraction(self):
        assert fraction(2, 3) != Fraction(3, 4)


class TestLessThan:

    def test_fraction(self):
        assert fraction(1, 3) < fraction(1, 2)

    def test_integer(self):
        assert fraction(3, 2) < 2

    def test_float(self):
        assert fraction(1, 2) < 0.75

    def test_std_fraction(self):
        assert fraction(1, 3) < Fraction(1, 2)


class TestLessEqual:

    def test_equal(self):
        assert fraction(1, 2) <= fraction(2, 4)

    def test_less(self):
        assert fraction(1, 3) <= fraction(1, 2)

    def test_integer(self):
        assert fraction(2, 1) <= 2

    def test_float(self):
        assert fraction(1, 2) <= 0.5


class TestGreaterThan:

    def test_fraction(self):
        assert fraction(5, 6) > fraction(3, 4)

    def test_integer(self):
        assert fraction(5, 2) > 2

    def test_float(self):
        assert fraction(3, 4) > 0.5

    def test_std_fraction(self):
        assert fraction(5, 6) > Fraction(3, 4)


class TestGreaterEqual:

    def test_equal(self):
        assert fraction(2, 4) >= fraction(1, 2)

    def test_greater(self):
        assert fraction(3, 4) >= fraction(1, 2)

    def test_integer(self):
        assert fraction(5, 1) >= 5

    def test_float(self):
        assert fraction(1, 2) >= 0.5


class TestSorting:

    def test_sorted(self):
        values = [
            fraction(3, 4),
            fraction(1, 2),
            fraction(1, 3),
            fraction(5, 6),
        ]

        expected = [
            fraction(1, 3),
            fraction(1, 2),
            fraction(3, 4),
            fraction(5, 6),
        ]

        assert sorted(values) == expected

    def test_min(self):
        values = [
            fraction(2, 3),
            fraction(1, 5),
            fraction(4, 7),
        ]

        assert min(values) == fraction(1, 5)

    def test_max(self):
        values = [
            fraction(2, 3),
            fraction(1, 5),
            fraction(4, 7),
        ]

        assert max(values) == fraction(2, 3)


class TestUnsupportedComparisons:

    @pytest.mark.parametrize(
        "value",
        [
            "abc",
            [],
            {},
            object(),
            complex(1, 2),
        ],
    )
    def test_eq(self, value):
        assert (fraction(1, 2) == value) is False

    @pytest.mark.parametrize(
        "value",
        [
            "abc",
            [],
            {},
            object(),
            complex(1, 2),
        ],
    )
    def test_lt(self, value):
        with pytest.raises(TypeError):
            fraction(1, 2) < value

    @pytest.mark.parametrize(
        "value",
        [
            "abc",
            [],
            {},
            object(),
            complex(1, 2),
        ],
    )
    def test_le(self, value):
        with pytest.raises(TypeError):
            fraction(1, 2) <= value

    @pytest.mark.parametrize(
        "value",
        [
            "abc",
            [],
            {},
            object(),
            complex(1, 2),
        ],
    )
    def test_gt(self, value):
        with pytest.raises(TypeError):
            fraction(1, 2) > value

    @pytest.mark.parametrize(
        "value",
        [
            "abc",
            [],
            {},
            object(),
            complex(1, 2),
        ],
    )
    def test_ge(self, value):
        with pytest.raises(TypeError):
            fraction(1, 2) >= value