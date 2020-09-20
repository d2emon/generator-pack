import random
from .factory import Factory


class PercentFactory(Factory):
    """
    Generate value from factories with percents
    """

    default_value = None

    def factory(self, chance=None):
        """
        Get factory by chance

        :param chance: Chance
        :return: Factory
        """
        if chance is None:
            chance = random.uniform(0, 100)
        return next((self.data.get(key) for key in sorted(self.data.keys()) if key >= chance), None)

    def model(self, *args, **kwargs):
        """
        Get value from factory

        :param args: Value args
        :param kwargs: Value kwargs
        :return: Value
        """
        factory = self.factory()
        return next(factory) if factory is not None else self.default_value
