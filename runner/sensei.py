"""The Sensei walks the path of koans and reports on the seeker's progress."""

from __future__ import annotations

import importlib
import inspect
import random
import traceback
from dataclasses import dataclass, field
from pathlib import Path

from runner.koan import Koan


WISDOM = [
    "mountains are merely mountains",
    "learn the rules like a pro, so you can break them like an artist",
    "remember that silence is sometimes the best answer",
    "sleep is the best meditation",
    "when you lose, don't lose the lesson",
    "things are not what they appear to be: nor are they otherwise",
    "to know, is to know that you know nothing — that is the meaning of true knowledge",
    "the only way to make sense out of change is to plunge into it, move with it, and join the dance",
    "knowing others is intelligence; knowing yourself is true wisdom",
    "do not seek to follow in the footsteps of the wise. seek what they sought",
    "before enlightenment; chop wood, carry water. after enlightenment; chop wood, carry water",
    "the obstacle is the path",
    "smile, breathe and go slowly",
]


COMPLETION = """
    *********************************************************
    That was the last one, well done! ENLIGHTENMENT AWAITS...

      "Programs must be written for people to read,
       and only incidentally for machines to execute."
                                         -- Harold Abelson

    If you want, take a moment to reflect upon what you have
    learned. The Python you have walked through is the Python
    you now carry with you.
    *********************************************************
"""


@dataclass
class KoanResult:
    module_name: str
    class_name: str
    method_name: str
    passed: bool
    error: BaseException | None = None
    traceback: str = ""
    file_path: str = ""
    line_number: int = 0


@dataclass
class Walk:
    results: list[KoanResult] = field(default_factory=list)

    @property
    def passed(self) -> int:
        return sum(1 for r in self.results if r.passed)

    @property
    def total(self) -> int:
        return len(self.results)

    @property
    def first_failure(self) -> KoanResult | None:
        return next((r for r in self.results if not r.passed), None)


class Sensei:
    """Loads each koan module in order, runs every koan, stops at the first
    that fails, and reports the result."""

    def __init__(self, modules: list[str] | None = None) -> None:
        if modules is None:
            from koans.path_to_enlightenment import KOAN_PATH
            modules = KOAN_PATH
        self.modules = modules

    def walk(self) -> int:
        walk = Walk()
        first_failure: KoanResult | None = None

        for module_name in self.modules:
            module = importlib.import_module(module_name)
            koan_classes = self._koan_classes(module)
            for cls in koan_classes:
                for method_name in getattr(cls, "_koan_order", []):
                    if first_failure is not None:
                        # Once we've found the first failure, we still want to
                        # know how many koans remain — so we keep counting but
                        # don't actually run them (their state may depend on
                        # earlier ones being correct).
                        walk.results.append(KoanResult(
                            module_name=module_name,
                            class_name=cls.__name__,
                            method_name=method_name,
                            passed=False,
                        ))
                        continue
                    result = self._run_one(module_name, cls, method_name)
                    walk.results.append(result)
                    if not result.passed:
                        first_failure = result

        self._render(walk)
        return 0 if walk.first_failure is None else 1

    def _koan_classes(self, module) -> list[type]:
        classes = []
        for _, obj in inspect.getmembers(module, inspect.isclass):
            if obj is Koan:
                continue
            if not issubclass(obj, Koan):
                continue
            if obj.__module__ != module.__name__:
                continue
            classes.append(obj)
        return classes

    def _run_one(self, module_name: str, cls: type, method_name: str) -> KoanResult:
        instance = cls(method_name)
        try:
            instance.setUp()
            getattr(instance, method_name)()
            instance.tearDown()
            return KoanResult(
                module_name=module_name,
                class_name=cls.__name__,
                method_name=method_name,
                passed=True,
            )
        except BaseException as e:
            file_path, line_number = self._locate_failure(e, cls)
            return KoanResult(
                module_name=module_name,
                class_name=cls.__name__,
                method_name=method_name,
                passed=False,
                error=e,
                traceback=traceback.format_exc(),
                file_path=file_path,
                line_number=line_number,
            )

    def _locate_failure(self, exc: BaseException, cls: type) -> tuple[str, int]:
        try:
            koan_file = inspect.getfile(cls)
        except (TypeError, OSError):
            koan_file = ""
        frames = traceback.extract_tb(exc.__traceback__)
        for frame in reversed(frames):
            if koan_file and Path(frame.filename).resolve() == Path(koan_file).resolve():
                return frame.filename, frame.lineno
        if frames:
            return frames[-1].filename, frames[-1].lineno
        return koan_file, 0

    # ------------------------------------------------------------------ output

    def _render(self, walk: Walk) -> None:
        failure = walk.first_failure
        if failure is None:
            print(COMPLETION)
            self._progress(walk.passed, walk.total)
            return

        print()
        print(f"Thinking {self._humanize(failure.class_name)}")
        # Show preceding passing koans in this class.
        for r in walk.results:
            if (r.module_name == failure.module_name
                    and r.class_name == failure.class_name):
                if r.method_name == failure.method_name:
                    print(f"  {r.method_name} has damaged your karma.")
                    break
                if r.passed:
                    print(f"  {r.method_name} has expanded your awareness.")

        print()
        print("The Master says:")
        print("  You have not yet reached enlightenment.")
        if failure.error is not None:
            extra = self._format_error_hint(failure.error)
            if extra:
                print(f"  {extra}")

        print()
        print("The answers you seek...")
        message = self._error_message(failure.error)
        for line in message.splitlines():
            print(f"  {line}")

        print()
        print("Please meditate on the following code:")
        print(f"  In {failure.file_path}:{failure.line_number}")
        print(f"  In {failure.class_name}.{failure.method_name}")

        print()
        print(random.choice(WISDOM))
        print()
        self._progress(walk.passed, walk.total)

    def _humanize(self, class_name: str) -> str:
        # "AboutStrings" -> "About Strings"
        out = []
        for i, ch in enumerate(class_name):
            if i > 0 and ch.isupper():
                out.append(" ")
            out.append(ch)
        return "".join(out)

    def _error_message(self, exc: BaseException | None) -> str:
        if exc is None:
            return ""
        # AssertionError messages from unittest are usually the most helpful.
        msg = str(exc).strip()
        if not msg:
            return f"{type(exc).__name__} was raised"
        return msg

    def _format_error_hint(self, exc: BaseException) -> str:
        name = type(exc).__name__
        hints = {
            "AssertionError": "",
            "NameError": "It looks like a name is not yet defined.",
            "TypeError": "The shape of a value does not fit.",
            "AttributeError": "An object lacks the attribute requested.",
            "KeyError": "A key was not found.",
            "IndexError": "An index is out of range.",
            "ValueError": "A value was of the right type but the wrong value.",
            "ZeroDivisionError": "Division by zero is not yet a thing.",
        }
        return hints.get(name, f"{name} was raised.")

    def _progress(self, passed: int, total: int) -> None:
        width = 50
        if total == 0:
            ratio = 0.0
        else:
            ratio = passed / total
        filled = int(ratio * width)
        bar = "." * filled + "X" + " " * max(0, width - filled - 1)
        if passed == total:
            bar = "." * width
        print(f"your path thus far [{bar}] {passed}/{total}")
