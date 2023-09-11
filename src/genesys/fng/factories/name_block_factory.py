"""
NameBlock factories.

Classes:
    MultipleFactoryNameFactory: Factory to build model with one of the nested factories.
    GenderNameBlockFactory: Factory to build model with choosen gender.
"""

import random
from .name_factory import ComplexFactory, BaseNameFactory
from utils import genders


class MultipleFactoryNameFactory(BaseNameFactory):
    """
    Factory to build model with one of the nested factories.

    Attributes:
        data (Database): Database for factory. Inherited from DBFactory.
        default_data (Database): Default database for factory. Inherited from Factory.
        factories (list[Factory]): Nested factories.
        factory_classes (list[class]): Classes for nested factories.
        model (Model): Model to build. Inherited from BaseNameFactory.
    """

    factory_classes = []

    def __init__(self, data=None):
        """
        Construct factory with nested factories.

        Args:
            data (Database, optional): Database for building model. Defaults to None.
        """
        super().__init__(data)

        self.factories = [factory(self.data) for factory in self.factory_classes]

    def __call__(self, *args, factory_id=None, **kwargs):
        """
        Build model using nested factory.

        Args:
            factory_id (int, optional): Id of a nested factory to use for building model.
                Defaults to None.

        Returns:
            Model: Model built with nested factory.
        """
        factory = self.factory(factory_id)

        if factory is None:
            return None

        model_args = factory.build_args(*args, **kwargs)
        model_kwargs = factory.build_kwargs(*args, **kwargs)

        return self.model(*model_args, **model_kwargs)

    def factory(self, factory_id=None):
        """
        Get nested factory.

        Args:
            factory_id (int, optional): Id of a nested factory to use for building model.
                Defaults to None.

        Returns:
            Factory: Nested factory.
        """
        if factory_id is None:
            return random.choice(self.factories)

        return self.factories[factory_id]


class GenderNameBlockFactory(ComplexFactory):
    class MaleNameFactory(BaseNameFactory):
        pass

    class FemaleNameFactory(BaseNameFactory):
        pass

    class NeutralNameFactory(BaseNameFactory):
        pass

    @property
    def genders(self):
        return self.factories.keys()

    @classmethod
    def get_factories(cls, factory_data):
        return {
            genders.MALE: cls.MaleNameFactory(factory_data),
            genders.FEMALE: cls.FemaleNameFactory(factory_data),
            genders.NEUTRAL: cls.NeutralNameFactory(factory_data),
        }

    def get_gender(self):
        return genders.MALE

    def factory(self, gender=None):
        return self.factories.get(gender if gender is not None else self.get_gender())

    def by_percent(self, percent):
        return self.factory(percent)

    def __call__(self, *args, gender=None, **kwargs):
        return self.from_factory(
            gender if gender is not None else self.get_gender(),
            *args,
            **kwargs,
        )
