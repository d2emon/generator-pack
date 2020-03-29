from src.rpg.savage_worlds.savage_worlds import dices, stats


class Skill(stats.Stat):
    stat = stats.Agility

    def __init__(self, dice=dices.D0, modifier=0):
        super().__init__(dice, modifier)

    @property
    def cost(self):
        return self.dice.dice_id

    def __str__(self):
        return '{} ({}):\t{}'.format(self.title, self.stat.title, self.value)

    def train(self):
        print('несколько дней тренировок в спокойном режиме '
              'или несколько часов интенсивной деятельности с использованием данного навыка')
        pass


class Gambling(Skill):
    CHEAT = 2

    skill_id = 'Gambling'
    title = 'Азартные игры'
    stat = stats.Smarts


class Attention(Skill):
    title = 'Внимание'
    stat = stats.Smarts


class Brawling(Skill):
    skill_id = 'Brawling'
    title = 'Драка'
    stat = stats.Agility


class Driving(Skill):
    title = 'Вождение'
    stat = stats.Agility


class KnowledgeSkill(Skill):
    stat = stats.Smarts


class Knowledge:
    class Science(KnowledgeSkill):
        title = 'Знания (наука)'


class Investigation(Skill):
    title = 'Расследование'
    stat = stats.Smarts


class Melding(Skill):
    title = 'Починка'
    stat = stats.Smarts


class Shooting(Skill):
    title = 'Стрельба'
    stat = stats.Agility


SKILLS = [
    Gambling,
    Attention,
    Brawling,
    Driving,
    Knowledge.Science,
    Investigation,
    Melding,
    Shooting,
]
