from . import Opponent, PlayerStack
from .terrain.field import Field
from .battle import Battle
from .battle.movesystem import MoveCounterMove


def play():
    players = PlayerStack()
    players.add(Opponent("First"))
    players.add(Opponent("Second"))

    field = Field()
    field.generate()
    for row in field.tiles:
        print([tile.name for tile in row])

    battle = Battle(MoveCounterMove(), players)
    battle.process()
