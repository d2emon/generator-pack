from factories.model_factory import ModelFactory
from .multiple import MultipleFactory
from .probable import ProbableFactory
from ..list_factory import ListFactory


class ThingFactories:
    class ChildrenFactory:
        default = []

        @classmethod
        def data(cls):
            yield from cls.default

        def __iter__(self):
            return self

        def __next__(self):
            return (child.factory().generate() for child in self.data() if child is not None)

        def __call__(self):
            return list(next(self))

    class DataFactory:
        default = []

    class NameFactory:
        default = ''

        def __iter__(self):
            return self

        def __next__(self):
            return self.default

        def __call__(self):
            return next(self)

    __children_factory = None
    __data_factory = None
    __name_factory = None

    @classmethod
    def children_factory(cls):
        """
        Children factory getter
        :return: Data factory
        """
        if cls.__children_factory is None:
            cls.__children_factory = cls.ChildrenFactory()
        return cls.__children_factory

    @classmethod
    def data_factory(cls):
        """
        Data factory getter
        :return: Data factory
        """
        if cls.__data_factory is None:
            cls.__data_factory = cls.DataFactory()
        return cls.__data_factory

    @classmethod
    def name_factory(cls):
        """
        Name factory getter
        :return: Name factory
        """
        if cls.__name_factory is None:
            cls.__name_factory = cls.NameFactory()
        return cls.__name_factory

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
        return ModelFactory(cls)

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
