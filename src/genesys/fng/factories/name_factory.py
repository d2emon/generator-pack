"""
NameBlock factories.

Classes:
    ModelFactory: Base factory to build model.
    BaseNameFactory: Base factory to build name model.
    ComplexFactory: Base factory to build complex model.
    PolymorphFactory: Base factory to build polymorph model.
    PercentFactory: Base factory to build percent model.
    GenderFactory: Base factory to build gender model.
"""

import random
from factories.factory import Factory
from factories.list_factory import ListFactory
from models.fng.names.name import Name
from utils.genders import MALE


class ModelFactory(Factory):
    """
    Base factory to build model.

    Attributes:
        model (Name): Name model to build.
        static_args (list): List of static args for model.
        static_kwargs (dict): Static kwargs for model.
    """

    model = Name
    static_args = []
    static_kwargs = {}

    def build_args(self, *args, **kwargs) -> list:
        """
        Build args for model.

        Args:
            *args (list): Args from factory method.
            **kwargs (dict): Kwargs from factory method.

        Returns:
            list: Args for model.
        """
        return [*self.static_args]

    def build_kwargs(self, *args, **kwargs) -> dict:
        """
        Build data for model.

        Args:
            *args (list): Args from factory method.
            **kwargs (dict): Kwargs from factory method.

        Returns:
            dict: Data for model.
        """
        return {**self.static_kwargs}

    def __call__(self, *args, **kwargs):
        """
        Build model.

        Args:
            *args (list): Args for factory method.
            **kwargs (dict): Kwargs for factory method.

        Returns:
            Model: Model built with factory.
        """
        model_args = self.build_args(*args, **kwargs)
        model_kwargs = self.build_kwargs(*args, **kwargs)
        return self.model(*model_args, **model_kwargs)


class BaseNameFactory(ModelFactory):
    """
    Base factory to build name model with data form database.

    Attributes:
        data (Database): Database for factory. Inherited from DBFactory.
        default_data (Database): Default database for factory Inherited from DBFactory.
        model (Name): Name model to build.
    """

    model = Name


class ComplexFactory(ModelFactory):
    """
    Complex Factory.

    Factory to build model with one of the nested factories.

    Attributes:
        block_map (dict): Map model fields to database blocks.
        data (Database): Database for factory. Inherited from Factory.
        default_data (Database): Default database for factory. Inherited from Factory.
        factories (dict[Factory]): Nested factories.
        factory_classes (dict[class]): Classes for nested factories.
        model (Model): Model to build. Inherited from BaseNameFactory.
        parts (list): List of fields to build args for model.
        static_args (list): List of static args for model.
        static_kwargs (dict): Static kwargs for model.
        validators (dict[function]): Validators for model fields.
    """

    block_map = {}
    factory_classes = {}
    parts = []
    validators = {}
    update_values = {}

    def __init__(self, data=None, providers=None):
        """
        Construct factory with nested factories.

        Args:
            data (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(data)

        self.factories = self.get_factories(self.data)
        self.args_factories = list(self.get_args_factories(self.data))
        self.providers = providers or []

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

    def build_args(self, *args, **kwargs) -> list:
        """
        Build args for model.

        Args:
            *args (list): Args from factory method.
            **kwargs (dict): Kwargs from factory method.

        Returns:
            list: Args for model.
        """
        invalid = []
        data = []

        for factory_id in range(len(self.args_factories)):
            invalid.append(factory_id)
            data.append(None)

        while len(invalid) > 0:
            for factory_id in invalid:
                factory = self.args_factories[factory_id]
                data[factory_id] = factory(*args, **kwargs)

            invalid = list(self.validate_args(data))

        return [
            *self.static_args,
            *data,
        ]


    def build_kwargs(self, *args, **kwargs) -> dict:
        """
        Build data for model.

        Args:
            *args (list): Args from factory method.
            **kwargs (dict): Kwargs from factory method.

        Returns:
            dict: Data for model.
        """
        data = {
            'built_with': self,
            **self.static_kwargs,
        }

        # Validate model data
        invalid = [*self.block_map.keys()]
        while len(invalid) > 0:
            data.update({
                item_id: self.get_field(item_id, *args, **kwargs)
                for item_id in invalid                
            })
            invalid = list(self.validate(data))

        return data

    def get_field(self, item_id, *args, **kwargs):
        """
        Generate value for field.

        Args:
            item_id (str): Id of field to build.
            *args (list): Args from factory method.
            **kwargs (dict): Kwargs from factory method.

        Returns:
            Value for model field.
        """
        factory = self.factories.get(item_id)

        if factory is None:
            return None

        return factory(*args, **kwargs)

    def validate_args(self, data):
        """
        Validate values from data.

        Args:
            data (dict): Values for model.

        Returns:
            list(str): List of invalid fields.
        """
        for item_id in range(len(self.args_factories)):
            # updater = self.update_values.get(item_id)

            # if updater is not None:
            #     data[item_id] = updater(self, data)

            validator = self.validators.get(item_id)

            if validator is None:
                continue

            item_validator = validator(data)
            if not item_validator(data[item_id]):
                yield item_id

    def validate(self, data):
        """
        Validate values from data.

        Args:
            data (dict): Values for model.

        Returns:
            list(str): List of invalid fields.
        """
        for item_id, value in data.items():
            updater = self.update_values.get(item_id)

            if updater is not None:
                data[item_id] = updater(self, data)

            validator = self.validators.get(item_id)

            if validator is None:
                continue

            item_validator = validator(data)
            if not item_validator(value):
                yield item_id

    @classmethod
    def get_data_factory(cls, block_id, data):
        """
        Create nested factories.

        Args:
            data (Database): Database for nested factories.

        Returns:
            dict[Factory]: Nested factories.
        """
        return data.find(block_id=block_id)

    @classmethod
    def get_factory(cls, block_id, data):
        """
        Create nested factories.

        Args:
            data (Database): Database for nested factories.

        Returns:
            dict[Factory]: Nested factories.
        """
        factory = cls.factory_classes.get(block_id)
        return factory(data)

    @classmethod
    def get_factories(cls, data):
        """
        Create nested factories.

        Args:
            data (Database): Database for nested factories.

        Returns:
            dict[Factory]: Nested factories.
        """
        # factories = {
        #     factory_id: cls.get_factory(factory_id, data)
        #     for factory_id, factory in cls.factory_classes.items()
        # }
        data_factories = {
            factory_id: cls.get_data_factory(block_id, data)
            for factory_id, block_id in cls.block_map.items()
        }
        return {
            # **factories,
            **data_factories,
        }

    @classmethod
    def get_args_factories(cls, data):
        """
        Create list of nested factories.

        Args:
            data (Database): Database for nested factories.

        Returns:
            dict[Factory]: Nested factories.
        """
        for block_id in cls.parts:
            yield cls.get_data_factory(block_id, data)

    def set_factory(self, factory_id, factory):
        self.factories[factory_id] = factory
        return self

    @classmethod
    def from_lists(cls, *parts):
        return cls(providers=[ListFactory(provider) for provider in parts])

    # DictFactory

    @classmethod
    def from_factories(cls, **factories):
        class FromFactories(cls):
            def __init__(self):
                super().__init__()
                self.factories = { **factories }

            def __call__(self, *args, **kwargs):
                items = {key: factory(*args, **kwargs) for key, factory in self.factories.items()}
                return {
                    **kwargs,
                    **items,
                }

        factory = FromFactories()
        return factory

    def __len__(self):
        """
        :return: Data length
        """
        return len(self.args_factories) + len(self.factories)


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
