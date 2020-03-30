from factories.nested.thing import ThingFactory, MultipleFactory, ProbableFactory, ListFactory


class Thing:
    class ChildrenGenerator:
        default = []

        @classmethod
        def data(cls):
            yield from cls.default

        @classmethod
        def generate(cls):
            return (child.factory().generate() for child in cls.data() if child is not None)

    class NameGenerator:
        default = ''

        @classmethod
        def generate(cls):
            return cls.default

    def __init__(self, name=None, children=None):
        self.__name = name
        self.__children = children

    @property
    def name(self):
        if self.__name is None:
            self.__name = self.NameGenerator.generate()
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def children(self):
        if self.__children is None:
            self.__children = list(self.ChildrenGenerator.generate())
        return self.__children

    @children.setter
    def children(self, value):
        self.__children = value

    def __str__(self):
        return self.name

    @classmethod
    def children_data(cls):
        return list(cls.ChildrenGenerator.data())

    @classmethod
    def generate_name(cls):
        return cls.NameGenerator.generate()

    @classmethod
    def generate(cls):
        return cls(
            cls.NameGenerator.generate(),
            list(cls.ChildrenGenerator.generate()),
        )

    # Factories

    @classmethod
    def factory(cls):
        return ThingFactory(cls)

    @classmethod
    def multiple_factory(cls, min_count, max_count=None):
        return MultipleFactory(cls, min_count, max_count)

    @classmethod
    def probable_factory(cls, probability):
        return ProbableFactory(cls, probability)

    @classmethod
    def list_factory(cls, items):
        return ListFactory(items)

    # Search

    def __child_by_class(self, child_class):
        return (child for child in self.children if isinstance(child, child_class))

    def all(self, child_class):
        return list(self.__child_by_class(child_class))

    def first(self, child_class):
        return next(self.__child_by_class(child_class), None)
