from .collection import Collection
from .. import dices, stats


class CharacterStats(Collection):
    def __init__(
        self,
        agility=dices.D4,
        smarts=dices.D4,
        spirit=dices.D4,
        strength=dices.D4,
        vigor=dices.D4,
    ):
        super().__init__([
            stats.Agility(agility),
            stats.Smarts(smarts),
            stats.Spirit(spirit),
            stats.Strength(strength),
            stats.Vigor(vigor),
        ])

    @property
    def agility(self):
        return self.get_item(stats.Agility)

    @property
    def smarts(self):
        return self.get_item(stats.Smarts)

    @property
    def spirit(self):
        return self.get_item(stats.Spirit)

    @property
    def strength(self):
        return self.get_item(stats.Strength)

    @property
    def vigor(self):
        return self.get_item(stats.Vigor)

    @property
    def value(self):
        return sum(stat.cost for stat in self.items)

    def set_values(
        self,
        agility=dices.D4,
        smarts=dices.D4,
        spirit=dices.D4,
        strength=dices.D4,
        vigor=dices.D4,
    ):
        self.agility.dice = agility
        self.smarts.dice = smarts
        self.spirit.dice = spirit
        self.strength.dice = strength
        self.vigor.dice = vigor
