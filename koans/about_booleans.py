"""``True`` and ``False`` are the gates of conditional thought.

Many values double as truth values: empty strings, empty containers, and
zeroes are all "falsy". Everything else is "truthy".
"""

from runner.koan import Koan, __


class AboutBooleans(Koan):

    def test_true_and_false_are_singletons(self):
        self.assertEqual(__, True is True)
        self.assertEqual(__, False is False)

    def test_booleans_are_ints(self):
        # bool is a subclass of int. True acts like 1, False acts like 0.
        self.assertEqual(__, True + True)
        self.assertEqual(__, True + False)
        self.assertEqual(__, isinstance(True, int))

    def test_empty_string_is_falsy(self):
        self.assertEqual(__, bool(""))

    def test_non_empty_string_is_truthy(self):
        self.assertEqual(__, bool("x"))

    def test_zero_is_falsy(self):
        self.assertEqual(__, bool(0))
        self.assertEqual(__, bool(0.0))

    def test_empty_list_is_falsy(self):
        self.assertEqual(__, bool([]))

    def test_empty_dict_is_falsy(self):
        self.assertEqual(__, bool({}))

    def test_none_is_falsy(self):
        self.assertEqual(__, bool(None))

    def test_and_returns_the_first_falsy_or_the_last_value(self):
        # ``and`` short-circuits and returns operands, not just True/False.
        self.assertEqual(__, "a" and "b")
        self.assertEqual(__, "" and "b")
        self.assertEqual(__, 0 and 1)

    def test_or_returns_the_first_truthy_or_the_last_value(self):
        self.assertEqual(__, "a" or "b")
        self.assertEqual(__, "" or "b")
        self.assertEqual(__, None or 0 or "default")

    def test_not_inverts_truthiness(self):
        self.assertEqual(__, not True)
        self.assertEqual(__, not "")
        self.assertEqual(__, not [1])
