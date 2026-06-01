"""The journey begins. Every koan in this project is a test that currently
fails. Your task is to make it pass by replacing the placeholder ``__`` with
the right value.

Open this file in your editor, follow along, and replace each ``__`` below.
Then re-run ``python contemplate_koans.py``.
"""

from runner.koan import Koan, __


class AboutAsserts(Koan):

    def test_assert_truth(self):
        # The simplest koan: assert that something is true.
        # Replace ``False`` with ``True``.
        self.assertTrue(False, "This should be true — make it so.")

    def test_assert_with_a_message(self):
        # Messages help future-you understand why a test mattered.
        self.assertTrue(False, "If you see this, you have not made it true yet.")

    def test_fill_in_values(self):
        # Replace __ with the value that makes this true.
        self.assertEqual(__, 1 + 1)

    def test_assert_equality(self):
        expected_value = __
        actual_value = 1 + 1
        self.assertEqual(expected_value, actual_value)

    def test_a_better_way_of_asserting_equality(self):
        # assertEqual is the idiomatic way to say "these should match".
        expected_value = __
        actual_value = 2 + 2
        self.assertEqual(expected_value, actual_value)

    def test_that_unittest_asserts_work_the_same_way_as_python_asserts(self):
        # A raw ``assert`` statement raises AssertionError on a falsy value.
        # Make it pass.
        assert __, "Truth is the foundation."

    def test_sometimes_we_will_ask_you_to_fill_in_the_value(self):
        # Sometimes the koans ask you to compute the answer. What's 5 * 7?
        self.assertEqual(__, 5 * 7)
