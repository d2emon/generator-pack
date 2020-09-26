from .scalable import Scalable


class Asteroid(Scalable):
    def __init__(self, name, size, scale=6):
        Scalable.__init__(self, name, size, scale)


class Planet(Scalable):
    def __init__(self, name, size, scale=6):
        Scalable.__init__(self, name, size, scale)


class Satellite(Planet):
    pass


class Star(Scalable):
    def __init__(self, name, size, scale=9):
        Scalable.__init__(self, name, size, scale)


SOLAR = [
    Asteroid("Тунгусский метеорит", .1, 3),

    Asteroid("Gaspra", 34, 3),
    Asteroid("Psyche", .264),
    Asteroid("Pallas", .522),
    Asteroid("Ceres", .975),
    Asteroid("Haumea", 1.400),
    Asteroid("Make Make", 1.420),
    Asteroid("Eris", 2.326),

    Planet("Плутон", 2.374),
    Satellite("Харон", 1.212),

    Planet("Меркурий", 4.879),

    Planet("Марс", 6.799),
    Satellite("Фобос", 22, 3),
    Satellite("Деймос", 12, 3),

    Planet("Венера", 12.104),

    Planet("Земля", 12.742),
    Satellite("Луна", 3.474),

    Planet("Нептун", 49.244),
    Satellite("Тритон", 2.706),
    Satellite("Протей", .420),

    Planet("Уран", 50.724),
    Satellite("Титания", 1.576),
    Satellite("Оберон", 1.522),
    Satellite("Умбриэль", 1.168),
    Satellite("Ариэль", 1.156),
    Satellite("Миранда", .470),

    Planet("Сатурн", 116.474),
    Satellite("Титан", 5.151),
    Satellite("Rhea", 1.525),
    Satellite("Iapetus", 1.468),
    Satellite("Dione", 1.122),
    Satellite("Enceladus", .502),
    Satellite("Mimas", .396),

    Planet("Юпитер", 139.822),
    Satellite("Ганимед", 5.262),
    Satellite("Каллисто", 4.821),
    Satellite("Ио", 3.643),
    Satellite("Европа", 3.122),

    Star("Солнце", 1.391),
]
