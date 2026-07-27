"""
Tests for utility methods and object behaviour.

Coverage:
- reciprocal()
- as_tuple()
- mixed()
- __hash__()
- __copy__()
- __deepcopy__()
- __reduce__()
- pickle support
- immutability
"""

import copy
import pickle

import pytest

from fraction import fraction


class TestAsTuple:

    def test_positive_fraction(self):
        assert fraction(3, 4).as_tuple() == (3, 4)

    def test_negative_fraction(self):
        assert fraction(-3, 4).as_tuple() == (-3, 4)

    def test_integer_fraction(self):
        assert fraction(5).as_tuple() == (5, 1)

    def test_zero_fraction(self):
        assert fraction(0, 10).as_tuple() == (0, 1)


class TestMixed:

    def test_positive_improper(self):
        whole, frac = fraction(7, 3).mixed()

        assert whole == 2
        assert frac == fraction(1, 3)

    def test_negative_improper(self):
        whole, frac = fraction(-7, 3).mixed()

        assert whole == -2
        assert frac == fraction(1, 3)

    def test_negative_proper(self):
        whole, frac = fraction(-1, 3).mixed()

        assert whole == 0
        assert frac == fraction(-1, 3)

    def test_positive_proper(self):
        whole, frac = fraction(1, 3).mixed()

        assert whole == 0
        assert frac == fraction(1, 3)

    def test_integer(self):
        whole, frac = fraction(5).mixed()

        assert whole == 5
        assert frac == fraction(0, 1)

    def test_zero(self):
        whole, frac = fraction(0).mixed()

        assert whole == 0
        assert frac == fraction(0, 1)


class TestHash:

    def test_equal_hash(self):
        assert hash(fraction(1, 2)) == hash(fraction(2, 4))

    def test_hash_dictionary(self):
        d = {fraction(1, 2): "half"}

        assert d[fraction(2, 4)] == "half"

    def test_hash_set(self):
        s = {fraction(1, 2), fraction(2, 4), fraction(3, 6)}

        assert len(s) == 1


class TestCopy:

    def test_copy(self):
        f = fraction(3, 4)

        assert copy.copy(f) is f

    def test_deepcopy(self):
        f = fraction(3, 4)

        assert copy.deepcopy(f) is f


class TestPickle:

    def test_pickle_roundtrip(self):
        f = fraction(7, 9)

        restored = pickle.loads(pickle.dumps(f))

        assert restored == f
        assert isinstance(restored, fraction)


class TestReduce:

    def test_reduce(self):
        f = fraction(5, 7)

        constructor, args = f.__reduce__()

        rebuilt = constructor(*args)

        assert rebuilt == f


class TestImmutability:

    def test_slots(self):
        f = fraction(1, 2)

        with pytest.raises(AttributeError):
            f.random_attribute = 100

    def test_numerator_readonly(self):
        f = fraction(3, 4)

        with pytest.raises(AttributeError):
            f.numerator = 10

    def test_denominator_readonly(self):
        f = fraction(3, 4)

        with pytest.raises(AttributeError):
            f.denominator = 10


class TestReciprocalProperties:

    def test_twice(self):
        f = fraction(8, 11)

        assert f.reciprocal().reciprocal() == f

    def test_product(self):
        f = fraction(8, 11)

        assert f * f.reciprocal() == fraction(1, 1)

    def test_negative(self):
        f = fraction(-8, 11)

        assert f.reciprocal() == fraction(-11, 8)

    def test_zero(self):
        with pytest.raises(ZeroDivisionError):
            fraction(0).reciprocal()
