import random
from .thing import ThingFactory


class MultipleFactory(ThingFactory):
    def __init__(self, provider=None, min_count=1, max_count=None):
        super().__init__(provider)
        self.min_count = min_count
        self.max_count = max_count

    def count(self):
        if self.max_count is None:
            return self.min_count
        return random.randint(self.min_count, self.max_count)

    def __next__(self):
        for _ in range(self.count()):
            yield from next(super())
