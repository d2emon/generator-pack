from factories import ListFactory
from factories.nested import ThingFactory, MultipleFactory, ProbableFactory
from .simple_item import SimpleItem


class Thing(SimpleItem):
    class ChildrenFactory:
        default = []

        @classmethod
        def data(cls):
            yield from cls.default

        def __iter__(self):
            return self

        def __next__(self):
            return (child.factory().generate() for child in self.data() if child is not None)

    class NameFactory:
        default = ''

        def __iter__(self):
            return self

        def __next__(self):
            return self.default

    def __init__(self, name=None, children=None, **fields):
        super().__init__(**fields)
        self.__name = name
        self.__children = children
        self.__children_factory = None

    @classmethod
    def children_factory(cls):
        """
        Children factory getter
        :return: Data factory
        """
        if cls.__children_factory is None:
            cls.__children_factory = cls.ChildrenFactory()
        return cls.__children_factory

    @property
    def children(self):
        if self.__children is None:
            self.__children = list(next(self.children_factory()))
        return self.__children

    @children.setter
    def children(self, value):
        self.__children = value

    @classmethod
    def children_data(cls):
        return list(cls.ChildrenFactory.data())

    @classmethod
    def generate_name(cls):
        return next(cls.NameFactory())

    @classmethod
    def generate_children(cls):
        return next(cls.ChildrenFactory())

    @classmethod
    def next(cls):
        return cls(
            name=next(cls.new_name_factory()),
            children=list(next(cls.new_children_factory())),
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

    @classmethod
    def new_name_factory(cls):
        return cls.NameFactory()

    @classmethod
    def new_children_factory(cls):
        return cls.ChildrenFactory()

    # Search

    def __by_class(self, child_class):
        return (child for child in self.children if isinstance(child, child_class))

    def all_by_class(self, child_class):
        return list(self.__by_class(child_class))

    def first_by_class(self, child_class):
        return next(self.__by_class(child_class), None)
