import random
from .descriptive_model import DescriptiveModel


class ComplexModel(DescriptiveModel):
    factories = dict()

    @classmethod
    def by_chance(cls, chance=0.0):
        return next((cls.factories[c] for c in sorted(cls.factories.keys()) if c >= chance), None)

    @classmethod
    def factory(cls):
        return cls.by_chance(random.uniform(0, 100))
