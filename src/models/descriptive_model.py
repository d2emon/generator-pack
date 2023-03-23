import random
from .model import Model


class DescriptiveModel(Model):
    def __init__(self, value=None, **kwargs):
        super().__init__(**kwargs)

        self.value = value

    @property
    def description(self):
        return str(self.value)

    @description.setter
    def description(self, value):
        self.value = value

    def __str__(self):
        return self.description


class ListDescriptiveModel(DescriptiveModel):
    @property
    def description(self):
        return " ".join(self.value)


class FactoryModel(Model):
    def __init__(self, *args, factory=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.factory = factory

    def build(self, *args, **kwargs):
        return self.factory(*args, **kwargs)


class ModelFactory:
    def fields_factory(self, *args, **kwargs):
        raise NotImplementedError()

    def __call__(self, *args, **kwargs):
        fields_factory = self.fields_factory()

        if fields_factory is None:
            return None

        data = fields_factory(*args, **kwargs)
        return self.model(**data)


class ChanceFactory:
    def __init__(self):
        super().__init__()
        self.factories = dict()

    def by_chance(self, chance=0.0):
        return next((self.factories[c] for c in sorted(self.factories.keys()) if c >= chance), None)

    def __call__(self, *args, **kwargs):
        return self.by_chance(random.uniform(0, 100))
