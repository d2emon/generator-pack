import random
from .models import Point


class RadiationFactory:
    def __init__(self, r1=None, r2=None, angle=None, speed=None):
        self.r1 = r1 or self.get_radius()
        self.r2 = r2 or self.get_radius()
        self.angle1 = angle or self.get_angle()
        self.speed = speed or self.get_speed()

    def get_point(self, time):
        point1 = Point.polar(self.r1, self.angle1)
        point2 = Point.polar(self.r2, time * self.speed)
        return Point.diffuse(point1, point2)

    @classmethod
    def get_radius(cls):
        return random.randrange(255)

    @classmethod
    def get_angle(cls):
        return random.randrange(8)

    @classmethod
    def get_speed(cls):
        return random.randrange(8)

    @classmethod
    def get_time(cls):
        return random.randrange(1024)

    def __iter__(self):
        return self

    def __next__(self):
        return self.get_point(self.get_time())
