from .collection import Collection
from ..traits import skills


class CharacterSkills(Collection):
    SKILLS = [
        skills.Gambling,
        skills.Riding,
        skills.Hack,
        skills.Attention,
        skills.Driving,
        skills.Surviving,
        skills.Trailing,
        skills.Brawling,
        skills.Frighten,
        skills.Knowledge.Science,
        skills.Climbing,
        skills.Healing,
        skills.Disguise,
        skills.Throwing,
        skills.Aircraft,
        skills.Swimming,
        skills.Tease,
        skills.Investigation,
        skills.Melding,
        skills.Shooting,
        skills.Shipcraft,
    ]

    def __init__(self, character_stats):
        super().__init__([skill() for skill in self.SKILLS])
        self.__stats = character_stats

    def __cost(self, skill):
        stat_value = self.__stats[skill.stat].dice_id
        skill_value = skill.dice.dice_id
        base = min(skill_value, stat_value)
        extra = skill_value - base
        return base + extra * 2

    @property
    def cost(self):
        return sum(self.__cost(item) for item in self.items)
