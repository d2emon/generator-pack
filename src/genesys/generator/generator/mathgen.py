import random
import math


def decart(r, a):
    return r * math.cos(a), r * math.sin(a)


def middle(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    x = int((x1 + x2) / 2)
    y = int((y1 + y2) / 2)
    return x, y


def diffuse(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    p = random.randrange(100) / 100
    dx = x2 - x1
    dy = y2 - y1

    return int(x1 + p * dx), int(y1 + p * dy)


class TwoPoint:
    def __init__(self, rotation=None, r1=None, r2=None, v=None):
        self.rotation = rotation or random.randrange(8)
        self.r1 = r1 or random.randrange(255)
        self.r2 = r2 or random.randrange(255)
        self.v = v or random.randrange(8)

    def calculate(self, t):
        p1 = decart(self.r1, self.rotation)
        p2 = decart(self.r2, t * self.v)
        return diffuse(p1, p2)

    def generate(self):
        t = random.randrange(1024)
        return self.calculate(t)
