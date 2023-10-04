from atlas.common import Named


class Star(Named):
    pass


class Constellation(Named):
    def __init__(self, name, stars=None):
        super().__init__(name)
        self.__stars = stars or []

    @property
    def stars(self):
        return self.__stars

    @stars.setter
    def stars(self, value):
        self.__stars = value


class Galaxy(Named):
    pass


galaxy = Galaxy('Млечный путь')
items = [
    Constellation('Козерог'),
    Constellation('Водолей'),
    Constellation('Рыбы'),
    Constellation('Овен'),
    Constellation('Телец', [
        Star('Альдебаран'),
    ]),
    Constellation('Близнецы', [
        Star('Кастор'),
        Star('Поллукс'),
    ]),
    Constellation('Рак'),
    Constellation('Лев', [
        Star('Регул'),
    ]),
    Constellation('Дева', [
        Star('Спика'),
    ]),
    Constellation('Весы'),
    Constellation('Скорпион', [
        Star('Антарес'),
    ]),
    Constellation('Стрелец'),
    Constellation('Кит'),
    Constellation('Эридан'),
    Constellation('Орион', [
        Star('Бетельгейзе'),
        Star('Ригель'),
    ]),
    Constellation('Заяц'),
    Constellation('Большой Пес', [
        Star('Сириус'),
    ]),
    Constellation('Малый Пес', [
        Star('Процион'),
    ]),
    Constellation('Компас'),
    Constellation('Гидра'),
    Constellation('Змея'),
    Constellation('Орел', [
        Star('Альтаир'),
    ]),
    Constellation('Лебедь', [
        Star('Денеб'),
    ]),
    Constellation('Цефей'),
    Constellation('Кассиопея'),
    Constellation('Персей', [
        Star('Альголь'),
    ]),
    Constellation('Возничий', [
        Star('Капелла'),
    ]),
    Constellation('Пегас'),
    Constellation('Андромеда'),
    Constellation('Змееносец'),
    Constellation('Лира', [
        Star('Вега'),
    ]),
    Constellation('Геркулес'),
    Constellation('Северная Корона'),
    Constellation('Дракон'),
    Constellation('Малая Медведица', [
        Star('Полярная звезда'),
    ]),
    Constellation('Большая Медведица', [
        Star('Мицар'),
    ]),
    Constellation('Волопас', [
        Star('Арктур'),
    ]),
    Constellation('Гончие Псы'),
    Constellation('Рысь'),
]
