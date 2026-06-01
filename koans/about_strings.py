"""Strings are immutable sequences of Unicode code points."""

from runner.koan import Koan, __


class AboutStrings(Koan):

    def test_double_quoted_strings_are_strings(self):
        s = "hello"
        self.assertEqual(__, isinstance(s, str))

    def test_single_quoted_strings_are_also_strings(self):
        s = 'hello'
        self.assertEqual(__, isinstance(s, str))

    def test_triple_quoted_strings_span_lines(self):
        s = """one
two"""
        self.assertEqual(__, s.count("\n"))

    def test_strings_can_be_concatenated(self):
        self.assertEqual(__, "hello" + " " + "world")

    def test_adjacent_string_literals_are_concatenated_at_parse_time(self):
        # Two literals next to each other are joined automatically.
        s = "hello" " " "world"
        self.assertEqual(__, s)

    def test_strings_can_be_multiplied(self):
        self.assertEqual(__, "ha" * 3)

    def test_strings_have_a_length(self):
        self.assertEqual(__, len("hello"))

    def test_strings_are_indexable(self):
        s = "python"
        self.assertEqual(__, s[0])
        self.assertEqual(__, s[-1])

    def test_strings_can_be_sliced(self):
        s = "abcdef"
        self.assertEqual(__, s[1:4])
        self.assertEqual(__, s[:3])
        self.assertEqual(__, s[3:])
        self.assertEqual(__, s[::2])
        self.assertEqual(__, s[::-1])

    def test_strings_are_immutable(self):
        s = "hello"
        try:
            s[0] = "H"
        except TypeError as e:
            self.assertEqual(__, type(e).__name__)

    def test_methods_return_new_strings(self):
        s = "hello"
        s.upper()
        # s itself is unchanged because strings are immutable.
        self.assertEqual(__, s)

    def test_upper_lower_title(self):
        self.assertEqual(__, "hello".upper())
        self.assertEqual(__, "HELLO".lower())
        self.assertEqual(__, "hello world".title())

    def test_strip(self):
        self.assertEqual(__, "  spaced  ".strip())
        self.assertEqual(__, "xxhelloxx".strip("x"))

    def test_split(self):
        self.assertEqual(__, "a,b,c".split(","))
        self.assertEqual(__, "a b c".split())

    def test_join(self):
        # The separator joins an iterable of strings.
        self.assertEqual(__, ",".join(["a", "b", "c"]))

    def test_replace(self):
        self.assertEqual(__, "banana".replace("a", "o"))

    def test_in_operator(self):
        self.assertEqual(__, "py" in "python")

    def test_starts_and_ends(self):
        self.assertEqual(__, "snake.py".endswith(".py"))
        self.assertEqual(__, "snake.py".startswith("snake"))

    def test_find_and_index(self):
        # find returns -1 if not found. index raises.
        self.assertEqual(__, "banana".find("na"))
        self.assertEqual(__, "banana".find("z"))
        try:
            "banana".index("z")
        except ValueError as e:
            self.assertEqual(__, type(e).__name__)

    def test_count(self):
        self.assertEqual(__, "banana".count("a"))

    def test_unicode_is_native(self):
        # Strings are Unicode by default.
        s = "café"
        self.assertEqual(__, len(s))
