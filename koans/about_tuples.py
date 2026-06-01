"""Tuples are immutable, ordered sequences. Use them for records of fixed shape."""

from runner.koan import Koan, __


class AboutTuples(Koan):

    def test_creating_tuples(self):
        t = (1, 2, 3)
        self.assertEqual(__, len(t))
        self.assertEqual(__, isinstance(t, tuple))

    def test_parentheses_are_optional(self):
        # It's the comma, not the parens, that makes a tuple.
        t = 1, 2, 3
        self.assertEqual(__, isinstance(t, tuple))

    def test_one_element_tuple_needs_a_trailing_comma(self):
        not_a_tuple = (1)
        a_tuple = (1,)
        self.assertEqual(__, isinstance(not_a_tuple, tuple))
        self.assertEqual(__, isinstance(a_tuple, tuple))

    def test_empty_tuple(self):
        empty = ()
        self.assertEqual(__, len(empty))

    def test_tuples_are_immutable(self):
        t = (1, 2, 3)
        try:
            t[0] = 99
        except TypeError as e:
            self.assertEqual(__, type(e).__name__)

    def test_tuple_unpacking(self):
        x, y = (10, 20)
        self.assertEqual(__, x)
        self.assertEqual(__, y)

    def test_swap_with_tuples(self):
        # The pythonic swap.
        a, b = 1, 2
        a, b = b, a
        self.assertEqual(__, a)
        self.assertEqual(__, b)

    def test_tuples_can_be_concatenated(self):
        self.assertEqual(__, (1, 2) + (3, 4))

    def test_tuples_can_be_repeated(self):
        self.assertEqual(__, (1, 2) * 3)

    def test_tuples_are_hashable(self):
        # Hashable means usable as dict keys or set members.
        d = {(1, 2): "point"}
        self.assertEqual(__, d[(1, 2)])

    def test_named_tuple(self):
        from collections import namedtuple
        Point = namedtuple("Point", ["x", "y"])
        p = Point(3, 4)
        self.assertEqual(__, p.x)
        self.assertEqual(__, p.y)
        # named tuples are still tuples.
        self.assertEqual(__, p[0])
        self.assertEqual(__, tuple(p))

    def test_named_tuple_unpacks_like_a_tuple(self):
        from collections import namedtuple
        Point = namedtuple("Point", ["x", "y"])
        p = Point(3, 4)
        x, y = p
        self.assertEqual(__, x + y)
