import random

from os import path

from utils.loaders import load_lines


class GeneratorData:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.data)


class StaticData(GeneratorData):
    def __next__(self):
        return self.data


class ListData(GeneratorData):
    def __init__(self, data=()):
        super().__init__(data)
        self.items = self.generator()

    def generator(self, data=None):
        data = data or self.data
        while True:
            yield random.choice(data)

    def __next__(self):
        if self.items is None:
            raise StopIteration
        return next(self.items)

    def unique(self, count=1):
        random.shuffle(self.data)
        for i in range(count):
            yield self.data[i]
        raise StopIteration

    def __len__(self):
        return len(self.data)


class FileData(ListData):
    def __init__(self, filename=""):
        self.filename = path.abspath(path.join("..", filename))
        data = load_lines(self.filename)
        super().__init__(data)
