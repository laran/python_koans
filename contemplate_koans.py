#!/usr/bin/env python3
"""Walk the Python path to enlightenment.

Run this script. It will walk every koan in order, stop at the first one that
fails, and tell you which file and line to edit. Replace each ``__`` with the
value that makes the test pass. Then run it again.

    $ python contemplate_koans.py

When all koans pass, enlightenment is yours.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Ensure the project root is on sys.path so ``koans`` and ``runner`` import
# regardless of where this script is invoked from.
ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runner.sensei import Sensei


if __name__ == "__main__":
    sys.exit(Sensei().walk())
