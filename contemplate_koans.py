#!/usr/bin/env python3
"""Walk the Python path to enlightenment.

Run this script. It will walk every koan in order, stop at the first one that
fails, and tell you which file and line to edit. Replace each ``__`` with the
value that makes the test pass. Then run it again.

    $ python contemplate_koans.py

For an automatic, file-watching re-run loop:

    $ python contemplate_koans.py --watch

When all koans pass, enlightenment is yours.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REQUIRED = (3, 14)
if sys.version_info < REQUIRED:
    sys.stderr.write(
        f"\npython-koans requires Python {REQUIRED[0]}.{REQUIRED[1]} or newer.\n"
        f"You are running {sys.version.split()[0]} ({sys.executable}).\n\n"
        f"Several koans use 3.14-only syntax — template strings (PEP 750)\n"
        f"and paren-free `except` (PEP 758) — so a SyntaxError will fire\n"
        f"on import under older interpreters.\n\n"
        f"Try:  python3.14 {Path(__file__).name} "
        f"{' '.join(sys.argv[1:])}\n\n"
    )
    sys.exit(2)

# Ensure the project root is on sys.path so ``koans`` and ``runner`` import
# regardless of where this script is invoked from.
ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="contemplate_koans",
        description="Walk the Python path to enlightenment.",
    )
    parser.add_argument(
        "--watch",
        action="store_true",
        help="re-run automatically whenever a koan file changes.",
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=0.5,
        help="seconds between file-change polls when --watch is set (default: 0.5).",
    )
    args = parser.parse_args(argv)

    if args.watch:
        # Imported lazily so that a plain run has no watcher overhead.
        from runner.watcher import watch
        return watch(interval=args.interval)

    from runner.sensei import Sensei
    return Sensei().walk()


if __name__ == "__main__":
    sys.exit(main())
