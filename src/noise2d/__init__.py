import random


def fill1d (x):
    return [random.random() for i in range(x)]


def fill2d (x, y):
    return [
        [random.random() for i in range(x)]
        for j in range(y)
    ]


def fill3d (x, y, z):
    return [
        [
            [random.random() for i in range(x)]
            for j in range(y)
        ]
        for k in range(z)
    ]
