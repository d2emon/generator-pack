import random
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
        return random.choice(self.data)

    def unique(self, count=1):
        """
        Select random items

        :param count: Number of items to select
        :return: Random items
        """
        values = [*self.data]
        random.shuffle(values)
        for item in values[:count]:
            yield item
