from ... import dices
from .. import Stat, Agility


class Skill(Stat):
    stat = Agility

    def __init__(self, dice=dices.D0, modifier=0):
        super().__init__(dice, modifier)

    @property
    def cost(self):
        return self.dice.dice_id

    def __str__(self):
        return '{} ({}):\t{}'.format(self.title, self.stat.title, self.value)

    @classmethod
    def train(cls):
        print('несколько дней тренировок в спокойном режиме '
              'или несколько часов интенсивной деятельности с использованием данного навыка')
        pass
