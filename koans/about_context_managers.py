"""``with`` statements drive context managers."""

from runner.koan import Koan, __


class Recorder:
    """A context manager that records when it enters and exits."""

    def __init__(self, log):
        self.log = log

    def __enter__(self):
        self.log.append("enter")
        return self

    def __exit__(self, exc_type, exc, tb):
        self.log.append("exit")
        return False


class Swallower:
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc, tb):
        # Returning True suppresses the exception.
        return True


class AboutContextManagers(Koan):

    def test_with_calls_enter_and_exit(self):
        log = []
        with Recorder(log) as r:
            log.append("inside")
        self.assertEqual(__, log)

    def test_exit_runs_even_on_exception(self):
        log = []
        try:
            with Recorder(log):
                raise ValueError("boom")
        except ValueError:
            log.append("caught")
        self.assertEqual(__, log)

    def test_exit_can_suppress_an_exception(self):
        # If __exit__ returns truthy, the exception is suppressed.
        result = "raised"
        with Swallower():
            raise RuntimeError("never seen")
            result = "skipped"
        result = "after"
        self.assertEqual(__, result)

    def test_contextlib_contextmanager_decorator(self):
        from contextlib import contextmanager

        @contextmanager
        def trace(log, name):
            log.append(f"enter {name}")
            try:
                yield name
            finally:
                log.append(f"exit {name}")

        log = []
        with trace(log, "block") as got:
            log.append(f"in {got}")
        self.assertEqual(__, log)

    def test_multiple_context_managers(self):
        log = []
        with Recorder(log) as a, Recorder(log) as b:
            log.append("body")
        self.assertEqual(__, log)

    def test_suppress_helper(self):
        from contextlib import suppress
        # ``suppress`` swallows specified exceptions inside its block.
        with suppress(KeyError):
            d = {}
            d["missing"]
            self.fail("should not reach")
        # We made it past the block without raising.
        self.assertEqual(__, True)

    def test_closing_helper(self):
        from contextlib import closing

        class Resource:
            def __init__(self):
                self.closed = False
            def close(self):
                self.closed = True

        r = Resource()
        with closing(r) as inner:
            pass
        self.assertEqual(__, r.closed)
