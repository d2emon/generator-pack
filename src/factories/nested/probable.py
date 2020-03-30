import random
from .thing import ThingFactory


class ProbableFactory(ThingFactory):
    def __init__(self, provider=None, probability=100):
        super().__init__(provider)
        self.probability = probability

    def probable(self):
        if self.probability <= 0:
            return False
        if self.probability >= 100:
            return True
        return random.uniform(0, 100) <= self.probability

    def __next__(self):
        return next(super()) if self.probable() else None
