"""Inheritance: deriving classes from classes. ``super()`` walks the MRO."""

from runner.koan import Koan, __


class AboutInheritance(Koan):

    def test_single_inheritance(self):
        class Animal:
            def sound(self):
                return "generic"

        class Dog(Animal):
            def sound(self):
                return "woof"

        self.assertEqual(__, Dog().sound())
        self.assertEqual(__, Animal().sound())

    def test_super_calls_parent(self):
        class Greeter:
            def hello(self):
                return "hello"

        class LoudGreeter(Greeter):
            def hello(self):
                return super().hello() + "!"

        self.assertEqual(__, LoudGreeter().hello())

    def test_inheritance_inherits_attributes(self):
        class A:
            kind = "A"
        class B(A):
            pass
        self.assertEqual(__, B().kind)

    def test_isinstance_with_inheritance(self):
        class Animal: pass
        class Dog(Animal): pass
        d = Dog()
        self.assertEqual(__, isinstance(d, Dog))
        self.assertEqual(__, isinstance(d, Animal))

    def test_issubclass(self):
        class A: pass
        class B(A): pass
        self.assertEqual(__, issubclass(B, A))
        self.assertEqual(__, issubclass(A, B))

    def test_multiple_inheritance(self):
        class Swimmer:
            def move(self):
                return "swim"

        class Flyer:
            def move(self):
                return "fly"

        class Duck(Swimmer, Flyer):
            pass

        # MRO is left-to-right; first parent wins.
        self.assertEqual(__, Duck().move())

    def test_method_resolution_order(self):
        class A: pass
        class B(A): pass
        class C(A): pass
        class D(B, C): pass
        # D -> B -> C -> A -> object
        self.assertEqual(__, [cls.__name__ for cls in D.__mro__])

    def test_super_with_multiple_inheritance(self):
        class A:
            def name(self):
                return ["A"]
        class B(A):
            def name(self):
                return ["B"] + super().name()
        class C(A):
            def name(self):
                return ["C"] + super().name()
        class D(B, C):
            def name(self):
                return ["D"] + super().name()
        # super() follows the MRO so each parent is visited exactly once.
        self.assertEqual(__, D().name())

    def test_object_is_the_ultimate_ancestor(self):
        class Anything: pass
        self.assertEqual(__, issubclass(Anything, object))

    def test_abstract_base_class(self):
        from abc import ABC, abstractmethod

        class Shape(ABC):
            @abstractmethod
            def area(self):
                ...

        class Square(Shape):
            def __init__(self, side):
                self.side = side
            def area(self):
                return self.side * self.side

        self.assertEqual(__, Square(4).area())

        try:
            Shape()
        except TypeError as e:
            self.assertEqual(__, type(e).__name__)
