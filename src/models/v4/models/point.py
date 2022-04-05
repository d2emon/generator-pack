import math
import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def length(self):
        return math.sqrt(self.x ^ 2 + self.y ^ 2)

    @property
    def angle(self):
        return math.atan(self.y / self.x)

    def rotate(self, angle):
        return self.polar(
            self.length,
            self.angle + angle,
        )

    @classmethod
    def polar(cls, radius, angle):
        return cls(
            radius * math.cos(angle),
            radius * math.sin(angle),
        )

    @classmethod
    def between(cls, point1, point2):
        return cls(
            int((point1.x + point2.x) / 2),
            int((point1.y + point2.y) / 2),
        )

    @classmethod
    def diffuse(cls, point1, point2):
        percent = random.uniform(100)
        dx = point2.x - point1.x
        dy = point2.y - point1.y
        return cls(
            int(point1.x + percent * dx),
            int(point1.y + percent * dy),
        )
