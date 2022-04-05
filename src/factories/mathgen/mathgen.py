import random
from factories.factory import Factory


class MathDataProvider(Factory):
    def __call__(self):
        return random.uniform(0, 100)

    @property
    def radius(self):
        while True:
            yield random.randrange(255)

    @property
    def angle(self):
        while True:
            yield random.randrange(8)

    @property
    def speed(self):
        while True:
            yield random.randrange(8)

    @property
    def time(self):
        while True:
            yield random.randrange(1024)

