"""Exceptions: try/except/else/finally, raising, chaining, and groups."""

from runner.koan import Koan, __


class CustomError(Exception):
    pass


class AboutExceptions(Koan):

    def test_catching_an_exception(self):
        try:
            int("not a number")
        except ValueError as e:
            self.assertEqual(__, type(e).__name__)

    def test_finally_always_runs(self):
        log = []
        try:
            log.append("try")
            raise RuntimeError("nope")
        except RuntimeError:
            log.append("except")
        finally:
            log.append("finally")
        self.assertEqual(__, log)

    def test_else_runs_when_no_exception(self):
        log = []
        try:
            log.append("try")
        except Exception:
            log.append("except")
        else:
            log.append("else")
        finally:
            log.append("finally")
        self.assertEqual(__, log)

    def test_raising_custom_exception(self):
        try:
            raise CustomError("specific")
        except CustomError as e:
            self.assertEqual(__, str(e))

    def test_exception_hierarchy(self):
        # Catching a base class catches all derived exceptions.
        try:
            raise ValueError("bad")
        except Exception as e:
            self.assertEqual(__, isinstance(e, ValueError))

    def test_multiple_except_clauses(self):
        def classify(x):
            try:
                if x == "key":
                    raise KeyError()
                if x == "value":
                    raise ValueError()
                return "ok"
            except KeyError:
                return "key error"
            except ValueError:
                return "value error"

        self.assertEqual(__, classify("key"))
        self.assertEqual(__, classify("value"))
        self.assertEqual(__, classify("hello"))

    def test_tuple_of_exception_types(self):
        def safe(x):
            try:
                return int(x)
            except (TypeError, ValueError):
                return -1

        self.assertEqual(__, safe("42"))
        self.assertEqual(__, safe("nope"))
        self.assertEqual(__, safe(None))

    def test_exception_chaining_with_raise_from(self):
        try:
            try:
                int("abc")
            except ValueError as inner:
                raise RuntimeError("processing failed") from inner
        except RuntimeError as e:
            self.assertEqual(__, type(e).__name__)
            self.assertEqual(__, type(e.__cause__).__name__)

    def test_exception_groups(self):
        # ExceptionGroup (3.11+) groups multiple exceptions.
        # ``except*`` (3.11+) catches by sub-type from the group.
        caught_types = []
        try:
            raise ExceptionGroup("multi", [ValueError("v"), KeyError("k")])
        except* ValueError as eg:
            caught_types.append("ValueError")
        except* KeyError as eg:
            caught_types.append("KeyError")

        self.assertEqual(__, sorted(caught_types))

    def test_except_without_parens(self):
        # PEP 758 (3.14): bare comma-separated except types, no parens needed.
        def safe(x):
            try:
                return int(x)
            except TypeError, ValueError:
                return -1

        self.assertEqual(__, safe("42"))
        self.assertEqual(__, safe("nope"))

    def test_re_raise_without_argument(self):
        log = []
        try:
            try:
                raise ValueError("inner")
            except ValueError:
                log.append("caught")
                raise
        except ValueError as e:
            log.append(str(e))
        self.assertEqual(__, log)
