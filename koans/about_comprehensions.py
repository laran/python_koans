"""List, set, and dict comprehensions: concise transformations of iterables."""

from runner.koan import Koan, __


class AboutComprehensions(Koan):

    def test_list_comprehension(self):
        squares = [n * n for n in range(5)]
        self.assertEqual(__, squares)

    def test_list_comprehension_with_filter(self):
        evens = [n for n in range(10) if n % 2 == 0]
        self.assertEqual(__, evens)

    def test_list_comprehension_with_expression(self):
        words = ["apple", "fig", "banana"]
        self.assertEqual(__, [w.upper() for w in words])

    def test_nested_list_comprehension(self):
        # Order: outer loop first.
        pairs = [(x, y) for x in range(2) for y in range(2)]
        self.assertEqual(__, pairs)

    def test_flattening_with_comprehension(self):
        rows = [[1, 2], [3, 4], [5, 6]]
        flat = [n for row in rows for n in row]
        self.assertEqual(__, flat)

    def test_set_comprehension(self):
        result = {c for c in "banana"}
        self.assertEqual(__, result)

    def test_dict_comprehension(self):
        result = {n: n * n for n in range(4)}
        self.assertEqual(__, result)

    def test_dict_comprehension_with_filter(self):
        result = {n: n * n for n in range(10) if n % 2}
        self.assertEqual(__, result)

    def test_inverting_a_dict_with_comprehension(self):
        d = {"a": 1, "b": 2, "c": 3}
        self.assertEqual(__, {v: k for k, v in d.items()})

    def test_generator_expression_uses_parens(self):
        # Generator expressions are lazy; they yield as you iterate.
        gen = (n * 2 for n in range(3))
        self.assertEqual(__, type(gen).__name__)
        self.assertEqual(__, list(gen))

    def test_passing_a_generator_to_a_function(self):
        # When passed alone to a single-argument call, the outer parens
        # can be elided.
        self.assertEqual(__, sum(n for n in range(5)))

    def test_walrus_inside_comprehension(self):
        data = [1, 4, 9, 16, 25]
        # ``:=`` lets you capture and use a value in one step.
        result = [(n, sq) for n in data if (sq := n * n) > 50]
        self.assertEqual(__, result)
