"""The base machinery every koan file imports from."""

from __future__ import annotations

import unittest


class _Blank:
    """A placeholder. Replace every ``__`` in the koans with the right value.

    ``__`` is never equal to anything, never truthy, and refuses to participate
    in arithmetic. Any assertion that compares against it will fail until you
    replace it.
    """

    _instance: "_Blank | None" = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __repr__(self) -> str:
        return "__"

    def __str__(self) -> str:
        return "__"

    def __eq__(self, other) -> bool:
        return isinstance(other, _Blank)

    def __ne__(self, other) -> bool:
        return not isinstance(other, _Blank)

    def __hash__(self) -> int:
        return 0

    def __bool__(self) -> bool:
        return False

    def __len__(self) -> int:
        return 0

    def __iter__(self):
        return iter(())

    def __contains__(self, _item) -> bool:
        return False


__ = _Blank()
"""Single-blank placeholder. Replace with the correct value."""


# A few synonyms so koan source reads naturally regardless of what kind of
# value the student is meant to supply. They all behave identically.
____ = __
______ = __
________ = __


class Koan(unittest.TestCase):
    """Base class for every koan file.

    Subclasses contain ``test_*`` methods. The runner walks them in the order
    they appear in the source file.
    """

    # Disable unittest's alphabetical reordering — we want source order.
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._koan_order = [
            name for name, obj in cls.__dict__.items()
            if name.startswith("test_") and callable(obj)
        ]
