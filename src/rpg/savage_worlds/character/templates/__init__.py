from .. import dices
from ..character import Character
from ..edges import edge
from ..traits import skills


class MadScientist(Character):
    def __init__(self):
        super().__init__()
        # Traits
        self.agility.value = dices.D4
        self.smarts.value = dices.D10
        self.spirit.value = dices.D6
        self.strength.value = dices.D6
        self.vigor.value = dices.D6
        self.skills.set_values({
            skills.Investigation: dices.D6,
            skills.Knowledge.Science: dices.D10,
            skills.Attention: dices.D6,
            skills.Melding: dices.D8,
        })
        # Edges
        self.traits.set_values([
            edge.Inventor,
            edge.Mystic.MadScience,
        ])


class Driver(Character):
    def __init__(self):
        super().__init__()
        # Traits
        self.agility.value = dices.D8
        self.smarts.value = dices.D6
        self.spirit.value = dices.D6
        self.strength.value = dices.D6
        self.vigor.value = dices.D6
        self.skills.set_values({
            skills.Driving: dices.D8,
            skills.Brawling: dices.D4,
            skills.Attention: dices.D6,
            skills.Shooting: dices.D6,
        })
        # Edges
        self.traits.set_values([
            edge.Ace,
            edge.Swift,
        ])


class DoubleWeaponWarrior(Character):
    def __init__(self):
        super().__init__()
        # Traits
        self.agility.value = dices.D6
        self.smarts.value = dices.D4
        self.spirit.value = dices.D6
        self.strength.value = dices.D10
        self.vigor.value = dices.D6
        self.skills.set_values({
            skills.Brawling: dices.D10,
            skills.Frighten: dices.D6,
            skills.Attention: dices.D6,
            skills.Shooting: dices.D6,
        })
        # Edges
        self.traits.set_values([
            edge.AttackAround,
        ])


class Healer(Character):
    def __init__(self):
        super().__init__()
        # Traits
        self.agility.value = dices.D6
        self.smarts.value = dices.D6
        self.spirit.value = dices.D8
        self.strength.value = dices.D6
        self.vigor.value = dices.D6
        self.skills.set_values({
            skills.Faith: dices.D8,
            skills.Brawling: dices.D6,
            skills.Healing: dices.D8,
            skills.Attention: dices.D6,
        })
        # Edges
        self.traits.set_values([
            edge.Miracles,
            edge.Healer,
        ])


class Researcher(Character):
    def __init__(self):
        super().__init__()
        # Traits
        self.agility.value = dices.D6
        self.smarts.value = dices.D8
        self.spirit.value = dices.D6
        self.strength.value = dices.D6
        self.vigor.value = dices.D6
        self.skills.set_values({
            skills.Brawling: dices.D6,
            skills.Investigation: dices.D8,
            skills.Attention: dices.D8,
            skills.FastTalk: dices.D6,
            skills.Shooting: dices.D6,
            skills.Streetwise: dices.D8,
        })
        # Edges
        self.traits.set_values([
            edge.Researcher,
            edge.Contact,
        ])
