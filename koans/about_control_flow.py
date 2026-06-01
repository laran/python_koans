"""Control flow: if/elif/else, while, for, break, continue, else-on-loops."""

from runner.koan import Koan, __


class AboutControlFlow(Koan):

    def test_if_elif_else(self):
        def grade(score):
            if score >= 90:
                return "A"
            elif score >= 80:
                return "B"
            elif score >= 70:
                return "C"
            else:
                return "F"

        self.assertEqual(__, grade(95))
        self.assertEqual(__, grade(82))
        self.assertEqual(__, grade(50))

    def test_ternary_expression(self):
        x = 7
        parity = "odd" if x % 2 else "even"
        self.assertEqual(__, parity)

    def test_while_loop(self):
        n, total = 1, 0
        while n <= 5:
            total += n
            n += 1
        self.assertEqual(__, total)

    def test_for_loop_over_range(self):
        total = 0
        for n in range(1, 6):
            total += n
        self.assertEqual(__, total)

    def test_break_exits_the_loop(self):
        for n in range(10):
            if n == 3:
                break
        self.assertEqual(__, n)

    def test_continue_skips_the_rest_of_an_iteration(self):
        kept = []
        for n in range(5):
            if n % 2 == 0:
                continue
            kept.append(n)
        self.assertEqual(__, kept)

    def test_for_else_runs_when_no_break(self):
        # The ``else`` clause on a loop runs when the loop completes normally.
        result = "not found"
        for n in [1, 2, 3]:
            if n == 99:
                result = "found"
                break
        else:
            result = "exhausted"
        self.assertEqual(__, result)

    def test_for_else_does_not_run_after_break(self):
        result = "not found"
        for n in [1, 2, 3]:
            if n == 2:
                result = "found"
                break
        else:
            result = "exhausted"
        self.assertEqual(__, result)

    def test_enumerate(self):
        # enumerate gives (index, value) pairs.
        items = ["a", "b", "c"]
        self.assertEqual(__, list(enumerate(items)))

    def test_enumerate_with_start(self):
        items = ["a", "b", "c"]
        self.assertEqual(__, list(enumerate(items, start=1)))

    def test_zip_pairs_iterables(self):
        # zip stops at the shortest input.
        self.assertEqual(__, list(zip([1, 2, 3], ["a", "b", "c"])))
        self.assertEqual(__, list(zip([1, 2, 3], ["a"])))

    def test_zip_strict_raises_on_unequal_lengths(self):
        # ``strict=True`` (3.10+) requires inputs to be the same length.
        try:
            list(zip([1, 2, 3], ["a"], strict=True))
        except ValueError as e:
            self.assertEqual(__, type(e).__name__)

    def test_pass_does_nothing(self):
        # ``pass`` is a syntactic placeholder.
        def noop():
            pass
        self.assertEqual(__, noop())
