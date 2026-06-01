"""Anything with ``__iter__`` is iterable. Anything with ``__next__`` is an iterator."""

from runner.koan import Koan, __


class AboutIterators(Koan):

    def test_iter_returns_an_iterator(self):
        it = iter([1, 2, 3])
        self.assertEqual(__, type(it).__name__)

    def test_next_advances_the_iterator(self):
        it = iter([10, 20, 30])
        self.assertEqual(__, next(it))
        self.assertEqual(__, next(it))

    def test_next_with_default_avoids_stopiteration(self):
        it = iter([])
        self.assertEqual(__, next(it, "done"))

    def test_strings_are_iterable(self):
        self.assertEqual(__, list(iter("abc")))

    def test_dicts_iterate_over_keys(self):
        d = {"a": 1, "b": 2}
        self.assertEqual(__, list(iter(d)))

    def test_custom_iterator_via_dunder(self):
        class Countdown:
            def __init__(self, n):
                self.n = n
            def __iter__(self):
                return self
            def __next__(self):
                if self.n <= 0:
                    raise StopIteration
                self.n -= 1
                return self.n + 1

        self.assertEqual(__, list(Countdown(3)))

    def test_iterable_versus_iterator(self):
        # A list is iterable but is not its own iterator.
        items = [1, 2, 3]
        self.assertEqual(__, items is iter(items))
        # An iterator IS its own iterator.
        it = iter(items)
        self.assertEqual(__, it is iter(it))

    def test_iter_with_sentinel(self):
        # iter(callable, sentinel) calls until the sentinel is returned.
        nums = iter([1, 2, 0, 3, 4])
        stream = iter(lambda: next(nums), 0)
        self.assertEqual(__, list(stream))

    def test_reversed(self):
        self.assertEqual(__, list(reversed([1, 2, 3])))

    def test_chained_with_for(self):
        # for X in Y calls iter(Y) once and then __next__ repeatedly.
        seen = []
        for ch in "hi":
            seen.append(ch)
        self.assertEqual(__, seen)
