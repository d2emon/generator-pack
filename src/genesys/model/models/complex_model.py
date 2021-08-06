import random
from .descriptive_model import DescriptiveModel


class ComplexModel(DescriptiveModel):
    factories = dict()

    @classmethod
    def by_chance(cls, chance=0.0):
        return next((cls.factories[c] for c in sorted(cls.factories.keys()) if c >= chance), None)

    def __get_factory(self):
        return self.by_chance(random.uniform(0, 100))

    @property
    def factory(self):
        if self.__factory is None:
            self.__factory = self.__get_factory()
        return self.__factory
