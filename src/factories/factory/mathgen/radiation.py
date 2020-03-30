import random
from factories.models.point import Point
from ..factory import Factory


class RadiationFactory(Factory):
    class DataProvider:
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

    def __init__(self, provider=None, start_point=None, end_point=None, speed=None):
        super().__init__(provider)
        self.start_point = start_point or Point.polar(
            next(self.provider.radius),
            next(self.provider.angle),
        )
        self.end_point = end_point or Point.polar(
            next(self.provider.radius),
            0,  # next(self.provider.angle),
        )
        self.speed = speed or next(self.provider.speed)

    def get_point(self, time=None):
        if time is None:
            time = next(self.provider.time)
        return Point.diffuse(
            self.start_point,
            self.end_point.rotate(time * self.speed),
        )

    def __iter__(self):
        return self

    def __next__(self):
        return self.get_point(next(self.provider.time))
