"""Lists are ordered, mutable sequences."""

from runner.koan import Koan, __


class AboutLists(Koan):

    def test_creating_lists(self):
        empty = []
        nums = [1, 2, 3]
        self.assertEqual(__, len(empty))
        self.assertEqual(__, len(nums))

    def test_list_constructor(self):
        # ``list(iterable)`` builds a list from any iterable.
        self.assertEqual(__, list("abc"))
        self.assertEqual(__, list(range(3)))

    def test_indexing(self):
        items = ["a", "b", "c", "d"]
        self.assertEqual(__, items[0])
        self.assertEqual(__, items[-1])
        self.assertEqual(__, items[-2])

    def test_slicing(self):
        items = [0, 1, 2, 3, 4, 5]
        self.assertEqual(__, items[1:4])
        self.assertEqual(__, items[:3])
        self.assertEqual(__, items[3:])
        self.assertEqual(__, items[::2])
        self.assertEqual(__, items[::-1])

    def test_slicing_returns_a_new_list(self):
        items = [1, 2, 3]
        copy = items[:]
        copy.append(4)
        self.assertEqual(__, items)
        self.assertEqual(__, copy)

    def test_append_mutates_in_place(self):
        items = [1, 2]
        result = items.append(3)
        self.assertEqual(__, items)
        # ``append`` returns None — it's a mutating method.
        self.assertEqual(__, result)

    def test_extend_versus_append(self):
        a = [1, 2]
        a.append([3, 4])
        self.assertEqual(__, a)

        b = [1, 2]
        b.extend([3, 4])
        self.assertEqual(__, b)

    def test_insert(self):
        items = ["a", "c"]
        items.insert(1, "b")
        self.assertEqual(__, items)

    def test_pop(self):
        items = [1, 2, 3]
        last = items.pop()
        self.assertEqual(__, last)
        self.assertEqual(__, items)

    def test_pop_at_index(self):
        items = ["a", "b", "c"]
        gone = items.pop(0)
        self.assertEqual(__, gone)
        self.assertEqual(__, items)

    def test_remove_first_match(self):
        items = [1, 2, 3, 2]
        items.remove(2)
        self.assertEqual(__, items)

    def test_sort_mutates(self):
        items = [3, 1, 2]
        items.sort()
        self.assertEqual(__, items)

    def test_sorted_returns_new(self):
        items = [3, 1, 2]
        new = sorted(items)
        self.assertEqual(__, items)
        self.assertEqual(__, new)

    def test_reverse_mutates(self):
        items = [1, 2, 3]
        items.reverse()
        self.assertEqual(__, items)

    def test_concatenation_and_repetition(self):
        self.assertEqual(__, [1, 2] + [3, 4])
        self.assertEqual(__, [0] * 4)

    def test_in_operator(self):
        self.assertEqual(__, 2 in [1, 2, 3])
        self.assertEqual(__, 4 in [1, 2, 3])

    def test_count_and_index(self):
        items = ["a", "b", "a", "c"]
        self.assertEqual(__, items.count("a"))
        self.assertEqual(__, items.index("b"))

    def test_lists_are_references(self):
        # Assignment shares the same underlying list.
        a = [1, 2, 3]
        b = a
        b.append(4)
        self.assertEqual(__, a)

    def test_copying_a_list(self):
        # Use ``.copy()`` or ``list(other)`` or ``other[:]``.
        a = [1, 2, 3]
        b = a.copy()
        b.append(4)
        self.assertEqual(__, a)

    def test_list_unpacking(self):
        a, b, c = [1, 2, 3]
        self.assertEqual(__, b)

    def test_starred_unpacking(self):
        first, *rest = [1, 2, 3, 4]
        self.assertEqual(__, first)
        self.assertEqual(__, rest)

        *head, last = [1, 2, 3, 4]
        self.assertEqual(__, head)
        self.assertEqual(__, last)

    def test_min_max_sum(self):
        items = [3, 1, 4, 1, 5, 9, 2, 6]
        self.assertEqual(__, min(items))
        self.assertEqual(__, max(items))
        self.assertEqual(__, sum(items))
