"""Classes bundle state and behavior. Everything is an object."""

from runner.koan import Koan, __


class AboutClasses(Koan):

    def test_creating_an_instance(self):
        class Dog:
            pass
        d = Dog()
        self.assertEqual(__, isinstance(d, Dog))

    def test_instance_attributes(self):
        class Dog:
            def __init__(self, name):
                self.name = name

        d = Dog("Rex")
        self.assertEqual(__, d.name)

    def test_class_attributes_are_shared(self):
        class Dog:
            species = "Canis familiaris"
            def __init__(self, name):
                self.name = name

        a = Dog("Rex")
        b = Dog("Fido")
        self.assertEqual(__, a.species)
        self.assertEqual(__, b.species)
        # Setting on the class affects all instances.
        Dog.species = "Doggo"
        self.assertEqual(__, a.species)

    def test_setting_on_instance_shadows_class_attribute(self):
        class Dog:
            sound = "woof"
        a = Dog()
        b = Dog()
        a.sound = "yip"
        self.assertEqual(__, a.sound)
        self.assertEqual(__, b.sound)

    def test_methods_receive_self(self):
        class Greeter:
            def __init__(self, name):
                self.name = name
            def hello(self):
                return f"hello, {self.name}"

        g = Greeter("Ada")
        self.assertEqual(__, g.hello())

    def test_class_method(self):
        class Counter:
            total = 0
            @classmethod
            def bump(cls):
                cls.total += 1
                return cls.total

        Counter.bump()
        Counter.bump()
        self.assertEqual(__, Counter.bump())

    def test_static_method(self):
        class MathBag:
            @staticmethod
            def add(a, b):
                return a + b

        self.assertEqual(__, MathBag.add(3, 4))

    def test_isinstance_and_type(self):
        class Animal: pass
        class Cat(Animal): pass
        c = Cat()
        self.assertEqual(__, isinstance(c, Cat))
        self.assertEqual(__, isinstance(c, Animal))
        # ``type()`` is exact, not polymorphic.
        self.assertEqual(__, type(c) is Cat)
        self.assertEqual(__, type(c) is Animal)

    def test_attributes_can_be_added_dynamically(self):
        class Empty:
            pass
        e = Empty()
        e.surprise = 42
        self.assertEqual(__, e.surprise)

    def test_slots_restrict_attributes(self):
        class Locked:
            __slots__ = ("x", "y")
            def __init__(self, x, y):
                self.x = x
                self.y = y

        p = Locked(1, 2)
        self.assertEqual(__, p.x)
        try:
            p.z = 99
        except AttributeError as e:
            self.assertEqual(__, type(e).__name__)
