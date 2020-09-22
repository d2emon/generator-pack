import random
from .model import Model


class ComplexModel(Model):
    factories = dict()

    @classmethod
    def factory(cls, chance=0):
        for c in sorted(cls.factories.keys()):
            if c >= chance:
                return cls.factories[c]
        return None

    @classmethod
    def generate(cls):
        factory = cls.factory(random.randint(0, 100))
        return factory.generate() if factory is not None else None
