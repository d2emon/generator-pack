from .collection import Collection
from .. import dices
from ..traits import Agility, Smarts, Spirit, Strength, Vigor


class CharacterStats(Collection):
    def __init__(
        self,
        agility=dices.D4,
        smarts=dices.D4,
        spirit=dices.D4,
        strength=dices.D4,
        vigor=dices.D4,
    ):
        super().__init__((
            Agility(agility),
            Smarts(smarts),
            Spirit(spirit),
            Strength(strength),
            Vigor(vigor),
        ))

    agility = property(lambda self: self[Agility])
    smarts = property(lambda self: self[Smarts])
    spirit = property(lambda self: self[Spirit])
    strength = property(lambda self: self[Strength])
    vigor = property(lambda self: self[Vigor])
