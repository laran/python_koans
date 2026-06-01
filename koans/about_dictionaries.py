"""Dictionaries map hashable keys to arbitrary values. Insertion order is preserved."""

from runner.koan import Koan, __


class AboutDictionaries(Koan):

    def test_creating_dicts(self):
        empty = {}
        person = {"name": "Ada", "age": 36}
        self.assertEqual(__, len(empty))
        self.assertEqual(__, len(person))

    def test_dict_constructor(self):
        self.assertEqual(__, dict(a=1, b=2))
        self.assertEqual(__, dict([("a", 1), ("b", 2)]))

    def test_indexing_a_dict(self):
        d = {"x": 1, "y": 2}
        self.assertEqual(__, d["x"])

    def test_missing_key_raises(self):
        d = {"x": 1}
        try:
            d["missing"]
        except KeyError as e:
            self.assertEqual(__, type(e).__name__)

    def test_get_returns_default_on_missing(self):
        d = {"x": 1}
        self.assertEqual(__, d.get("missing"))
        self.assertEqual(__, d.get("missing", "fallback"))

    def test_setdefault(self):
        # setdefault returns the existing value or sets and returns the default.
        d = {"x": 1}
        self.assertEqual(__, d.setdefault("x", 99))
        self.assertEqual(__, d.setdefault("y", 5))
        self.assertEqual(__, d)

    def test_keys_values_items(self):
        d = {"a": 1, "b": 2}
        self.assertEqual(__, list(d.keys()))
        self.assertEqual(__, list(d.values()))
        self.assertEqual(__, list(d.items()))

    def test_iteration_yields_keys(self):
        d = {"a": 1, "b": 2}
        self.assertEqual(__, [k for k in d])

    def test_in_checks_keys_not_values(self):
        d = {"a": 1}
        self.assertEqual(__, "a" in d)
        self.assertEqual(__, 1 in d)

    def test_insertion_order_is_preserved(self):
        # Since Python 3.7, dicts remember insertion order.
        d = {}
        d["c"] = 1
        d["a"] = 2
        d["b"] = 3
        self.assertEqual(__, list(d.keys()))

    def test_update_merges(self):
        d = {"a": 1, "b": 2}
        d.update({"b": 99, "c": 3})
        self.assertEqual(__, d)

    def test_dict_union_with_pipe(self):
        # ``|`` returns a new merged dict; the right-hand side wins on conflicts.
        a = {"x": 1, "y": 2}
        b = {"y": 99, "z": 3}
        self.assertEqual(__, a | b)
        # The originals are unchanged.
        self.assertEqual(__, a)

    def test_dict_inplace_union(self):
        a = {"x": 1}
        a |= {"y": 2}
        self.assertEqual(__, a)

    def test_pop(self):
        d = {"a": 1, "b": 2}
        gone = d.pop("a")
        self.assertEqual(__, gone)
        self.assertEqual(__, d)

    def test_only_hashable_keys(self):
        # Lists are not hashable, so they cannot be keys.
        try:
            {[1, 2]: "nope"}
        except TypeError as e:
            self.assertEqual(__, type(e).__name__)

    def test_tuples_can_be_keys(self):
        d = {(0, 0): "origin", (1, 1): "diagonal"}
        self.assertEqual(__, d[(0, 0)])

    def test_dict_comprehension(self):
        squares = {n: n * n for n in range(4)}
        self.assertEqual(__, squares)
