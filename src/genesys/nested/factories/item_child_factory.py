import random


# TODO: Convert to ModelFactory
class ItemChildFactory:
    def __init__(
        self,
        factory_id,
        min_amount=1,
        max_amount=None,
        probability=None,
    ):
        self.factory_id = factory_id
        self.min_amount = min_amount
        self.max_amount = max_amount

        if probability is None:
            self.probability = 100
        else:
            self.min_amount = 1
            self.max_amount = None
            self.probability = probability

    @property
    def items(self):
        yield self

    @property
    def item(self):
        return self

    def cleanup(self):
        self.data = [i for i in self.items if i]

    def get_amount(self):
        if self.max_amount is None:
            return self.min_amount
        
        return random.randrange(
            self.min_amount,
            self.max_amount,
        )

    def check_probability(self):
        return random.uniform(0, 100) <= self.probability


# TODO: Convert to ModelFactory
class TemplatedItemChildFactory(ItemChildFactory):
    @property
    def pattern(self):
        raise NotImplementedError()

    @property
    def items(self):
        if self.pattern is None:
            return

        yield from self.pattern.content


# TODO: Convert to ModelFactory
class ItemChildrenFactory(ItemChildFactory):
    @property
    def items(self):
        raise NotImplementedError()

    @property
    def item(self):
        return random.choice(self.items)

    def get_to_concat(self):
        yield self.items
