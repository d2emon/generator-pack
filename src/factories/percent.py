import random
from factories.factory import Factory


class PercentFactory(Factory):
    default_value = None

    def factory(self, chance=None):
        if chance is None:
            chance = random.uniform(0, 100)
        return next((self.data.get(key) for key in sorted(self.data.keys()) if key >= chance), None)

    def value(self):
        factory = self.factory()
        return next(factory) if factory is not None else self.default_value
