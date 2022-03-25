import random
from v1.fixtures.genders import MALE
from models.name import TextModel
from models.fng.names.name import Name
from v1.factories.factory import Factory
from factories.model.name.factories import NameFactory


class TextFactory(Factory):
    model = TextModel


class BaseNameFactory(Factory):
    model = Name


class ComplexFactory(BaseNameFactory):
    """
    Complex Factory

    Class fields:

    - factory_classes: Classes for child factories
    """
    factory_classes = {}

    def __init__(self, data=None):
        """
        :param data: Data blocks for factory
        """
        super().__init__(data or self.default_data)
        self.factories = self.get_factories(self.factory_data)

    @classmethod
    def get_factories(cls, factory_data):
        return {
            factory_id: factory(factory_data.data)
            for factory_id, factory in cls.factory_classes.items()
        }

    def factory(self, factory_id):
        return self.factories.get(factory_id, lambda item_id: None)

    def __getitem__(self, item_id):
        """
        Get child factory by factory_id

        :param item_id: Id of factory
        :return: Child factory
        """
        return self.factory(item_id)

    def from_factory(self, factory_id, *args, **kwargs):
        factory = self.factory(factory_id)
        return factory(*args, **kwargs) if factory is not None else None


class ComplexNameFactory(ComplexFactory):
    """
    Factory for name

    Class fields:
    - blocks: Data blocks
    """
    block_map = {}

    @classmethod
    def get_factories(cls, factory_data):
        return {
            factory_id: TextFactory(factory_data.find(block_id=block_id))
            for factory_id, block_id in cls.block_map.items()
        }

    def get_data(self, *args, **kwargs):
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
    def __call__(self, *args, factory_id=None, **kwargs):
        """
        Main factory method

        :param args: Model args
        :param factory_id: Factory Id
        :param kwargs: Fields to search in data
        :return: Model, built by factory
        """
        return self.from_factory(factory_id, *args, **kwargs)


class PercentFactory(PolymorphFactory):
    @property
    def default_percent(self):
        return random.randrange(100)

    def factory(self, factory_id=None):
        return self.factories.get(factory_id if factory_id is not None else self.default_percent)


class GenderFactory(PolymorphFactory):
    @property
    def default_gender(self):
        return MALE

    def factory(self, factory_id=None):
        return self.factories.get(factory_id if factory_id is not None else self.default_gender)


# TODO: Remove it
class GenderNameFactory(Factory):
    pass
