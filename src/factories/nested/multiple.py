import random
from .thing import ThingFactory


class MultipleFactory(ThingFactory):
    def __init__(
        self,
        provider=None,
        min_count=1,
        max_count=None,
    ):
        """
        Multiple factory constructor

        :param provider: Data providers
        :param min_count: Minimal items
        :param max_count: Maximal items
        """
        super().__init__(provider)
        self.min_count = min_count
        self.max_count = max_count

    def count(self):
        """
        Random items count

        :return: Items count
        """
        if self.max_count is None:
            return self.min_count
        return random.randint(self.min_count, self.max_count)

    def model(self, *args, **kwargs):
        """
        Generate some models

        :param args: Model args
        :param kwargs: Model kwargs
        :return: Models
        """
        for _ in range(self.count()):
            yield from next(super())
