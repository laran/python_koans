"""Functions are first-class. Arguments come in many flavors."""

from runner.koan import Koan, __


class AboutFunctions(Koan):

    def test_calling_a_function(self):
        def greet():
            return "hello"
        self.assertEqual(__, greet())

    def test_positional_arguments(self):
        def add(a, b):
            return a + b
        self.assertEqual(__, add(3, 4))

    def test_keyword_arguments(self):
        def divide(numerator, denominator):
            return numerator / denominator
        self.assertEqual(__, divide(denominator=2, numerator=10))

    def test_default_arguments(self):
        def greet(name, greeting="hello"):
            return f"{greeting}, {name}"
        self.assertEqual(__, greet("Ada"))
        self.assertEqual(__, greet("Ada", "hi"))

    def test_default_mutable_argument_pitfall(self):
        # A mutable default is created once and shared across calls.
        def append_to(item, target=[]):
            target.append(item)
            return target

        a = append_to(1)
        b = append_to(2)
        # b includes 1 because the same list is reused.
        self.assertEqual(__, b)

    def test_args_collects_extra_positional(self):
        def total(*nums):
            return sum(nums)
        self.assertEqual(__, total(1, 2, 3, 4))
        self.assertEqual(__, total())

    def test_kwargs_collects_extra_keyword(self):
        def describe(**fields):
            return sorted(fields.items())
        self.assertEqual(__, describe(name="Ada", age=36))

    def test_unpacking_into_a_call(self):
        def f(a, b, c):
            return (a, b, c)
        args = [1, 2, 3]
        self.assertEqual(__, f(*args))
        kwargs = {"a": 1, "b": 2, "c": 3}
        self.assertEqual(__, f(**kwargs))

    def test_keyword_only_arguments(self):
        # Anything after a bare ``*`` must be passed by keyword.
        def slice_it(items, *, start, end):
            return items[start:end]
        self.assertEqual(__, slice_it([1, 2, 3, 4, 5], start=1, end=4))

    def test_positional_only_arguments(self):
        # Anything before ``/`` must be passed positionally.
        def power(base, exponent, /):
            return base ** exponent
        self.assertEqual(__, power(2, 10))

    def test_functions_are_objects(self):
        def f():
            pass
        self.assertEqual(__, callable(f))
        self.assertEqual(__, isinstance(f, object))

    def test_functions_have_names(self):
        def f():
            pass
        self.assertEqual(__, f.__name__)

    def test_passing_functions_around(self):
        def double(x):
            return x * 2
        def apply(fn, value):
            return fn(value)
        self.assertEqual(__, apply(double, 7))

    def test_returning_functions(self):
        def make_adder(n):
            def add(x):
                return x + n
            return add

        add5 = make_adder(5)
        self.assertEqual(__, add5(10))

    def test_closures_capture_variables(self):
        def counter():
            count = 0
            def inc():
                nonlocal count
                count += 1
                return count
            return inc

        c = counter()
        c()
        c()
        self.assertEqual(__, c())

    def test_docstrings(self):
        def greet():
            """Return a friendly greeting."""
            return "hello"
        self.assertEqual(__, greet.__doc__)
