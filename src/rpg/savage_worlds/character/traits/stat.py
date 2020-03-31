from .. import dices


class Stat:
    MIN_DICE = dices.D4
    MAX_DICE = dices.D12
    title = ''

    def __init__(self, dice=dices.D4, modifier=0):
        self.__dice = dice if dice.max_value <= self.MAX_DICE.max_value else self.MAX_DICE
        self.modifier = modifier

    @property
    def dice(self):
        return self.__dice

    @dice.setter
    def dice(self, value):
        self.__dice = value

    @property
    def value(self):
        return str(self.dice)

    @value.setter
    def value(self, value):
        self.__dice = value

    @property
    def cost(self):
        return self.dice.dice_id - 1

    @property
    def half(self):
        return int(self.dice.max_value / 2) + int(self.modifier / 2)

    def check(self, modifier=0):
        return self.dice.roll() + self.modifier + modifier

    def __str__(self):
        return '{}:\t{}'.format(self.title, self.value)
