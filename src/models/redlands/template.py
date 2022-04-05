from models.model import Model
from data.redlands.skills import SKILLS


class Template(Model):
    __stat_names = [
        'agility',
        'smarts',
        'spirit',
        'strength',
        'vigor',
    ]

    def stat_value(self, stat):
        stats = self.stats
        value = stats.get(stat, 1) + 1
        return 2 + value

    def skill_value(self, skill):
        skills = self.skills
        value = skills.get(skill, 0)
        modifier = value + 1 if value else 0
        return 2 + modifier

    @property
    def title(self):
        return self.data.get('title', '')

    @property
    def stats(self):
        return self.data.get('stats', {})

    @property
    def skills(self):
        return self.data.get('skills', {})

    @property
    def hindrances(self):
        return self.data.get('hindrances', [])

    @property
    def edges(self):
        return self.data.get('edges', [])

    @property
    def charisma(self):
        return 0

    @property
    def pace(self):
        return 6

    @property
    def parry(self):
        return self.skill_value('Fighting')

    @property
    def toughness(self):
        return self.stat_value('vigor')

    @property
    def stat_points(self):
        stats = self.stats
        total = 0
        for stat_name in self.__stat_names:
            value = stats.get(stat_name, 1)
            total += value
        return total

    @property
    def skill_points(self):
        skills = self.skills
        total = 0
        for skill, value in skills.items():
            if value:
                skill_data = SKILLS.get(skill, {})
                stat = skill_data.get('stat', 'agility')
                max_value = self.stats.get(stat, 1)
                if value <= max_value:
                    total += value
                else:
                    total += max_value + (value - max_value) * 2
        return total

    @property
    def hindrance_points(self):
        total = 0
        for value in self.hindrances:
            if value:
                total += value.get('points', 0)
        return total

    @property
    def edge_points(self):
        total = 0
        for value in self.edges:
            if value:
                total += 1
        return total

    def __str__(self):
        return self.title
