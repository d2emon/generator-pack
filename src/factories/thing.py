import random
from.factory import SimpleFactory


class ThingFactory(SimpleFactory):
    def __init__(self, generated_class):
        self.generated_class = generated_class
        super().__init__()

    def __next__(self):
        return next(self.generate())

    def generate(self):
        yield self.generated_class()

    def next(self):
        return next(self)

    def factory(self):
        return self


class MultipleFactory(ThingFactory):
    def __init__(self, children_class, min_count, max_count=None):
        super().__init__(children_class)
        self.min_count = min_count
        self.max_count = max_count

    def generate(self):
        if self.max_count is None:
            count = self.min_count
        else:
            count = random.randint(self.min_count, self.max_count)
        for _ in range(count):
            yield from super().generate()


class ProbableFactory(ThingFactory):
    def __init__(self, children_class, probability):
        super().__init__(children_class)
        self.probability = probability

    def generate(self):
        if self.probability <= 0:
            return
        if self.probability < 100 and random.uniform(0, 100) > self.probability:
            return
        yield from super().generate()


class ListFactory(ThingFactory):
    def __init__(self, items):
        super().__init__(None)
        self.items = items

    def generate(self):
        if len(self.items) <= 0:
            return
        yield random.choice(self.items)
