# Python Koans

Inspired by [Ruby Koans](https://github.com/edgecase/ruby_koans), this is a set
of small, ordered exercises that walk you through the Python language one
failing test at a time. You learn by fixing the next broken thing.

Targets **Python 3.14**. No third-party dependencies — just the standard library.

## Running

```bash
python3.14 contemplate_koans.py
```

Each run:

1. Walks every koan in the order defined in
   [`koans/path_to_enlightenment.py`](koans/path_to_enlightenment.py).
2. Stops at the **first failing koan**.
3. Tells you the file, line number, and what the assertion expected.
4. Shows your progress bar.

## The workflow

Every koan is a `unittest`-style test. Many tests contain a placeholder named
`__` (double underscore). Your job is to **edit the koan file** and replace
each `__` with the value that makes the test pass. Then re-run.

```python
def test_fill_in_values(self):
    self.assertEqual(__, 1 + 1)   # become: self.assertEqual(2, 1 + 1)
```

A typical session looks like this:

```
$ python3.14 contemplate_koans.py

Thinking About Asserts
  test_assert_truth has damaged your karma.

The Master says:
  You have not yet reached enlightenment.

The answers you seek...
  False is not true : This should be true — make it so.

Please meditate on the following code:
  In /…/koans/about_asserts.py:17
  In AboutAsserts.test_assert_truth

mountains are merely mountains

your path thus far [X                                                 ] 0/361
```

Open `koans/about_asserts.py` at line 17, fix it, save, and run again. Repeat
until you reach enlightenment.

## What's covered

The koans walk through:

- Asserts, `None`, booleans
- Numbers, strings, **f-strings**, **t-strings** (PEP 750, new in 3.14)
- Lists, tuples, dictionaries, sets
- Control flow, **structural pattern matching** (`match`/`case`)
- Functions, lambdas, comprehensions, generators, iterators, decorators
- Classes, inheritance, dunder methods, properties
- Dataclasses, enums
- Exceptions (including `ExceptionGroup` / `except*` and PEP 758
  paren-free `except`)
- Context managers
- Type hints (modern `int | None`, PEP 695 generics)
- The walrus operator
- `collections`, `itertools`, `functools`, `pathlib`
- `async` / `await`

## Project layout

```
python_koans/
├── contemplate_koans.py        # entry point — run this
├── koans/
│   ├── about_*.py              # one file per topic; edit these
│   └── path_to_enlightenment.py
└── runner/
    ├── koan.py                 # Koan base class + the `__` placeholder
    └── sensei.py               # walks the path and reports
```

The koan files under `koans/` are the only files you should need to edit. Walk
slowly. Read each `__` in context. Look up the docs when you need to. The
machine is patient; so should you be.

## Why?

Because the most efficient way to learn a language is to be wrong in small,
specific, immediately-corrected ways. The koan structure forces you to
confront one idea at a time and to verify your mental model against the
interpreter — which is the only authority that matters.

> Before enlightenment; chop wood, carry water.
> After enlightenment; chop wood, carry water.
