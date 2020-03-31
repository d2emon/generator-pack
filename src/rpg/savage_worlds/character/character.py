from .traits.skills import skill
from . import races
from .collections.edges import CharacterEdges
from .collections.skills import CharacterSkills
from .collections.stats import CharacterStats


class Character:
    def __init__(self):
        self.name = ''
        self.bio = ''
        # Race
        self.race = races.Human
        # Traits
        self.__stats = CharacterStats()
        self.skills = CharacterSkills(self.__stats)
        self.__charisma = 0
        self.__armor = 0
        # Edges
        self.traits = CharacterEdges()
        # Equipment
        self.equipment = []
        self.__money = 500

    # Stats
    agility = property(lambda self: self.__stats.agility)
    smarts = property(lambda self: self.__stats.smarts)
    spirit = property(lambda self: self.__stats.spirit)
    strength = property(lambda self: self.__stats.strength)
    vigor = property(lambda self: self.__stats.vigor)

    # Secondary
    pace = property(lambda self: self.race.movement)
    parry = property(lambda self: 2 + self.get_skill(skill.Brawling).half)
    charisma = property(lambda self: self.__charisma)
    toughness = property(lambda self: 2 + self.vigor.half)

    # Edges
    edges = property(lambda self: self.traits.edges)
    hindrances = property(lambda self: self.traits.hindrances)

    # Racial
    extra_traits = property(lambda self: self.race.extra_trait)
    run = property(lambda self: self.race.run)

    # Actions
    def use_agility(self, modifier=0):
        return self.agility.check(modifier)

    def use_skill(self, skill, modifier=0):
        return self.skills[skill].check(modifier)

    def general_knowledge(self, modifier=0):
        return self.smarts.check(modifier)
