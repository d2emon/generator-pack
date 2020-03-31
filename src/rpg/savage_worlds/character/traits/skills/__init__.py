from .. import Agility, Smarts, Spirit, Strength
from .skill import Skill


class AgilitySkill(Skill):
    stat = Agility


class SmartsSkill(Skill):
    stat = Smarts


class SpiritSkill(Skill):
    stat = Spirit


class StrengthSkill(Skill):
    stat = Strength


class Gambling(SmartsSkill):
    title = 'Азартные игры'
    CHEAT = 2

    def cheat(self, modifier=0):
        return self.check(modifier + self.CHEAT)


class Riding(AgilitySkill):
    title = 'Верховая Езда'


class Hack(AgilitySkill):
    title = 'Взлом'


class Attention(SmartsSkill):
    title = 'Внимание'


class Driving(AgilitySkill):
    title = 'Вождение'


class Surviving(SmartsSkill):
    title = 'Выживание'


class Trailing(SmartsSkill):
    title = 'Слежка'


class Brawling(AgilitySkill):
    title = 'Драка'


class Frighten(SpiritSkill):
    title = 'Запугивание'


class KnowledgeSkill(SmartsSkill):
    pass


class Knowledge:
    class Science(KnowledgeSkill):
        title = 'Знания (наука)'


class Climbing(StrengthSkill):
    title = 'Лазание'


class Healing(SmartsSkill):
    title = 'Лечение'


class Disguise(AgilitySkill):
    title = 'Маскировка'


class Throwing(AgilitySkill):
    title = 'Метание'


class Aircraft(AgilitySkill):
    title = 'Пилотирование'


class Swimming(AgilitySkill):
    title = 'Плавание'


class Tease(SmartsSkill):
    title = 'Провокация'


class Investigation(SmartsSkill):
    title = 'Расследование'


class Melding(SmartsSkill):
    title = 'Починка'


class Shooting(AgilitySkill):
    title = 'Стрельба'


class Shipcraft(AgilitySkill):
    title = 'Судовождение'


class Faith(Skill):
    title = ''


class FastTalk(Skill):
    title = ''


class Streetwise(Skill):
    title = ''
