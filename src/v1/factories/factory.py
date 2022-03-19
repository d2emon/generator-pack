import random
from v1.models.encounters import Encounter


class Factory:
    """
    Base factory class

    Class fields:
    - default_data: Default data for factory
    """
    default_data = []
    __instance = None

    def __init__(self, data=None):
        """
        Create factory

        :param data: Array of data dicts
        """
        self.data = data or self.default_data
        self.data = list(self.data)

    @classmethod
    def instance(cls):
        """
        Get static instance of factory

        :return: Static instance
        """
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    @property
    def model(self):
        """
        Build model

        :return: Model, built by factory
        """
        raise NotImplementedError()

    def find(self, *args, **kwargs):
        """
        Find dicts in data with fields

        :param kwargs: Fields to search
        :return: Filtered dicts
        """
        return filter(lambda item: all(item.get(k) == v for k, v in kwargs.items()), self.data)

    def validate(self, items) -> dict:
        """
        Validate items

        :param items: Name items
        :return: Validated name items
        """
        return items

    def generate(self, *args, **kwargs):
        """
        Generate value from data

        :param args: Args for generation
        :param kwargs: Kwargs for generation
        :return: Generated value
        """
        items = list(self.find(*args, **kwargs))
        if len(items) == 0:
            return {}

        return random.choice(items)

    def multiple(self, count=10, *args, **kwargs):
        """
        Build multiple models

        :param count: Count of models
        :param args: Model args
        :param kwargs: Fields to search in data
        :return: Models, built by factory
        """
        for generated_id in range(count):
            yield self(*args, generated_id=generated_id * 10, **kwargs)

    def __call__(self, *args, **kwargs):
        """
        Main factory method

        :param args: Model args
        :param kwargs: Fields to search in data
        :return: Model, built by factory
        """
        values = self.generate(*args, **kwargs)
        values = self.validate(values)
        return self.model(*args, **values)
