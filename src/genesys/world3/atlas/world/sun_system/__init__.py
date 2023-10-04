from atlas.common import Named


class AsteroidBelt(Named):
    pass


class Comet(Named):
    pass


class StarSystem(Named):
    def __init__(self, name, star=None, planets=None):
        super().__init__(name)
        self.__star = star
        self.__planets = planets or []

    @property
    def star(self):
        return self.__star

    @star.setter
    def star(self, value):
        self.__star = value

    @property
    def planets(self):
        return self.__planets

    @planets.setter
    def planets(self, value):
        self.__planets = value
