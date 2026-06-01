"""Decorators wrap a function (or class) to alter or extend its behavior."""

from runner.koan import Koan, __


def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper


def repeat(times):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            return [fn(*args, **kwargs) for _ in range(times)]
        return wrapper
    return decorator


class AboutDecorators(Koan):

    def test_simple_decorator(self):
        @shout
        def greet():
            return "hello"

        self.assertEqual(__, greet())

    def test_decorator_is_just_function_application(self):
        def hello():
            return "hi"
        # The @ syntax is sugar for ``hello = shout(hello)``.
        wrapped = shout(hello)
        self.assertEqual(__, wrapped())

    def test_decorator_with_arguments(self):
        @repeat(times=3)
        def hi():
            return "hi"
        self.assertEqual(__, hi())

    def test_preserving_name_with_functools_wraps(self):
        from functools import wraps

        def announce(fn):
            @wraps(fn)
            def wrapper(*args, **kwargs):
                return f"calling {fn.__name__}: {fn(*args, **kwargs)}"
            return wrapper

        @announce
        def greet():
            """Greet the world."""
            return "hello"

        # Without @wraps, greet.__name__ would become "wrapper".
        self.assertEqual(__, greet.__name__)
        self.assertEqual(__, greet.__doc__)
        self.assertEqual(__, greet())

    def test_stacked_decorators_apply_bottom_up(self):
        def exclaim(fn):
            def wrapper(*args, **kwargs):
                return fn(*args, **kwargs) + "!"
            return wrapper

        @shout
        @exclaim
        def greet():
            return "hi"
        # exclaim runs first (closest to function), then shout wraps the result.
        self.assertEqual(__, greet())

    def test_class_as_decorator(self):
        class CountCalls:
            def __init__(self, fn):
                self.fn = fn
                self.count = 0
            def __call__(self, *args, **kwargs):
                self.count += 1
                return self.fn(*args, **kwargs)

        @CountCalls
        def beep():
            return "beep"

        beep()
        beep()
        beep()
        self.assertEqual(__, beep.count)
