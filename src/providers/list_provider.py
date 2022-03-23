from factories.list_factory import ListFactory
from utils.loaders import load_lines
from .provider import ProviderFactory


class ComplexFactory(ProviderFactory):
    def __init__(self, *factories):
        self.factories = list(factories)

    def __call__(self):
        return [next(factory.items) for factory in self.factories]

    def __add__(self, other):
        return ComplexFactory(*self.factories, other)


class ListProvider(ProviderFactory, ListFactory):
    def __init__(self, data=()):
        super().__init__(data)

        self.__items = []
        self.unique = self.shuffle()

    def shuffle(self):
        self.__items = super().shuffle()
        return self.__items

    def __add__(self, other):
        return ComplexFactory(self, other)

    @classmethod
    def multiple(cls, parts):
        return ComplexFactory(*[cls(provider) for provider in parts])

    @classmethod
    def from_file(cls, filename):
        return cls(load_lines(filename))


class StaticListProvider(ListProvider):
    static_data = []

    def __init__(self):
        super().__init__(self.static_data)


class ListDataProvider(ProviderFactory):
    default_data = ()

    def __init__(self, data=None):
        self.__data = data

    @property
    def data(self):
        if self.__data is None:
            self.__data = self.default_data
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    def __call__(self):
        raise NotImplementedError()
