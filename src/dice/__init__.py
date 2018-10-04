import random


def d(count=1, sides=6, multiplier=1, modifier=0):
    res = 0
    for _ in range(count):
        res += random.randint(1, sides)
    return res * multiplier + modifier


class Dice:
    def __init__(self, count=1, sides=6, multiplier=1, modifier=0):
        self.count = count
        self.sides = sides
        self.multiplier = multiplier
        self.modifier = modifier
        self.value = None

    def roll(self):
        self.value = d(self.count, self.sides, self.multiplier, self.modifier)
        return self.value
