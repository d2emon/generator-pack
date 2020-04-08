import random


class ProviderFactory:
    def __init__(self, provider):
        self.provider = provider

    def __iter__(self):
        return self

    def __next__(self):
        raise NotImplementedError()


class ListFactory:
    default = []

    def __init__(self, data):
        self.data = data or self.default

    def __iter__(self):
        return self

    def __next__(self):
        data = self.data
        return random.choice(data) if len(data) > 0 else None


class ThingBuilder:
    data_provider_class = None

    class DataProvider:
        pass

    class NameFactory(ProviderFactory):
        def __next__(self):
            return None

    class BaseFactory(ProviderFactory):
        @classmethod
        def factory(cls, data):
            class SubFactory(ListFactory):
                @property
                def data(self):
                    return data

            return SubFactory

        def __next__(self):
            raise NotImplementedError()

    class ChildrenFactory(ProviderFactory):
        def builders(self):
            yield from []

        def __next__(self):
            return [model.placeholder() for model in self.builders() if model is not None]

    def __init__(self, provider=None):
        data_provider_class = self.data_provider_class or self.DataProvider
        self.provider = provider or data_provider_class()
        self.thing = None
        self.name_factory = self.NameFactory(self.provider)
        self.base_factory = self.BaseFactory(self.provider)
        self.children_factory = self.ChildrenFactory(self.provider)

    def create_thing(self, **kwargs):
        return self.model(**kwargs)

    @property
    def default_name(self):
        return self.model.default_name or self.model.__name__

    def __build_base(self):
        return next(self.base_factory)

    def __build_name(self):
        return self.__build_base() or next(self.name_factory) or self.default_name

    def __build_children(self):
        return next(self.children_factory)

    def build(self):
        return {
            # 'name': self.__build_name(),
            'children': self.__build_children(),
        }

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
