"""Re-run the koans whenever a koan file changes.

Stdlib-only. Polls mtimes on a short interval — no inotify, no fsevents, no
third-party dependencies. The koan set is small enough that polling is fine.
"""

from __future__ import annotations

import importlib
import os
import sys
import time
from pathlib import Path

from runner.sensei import Sensei


def _drop_koans_from_cache() -> None:
    """Force re-import of every koan module on the next walk.

    Without this, edits to a koan file are invisible — Python caches the
    imported module forever in ``sys.modules``.
    """
    for name in list(sys.modules):
        if name == "koans" or name.startswith("koans."):
            del sys.modules[name]
    # Also reset the importer's negative cache so deletions/renames behave.
    importlib.invalidate_caches()


def _snapshot(roots: list[Path]) -> dict[str, float]:
    """Return {path: mtime} for every .py file beneath ``roots``."""
    seen: dict[str, float] = {}
    for root in roots:
        if not root.exists():
            continue
        for path in root.rglob("*.py"):
            try:
                seen[str(path)] = path.stat().st_mtime
            except OSError:
                continue
    return seen


def _clear() -> None:
    # ANSI clear screen. Falls back gracefully if the terminal doesn't render it.
    sys.stdout.write("\x1b[2J\x1b[H")
    sys.stdout.flush()


def watch(interval: float = 0.5) -> int:
    """Run the koans, then re-run any time a watched .py file changes.

    Returns the exit code of the last run when interrupted (Ctrl-C).
    """
    project_root = Path(__file__).resolve().parent.parent
    roots = [project_root / "koans", project_root / "runner"]

    last_seen = _snapshot(roots)
    _clear()
    print(f"[watch] watching {', '.join(r.name + '/' for r in roots)} "
          f"(Ctrl-C to stop)\n")
    exit_code = Sensei().walk()

    try:
        while True:
            time.sleep(interval)
            current = _snapshot(roots)
            if current == last_seen:
                continue

            changed = sorted(
                {p for p in current if current.get(p) != last_seen.get(p)}
                | {p for p in last_seen if p not in current}
            )
            last_seen = current

            _clear()
            print(f"[watch] change detected: "
                  f"{', '.join(os.path.relpath(p, project_root) for p in changed)}\n")
            _drop_koans_from_cache()
            try:
                exit_code = Sensei().walk()
            except Exception as e:
                # If a koan file has a syntax error or import-time crash, the
                # sensei may raise. Don't kill the watcher — keep waiting for
                # the next save.
                print(f"\n[watch] error during run: {type(e).__name__}: {e}")
                exit_code = 1
    except KeyboardInterrupt:
        print("\n[watch] stopped.")
        return exit_code
