from scale.scalable import Scalable, Distance


parsec = 3.26


class LightYears(Distance):
    default_scale = 15
    light_year = 9.46

    def __init__(self, name, size, scale=0):
        size *= LightYears.light_year
        scale += LightYears.default_scale
        Distance.__init__(self, name, size, scale)


class LightYearsSized(Scalable):
    default_scale = 15
    light_year = 9.46

    def __init__(self, name, width, scale=0, length=None):
        scale += LightYearsSized.default_scale
        width *= self.light_year
        length = length and length * self.light_year
        Scalable.__init__(self, name, width=width, length=length, scale=scale)


class GalaxySized:
    title = ""
    distance_scale = 6
    default_scale = 3

    def __init__(self, name, width, scale, distance=None, length=None):
        scale = scale or self.default_scale
        self.name = self.title and "{} {}".format(self.title, name) or name
        self.size = LightYearsSized(self.name, width=width, scale=scale, length=length)
        if distance is None:
            self.distance = None
        else:
            self.distance = LightYears("", distance, self.distance_scale)

    @property
    def width(self):
        return self.size.width

    @property
    def length(self):
        return self.size.length

    def __repr__(self):
        distance = self.distance and " -> {}".format(self.distance.width) or ''
        size = str(self.size.width)
        if self.size.length:
            size = "{} x {}".format(size, self.size.length)
        return "{} ({}{})".format(self.name, size, distance)


class SuperCluster(GalaxySized):
    distance_scale = 9
    default_scale = 9

    def __init__(self, name, width, scale=None, distance=None, length=None, clusters=50, galaxies=50):
        GalaxySized.__init__(
            self,
            name,
            width=width,
            length=length,
            scale=scale,
            distance=distance
        )
        self.galaxies = galaxies
        self.clusters = clusters


class Cluster(GalaxySized):
    title = "Скопление"
    default_scale = 6

    def __init__(self, name, size, scale=None, distance=None, galaxies=50):
        GalaxySized.__init__(
            self,
            name,
            width=size,
            length=None,
            scale=scale,
            distance=distance
        )
        self.galaxies = galaxies


class Galaxy(GalaxySized):
    MIN_SIZE = (16, 3)
    MAX_SIZE = (800, 3)
    title = "Галактика"
    default_scale = 3

    def __init__(self, name, size, scale=None, distance=None, stars_scale=15):
        GalaxySized.__init__(
            self,
            name,
            width=size,
            length=None,
            scale=scale,
            distance=distance
        )
        self.stars_scale = stars_scale


class DwarfGalaxy(Galaxy):
    title = "Карликовая Галактика"


class StarCluster(Galaxy):
    title = "Звездное Скопление"
    default_scale = 0
    distance_scale = 3


class Nebula(GalaxySized):
    title = "Туманность"
    default_scale = 0
    distance_scale = 3

    def __init__(self, name, size, scale=None, distance=None):
        GalaxySized.__init__(
            self,
            name,
            width=size,
            length=None,
            scale=scale,
            distance=distance
        )


SIZES = [
    # Parsecs
    LightYearsSized("Световой Год", 1),

    LightYearsSized("Парсек", parsec),
    LightYearsSized("Мегапарсек", parsec, 6),
    LightYearsSized("Гигапарсек", parsec, 9),
]

NEBULAS = [
    Nebula("Гомункул", 0.29, distance=7.5),
    Nebula("Скат", 0.08, distance=18),
    Nebula("Гамбургер Гомеса", 0.25, distance=0.9),
    Nebula("Кошачий Глаз", 0.25, distance=3.3),
    Nebula("Песочные Часы", 0.3, distance=8),
    Nebula("Мерцающая", 0.45),
    Nebula("Тухлое Яйцо", 1.4, distance=5),
    Nebula("Муравей", 1, distance=8),
    Nebula("Эскимос", .34, distance=3),
    Nebula("Кольцо", 1.3, distance=2),
    Nebula("Улитка", 2.5, distance=.65),
    Nebula("Бумеранг", 2.2, distance=5),
    Nebula("Конская Голова", 3.5, distance=1.5),
    Nebula("Конус", 4, distance=2.7),
    Nebula("Пузырь", 3.5, distance=11),
    Nebula("Крабовидная", 11, distance=6.5),

    Nebula("Орел (Столпы Творения)", 4, distance=7),
    Nebula("Орел (Фея)", 10, distance=7),

    Nebula("Ориона", 33, distance=1.344),
    Nebula("Северная Америка", 100, distance=1.6),
    Nebula("Киля", 60, distance=10),
    Nebula("Орел", 70, distance=7),
    Nebula("Пещера", 10, distance=2.4),
    Nebula("Розетка", 130, distance=5.2),
    Nebula("Лагуна", 140, distance=5.2),
    Nebula("Петля Барнарда", 300, distance=.440 * parsec),
    Nebula("Тарантул", 200 * parsec, distance=160),
]

GALAXIES = [
    StarCluster("Солнечной Системы", 16.3),
    StarCluster("M 41", 25, stars_scale=2),
    StarCluster("M 54", 150, distance=88),
    StarCluster("Омега Центавра", 150, distance=18.3),
    StarCluster("Messier 54", 150, distance=88),
    DwarfGalaxy("Лев II", 0.58, distance=0.69),
    DwarfGalaxy("в Большом Псе", 0.87 * parsec, distance=0.025),
    DwarfGalaxy("Малое Магелланово Облако", 7, distance=0.2, stars_scale=8),
    DwarfGalaxy("в Стрельце", 10, distance=0.07),
    DwarfGalaxy("Гончие Псы I", 1.79, distance=0.72),
    Galaxy("Большое Магелланово Облако", 14, distance=0.163),
    Galaxy("NGC 3310", 50, distance=50),
    Galaxy("NGC 7714", 40, distance=100),
    Galaxy("Сомбреро", 50, distance=29.3),
    Galaxy("Треугольника", 50),
    Galaxy("Млечный Путь", 100),
    Galaxy("Черный Глаз", 53),
    Galaxy("Андромеды", 260, distance=2.537),
    Galaxy("Вертушка", 170),
    Galaxy("Колесо Телеги", 150, distance=500),
    Galaxy("Водоворот", 100, distance=23),
    Galaxy("NGC 1232", 200),
    Galaxy("Головастик", 300, distance=400),
    Galaxy("M 87 (Virgo A)", 490, distance=53.5),
    Galaxy("NGC 4889", 239),
    Galaxy("IC 1101", 6000, stars_scale=15),
]

CLUSTERS = [
    Cluster("Abell 2029", 8, galaxies=50, distance=1027),
    Cluster("Местная группа галактик", 10, galaxies=50),
    Cluster("Печи", 10, galaxies=58, distance=62),
    Cluster("Девы", 2.2 * parsec, galaxies=2000, distance=59),

    SuperCluster("Сверхскопление Девы", .2, clusters=100, galaxies=30),
    SuperCluster("Сверхпустота Эридана", width=1, length=10),
    SuperCluster("Комплекс сверхскоплений Рыб-Кита", width=1, length=0.150),
    SuperCluster("Великая стена Слоуна", 1.37, distance=1.2),
]

ITEMS = SIZES + NEBULAS + GALAXIES + CLUSTERS + [
    Distance("от Седны до Солнца", 0.14, 15),

    # ----

    Scalable("Джет из сверхмассивной черной дыры в центре галактики M87 в Скоплении Девы", 50, 18),

    LightYears("до Великого Аттрактора", 250, 6),
    LightYears("до Сверхскопления Шепли", 650, 6),

    LightYearsSized("Обозреваемая вселенная", 28 * parsec, 9),
    Scalable("Вселенная", 1.6, 27),

    # LightYearsSized("Ланиакея", 0.52, 9),
]
