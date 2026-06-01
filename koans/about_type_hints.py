"""Type hints describe shapes. They do not run anything at runtime."""

from runner.koan import Koan, __


class AboutTypeHints(Koan):

    def test_hints_do_not_enforce_types(self):
        def double(x: int) -> int:
            return x * 2
        # The annotation is documentation; passing a string still works.
        self.assertEqual(__, double("ab"))

    def test_annotations_are_introspectable(self):
        def f(x: int, y: str = "hi") -> bool:
            return True
        self.assertEqual(__, f.__annotations__["x"].__name__)
        self.assertEqual(__, f.__annotations__["return"].__name__)

    def test_union_with_pipe(self):
        # ``int | str`` is the modern union syntax (3.10+).
        def parse(v: int | str) -> int:
            return int(v)
        self.assertEqual(__, parse("42"))
        self.assertEqual(__, parse(42))

    def test_optional_is_just_a_union_with_none(self):
        # ``X | None`` is the new "Optional".
        def maybe(x: int | None) -> int:
            return x if x is not None else 0
        self.assertEqual(__, maybe(None))
        self.assertEqual(__, maybe(7))

    def test_built_in_generics(self):
        # In modern Python, ``list[int]``, ``dict[str, int]`` etc. work directly.
        def lengths(words: list[str]) -> list[int]:
            return [len(w) for w in words]
        self.assertEqual(__, lengths(["hi", "hello"]))

    def test_type_alias_pep_695(self):
        # PEP 695 ``type X = ...`` declares an alias at module level.
        # Inside a function body we use a plain assignment to demo the value.
        Vector = list[float]
        def magnitude_squared(v: Vector) -> float:
            return sum(x * x for x in v)
        self.assertEqual(__, magnitude_squared([3.0, 4.0]))

    def test_generic_function_pep_695(self):
        # PEP 695 also introduced ``def f[T](...)`` and ``class C[T]`` syntax.
        def first[T](items: list[T]) -> T:
            return items[0]
        self.assertEqual(__, first([10, 20, 30]))
        self.assertEqual(__, first(["a", "b"]))

    def test_protocol_for_duck_typing(self):
        from typing import Protocol

        class HasName(Protocol):
            name: str

        def greet(thing: HasName) -> str:
            return f"hello, {thing.name}"

        class Dog:
            name = "Rex"

        self.assertEqual(__, greet(Dog()))
