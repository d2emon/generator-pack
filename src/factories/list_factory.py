import random
from .factory import Factory


class ListFactory(Factory):
    def __init__(self, provider=None):
        super().__init__(provider)
        self.data = []

    def model(self, *args, **kwargs):
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
        data = [*self.data]
        random.shuffle(data)
        for item in data[:count]:
            yield item

    def __len__(self):
        """
        :return: Data length
        """
        return len(self.data)
