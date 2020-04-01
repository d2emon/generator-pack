import random


class DataFactory:
    default = None
    __instance = None

    def __init__(self, data=default):
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        return self.data

    @classmethod
    def instance(cls):
        if cls.__instance is None:
            cls.__instance = cls(cls.default)
        return cls.__instance

    @classmethod
    def next(cls, default=None):
        return next(cls.instance()) or default


class NameFactory(DataFactory):
    pass


class BaseFactory(DataFactory):
    default = []

    def __next__(self):
        return random.choice(self.data) if self.data and len(self.data) > 0 else None


class ChildrenFactory(DataFactory):
    default = [[]]

    def children_classes(self):
        for group in self.data:
            yield from group

    def __next__(self):
        return [c() for c in self.children_classes() if c is not None]

