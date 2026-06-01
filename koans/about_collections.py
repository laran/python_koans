"""The ``collections`` module: specialized containers beyond list/dict/tuple."""

from runner.koan import Koan, __


class AboutCollections(Koan):

    def test_counter(self):
        from collections import Counter
        c = Counter("banana")
        self.assertEqual(__, c["a"])
        self.assertEqual(__, c["b"])
        self.assertEqual(__, c["z"])  # missing keys are 0, not KeyError

    def test_counter_most_common(self):
        from collections import Counter
        c = Counter("mississippi")
        self.assertEqual(__, c.most_common(2))

    def test_counter_arithmetic(self):
        from collections import Counter
        a = Counter(a=3, b=1)
        b = Counter(a=1, b=2, c=4)
        self.assertEqual(__, a + b)
        self.assertEqual(__, a - b)

    def test_defaultdict(self):
        from collections import defaultdict
        d = defaultdict(list)
        d["a"].append(1)
        d["a"].append(2)
        d["b"].append(3)
        self.assertEqual(__, dict(d))

    def test_defaultdict_with_int(self):
        from collections import defaultdict
        tally = defaultdict(int)
        for ch in "banana":
            tally[ch] += 1
        self.assertEqual(__, dict(tally))

    def test_ordereddict_preserves_order(self):
        # Regular dicts preserve order too — OrderedDict adds explicit
        # ordering operations like ``move_to_end``.
        from collections import OrderedDict
        d = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
        d.move_to_end("a")
        self.assertEqual(__, list(d.keys()))

    def test_deque(self):
        from collections import deque
        d = deque([1, 2, 3])
        d.appendleft(0)
        d.append(4)
        self.assertEqual(__, list(d))
        self.assertEqual(__, d.popleft())
        self.assertEqual(__, d.pop())

    def test_deque_with_maxlen(self):
        from collections import deque
        d = deque(maxlen=3)
        for n in range(5):
            d.append(n)
        self.assertEqual(__, list(d))

    def test_namedtuple(self):
        from collections import namedtuple
        Point = namedtuple("Point", ["x", "y"])
        p = Point(3, 4)
        self.assertEqual(__, p.x + p.y)
        self.assertEqual(__, p._asdict())

    def test_chainmap(self):
        from collections import ChainMap
        defaults = {"theme": "light", "lang": "en"}
        overrides = {"theme": "dark"}
        view = ChainMap(overrides, defaults)
        self.assertEqual(__, view["theme"])
        self.assertEqual(__, view["lang"])
