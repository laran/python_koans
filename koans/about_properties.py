"""Properties let attribute access run code."""

from runner.koan import Koan, __


class AboutProperties(Koan):

    def test_property_makes_method_look_like_attribute(self):
        class Circle:
            def __init__(self, radius):
                self.radius = radius
            @property
            def area(self):
                return 3.14 * self.radius ** 2

        # Notice: no parentheses on ``area``.
        c = Circle(2)
        self.assertEqual(__, c.area)

    def test_property_with_setter(self):
        class Celsius:
            def __init__(self, temp):
                self._temp = temp
            @property
            def fahrenheit(self):
                return self._temp * 9 / 5 + 32
            @fahrenheit.setter
            def fahrenheit(self, value):
                self._temp = (value - 32) * 5 / 9

        c = Celsius(0)
        self.assertEqual(__, c.fahrenheit)
        c.fahrenheit = 212
        self.assertEqual(__, c._temp)

    def test_setting_without_setter_raises(self):
        class Locked:
            @property
            def name(self):
                return "constant"

        l = Locked()
        try:
            l.name = "new"
        except AttributeError as e:
            self.assertEqual(__, type(e).__name__)

    def test_property_with_deleter(self):
        class Bag:
            def __init__(self):
                self._items = [1, 2, 3]
            @property
            def items(self):
                return self._items
            @items.deleter
            def items(self):
                self._items = []

        b = Bag()
        del b.items
        self.assertEqual(__, b.items)

    def test_cached_property(self):
        from functools import cached_property

        class Slow:
            def __init__(self):
                self.calls = 0
            @cached_property
            def value(self):
                self.calls += 1
                return 42

        s = Slow()
        s.value
        s.value
        s.value
        # The body ran only once because the result is cached.
        self.assertEqual(__, s.calls)
