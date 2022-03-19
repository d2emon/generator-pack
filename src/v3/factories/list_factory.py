import random
from .factory import Factory


class ListFactory(Factory):
    """
    Factory to get data from list
   """

    def __init__(self, data, *args, **kwargs):
        """
        Create factory

        :param data: Array of data dicts
        """
        super().__init__(data)
        self.data = list(data)

    def find(self, *args, **kwargs):
        """
        Find dicts in data with fields

        :param kwargs: Fields to search
        :return: Filtered dicts
        """
        return filter(lambda item: all(item.get(k) == v for k, v in kwargs.items()), self.data)

    def generate(self, *args, **kwargs):
        """
        Generate value from data

        :param args: Args for generation
        :param kwargs: Kwargs for generation
        :return: Generated value
        """
        items = list(self.find(*args, **kwargs))
        return random.choice(items) if len(items) > 0 else {}

    def validate(self, items) -> dict:
        """
        Validate items

        :param items: Name items
        :return: Validated name items
        """
        return items

    def __call__(self, *args, **kwargs) -> dict:
        """
        Main factory method

        :param args: Search args
        :param kwargs: Fields to search in data
        :return: Dictionary, built by factory
        """
        values = self.generate(*args, **kwargs)
        values = self.validate(values)
        return values
