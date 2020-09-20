import random
from .provider import DataProvider


class ListProvider(DataProvider):
    def __init__(self, data=()):
        self.data = data
        self.__items = []
        self.unique = self.shuffle()

    def __next__(self):
        return random.choice(self.data) if len(self.data) > 0 else None

    def shuffle(self):
        self.__items = list(self.data)
        random.shuffle(self.__items)
        return self.__items

    def __len__(self):
        return len(self.data)


class StaticListProvider(ListProvider):
    static_data = []

    def __init__(self):
        super().__init__(self.static_data)


class ListDataProvider(DataProvider):
    default_data = ()

    def __init__(self, data=None):
        self.__data = data

    def __next__(self):
        raise NotImplementedError()

    @property
    def data(self):
        if self.__data is None:
            self.__data = self.default_data
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value
