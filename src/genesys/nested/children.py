import random


class ChildFactory:
    def __init__(
        self,
        thing,
        min_amount=1,
        max_amount=None,
        probability=100,
    ):
        self.thing = thing
        self.min_amount = min_amount
        self.max_amount = max_amount
        self.probability = probability

    def get_amount(self):
        if self.max_amount is None:
            return self.min_amount
        
        return random.randrange(self.min_amount, self.max_amount)

    def get_probability(self):
        return self.probability

    def factories(self):
        yield self

    def __call__(self, *args, **kwargs):
        probability = self.get_probability()
        if random.uniform(0, 100) > probability:
            yield from []
            return

        amount = self.get_amount()
        for _ in range(0, amount):
            yield self.thing


class ComplexChildFactory:
    def __init__(self, children):
        self.children = children

    def factories(self):
        yield from self.children

    def __call__(self, *args, **kwargs):
        factory = random.choice(self.children)
        yield from factory()
