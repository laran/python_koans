"""Template strings (PEP 750), new in Python 3.14.

A ``t""`` literal looks like an f-string but returns a ``Template`` object
instead of a fully-rendered ``str``. The interpolations are kept separate so
your code can sanitize, escape, or otherwise process them safely — for HTML,
SQL, shell, you name it.
"""

from string.templatelib import Template, Interpolation

from runner.koan import Koan, __


class AboutTemplateStrings(Koan):

    def test_t_string_returns_a_template(self):
        name = "Ada"
        t = t"hello, {name}"
        self.assertEqual(__, isinstance(t, Template))

    def test_f_string_returns_a_string(self):
        name = "Ada"
        f = f"hello, {name}"
        self.assertEqual(__, isinstance(f, str))

    def test_template_strings_dont_eagerly_render(self):
        # Note: ``str(t"...")`` does NOT produce the interpolated text.
        # You must walk the template yourself.
        name = "Ada"
        t = t"hello, {name}"
        self.assertEqual(__, isinstance(str(t), str))  # it returns a str, but...
        # the str(t) is a repr-like form, not the interpolated body.

    def test_iterating_a_template_yields_strings_and_interpolations(self):
        name = "Ada"
        t = t"hello, {name}!"
        parts = list(t)
        # Strings between interpolations are plain str. Interpolations are
        # Interpolation objects with .value, .expression, .conversion, .format_spec.
        self.assertEqual(__, parts[0])
        self.assertEqual(__, isinstance(parts[1], Interpolation))
        self.assertEqual(__, parts[1].value)
        self.assertEqual(__, parts[1].expression)
        self.assertEqual(__, parts[2])

    def test_template_strings_separate_static_and_dynamic(self):
        # ``Template.strings`` gives the static text between interpolations.
        # ``Template.values`` gives the substituted values.
        name = "Ada"
        place = "Earth"
        t = t"hello, {name} of {place}!"
        self.assertEqual(__, t.strings)
        self.assertEqual(__, t.values)

    def test_template_format_specs_are_carried_through(self):
        x = 3.14159
        t = t"pi is {x:.2f}"
        interp = list(t)[1]
        self.assertEqual(__, interp.format_spec)

    def test_simple_renderer_using_format(self):
        # A naive renderer reproduces what an f-string would have done.
        def render(template):
            out = []
            for part in template:
                if isinstance(part, str):
                    out.append(part)
                else:
                    out.append(format(part.value, part.format_spec))
            return "".join(out)

        name = "Ada"
        self.assertEqual(__, render(t"hello, {name}"))

    def test_template_strings_enable_safe_renderers(self):
        # The point of t-strings: write a renderer that escapes interpolations
        # without escaping the static text. Here, we shout interpolated values.
        def loud(template):
            out = []
            for part in template:
                if isinstance(part, str):
                    out.append(part)
                else:
                    out.append(str(part.value).upper())
            return "".join(out)

        who = "world"
        self.assertEqual(__, loud(t"hello, {who}!"))
