"""Numbers in Python: int, float, complex, and the operations that bind them."""

from runner.koan import Koan, __


class AboutNumbers(Koan):

    def test_integers(self):
        self.assertEqual(__, type(42).__name__)

    def test_floats(self):
        self.assertEqual(__, type(3.14).__name__)

    def test_complex_numbers(self):
        self.assertEqual(__, type(1 + 2j).__name__)

    def test_int_division_is_floor_division(self):
        # ``//`` rounds toward negative infinity, not toward zero.
        self.assertEqual(__, 7 // 2)
        self.assertEqual(__, -7 // 2)

    def test_true_division_returns_a_float(self):
        # ``/`` always produces a float, even when the result is whole.
        self.assertEqual(__, 4 / 2)
        self.assertEqual(__, type(4 / 2).__name__)

    def test_modulo(self):
        self.assertEqual(__, 10 % 3)

    def test_power(self):
        # ``**`` raises to a power. There is no overflow for ints.
        self.assertEqual(__, 2 ** 10)

    def test_int_has_arbitrary_precision(self):
        # ints can grow as large as memory allows.
        big = 10 ** 100
        self.assertEqual(__, big > 0)
        self.assertEqual(__, type(big).__name__)

    def test_float_precision_is_limited(self):
        # IEEE-754 strikes again.
        self.assertEqual(__, 0.1 + 0.2 == 0.3)

    def test_underscores_in_numeric_literals(self):
        # Underscores are allowed for readability.
        self.assertEqual(__, 1_000_000)

    def test_int_from_string(self):
        self.assertEqual(__, int("42"))

    def test_int_from_binary_string(self):
        self.assertEqual(__, int("1010", 2))

    def test_int_from_hex_string(self):
        self.assertEqual(__, int("ff", 16))

    def test_bin_oct_hex(self):
        self.assertEqual(__, bin(5))
        self.assertEqual(__, oct(8))
        self.assertEqual(__, hex(255))

    def test_abs_and_round(self):
        self.assertEqual(__, abs(-7))
        self.assertEqual(__, round(2.5))   # banker's rounding!
        self.assertEqual(__, round(3.5))
        self.assertEqual(__, round(2.675, 2))

    def test_divmod(self):
        # divmod returns (quotient, remainder) in one go.
        self.assertEqual(__, divmod(17, 5))
