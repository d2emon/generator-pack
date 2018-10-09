import os
import random

from utils.loaders import load_lines


class DataProvider:
    instance = None
    data = None

    def __init__(self, data=None):
        if self.instance is None:
            self.instance = self
            self.instance.set_data(data)

    @classmethod
    def set_data(cls, data):
        if cls.instance is None:
            cls.instance = cls()
        cls.instance.data = data

    @property
    def items(self):
        raise NotImplementedError

    def __iter__(self):
        return self.instance

    def __next__(self):
        if self.items is None:
            raise StopIteration
        return next(self.items)


class StaticProvider(DataProvider):
    instance = None
    data = None

    @property
    def items(self):
        while True:
            yield self.data


class ListProvider(DataProvider):
    instance = None
    data = None
    _items = None

    @classmethod
    def shuffle(cls):
        cls._items = list(cls.data)
        random.shuffle(cls._items)
        return cls._items

    @property
    def items(self):
        while True:
            yield random.choice(self.data)

    @classmethod
    def unique(cls):
        for item in cls._items:
            yield item

    def __len__(self):
        return len(self.data)


class FileData(ListProvider):
    instance = None
    _data = None
    filename = None

    def set_data(self, filename=""):
        self.filename = os.path.abspath(filename)
        _data = load_lines(self.filename)
