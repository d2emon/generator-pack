from utils import load_lines

import random


class GeneratorData():
    def select(self):
        return None
        random.shuffle(data_list)


class ListData(GeneratorData):
    def __init__(self, data=[]):
        self.data = data

    def select(self, count=1):
        if count <= 1:
            return random.choice(self.data)
        random.shuffle(self.data)
        return self.data[0:count]

    @property
    def length(self):
        return len(self.data)


class FileData(ListData):
    def __init__(self, filename=""):
        ListData.__init__(self)
        self.filename = filename

    def select(self, count=1):
        if self.length < 1:
            self.data = load_lines(self.filename)
        return ListData.select(self, count=count)
