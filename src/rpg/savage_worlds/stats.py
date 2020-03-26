from . import dices


class Stat:
    MAX_DICE = dices.D12
    stat_id = None
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

    @property
    def cost(self):
        return self.dice.dice_id - 1

    @property
    def half(self):
        return int(self.dice.max_value / 2) + int(self.modifier / 2)

    def __str__(self):
        return '{}:\t{}'.format(self.title, self.value)

    def check(self, modifier=0):
        return self.dice.roll() + self.modifier + modifier


class Agility(Stat):
    stat_id = 'AGILITY'
    title = 'Ловкость'


class Smarts(Stat):
    stat_id = 'SMARTS'
    title = 'Смекалка'


class Spirit(Stat):
    stat_id = 'SPIRIT'
    title = 'Характер'


class Strength(Stat):
    stat_id = 'STRENGTH'
    title = 'Сила'


class Vigor(Stat):
    stat_id = 'VIGOR'
    title = 'Выносливость'
