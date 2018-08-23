import random

from deck import Deck
from .terrain import *


Terrains = Deck([
    Marsh,
    Pond,
    Gulley,
    Rough,
    Wood,
    River,
    Hill,
    Plain
])


class Field:
    def __init__(self, width=8, height=8):
        self.width = width
        self.height = height
        self.tiles = [[Plain for _ in range(self.height)] for _ in range(self.width)]

    def generate(self):
        for card in Terrains.shuffle().cards[:8]:
            x = random.randrange(self.width)
            y = random.randrange(self.height)
            self.tiles[x][y] = card
