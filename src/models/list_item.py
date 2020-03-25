import random


class SimpleItem:
    default_data = []
    default_name = "Unnamed"
    __data = None

    def __init__(self, name=None):
        self.name = name or self.default_name

    def __str__(self):
        return self.name

    @classmethod
    def set_data(cls, data):
        cls.__data = data

    @classmethod
    def __next_data(cls):
        if cls.__data is None:
            cls.set_data(list(cls.default_data))
        if not len(cls.__data):
            return None
        # random.shuffle(cls.__data)
        return random.choice(cls.__data)

    @classmethod
    def next(cls):
        data = cls.__next_data()
        if data is None:
            return None
        return cls(data)
