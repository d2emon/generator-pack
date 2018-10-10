import os
import random

from utils.loaders import load_lines


class DataProvider:
    @property
    def items(self):
        raise NotImplementedError

    def __iter__(self):
        return self

    def __next__(self):
        if self.items is None:
            raise StopIteration
        return next(self.items)

    def __add__(self, other):
        return ProvidersList(self, other)


class ProvidersList(DataProvider):
    def __init__(self, *providers):
        self.providers = list(providers)

    @property
    def items(self):
        if len(self.providers) < 1:
            raise StopIteration
        while True:
            yield [next(provider.items) for provider in self.providers]

    def __add__(self, other):
        self.providers.append(other)
        return self


class StaticProvider(DataProvider):
    def __init__(self, value=None):
        self.value = value

    @property
    def items(self):
        if self.value is None:
            raise StopIteration
        while True:
            yield self.value


class GeneratorProvider(DataProvider):
    def __init__(self, generator=None):
        self.generator = generator

    @property
    def items(self):
        if self.generator is None:
            raise StopIteration
        while True:
            yield self.generator.generate()


class ListProvider(DataProvider):
    def __init__(self, data=()):
        self.data = data
        self._items = []
        self.unique = self.shuffle()

    def shuffle(self):
        self._items = list(self.data)
        random.shuffle(self._items)
        return self._items

    @property
    def items(self):
        while True:
            yield random.choice(self.data)

    def __len__(self):
        return len(self.data)


class FileProvider(ListProvider):
    def __init__(self, filename=""):
        self.filename = os.path.abspath(os.path.join("..", filename))
        data = load_lines(self.filename)
        super().__init__(data)
