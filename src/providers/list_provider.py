import random
from .provider import DataProvider


class ListProvider(DataProvider):
    def __init__(self, data=()):
        self.data = data
        self.__items = []
        self.unique = self.shuffle()

    def __next__(self):
        return random.choice(self.data)

    def shuffle(self):
        self.__items = list(self.data)
        random.shuffle(self.__items)
        return self.__items

    def __len__(self):
        return len(self.data)
