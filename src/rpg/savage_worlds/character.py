from . import dices, races, stats, skills
from .collections.stats import CharacterStats
from .collections.skills import CharacterSkills
from .collections.edges import CharacterEdges


class Character:
    STAT_POINTS = 10
    SKILL_POINTS = 15
    BIG_HINDRANCES = 2
    SMALL_HINDRANCES = 1

    def __init__(self):
        self.__race = races.Human
        self.__stats = CharacterStats()
        self.__skills = CharacterSkills(self.__stats)
        self.__charisma = 0
        self.__armor = 0
        self.__edges = CharacterEdges()
        self.__wealth = 1
        self.__equipment = []
        self.__money = 500
        self.bio = ''

    # Race
    @property
    def race(self):
        return self.__race

    # Stats
    @property
    def agility(self):
        return self.__stats.agility

    @property
    def smarts(self):
        return self.__stats.smarts

    @property
    def spirit(self):
        return self.__stats.spirit

    @property
    def strength(self):
        return self.__stats.strength

    @property
    def vigor(self):
        return self.__stats.vigor

    # Secondary
    @property
    def pace(self):
        return self.race.movement

    @property
    def parry(self):
        brawling = self.get_skill(skills.Brawling)
        return 2 + brawling.half

    @property
    def charisma(self):
        return self.__charisma

    @property
    def toughness(self):
        vigor = self.vigor
        return 2 + vigor.half

    # Edges
    @property
    def edges(self):
        return self.__edges.edges

    @property
    def hindrances(self):
        return self.__edges.hindrances

    # Equipment
    @property
    def equipment(self):
        return self.__equipment

    @property
    def money(self):
        return self.__money

    # Racial
    @property
    def additional_traits(self):
        return self.race.additional_trait

    @property
    def run(self):
        return self.race.run

    # Unused points
    @property
    def unused_stat_points(self):
        return int((self.STAT_POINTS - self.__stats.value) / 2)

    @property
    def unused_skill_points(self):
        return self.SKILL_POINTS - self.__skills.value

    @property
    def unused_big_hindrance_points(self):
        hindrances = [hindrance for hindrance in self.hindrances if hindrance.is_big]
        return self.BIG_HINDRANCES - len(hindrances)

    @property
    def unused_small_hindrance_points(self):
        hindrances = [hindrance for hindrance in self.hindrances if not hindrance.is_big]
        return self.SMALL_HINDRANCES - len(hindrances)

    @property
    def unused_points(self):
        stats_value = max(0, self.__stats.value - self.STAT_POINTS)
        skills_value = max(0, self.__skills.value - self.SKILL_POINTS)
        wealth_value = self.__wealth - 1
        return 0 - self.__edges.value - stats_value - skills_value - wealth_value

    # Creating
    def get_skill(self, skill_class):
        return self.__skills.get_item(skill_class)

    def set_race(self, race):
        self.__race = race

    def set_stats(
        self,
        agility=dices.D4,
        smarts=dices.D4,
        spirit=dices.D4,
        strength=dices.D4,
        vigor=dices.D4,
        skills_list=None,
    ):
        self.__stats.set_values(
            agility,
            smarts,
            spirit,
            strength,
            vigor,
        )
        self.__skills.set_values(skills_list or {})

    def set_edges(
        self,
        edges=(),
        wealth=1,
    ):
        self.__edges.set_edges(edges)
        self.__wealth = wealth

    def set_equipment(
        self,
        money=500,
        equipment=(),
    ):
        self.__money = money * self.__wealth
        self.__equipment = equipment

    def set_bio(self, bio):
        self.bio = bio

    @classmethod
    def generate(
        cls,
        race=None,
        # Stats
        agility=dices.D4,
        smarts=dices.D4,
        spirit=dices.D4,
        strength=dices.D4,
        vigor=dices.D4,
        skills_list=None,
        # Traits
        edges=(),
        wealth=1,
        # Equipment
        money=500,
        equipment=(),
        # Bio
        bio='',
    ):
        character = cls()
        character.set_race(race)
        character.set_stats(
            agility,
            smarts,
            spirit,
            strength,
            vigor,
            skills_list,
        )
        character.set_edges(
            edges,
            wealth,
        )
        character.set_equipment(
            money,
            equipment,
        )
        character.set_bio(bio)
        return character

    # Actions
    def use_agility(self, modifier=0):
        return self.agility.check(modifier)

    def use_skill(self, skill_class, modifier=0):
        return self.get_skill(skill_class).check(modifier)

    def general_knowledge(self, modifier=0):
        return self.smarts.check(modifier)

    # Char sheet
    def charsheet(self):
        def show_stats(character):
            print(character.agility)
            print(character.smarts)
            print(character.spirit)
            print(character.strength)
            print(character.vigor)
            print('Шаг:\t{}'.format(character.pace))
            print('Защита:\t{}'.format(character.parry))
            print('Харизма:\t{}'.format(character.charisma))
            print('Стойкость:\t{}'.format(character.toughness))
            print('Неиспользованных Улучшений:\t{}'.format(max(0, character.unused_stat_points)))
            print()

        def show_edges(character):
            print('Черты:')
            for edge in character.edges:
                print('\t{}'.format(edge))
            print('Обычные черты:')
            print('Цветные черты:')
            print('Неиспользованных Улучшений:\t{}'.format(max(0, character.unused_points)))
            print()

        def show_skills(character):
            print('Умения:')
            for skill_class in skills.SKILLS:
                print('\t{}'.format(character.get_skill(skill_class)))
            print('\tНеиспользованных Улучшений:\t{}'.format(max(0, character.unused_skill_points)))
            print()

        def show_hindrances(character):
            print('Изъяны:')
            for hindrance in character.hindrances:
                print('\t{}'.format(hindrance))
            print('Увечья:')
            print('Отпечатки:')
            print('Возможных больших изъянов:\t{}'.format(max(0, character.unused_big_hindrance_points)))
            print('Возможных малых изъянов:\t{}'.format(max(0, character.unused_small_hindrance_points)))
            print()

        def show_equipment(character):
            print('Валюта:\t{}'.format(character.money))
            print()
            print('Снаряжение:')
            print('\tСнаряжение\tКачество\tВес')
            for equipment in character.equipment:
                print('\t{}'.format(equipment))

        print('Имя:')
        print('Происхождение:')
        print('Движение:')
        print('Концепция:')
        print('Ранг:')
        print('Повышения:')
        print('Погружение:')
        print('Фишки:')
        print('\tОбычные:')
        print('\tЦветные:')
        print()

        show_stats(self)
        show_edges(self)
        show_skills(self)
        show_hindrances(self)

        print('Сила:')
        print('\tСила\tЦена\tДистанция\tУрон/эффект\tДлительность')
        print()

        print('Оружие:')
        print('\tОружие\tДистанция\tСк\tУрон\tББ\tВес\tЗаметки')
        print()

        show_equipment(self)

        print('Максимальный вес:')
        print('Нагрузка:')
        print('Штраф:')
        print()

        print('Ранения:')
        print('Усталость:')
        print()

        print('Патроны:')
        print('Пункты Силы:')
        print()

        print(self.bio)
        print(self.unused_points)
