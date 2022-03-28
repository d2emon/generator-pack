from factories.factory import Factory
from factories.list_factory import ListFactory


class ComplexFactory(Factory):
    def __init__(self, *factories):
        self.factories = list(factories)

    def __call__(self):
        return [next(factory.items) for factory in self.factories]

    def __add__(self, other):
        return ComplexFactory(*self.factories, other)

    @classmethod
    def from_lists(cls, *parts):
        return cls(*[ListFactory(provider) for provider in parts])
