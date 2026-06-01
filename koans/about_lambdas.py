"""Lambdas are tiny anonymous functions. One expression. No statements."""

from runner.koan import Koan, __


class AboutLambdas(Koan):

    def test_lambda_basics(self):
        double = lambda x: x * 2
        self.assertEqual(__, double(7))

    def test_lambda_with_multiple_args(self):
        add = lambda a, b: a + b
        self.assertEqual(__, add(3, 4))

    def test_lambda_in_sorted_key(self):
        words = ["apple", "fig", "banana"]
        self.assertEqual(__, sorted(words, key=lambda w: len(w)))

    def test_lambda_in_max(self):
        pairs = [(1, "a"), (3, "b"), (2, "c")]
        self.assertEqual(__, max(pairs, key=lambda p: p[0]))

    def test_lambda_default_argument(self):
        # Default args work in lambdas, too — useful to capture loop vars.
        funcs = [lambda x, n=i: x + n for i in range(3)]
        self.assertEqual(__, [f(10) for f in funcs])

    def test_lambdas_are_just_functions(self):
        identity = lambda x: x
        self.assertEqual(__, identity.__name__)
        self.assertEqual(__, callable(identity))

    def test_lambda_only_takes_an_expression(self):
        # No statements allowed. Conditional expressions are fine.
        sign = lambda n: "negative" if n < 0 else "zero" if n == 0 else "positive"
        self.assertEqual(__, sign(-5))
        self.assertEqual(__, sign(0))
        self.assertEqual(__, sign(7))
