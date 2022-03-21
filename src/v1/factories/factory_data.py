import random


class FactoryData:
    def __init__(self, data) -> None:
        self.data = list(data)

    def find(self, *args, **kwargs):
        """
        Find dicts in data with fields

        :param kwargs: Fields to search
        :return: Filtered dicts
        """
        for item in self.data:
            if all(item.get(k) == v for k, v in kwargs.items()):
                yield item

    def get_random(self, *args, **kwargs) -> dict:
        """
        Build value from data

        :param args: Args for generation
        :param kwargs: Kwargs for generation
        :return: Generated value
        """
        items = list(self.find(*args, **kwargs))
        return random.choice(items) if len(items) > 0 else {}
