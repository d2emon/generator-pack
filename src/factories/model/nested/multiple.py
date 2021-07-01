import random
from .thing import ThingFactory


class MultipleFactory(ThingFactory):
    """
    Generate multiple items
    """

    def __init__(
        self,
        min_count=1,
        max_count=None,
    ):
        """
        Multiple factory constructor

        :param min_count: Minimal items
        :param max_count: Maximal items
        """
        super().__init__()
        self.min_count = min_count
        self.max_count = max_count

    @property
    def data(self):
        raise NotImplementedError()

    def count(self):
        """
        Random items count

        :return: Items count
        """
        if self.max_count is None:
            return self.min_count
        return random.randint(self.min_count, self.max_count)

    def build(self, count=None, *args, **kwargs):
        """
        Generate some models

        :param count: NUmber of models
        :param args: Model args
        :param kwargs: Model kwargs
        :return: Models
        """
        for _ in range(count or self.count()):
            yield from next(super())
