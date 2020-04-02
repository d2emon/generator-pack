class LevelUp:
    def apply(self):
        raise NotImplementedError()


class AddEdge(LevelUp):
    def __init__(self, edge):
        self.edge = edge

    def apply(self):
        raise NotImplementedError()


class UpdateSkill(LevelUp):
    def __init__(self, skill):
        self.skill = skill

    def apply(self):
        if self.skill.value < self.skill.stat.value:
            raise ValueError()
        self.skill.value += 1


class UpdateSkills(LevelUp):
    def __init__(self, *skills):
        self.skills = skills

    def apply(self):
        if len(self.skills) != 2:
            raise ValueError()
        if any(skill.value >= skill.stat.value for skill in self.skills):
            raise ValueError()
        for skill in self.skills:
            skill.value += 1


class NewSkill(LevelUp):
    def __init__(self, skill):
        self.skill = skill

    def apply(self):
        self.skill.value = 1


class UpdateStat(LevelUp):
    once_per_rank = True

    def __init__(self, stat):
        self.stat = stat

    def apply(self):
        if self.stat.value >= 12:
            raise ValueError()
        self.stat.value += 1
