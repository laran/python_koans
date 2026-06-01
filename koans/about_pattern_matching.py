"""Structural pattern matching, via ``match``/``case`` (Python 3.10+)."""

from runner.koan import Koan, __


class AboutPatternMatching(Koan):

    def test_literal_pattern(self):
        def describe(x):
            match x:
                case 0:
                    return "zero"
                case 1:
                    return "one"
                case _:
                    return "other"

        self.assertEqual(__, describe(0))
        self.assertEqual(__, describe(1))
        self.assertEqual(__, describe(42))

    def test_or_pattern(self):
        def is_weekend(day):
            match day:
                case "Sat" | "Sun":
                    return True
                case _:
                    return False

        self.assertEqual(__, is_weekend("Sat"))
        self.assertEqual(__, is_weekend("Mon"))

    def test_sequence_pattern(self):
        def head(items):
            match items:
                case []:
                    return None
                case [x]:
                    return x
                case [x, *_]:
                    return x

        self.assertEqual(__, head([]))
        self.assertEqual(__, head([7]))
        self.assertEqual(__, head([1, 2, 3]))

    def test_sequence_capture(self):
        def first_and_rest(items):
            match items:
                case [first, *rest]:
                    return first, rest
                case _:
                    return None, []

        self.assertEqual(__, first_and_rest([1, 2, 3, 4]))

    def test_mapping_pattern(self):
        def find_name(record):
            match record:
                case {"name": name}:
                    return name
                case _:
                    return None

        self.assertEqual(__, find_name({"name": "Ada", "age": 36}))
        self.assertEqual(__, find_name({"x": 1}))

    def test_class_pattern(self):
        class Point:
            __match_args__ = ("x", "y")
            def __init__(self, x, y):
                self.x = x
                self.y = y

        def describe(p):
            match p:
                case Point(0, 0):
                    return "origin"
                case Point(x, 0):
                    return f"x-axis at {x}"
                case Point(0, y):
                    return f"y-axis at {y}"
                case Point(x, y):
                    return f"point at ({x},{y})"

        self.assertEqual(__, describe(Point(0, 0)))
        self.assertEqual(__, describe(Point(3, 0)))
        self.assertEqual(__, describe(Point(0, 4)))
        self.assertEqual(__, describe(Point(2, 5)))

    def test_guarded_pattern(self):
        def classify(n):
            match n:
                case x if x < 0:
                    return "negative"
                case 0:
                    return "zero"
                case x if x > 0:
                    return "positive"

        self.assertEqual(__, classify(-3))
        self.assertEqual(__, classify(0))
        self.assertEqual(__, classify(7))

    def test_wildcard_pattern(self):
        # ``_`` matches anything and does not bind a name.
        def describe(x):
            match x:
                case (a, b, _):
                    return a + b
                case _:
                    return -1

        self.assertEqual(__, describe((1, 2, 99)))
        self.assertEqual(__, describe("anything"))
