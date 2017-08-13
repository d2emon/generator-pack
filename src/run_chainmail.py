#! /usr/bin/python
from chainmail import Opponent, PlayerStack, Battle
from chainmail.movesystem import MoveCounterMove


def main():
    players = PlayerStack()
    players.add(Opponent("First"))
    players.add(Opponent("Second"))

    battle = Battle(MoveCounterMove(), players)
    battle.process()


if __name__ == "__main__":
    main()
