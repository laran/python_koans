"""Generators: lazy iterators built with ``yield``."""

from runner.koan import Koan, __


class AboutGenerators(Koan):

    def test_a_generator_function_returns_a_generator(self):
        def counter():
            yield 1
            yield 2
            yield 3
        g = counter()
        self.assertEqual(__, type(g).__name__)

    def test_generators_yield_one_at_a_time(self):
        def counter():
            yield 1
            yield 2
            yield 3
        g = counter()
        self.assertEqual(__, next(g))
        self.assertEqual(__, next(g))
        self.assertEqual(__, next(g))

    def test_generators_raise_stop_iteration_when_exhausted(self):
        def one_shot():
            yield 1
        g = one_shot()
        next(g)
        try:
            next(g)
        except StopIteration as e:
            self.assertEqual(__, type(e).__name__)

    def test_iterating_a_generator_with_for(self):
        def counter():
            yield 1
            yield 2
            yield 3
        self.assertEqual(__, [n for n in counter()])

    def test_generators_remember_state(self):
        def naturals():
            n = 0
            while True:
                yield n
                n += 1
        g = naturals()
        first_three = [next(g) for _ in range(3)]
        self.assertEqual(__, first_three)
        # Resume from where it left off.
        self.assertEqual(__, next(g))

    def test_generator_expression(self):
        # Built with parens, no need for a function.
        g = (n * 2 for n in range(3))
        self.assertEqual(__, list(g))

    def test_yield_from_delegates(self):
        def inner():
            yield 1
            yield 2
        def outer():
            yield 0
            yield from inner()
            yield 3
        self.assertEqual(__, list(outer()))

    def test_generators_are_lazy(self):
        log = []
        def trace():
            log.append("started")
            yield 1
            log.append("midway")
            yield 2
            log.append("done")

        g = trace()
        self.assertEqual(__, log)        # Nothing happens until iteration.
        next(g)
        self.assertEqual(__, log)        # Just the first chunk.
        next(g)
        self.assertEqual(__, log)        # Second chunk.

    def test_send_passes_a_value_back_in(self):
        def echo():
            while True:
                received = yield
                yield received * 2

        g = echo()
        next(g)                          # advance to the first ``yield``.
        self.assertEqual(__, g.send(5))
