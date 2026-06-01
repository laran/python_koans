"""``None`` is Python's name for nothing. It is a value, a type, and a singleton.
"""

from runner.koan import Koan, __


class AboutNone(Koan):

    def test_none_is_an_object(self):
        # Even nothing is something in Python.
        self.assertEqual(__, isinstance(None, object))

    def test_none_is_unique(self):
        # There is exactly one None. ``is`` checks identity.
        self.assertEqual(__, None is None)

    def test_none_is_not_the_same_as_false(self):
        self.assertEqual(__, None is False)

    def test_none_is_not_the_same_as_zero(self):
        self.assertEqual(__, None == 0)

    def test_none_is_falsy(self):
        # In a boolean context, None acts like False.
        if None:
            result = "truthy"
        else:
            result = "falsy"
        self.assertEqual(__, result)

    def test_calling_method_on_none_raises(self):
        # None has very few methods. Accessing one that does not exist raises.
        try:
            None.some_method_that_does_not_exist()
        except Exception as e:
            self.assertEqual(__, type(e).__name__)

    def test_functions_that_return_nothing_return_none(self):
        def silent():
            pass
        self.assertEqual(__, silent())

    def test_the_type_of_none(self):
        # The type of None has a name.
        self.assertEqual(__, type(None).__name__)
