import random
from v3.models.encounter_model import Encounter
from .factory_data import FactoryData


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
        self.factory_data = FactoryData(data or self.default_data)

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

    def validate(self, items) -> dict:
        """
        Validate items

        :param items: Generated items
        :return: Validated items
        """
        return items

    def build(self, *args, **kwargs):
        return self.model(*args, **kwargs)

    def get_data(self, *args, **kwargs):
        return self.factory_data.get_random(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        """
        Main factory method

        :param args: Model args
        :param kwargs: Fields to search in data
        :return: Model, built by factory
        """
        values = self.get_data(*args, **kwargs)
        values = self.validate(values)
        return self.build(*args, **values)

    def buildMultiple(self, count, *args, **kwargs):
        """
        Build multiple models

        :param count: Count of models
        :param args: Model args
        :param kwargs: Fields to search in data
        :return: Models, built by factory
        """
        for generated_id in range(count):
            yield self(*args, generated_id=generated_id, **kwargs)
