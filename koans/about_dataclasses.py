"""Dataclasses generate ``__init__``, ``__repr__``, ``__eq__`` from annotations."""

from runner.koan import Koan, __


class AboutDataclasses(Koan):

    def test_basic_dataclass(self):
        from dataclasses import dataclass

        @dataclass
        class Point:
            x: int
            y: int

        p = Point(3, 4)
        self.assertEqual(__, p.x)
        self.assertEqual(__, p.y)

    def test_dataclass_repr(self):
        from dataclasses import dataclass

        @dataclass
        class Point:
            x: int
            y: int

        self.assertEqual(__, repr(Point(1, 2)))

    def test_dataclass_equality(self):
        from dataclasses import dataclass

        @dataclass
        class Point:
            x: int
            y: int

        self.assertEqual(__, Point(1, 2) == Point(1, 2))
        self.assertEqual(__, Point(1, 2) == Point(1, 3))

    def test_default_values(self):
        from dataclasses import dataclass

        @dataclass
        class Settings:
            host: str = "localhost"
            port: int = 8080

        s = Settings()
        self.assertEqual(__, s.host)
        self.assertEqual(__, s.port)

    def test_default_factory_for_mutable(self):
        from dataclasses import dataclass, field

        @dataclass
        class Inventory:
            items: list = field(default_factory=list)

        a = Inventory()
        b = Inventory()
        a.items.append("apple")
        # Each instance gets its own list.
        self.assertEqual(__, b.items)

    def test_frozen_dataclass(self):
        from dataclasses import dataclass, FrozenInstanceError

        @dataclass(frozen=True)
        class Tag:
            name: str

        t = Tag("urgent")
        try:
            t.name = "calm"
        except FrozenInstanceError as e:
            self.assertEqual(__, type(e).__name__)

    def test_frozen_dataclasses_are_hashable(self):
        from dataclasses import dataclass

        @dataclass(frozen=True)
        class Tag:
            name: str
        s = {Tag("a"), Tag("a"), Tag("b")}
        self.assertEqual(__, len(s))

    def test_field_ordering_in_inheritance(self):
        # Fields without defaults must come before fields with defaults.
        from dataclasses import dataclass

        @dataclass
        class Animal:
            name: str

        @dataclass
        class Dog(Animal):
            breed: str = "unknown"

        d = Dog(name="Rex", breed="Husky")
        self.assertEqual(__, d.name)
        self.assertEqual(__, d.breed)

    def test_asdict(self):
        from dataclasses import dataclass, asdict

        @dataclass
        class Point:
            x: int
            y: int

        self.assertEqual(__, asdict(Point(3, 4)))
