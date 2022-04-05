import random


class GeneratingModel:
    @classmethod
    def probable(cls, probability=100):
        return cls if random.uniform(0, 100) < probability else None

    @classmethod
    def multiple(cls, min_items=1, max_items=None):
        count = random.randint(min_items, max_items) if max_items is not None else min_items
        for _ in range(count):
            yield cls

    @classmethod
    def choice(cls, items):
        return random.choice(items) if len(items) > 0 else None
