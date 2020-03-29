from .collection import Collection
from src.rpg.savage_worlds.savage_worlds.skills import SKILLS


class CharacterSkills(Collection):
    def __init__(self, character_stats):
        super().__init__([skill() for skill in SKILLS])
        self.__stats = character_stats

    def __skill_cost(self, skill):
        stat = self.__stats.get_item(skill.stat)
        base_value = min(skill.dice.dice_id, stat.dice.dice_id)
        extra_value = skill.dice.dice_id - base_value
        return base_value + extra_value * 2

    @property
    def value(self):
        return sum(self.__skill_cost(skill) for skill in self.items)

    def set_values(self, skills):
        for skill_class, value in skills.items():
            skill = self.get_item(skill_class)
            skill.dice = value
