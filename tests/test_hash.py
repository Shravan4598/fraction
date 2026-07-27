"""
Tests for hashing, equality consistency, copying, and pickling.

Coverage:
- __hash__()
- Equality/hash contract
- Dictionary keys
- Set behavior
- Copy
- Deep copy
- Pickling
"""

import copy
import pickle
from fractions import Fraction

from fraction import fraction


class TestHashEquality:

    def test_equal_objects_have_same_hash(self):
        f1 = fraction(1, 2)
        f2 = fraction(2, 4)

        assert f1 == f2
        assert hash(f1) == hash(f2)

    def test_equal_to_std_fraction(self):
        f = fraction(3, 4)
        std = Fraction(3, 4)

        assert hash(f) == hash(std)

    def test_hash_is_stable(self):
        f = fraction(7, 9)

        h1 = hash(f)
        h2 = hash(f)
        h3 = hash(f)

        assert h1 == h2 == h3

    def test_different_fractions_have_different_hashes(self):
        assert hash(fraction(1, 2)) != hash(fraction(2, 3))


class TestDictionaryBehavior:

    def test_lookup_using_equivalent_fraction(self):
        d = {fraction(1, 2): "half"}

        assert d[fraction(2, 4)] == "half"

    def test_overwrite_equivalent_key(self):
        d = {}

        d[fraction(1, 2)] = "first"
        d[fraction(2, 4)] = "second"

        assert len(d) == 1
        assert d[fraction(1, 2)] == "second"

    def test_multiple_keys(self):
        d = {
            fraction(1, 2): "a",
            fraction(2, 3): "b",
            fraction(3, 4): "c",
        }

        assert d[fraction(1, 2)] == "a"
        assert d[fraction(2, 3)] == "b"
        assert d[fraction(3, 4)] == "c"


class TestSetBehavior:

    def test_duplicates_removed(self):
        s = {
            fraction(1, 2),
            fraction(2, 4),
            fraction(3, 6),
        }

        assert len(s) == 1

    def test_unique_values(self):
        s = {
            fraction(1, 2),
            fraction(2, 3),
            fraction(3, 4),
        }

        assert len(s) == 3

    def test_membership(self):
        s = {
            fraction(5, 7),
        }

        assert fraction(10, 14) in s


class TestCopyBehavior:

    def test_copy_returns_same_object(self):
        f = fraction(4, 5)

        assert copy.copy(f) is f

    def test_deepcopy_returns_same_object(self):
        f = fraction(4, 5)

        assert copy.deepcopy(f) is f


class TestPickleBehavior:

    def test_pickle_roundtrip(self):
        original = fraction(8, 11)

        restored = pickle.loads(pickle.dumps(original))

        assert restored == original
        assert hash(restored) == hash(original)

    def test_pickle_preserves_type(self):
        restored = pickle.loads(pickle.dumps(fraction(3, 8)))

        assert isinstance(restored, fraction)


class TestReduce:

    def test_reduce_reconstructs_object(self):
        f = fraction(13, 17)

        constructor, args = f.__reduce__()

        rebuilt = constructor(*args)

        assert rebuilt == f
        assert hash(rebuilt) == hash(f)


class TestHashProperties:

    def test_hash_after_operations(self):
        result = fraction(1, 3) + fraction(1, 6)

        assert result == fraction(1, 2)
        assert hash(result) == hash(fraction(1, 2))

    def test_hash_negative_fraction(self):
        assert hash(fraction(-2, 4)) == hash(fraction(-1, 2))

    def test_hash_zero(self):
        assert hash(fraction(0, 5)) == hash(fraction(0, 1))
