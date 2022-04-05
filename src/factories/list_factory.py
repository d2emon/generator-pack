import random

from utils.loaders import load_lines
from .factory import Factory


class ListFactory(Factory):
    """
    Generate random value from list
    """

    def __init__(self, data=()):
        self.__data = data

    @property
    def data(self):
        return self.__data

    def __len__(self):
        """
        :return: Data length
        """
        return len(self.data)

    def __call__(self, *args, **kwargs):
        """
        Select random item

        :param args: Roll args
        :param kwargs: Roll kwargs
        :return: Random item
        """
        items = list(self.find(*args, **kwargs))
        return random.choice(items) if len(items) > 0 else None

    def shuffle(self):
        """
        Shuffle items

        :return: Random items
        """
        values = [*self.data]
        random.shuffle(values)
        yield from values

    def unique(self, count=1):
        """
        Select random items

        :param count: Number of items to select
        :return: Random items
        """
        values = self.shuffle()
        for _ in range(count):
            yield next(values)

    @classmethod
    def from_text_file(cls, filename):
        data = list(load_lines(filename))
        return cls(data)

    def find(self, **kwargs):
        """
        Find dicts in data with fields

        :param kwargs: Fields to search
        :return: Filtered dicts
        """
        return filter(lambda item: all(item.get(k) == v for k, v in kwargs.items()), self.data)
