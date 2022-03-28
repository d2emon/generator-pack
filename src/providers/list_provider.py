from factories.list_factory import ListFactory
from .provider import ProviderFactory


class ComplexFactory(ProviderFactory):
    def __init__(self, *factories):
        self.factories = list(factories)

    def __call__(self):
        return [next(factory.items) for factory in self.factories]

    def __add__(self, other):
        return ComplexFactory(*self.factories, other)

    @classmethod
    def from_lists(cls, *parts):
        return cls(*[ListFactory(provider) for provider in parts])


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
