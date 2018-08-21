class Opponent:
    def __init__(self, title="Untitled"):
        self.title = title

    def roll(self):
        import random
        roll = random.randint(1, 6)
        print("%s rolls a die (%d)" % (self.title, roll))
        return roll


class PlayerStack:
    def __init__(self):
        self.__players = []

    def add(self, player):
        if len(self.__players) >= 2:
            self.__players = self.__players[-1:]
        self.__players.append(player)

    @property
    def players(self):
        return self.__players

    def roll_order(self):
        rolls = dict()
        while len(rolls) < len(self.__players):
            if len(rolls):
                print("Reroll")
            rolls = {p.roll(): p for p in self.__players}
        order = sorted(rolls, reverse=True)
        return [rolls[r] for r in order]
