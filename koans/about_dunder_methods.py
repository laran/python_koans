"""Dunder ("double underscore") methods make objects behave like built-ins."""

from runner.koan import Koan, __


class AboutDunderMethods(Koan):

    def test_str_versus_repr(self):
        class Point:
            def __init__(self, x, y):
                self.x = x; self.y = y
            def __repr__(self):
                return f"Point({self.x}, {self.y})"
            def __str__(self):
                return f"({self.x}, {self.y})"

        p = Point(3, 4)
        self.assertEqual(__, str(p))
        self.assertEqual(__, repr(p))

    def test_repr_is_fallback_for_str(self):
        class OnlyRepr:
            def __repr__(self):
                return "OnlyRepr()"
        # When __str__ is not defined, str() falls back to __repr__.
        self.assertEqual(__, str(OnlyRepr()))

    def test_len(self):
        class Bag:
            def __init__(self, items):
                self.items = items
            def __len__(self):
                return len(self.items)
        self.assertEqual(__, len(Bag([1, 2, 3, 4])))

    def test_getitem(self):
        class Reverse:
            def __init__(self, s):
                self.s = s
            def __getitem__(self, i):
                return self.s[-1 - i]

        r = Reverse("hello")
        self.assertEqual(__, r[0])
        self.assertEqual(__, r[1])

    def test_eq_and_hash(self):
        class Color:
            def __init__(self, name):
                self.name = name
            def __eq__(self, other):
                return isinstance(other, Color) and self.name == other.name
            def __hash__(self):
                return hash(self.name)

        self.assertEqual(__, Color("red") == Color("red"))
        self.assertEqual(__, {Color("red"), Color("red")} == {Color("red")})

    def test_lt_enables_sorting(self):
        class Box:
            def __init__(self, weight):
                self.weight = weight
            def __lt__(self, other):
                return self.weight < other.weight
            def __repr__(self):
                return f"Box({self.weight})"

        boxes = [Box(3), Box(1), Box(2)]
        self.assertEqual(__, [b.weight for b in sorted(boxes)])

    def test_add(self):
        class Vector:
            def __init__(self, x, y):
                self.x = x; self.y = y
            def __add__(self, other):
                return Vector(self.x + other.x, self.y + other.y)
            def __repr__(self):
                return f"V({self.x},{self.y})"

        v = Vector(1, 2) + Vector(3, 4)
        self.assertEqual(__, (v.x, v.y))

    def test_call_makes_instance_callable(self):
        class Greeter:
            def __init__(self, greeting):
                self.greeting = greeting
            def __call__(self, name):
                return f"{self.greeting}, {name}"

        hello = Greeter("hello")
        self.assertEqual(__, hello("Ada"))
        self.assertEqual(__, callable(hello))

    def test_contains(self):
        class OneToTen:
            def __contains__(self, item):
                return isinstance(item, int) and 1 <= item <= 10
        self.assertEqual(__, 5 in OneToTen())
        self.assertEqual(__, 20 in OneToTen())

    def test_iter(self):
        class Fibs:
            def __init__(self, n):
                self.n = n
            def __iter__(self):
                a, b = 0, 1
                for _ in range(self.n):
                    yield a
                    a, b = b, a + b
        self.assertEqual(__, list(Fibs(7)))
