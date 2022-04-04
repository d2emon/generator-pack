from models.scales import Sized as Scalable, Distance, ScalableSize as Size
from .galaxy import LightYears


class AstronomicUnit(Distance):
    default_scale = 12
    au = 0.149

    def __init__(self, name, size, scale=0):
        size *= AstronomicUnit.au
        scale += AstronomicUnit.default_scale
        super().__init__(name, size, scale)


class AUSized(Scalable):
    default_scale = 12
    au = 0.149

    def __init__(self, name, length, scale=0, width=None):
        scale += self.default_scale
        super().__init__(
            name=name,
            length=length and Size(length * self.au, scale),
            width=width and Size(width * self.au, scale),
        )


class SunSized(Scalable):
    default_scale = 9
    sun = 0.696 * 2

    def __init__(self, name, length, scale=0, width=None):
        scale += self.default_scale
        super().__init__(
            name=name,
            width=width and Size(width * self.sun, scale),
            length=length and Size(length * self.sun, scale),
        )


class PlanetSized(Scalable):
    default_scale = 6

    def __init__(self, name, length, scale=0):
        scale += self.default_scale
        length *= 2
        super().__init__(
            name=name,
            width=Size(length, scale),
        )


class SystemSized(Scalable):
    title = ""
    distance_scale = 6

    name = Scalable.field_property('name')
    size = Scalable.field_property('size')
    distance = Scalable.field_property('distance')

    def __init__(self, name, length, scale=0, distance=None, width=None, *args, **kwargs):
        name = f"{self.title} {name}" if self.title else name
        super().__init__(
            name=name,
            size=AUSized(name, width=width, length=length, scale=scale),
            distance=distance and AstronomicUnit(name, distance, self.distance_scale),
            *args,
            **kwargs,
        )

    @property
    def field_names(self):
        yield "name"
        yield "size"
        yield "distance"

    @property
    def width(self):
        return self.size.width

    @property
    def length(self):
        return self.size.length

    def __str__(self):
        distance = f" -> {self.distance.length}" if self.distance else ''
        size = f"{self.size.width} x {self.size.length}" if self.size.length else str(self.size.width)
        return f"{self.name} ({size}{distance})"


class Star(Scalable):
    title = ""
    distance_scale = 3

    name = Scalable.field_property('name')
    letter = Scalable.field_property('letter')
    constellation = Scalable.field_property('constellation')
    size = Scalable.field_property('size')
    distance = Scalable.field_property('distance')

    def __init__(self, name, length, letter=None, constellation=None, scale=0, distance=None, width=None, *args, **kwargs):
        name = f"{self.title} {name}" if self.title else name
        super().__init__(
            name=name,
            letter=letter,
            constellation=constellation,
            size=SunSized(name, width=width, length=length, scale=scale),
            distance=distance and LightYears(name, size=distance, scale=self.distance_scale),
            *args,
            **kwargs,
        )

    @property
    def field_names(self):
        yield "name"
        yield "letter"
        yield "constellation"
        yield "size"
        yield "distance"

    @property
    def width(self):
        return self.size.width

    @property
    def length(self):
        return self.size.length

    def __str__(self):
        distance = f" -> {self.distance.length}" if self.distance else ''
        size = f"{self.size.width} x {self.size.length}" if self.size.length else str(self.size.width)

        name = ""
        if self.name:
            name = f" \"{self.name}\""
        if self.constellation:
            name = f"{self.letter} {self.constellation}{name}"

        return f"{name} ({size}{distance})"


class Planet(Scalable):
    title = ""
    distance_scale = 9

    name = Scalable.field_property('name')
    size = Scalable.field_property('size')
    distance = Scalable.field_property('distance')

    def __init__(self, name, length, scale=0, distance=None, *args, **kwargs):
        name = f"{self.title} {name}" if self.title else name
        super().__init__(
            name=name,
            size=PlanetSized(name, length=length, scale=scale),
            distance=distance and Distance(name, distance=Size(distance, self.distance_scale)),
            *args,
            **kwargs,
        )

    @property
    def field_names(self):
        yield "name"
        yield "size"
        yield "distance"

    @property
    def width(self):
        return self.size.width

    @property
    def length(self):
        return self.size.width

    def __str__(self):
        distance = f" -> {self.distance.length}" if self.distance else ''
        size = str(self.size.width)
        return f"{self.name} ({size}{distance})"


class GiantPlanet(Planet):
    distance_scale = 9


class Moon(Planet):
    distance_scale = 9

    #  def __init__(self, name, width, scale=0, distance=None):
    #     super().__init__(name, width / 2, scale, distance)


class Asteroid(Planet):
    pass


class Comet(Asteroid):
    pass


ITEMS = [
    Comet("Комета Галлея", .011 / 2),

    Moon("Деймос (Марс)", .012 / 2),
    Moon("Фобос (Марс)", .022 / 2),
    Moon("Белинда (Уран)", .045),
    Moon("Никта (Плутон)", .040 / 2),
    Moon("Гидра (Плутон)", .040),
    Moon("Дисномия (Эрида)", .316 / 2),
    Moon("Галатея (Нептун)", .088),
    Moon("Нереида (Нептун)", .170),
    Moon("Миранда (Уран)", .235),
    Moon("Тритон (Нептун)", 1.353),
    Moon("Каллисто (Юпитер)", 2.410),
    Moon("Ганимед (Юпитер)", 2.634),
    Moon("Европа (Юпитер)", 1.560),
    Moon("Ио (Юпитер)", 1.821),
    Moon("Луна", 1.737),
    Moon("Титан (Уран)", 5.152 / 2),
    Moon("Титания (Уран)", 1.576 / 2),
    Moon("Харон (Плутон)", 1.212 / 2),

    Planet("Меркурий", 2.439),
    Planet("Венера", 6),
    Planet("Земля", 6.371),
    Planet("Марс", 3.389),
    Asteroid("Круитни", .005 / 2),
    Asteroid("Ганимед", .031 / 2),
    Asteroid("Бианка", .060 / 2),
    Asteroid("Нюкта", .00104),
    Asteroid("Церера", .460),
    GiantPlanet("Юпитер", 69.9),
    GiantPlanet("Сатурн", 58.2),
    GiantPlanet("Уран", 25.3),
    GiantPlanet("Нептун", 24.6),
    Asteroid("Плутон", 1.187),
    Asteroid("Эрида", 1.163),
    Asteroid("Седна", .995 / 2),
    Asteroid("Квавар", 1.110 / 2),

    GiantPlanet("TrES-4 A b", 69.9 * 1.7),

    Star("Вольф 359", .1, distance=.0078),
    Star("Звезда Лейтена", .11, distance=.012),
    Star("Звезда Каптейна", .291, distance=.013),
    Star("Солнце", 1),
    Star("Глизе 229 A", .69, distance=.018),
    Star("Глизе 229 B", .047, distance=.018),
    Star(None, 1.227, "α", "Центавра A", distance=.004),
    Star(None, .865, "α", "Центавра B", distance=.004),
    Star(None, .14, "Проксима", "Центавра", distance=.004),
    Star("Сириус A", 1.7, "α", "Большого Пса", distance=.0086),
    Star("Сириус B", 0.008, "α", "Большого Пса", distance=.0086),
    Star("Альтаир", 1.7, "α", "Орла", distance=.017),
    Star("Вега", 2.8, "α", "Лиры", distance=.0253),
    Star("Процион", 1.86, "α", "Малого Пса", distance=.011),
    Star("Регул", 4, "α", "Льва", distance=.077),
    Star("Поллукс", 8, "β", "Близнецов", distance=.033),
    Star("Спика", 7.8, "α", "Девы", distance=.26),
    Star("Капелла", 12, "α", "Возничего", distance=.042),
    Star("Альбирео", 100, "β", "Лебедя", distance=.385),
    Star(None, 8, "VV", "Цефея B", distance=5),
    Star("Арктур", 25.7, "α", "Волопаса", distance=0.036),
    Star("Полярная звезда", 37.5, "α", "Малой Медведицы", distance=.447),
    Star("Альдебаран", 43, "α", "Тельца", distance=.65),
    Star("Альнитак", 20, "ζ", "Ориона", distance=.817),
    Star("Ригель", 74, "β", "Ориона", distance=.86),
    Star("Гакрукс", 113, "γ", "Южного Креста", distance=.088),
    Star("Денеб", 210, "α", "Лебедя", distance=1.64),
    Star("La Superba", 215, "Y", "Гончих Псов", distance=.71),
    Star(None, 370, "R", "Золотой Рыбы", distance=.204),
    Star("Пистолет", 306, distance=25),
    Star("Антарес", 400, "α", "Скорпиона", distance=0.6),
    Star(None, 390, "S", "Золотой Рыбы", distance=169),
    Star(None, 700, "V382", "Киля", distance=5.93),
    Star(None, 380, "V838", "Единорога", distance=20),

    Star("Бетельгейзе", 1200, "α", "Ориона", distance=0.724),
    Star("WOH G64", 2000, distance=163),
    Star(None, 1700, "VV", "Цефея A", distance=5),
    Star(None, 1450, "VY", "Большого Пса", distance=3.9),
    Star(None, 2850, "KY", "Лебедя", distance=5.153),
    Star(None, 1250, "V354", "Цефея", distance=9),
    Star("Гранатовая Звезда Гершеля", 1420, "μ", "Цефея", distance=9),

    SystemSized("Пояс Койпера", 55),
    SystemSized("Внутренний Край Облака Оорта", 50, scale=3),
    SystemSized("Внешний Край Облака Оорта", .2, scale=6),

    Distance("от Земли до Луны", Size(.38, 9)),
    Distance("от Меркурия до Солнца", Size(60, 9)),
    Distance("от Земли до Солнца", Size(0.15, 12)),
    Distance("от Юпитера до Солнца", Size(0.78, 12)),
    Distance("от Нептуна до Солнца", Size(4.5, 12)),
    Distance("от Плутона до Солнца", Size(5.9, 12)),
    Distance("от Вояджера 1 до Земли", Size(17, 12)),
    Distance("Световой День", Size(26, 12)),

    Distance("от Проксимы Центавра до Альфы Центавра A", Size(1.5, 15)),
    Distance("от Солнца до Проксимы Центавра", Size(42, 15)),
]
