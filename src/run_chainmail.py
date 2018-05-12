#! /usr/bin/python
from chainmail import Opponent, PlayerStack, Battle
from chainmail.movesystem import MoveCounterMove
from chainmail.terrain import generateTerrain


def play(*args, **kwargs):
    players = PlayerStack()
    players.add(Opponent("First"))
    players.add(Opponent("Second"))

    terrain = generateTerrain()
    for row in terrain:
        print([t.name for t in row])

    battle = Battle(MoveCounterMove(), players)
    battle.process()


if __name__ == "__main__":
    play()
