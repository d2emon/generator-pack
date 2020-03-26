import random


class SimpleItem:
    class NameGenerator:
        default = 'Unnamed'

        def __init__(self, data=None):
            self.__data = data or []

        @property
        def data(self):
            if self.__data is None:
                self.data = self.default
            return self.__data

        @data.setter
        def data(self, value):
            self.__data = value

        def __iter__(self):
            return self

        def __next__(self):
            return self.data

    class ItemGenerator:
        default = []

        def __init__(self, data=None):
            self.__data = data or []

        @property
        def data(self):
            if self.__data is None:
                self.data = list(self.default)
            return self.__data

        @data.setter
        def data(self, value):
            self.__data = value

        def __iter__(self):
            return self

        def __next__(self):
            if not len(self.__data):
                return None
            # random.shuffle(self.__data)
            return random.choice(self.data)

    default_name = "Unnamed"

    def __init__(self, name=None):
        self.__name = name

    @property
    def name(self):
        if self.__name is None:
            self.__name = next(self.NameGenerator())
        return self.__name

    def __str__(self):
        return self.name

    @classmethod
    def next(cls):
        return cls.from_data(next(cls.ItemGenerator()))

    @classmethod
    def from_data(cls, data):
        return cls(data) if data is not None else None
