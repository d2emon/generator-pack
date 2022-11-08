import random
from .name_factory import ComplexFactory, ComplexNameFactory
from utils import genders


class MultipleFactoryNameFactory(ComplexFactory):
    factory_classes = []

    @classmethod
    def get_factories(cls, data):
        return [ factory(data) for factory in cls.factory_classes ]

    def random_factory(self):
        return random.choice(self.factories)

    def __call__(self, *args, factory_id=None, **kwargs):
        if factory_id is None:
            factory = self.random_factory()
        else:
            factory = self.factories[factory_id]

        return factory(*args, **kwargs)


class GenderNameBlockFactory(ComplexFactory):
    class MaleNameFactory(ComplexNameFactory):
        pass

    class FemaleNameFactory(ComplexNameFactory):
        pass

    class NeutralNameFactory(ComplexNameFactory):
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
