"""Sets: unordered collections of unique, hashable elements."""

from runner.koan import Koan, __


class AboutSets(Koan):

    def test_creating_sets(self):
        s = {1, 2, 3}
        self.assertEqual(__, len(s))

    def test_empty_set_braces_are_a_dict(self):
        # ``{}`` is an empty dict. For an empty set, use ``set()``.
        self.assertEqual(__, type({}).__name__)
        self.assertEqual(__, type(set()).__name__)

    def test_sets_deduplicate(self):
        self.assertEqual(__, len({1, 1, 2, 2, 3}))

    def test_set_from_iterable(self):
        self.assertEqual(__, set("banana"))

    def test_add_and_discard(self):
        s = {1, 2}
        s.add(3)
        self.assertEqual(__, s)
        s.discard(1)
        self.assertEqual(__, s)

    def test_discard_does_not_raise_on_missing(self):
        s = {1}
        s.discard(99)
        self.assertEqual(__, s)

    def test_remove_raises_on_missing(self):
        s = {1}
        try:
            s.remove(99)
        except KeyError as e:
            self.assertEqual(__, type(e).__name__)

    def test_union(self):
        a = {1, 2, 3}
        b = {3, 4, 5}
        self.assertEqual(__, a | b)
        self.assertEqual(__, a.union(b))

    def test_intersection(self):
        a = {1, 2, 3}
        b = {2, 3, 4}
        self.assertEqual(__, a & b)

    def test_difference(self):
        a = {1, 2, 3}
        b = {2, 3, 4}
        self.assertEqual(__, a - b)

    def test_symmetric_difference(self):
        a = {1, 2, 3}
        b = {2, 3, 4}
        self.assertEqual(__, a ^ b)

    def test_subset_and_superset(self):
        a = {1, 2}
        b = {1, 2, 3}
        self.assertEqual(__, a <= b)
        self.assertEqual(__, b >= a)
        self.assertEqual(__, a < b)  # strict subset

    def test_disjoint(self):
        self.assertEqual(__, {1, 2}.isdisjoint({3, 4}))

    def test_frozenset_is_hashable(self):
        # Regular sets are unhashable, but frozensets are not.
        fs = frozenset({1, 2, 3})
        d = {fs: "frozen"}
        self.assertEqual(__, d[fs])

    def test_set_comprehension(self):
        self.assertEqual(__, {n % 3 for n in range(10)})
