"""F-strings: formatted string literals. Concise, fast, and expressive."""

from runner.koan import Koan, __


class AboutFStrings(Koan):

    def test_basic_interpolation(self):
        name = "Ada"
        self.assertEqual(__, f"hello, {name}")

    def test_expressions_inside_braces(self):
        self.assertEqual(__, f"{2 + 3}")

    def test_calling_methods_inside_braces(self):
        self.assertEqual(__, f"{'python'.upper()}")

    def test_format_spec_floats(self):
        # ``:.2f`` means: float, two decimals.
        self.assertEqual(__, f"{3.14159:.2f}")

    def test_format_spec_padding(self):
        # right-align in a 5-char field, padded with zeros.
        self.assertEqual(__, f"{7:05d}")

    def test_format_spec_alignment(self):
        # ``<`` left, ``^`` center, ``>`` right.
        self.assertEqual(__, f"|{'hi':<6}|")
        self.assertEqual(__, f"|{'hi':^6}|")
        self.assertEqual(__, f"|{'hi':>6}|")

    def test_format_spec_thousands(self):
        self.assertEqual(__, f"{1000000:,}")

    def test_repr_versus_str(self):
        # ``!r`` calls repr, ``!s`` calls str.
        self.assertEqual(__, f"{'a'!r}")

    def test_self_documenting_expressions(self):
        # The ``=`` suffix is great for debugging.
        x = 42
        self.assertEqual(__, f"{x=}")

    def test_braces_are_escaped_by_doubling(self):
        self.assertEqual(__, f"{{{1 + 1}}}")

    def test_nested_f_strings(self):
        # You can nest f-strings inside f-strings.
        width = 6
        self.assertEqual(__, f"{'hi':>{width}}")

    def test_old_format_method_still_works(self):
        # ``str.format`` was the previous generation.
        self.assertEqual(__, "hello, {}".format("Ada"))

    def test_old_percent_formatting_still_works(self):
        # ``%`` formatting is even older but still around.
        self.assertEqual(__, "%d items" % 3)
