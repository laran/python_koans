"""``itertools``: composable iterator algorithms."""

from runner.koan import Koan, __


class AboutItertools(Koan):

    def test_count(self):
        from itertools import count, islice
        # ``count`` is infinite; pair it with islice or take.
        self.assertEqual(__, list(islice(count(10, 2), 4)))

    def test_cycle(self):
        from itertools import cycle, islice
        self.assertEqual(__, list(islice(cycle("AB"), 5)))

    def test_repeat(self):
        from itertools import repeat
        self.assertEqual(__, list(repeat("x", 3)))

    def test_chain(self):
        from itertools import chain
        self.assertEqual(__, list(chain([1, 2], [3, 4], [5])))

    def test_chain_from_iterable(self):
        from itertools import chain
        self.assertEqual(__, list(chain.from_iterable([[1, 2], [3, 4]])))

    def test_islice(self):
        from itertools import islice
        self.assertEqual(__, list(islice(range(10), 2, 8, 2)))

    def test_takewhile(self):
        from itertools import takewhile
        self.assertEqual(__, list(takewhile(lambda n: n < 5, [1, 4, 6, 3, 8])))

    def test_dropwhile(self):
        from itertools import dropwhile
        self.assertEqual(__, list(dropwhile(lambda n: n < 5, [1, 4, 6, 3, 8])))

    def test_groupby(self):
        from itertools import groupby
        # groupby groups consecutive equal items.
        items = "aaabbcddd"
        result = [(k, "".join(g)) for k, g in groupby(items)]
        self.assertEqual(__, result)

    def test_product(self):
        from itertools import product
        self.assertEqual(__, list(product([1, 2], "AB")))

    def test_permutations(self):
        from itertools import permutations
        self.assertEqual(__, list(permutations([1, 2, 3], 2)))

    def test_combinations(self):
        from itertools import combinations
        self.assertEqual(__, list(combinations([1, 2, 3, 4], 2)))

    def test_pairwise(self):
        from itertools import pairwise
        # ``pairwise`` (3.10+): consecutive overlapping pairs.
        self.assertEqual(__, list(pairwise([1, 2, 3, 4])))

    def test_accumulate(self):
        from itertools import accumulate
        self.assertEqual(__, list(accumulate([1, 2, 3, 4])))
