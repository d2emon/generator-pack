import random
from .factory import Factory


class PercentFactory(Factory):
    class DataProvider(Factory.DataProvider):
        factories = {}

        def factory(self, chance=0):
            return next((self.factories.get(key) for key in sorted(self.factories.keys()) if key >= chance), None)

        def __next__(self):
            factory = self.factory(random.randint(0, 100))
            return next(factory) if factory is not None else self.default
