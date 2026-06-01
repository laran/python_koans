"""``functools``: tools for higher-order functions."""

from runner.koan import Koan, __


class AboutFunctools(Koan):

    def test_partial(self):
        from functools import partial
        def divide(a, b):
            return a / b
        halve = partial(divide, b=2)
        self.assertEqual(__, halve(10))

    def test_partial_freezing_first_argument(self):
        from functools import partial
        def power(base, exponent):
            return base ** exponent
        square = partial(power, exponent=2)
        cube = partial(power, exponent=3)
        self.assertEqual(__, square(5))
        self.assertEqual(__, cube(3))

    def test_reduce(self):
        from functools import reduce
        self.assertEqual(__, reduce(lambda a, b: a + b, [1, 2, 3, 4]))

    def test_reduce_with_initial(self):
        from functools import reduce
        self.assertEqual(__, reduce(lambda a, b: a + b, [1, 2, 3], 100))

    def test_lru_cache(self):
        from functools import lru_cache
        calls = []

        @lru_cache(maxsize=None)
        def slow(n):
            calls.append(n)
            return n * n

        slow(3)
        slow(3)
        slow(3)
        # Body ran only once.
        self.assertEqual(__, calls)

    def test_cache_decorator(self):
        from functools import cache

        @cache
        def fib(n):
            return n if n < 2 else fib(n - 1) + fib(n - 2)

        # Without caching this would be exponential.
        self.assertEqual(__, fib(20))

    def test_wraps_preserves_metadata(self):
        from functools import wraps

        def announce(fn):
            @wraps(fn)
            def wrapper(*a, **k):
                return fn(*a, **k)
            return wrapper

        @announce
        def hi():
            """say hi"""
            return "hi"

        self.assertEqual(__, hi.__name__)
        self.assertEqual(__, hi.__doc__)

    def test_singledispatch(self):
        from functools import singledispatch

        @singledispatch
        def describe(x):
            return "unknown"

        @describe.register
        def _(x: int):
            return "an int"

        @describe.register
        def _(x: str):
            return "a string"

        self.assertEqual(__, describe(42))
        self.assertEqual(__, describe("hi"))
        self.assertEqual(__, describe(3.14))
