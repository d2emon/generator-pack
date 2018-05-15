from utils import load_lines

import random


class GeneratorData:
    def __init__(self, data=None):
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.data)


class StaticData(GeneratorData):
    def __next__(self):
        return self.data


class ListData(GeneratorData):
    def __init__(self, data=[]):
        self.data = data
        self.items = None
        self.load(data)

    def load(self, data):
        self.data = data
        self.items = self.generator(data)

    def generator(self, data):
        self.data = data
        while True:
            yield random.choice(self.data)

    def __next__(self):
        if self.items is None:
            raise StopIteration
        return self.items.__next__()

    def unique(self, count=1):
        random.shuffle(self.data)
        return self.data[:count]

    def shuffled(self):
        random.shuffle(self.data)
        return self.data

    @property
    def length(self):
        return len(self.data)


class FileData(ListData):
    def __init__(self, filename=""):
        self.load(filename)

    def load(self, filename):
        self.filename = filename
        lines = load_lines(self.filename)
        self.items = self.generator(lines)
