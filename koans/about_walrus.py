"""The walrus operator ``:=`` (PEP 572): assignment within an expression."""

from runner.koan import Koan, __


class AboutWalrus(Koan):

    def test_walrus_in_if(self):
        # Capture and test in one step.
        data = "hello world"
        if (n := len(data)) > 5:
            result = n
        else:
            result = 0
        self.assertEqual(__, result)

    def test_walrus_in_while(self):
        # Useful for read-until-sentinel loops.
        source = iter([1, 2, 3, 0, 99])
        seen = []
        while (n := next(source)) != 0:
            seen.append(n)
        self.assertEqual(__, seen)

    def test_walrus_in_comprehension(self):
        # Compute once, use twice.
        words = ["hi", "hello", "world", "ok"]
        long_lengths = [n for w in words if (n := len(w)) > 2]
        self.assertEqual(__, long_lengths)

    def test_walrus_returns_the_assigned_value(self):
        # ``(x := 5)`` both assigns x and evaluates to 5.
        result = (x := 5) + 1
        self.assertEqual(__, x)
        self.assertEqual(__, result)
