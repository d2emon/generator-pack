import random
from utils.genders import MALE
from models.fng.names.name import Name
from factories.factory import Factory
from genesys.fng.factories.validators import generate_while


class DbFactory(Factory):
    """
    Base factory to build model with data from database.

    Attributes:
        data (Database): Database for factory.
        default_data (Database): Default database for factory.
    """

    default_data = None

    def __init__(self, data=None):
        """
        Construct factory with data from database.

        Args:
            data (Database, optional): Database for factory. Defaults to None.
        """
        self.data = data or self.default_data


class ModelFactory(Factory):
    """
    Base factory to build name model.

    Attributes:
        # default_data (Database): Default database for factory
        # factories (dict[Factory]): Nested factories.
        # factory_classes (dict[Factory]): Classes for nested factories.
        model (Name): Name model to build
    """

    model = Name

    def build_args(self, *args, **kwargs) -> list:
        """
        Build args for model.

        Returns:
            list: Args for model.
        """
        return []

    def build_kwargs(self, *args, **kwargs) -> dict:
        """
        Build data for model.

        Returns:
            dict: Data for model.
        """
        return {}

    def __call__(self, *args, **kwargs):
        """
        Build model.

        Returns:
            Model: Model built with factory.
        """
        model_args = self.build_args(*args, **kwargs)
        model_kwargs = self.build_kwargs(*args, **kwargs)
        return self.model(*model_args, **model_kwargs)


class BaseNameFactory(ModelFactory, DbFactory):
    """
    Base factory to build name model with data form database.

    Attributes:
        data (Database): Database for factory. Inherited from DBFactory.
        default_data (Database): Default database for factory Inherited from DBFactory.
        model (Name): Name model to build.
    """

    model = Name


class ComplexFactory(BaseNameFactory):
    """
    Complex Factory.

    Factory to build model with one of the nested factories.

    Attributes:
        data (Database): Database for factory. Inherited from DBFactory.
        default_data (Database): Default database for factory. Inherited from DbFactory.
        factories (dict[Factory]): Nested factories.
        factory_classes (dict[class]): Classes for nested factories.
        model (Model): Model to build. Inherited from BaseNameFactory.
    """

    factory_classes = {}

    def __init__(self, data=None):
        """
        Construct factory with nested factories.

        Args:
            data (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(data)

        self.factories = self.get_factories(self.data)

    # TODO: Remove it
    def __getitem__(self, item_id):
        """
        Get nested factory as item of parent factory.

        Args:
            item_id: Id of a nested factory.

        Returns:
            Factory: Nested factory.
        """
        return self.factory(item_id)

    # TODO: Remove it
    def factory(self, factory_id):
        """
        Get nested factory of parent factory.

        Args:
            item_id: Id of a nested factory.

        Returns:
            Factory: Nested factory.
        """
        return self.factories.get(factory_id)

    def from_factory(self, factory_id, *args, **kwargs):
        """
        Build model with nested factory.

        Args:
            factory_id: Id of a nested factory.

        Returns:
            Model: Model built by nested factory.
        """
        factory = self.factory(factory_id)
        return factory(*args, **kwargs) if factory is not None else None

    @classmethod
    def get_factories(cls, data):
        """
        Create nested factories.

        Args:
            data (Database): Database for nested factories.

        Returns:
            dict[Factory]: Nested factories.
        """
        return {
            factory_id: factory(data)
            for factory_id, factory in cls.factory_classes.items()
        }


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
        factory = self.factories.get(item_id)

        if factory is None:
            return None

        return factory(*args, **kwargs)

    def build_kwargs(self, *args, **kwargs) -> dict:
        """
        Build data for model.

        Returns:
            dict: Data for model.
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
