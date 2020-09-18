import random


class MathDataProvider:
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

