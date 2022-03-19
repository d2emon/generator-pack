import random
from v1.fixtures.genders import MALE
from v3.models import TextModel
from v1.models.fng.names.name import Name
from v1.factories.factory import Factory


class TextFactory(Factory):
    model = TextModel


class ComplexFactory(Factory):
    """
    Complex Factory

    Class fields:

    - factory_classes: Classes for child factories
    """
    model = Name
    factory_classes = {}

    def __init__(self, data=None):
        """
        :param data: Data blocks for factory
        """
        super().__init__(data)
        self.factories = {
            factory_id: factory(data or self.default_data)
            for factory_id, factory in self.factory_classes.items()
        }

    def __getitem__(self, item_id):
        """
        Get child factory by factory_id

        :param item_id: Id of factory
        :return: Child factory
        """
        return self.factory(item_id)

    def factory(self, factory_id=None):
        return self.factories.get(factory_id)


class NameFactory(ComplexFactory):
    """
    Factory for name

    Class fields:
    - blocks: Data blocks
    """
    block_map = {}

    def __init__(self, data=None):
        """
        :param data: Data blocks for factory
        """
        super().__init__(data)
        self.factories = {
            factory_id: TextFactory(self.find(block_id=block_id))
            for factory_id, block_id in self.block_map.items()
        }

    def generate(self, *args, generated_id=0, **kwargs):
        """
        Generate value from data

        :param args: Args for generation
        :param kwargs: Kwargs for generation
        :return: Generated value
        """
        return {
            item_id: factory(*args, **kwargs)
            for item_id, factory in self.factories.items()
            if factory is not None
        }


class PolymorphFactory(ComplexFactory):
    @property
    def default_gender(self):
        return MALE

    @property
    def default_percent(self):
        return random.randrange(100)

    def __call__(self, *args, factory_id=None, **kwargs):
        """
        Main factory method

        :param args: Model args
        :param factory_id: Factory Id
        :param kwargs: Fields to search in data
        :return: Model, built by factory
        """
        factory = self.factory(factory_id)
        return factory(*args, **kwargs) if factory is not None else None


class PercentFactory(PolymorphFactory):
    def factory(self, factory_id=None):
        return self.factories.get(factory_id if factory_id is not None else self.default_percent)

    def multiple(self, count=10, *args, **kwargs):
        """
        Build multiple models

        :param count: Count of models
        :param args: Model args
        :param kwargs: Fields to search in data
        :return: Models, built by factory
        """
        for generated_id in range(count):
            yield self(*args, factory_id=generated_id * 10, **kwargs)


class GenderFactory(PolymorphFactory):
    def factory(self, factory_id=None):
        return self.factories.get(factory_id if factory_id is not None else self.default_gender)
