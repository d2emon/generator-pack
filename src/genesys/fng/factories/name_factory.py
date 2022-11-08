import random
from utils.genders import MALE
from models.fng.names.name import Name
from factories.factory import Factory
from genesys.fng.factories.validators import generate_while


class DbFactory(Factory):
    default_data = None

    def __init__(self, data=None):
        """
        :param data: Data blocks for factory
        """
        self.data = data or self.default_data


class ModelFactory(Factory):
    model = Name

    def get_data(self, *args, **kwargs) -> dict:
        """
        Get data for model.

        :param args: Args for data
        :param kwargs: Kwargs for data
        :return: Data for model
        :rtype: dict
        """
        return {}

    def __call__(self, *args, **kwargs):
        """
        Build model.
        
        :param args: Args for model
        :param kwargs: Kwargs for model
        :return: Model
        :rtype: dict
        """
        items = self.get_data(*args, **kwargs)
        return self.model(**items)


class BaseNameFactory(ModelFactory, DbFactory):
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
        super().__init__(data)

        self.factories = self.get_factories(self.data)

    @classmethod
    def get_factories(cls, data):
        return {
            factory_id: factory(data)
            for factory_id, factory in cls.factory_classes.items()
        }

    # TODO: Remove it
    def factory(self, factory_id):
        return self.factories.get(factory_id, lambda item_id: None)

    # TODO: Remove it
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
    validators = {
        # 'nm3': item_is_unique(self.data['nm1'], self.data['nm5']),
        # 'nm4': self.__validate_nm4() if method != 2 else None,
    }

    @classmethod
    def get_factories(cls, data):
        return {
            factory_id: data.find(block_id=block_id)
            for factory_id, block_id in cls.block_map.items()
        }

    def get_field(self, item_id, *args, **kwargs):
        """
        Generate value from data

        :param args: Args for generation
        :param kwargs: Kwargs for generation
        :return: Generated value
        """
        factory = self.factories[item_id]

        if factory is None:
            return None

        return factory(*args, **kwargs)

    def get_data(self, *args, **kwargs):
        """
        Generate value from data

        :param args: Args for generation
        :param kwargs: Kwargs for generation
        :return: Generated value
        """
        return {
            item_id: self.get_field(item_id, *args, **kwargs)
            for item_id, factory in self.factories.items()
            if factory is not None
        }

    def validate_item(self, item_id, item, items):
        validator = self.validators.get(item_id)

        if validator is None:
            return items

        items[item_id] = generate_while(
            item,
            validator(self, items),
            self[item_id],
        )

        return items

    def validate(self, items):
        for item_id, item in items.items():
            items = self.validate_item(item_id, item, items)

        return items

    def __validate_model(self, data):
        for item_id, value in data.items():
            validator = self.validators.get(item_id)

            if validator is None:
                continue

            item_validator = validator(self, data)
            if not item_validator(value):
                yield item_id

    def __call__(self, *args, **kwargs):
        data = {}

        # Validate model data
        invalid = [*self.block_map.keys()]
        model = self.model()
        while len(invalid) > 0:
            data.update({
                item_id: self.factories[item_id]()
                for item_id in invalid                
            })
            invalid = list(self.__validate_model(data))

            model = self.model(**data)

        return model


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
