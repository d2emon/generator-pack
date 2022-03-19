import random
from genesys.nested.factories.v2.thing import Thing
from genesys.nested.factories.v2.children import ChildFactory
from .universe import *
from .life import *


class Things:
    FACTORIES = {}

    @classmethod
    def from_contents(cls, content):
        items = (c() for c in content)
        cls.FACTORIES.update({item.name: item for item in items})

    @classmethod
    def add_thing(cls, name, children_data, factory=None):
        cls.FACTORIES[name] = Thing.from_str(name, children_data, factory)

    @classmethod
    def get_thing(cls, key):
        return cls.FACTORIES.get(key)

    @classmethod
    def cleanup(cls):
        for key, factory in cls.FACTORIES.items():
            factory.clear()

    @classmethod
    def get_factories(cls, name):
        def inherit_factories(name):
            return cls.get_factories(name.value[1:])

        def get_children_factories(item):
            if item is None:
                return
            for factory in item.factories:
                if isinstance(factory, list):
                    yield random.choice(factory)
                elif isinstance(factory.value, str) and factory.value[0] == '.':
                    yield from cls.get_factories(factory.value[1:])
                    # self.type.generators[i] = None
                else:
                    yield factory

        # return list(filter(lambda item: item is not None, self.type.generators + to_concat))
        return [f for f in get_children_factories(Things.get_thing(name)) if f is not None]
