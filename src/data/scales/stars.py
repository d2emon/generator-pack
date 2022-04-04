from models.scales import Sized as Scalable, ScalableSize as Size


class Star(Scalable):
    def __init__(self, name, size, scale=9):
        super().__init__(name, Size(size, scale))


STARS = [
    Star("A.C. +70 8247", 6.6, 6),
    Star("Сириус B", 10.932, 6),
    Star("Земля", 12.742, 6),
    Star("Процион", 13.4, 6),
    Star("Юпитер", .139),
    Star("Проксима Центавра", .202),
    Star("Звезда Каптейна", .406),
    Star("Солнце", 1.391),
    Star("Арктур", 33.341),
    Star("Полярная звезда", 52.177),
    Star("Ригель A", 109.781),
    Star("Дельта Большого Пса", 329.761),
    Star("La Superba", 542.646),
    Star("Антарес", 1228.606),
    Star("VY Большого Пса", 1975.788),
    Star("UY Щита", 2376.511),
]
