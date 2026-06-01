"""Enums: named, distinct constants."""

from runner.koan import Koan, __


class AboutEnums(Koan):

    def test_basic_enum(self):
        from enum import Enum

        class Color(Enum):
            RED = 1
            GREEN = 2
            BLUE = 3

        self.assertEqual(__, Color.RED.name)
        self.assertEqual(__, Color.RED.value)

    def test_enum_members_are_singletons(self):
        from enum import Enum

        class Color(Enum):
            RED = 1
            GREEN = 2

        self.assertEqual(__, Color.RED is Color.RED)

    def test_enum_iteration(self):
        from enum import Enum

        class Direction(Enum):
            N = 1
            E = 2
            S = 3
            W = 4

        self.assertEqual(__, [d.name for d in Direction])

    def test_lookup_by_value(self):
        from enum import Enum

        class Color(Enum):
            RED = 1
            GREEN = 2

        self.assertEqual(__, Color(1))

    def test_lookup_by_name(self):
        from enum import Enum

        class Color(Enum):
            RED = 1

        self.assertEqual(__, Color["RED"])

    def test_int_enum_behaves_like_int(self):
        from enum import IntEnum

        class Priority(IntEnum):
            LOW = 1
            HIGH = 10

        self.assertEqual(__, Priority.LOW + 1)
        self.assertEqual(__, Priority.HIGH > Priority.LOW)

    def test_str_enum_behaves_like_str(self):
        from enum import StrEnum

        class Role(StrEnum):
            ADMIN = "admin"
            GUEST = "guest"

        self.assertEqual(__, Role.ADMIN.upper())
        self.assertEqual(__, Role.ADMIN == "admin")

    def test_flag_enum_supports_or(self):
        from enum import Flag, auto

        class Perm(Flag):
            READ = auto()
            WRITE = auto()
            EXEC = auto()

        rw = Perm.READ | Perm.WRITE
        self.assertEqual(__, Perm.READ in rw)
        self.assertEqual(__, Perm.EXEC in rw)

    def test_auto_assigns_values(self):
        from enum import Enum, auto

        class State(Enum):
            START = auto()
            RUNNING = auto()
            DONE = auto()

        self.assertEqual(__, State.START.value)
        self.assertEqual(__, State.DONE.value)
