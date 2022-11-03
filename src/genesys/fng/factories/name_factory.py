import random
from utils.genders import MALE
from models.name.name import TextModel
from models.fng.names.name import Name
from factories.factory import Factory
from factories.model.name.factories import NameFactory
from genesys.fng.factories.validators import item_is_not_unique, item_equals, generate_while


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
        self.data = data or self.default_data
        self.factories = self.get_factories(self.data)

    @classmethod
    def get_factories(cls, factory_data):
        return {
            factory_id: factory(factory_data)
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

    validators = {}

    @classmethod
    def get_factories(cls, factory_data):
        def text_factory(block_id):
            items = [item for item in factory_data if item['block_id'] == block_id]

            def get_item(*args, item_id=None, **kwargs):
                if item_id is not None:
                    return next(item for item in items if item['item_id'] == item_id)

                return random.choice(items)

            def build(*args, **kwargs):
                item = get_item(*args, **kwargs)

                if item is None:
                    return None

                return item.get('value')

            return build

        return {
            # factory_id: TextFactory(factory_data.find(block_id=block_id))
            # factory_id: lambda: next(filter(lambda item: item['block_id'] == block_id, factory_data))
            factory_id: text_factory(block_id)
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

    def validate_item(self, item_id, item, items):
        validator = self.validators.get(item_id)

        if validator is None:
            return items

        items[item_id] = generate_while(
            item,
            validator(items),
            self[item_id],
        )

        return items

    def validate(self, items):
        for item_id, item in items.items():
            items = self.validate_item(item_id, item, items)

        return items

    def __call__(self, *args, **kwargs):
        items = self.get_data()
        validated = self.validate(items)
        return self.model(**validated)


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
