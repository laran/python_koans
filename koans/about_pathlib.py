"""``pathlib`` gives filesystem paths first-class objects."""

from runner.koan import Koan, __


class AboutPathlib(Koan):

    def test_creating_a_path(self):
        from pathlib import PurePosixPath
        p = PurePosixPath("/usr/bin/python")
        self.assertEqual(__, str(p))

    def test_path_parts(self):
        from pathlib import PurePosixPath
        p = PurePosixPath("/usr/local/bin/python")
        self.assertEqual(__, p.parts)

    def test_path_name_and_stem(self):
        from pathlib import PurePosixPath
        p = PurePosixPath("/tmp/report.txt")
        self.assertEqual(__, p.name)
        self.assertEqual(__, p.stem)
        self.assertEqual(__, p.suffix)

    def test_parent(self):
        from pathlib import PurePosixPath
        p = PurePosixPath("/a/b/c.txt")
        self.assertEqual(__, str(p.parent))

    def test_with_suffix(self):
        from pathlib import PurePosixPath
        p = PurePosixPath("notes.md")
        self.assertEqual(__, str(p.with_suffix(".txt")))

    def test_with_name(self):
        from pathlib import PurePosixPath
        p = PurePosixPath("/a/b/c.txt")
        self.assertEqual(__, str(p.with_name("z.txt")))

    def test_joining_with_slash(self):
        from pathlib import PurePosixPath
        base = PurePosixPath("/var")
        self.assertEqual(__, str(base / "log" / "app.log"))

    def test_is_absolute(self):
        from pathlib import PurePosixPath
        self.assertEqual(__, PurePosixPath("/etc").is_absolute())
        self.assertEqual(__, PurePosixPath("etc").is_absolute())

    def test_match(self):
        from pathlib import PurePosixPath
        self.assertEqual(__, PurePosixPath("a/b/c.py").match("*.py"))
        self.assertEqual(__, PurePosixPath("a/b/c.txt").match("*.py"))
