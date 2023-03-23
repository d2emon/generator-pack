import random
from .complex_model import ComplexModel


class DescriptiveModel(ComplexModel):
    fields = []

    class Factory:
        def __init__(self, provider):
            self.provider = provider

        def __call__(self, *args, **kwargs):
            return next(self.provider())

    def __init__(self, value=None, factory=None, **kwargs):
        self.__value = value
        self.__factory = None
        super().__init__(**kwargs)

    @property
    def value(self):
        return self.__value

    @property
    def description(self):
        return str(self.value)

    @description.setter
    def description(self, value):
        self.__value = value

    def __str__(self):
        return self.description

    def __get_factory(self):
        f = self.Factory(None)

        def build(*args, **kwargs):
            if f is None:
                return None

            data = f(*args, **kwargs)
            return self.__class__(**data)

        return build

    @property
    def factory(self):
        if self.__factory is None:
            self.__factory = self.__get_factory()
        return self.__factory

    def build(self, *args, **kwargs):
        factory = self.factory

        if factory is None:
            return None

        return factory(*args, **kwargs)


class ComplexModelV4(DescriptiveModel):
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


class ListModelV4(DescriptiveModel):
    @property
    def description(self):
        return " ".join(self.value)
