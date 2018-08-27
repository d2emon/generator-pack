import random


def d(count=1, sides=6):
    res = 0
    for _ in range(count):
        res += random.randint(1, sides)
    return res
