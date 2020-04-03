import random
from genesys.nested.models import Placeholder, Model


class ProviderFactory:
    def __init__(self, provider):
        self.provider = provider

    def __iter__(self):
        return self

    def __next__(self):
        raise NotImplementedError()


class ThingBuilder:
    class DataProvider:
        pass

    class NameFactory(ProviderFactory):
        def __next__(self):
            return None

    class ChildrenFactory(ProviderFactory):
        def builders(self):
            yield from []

        def __next__(self):
            return [Placeholder(builder) for builder in self.builders() if builder is not None]

    model = Model

    def __init__(self, provider=None):
        self.provider = provider or self.DataProvider()
        self.thing = None
        self.name_factory = self.NameFactory(self.provider)
        self.children_factory = self.ChildrenFactory(self.provider)

    def create_thing(self, **kwargs):
        return self.model(**kwargs)

    @property
    def default_name(self):
        return self.model.__name__

    def __build_name(self):
        # return self.base or next(self.name_factory) or self.default_name
        return next(self.name_factory) or self.default_name

    def __build_children(self):
        return next(self.children_factory)

    def build(self):
        self.thing = self.create_thing(
            name=self.__build_name(),
            children=self.__build_children(),
        )
        print(self.__build_name())
        print(self.__build_children())
        return self.thing

    @classmethod
    def probable(cls, probability=100):
        return cls if random.uniform(0, 100) < probability else None

    @classmethod
    def multiple(cls, min_items=1, max_items=None):
        count = random.randint(min_items, max_items) if max_items is not None else min_items
        for _ in range(count):
            yield cls

    @classmethod
    def choice(cls, items):
        return random.choice(items) if len(items) > 0 else None
