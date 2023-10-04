from atlas.common import Named


class Core:
    pass


class Mantle:
    pass


class Crust:
    pass


class Troposphere:
    def __init__(self, clouds=None):
        self.clouds = clouds or []


class Stratosphere:
    def __init__(self, clouds=None):
        self.clouds = clouds or []


class Mesosphere:
    def __init__(self, clouds=None):
        self.clouds = clouds or []


class Thermosphere:
    def __init__(self, meteorites=None, auroras=None):
        self.meteorites = meteorites or []
        self.auroras = auroras or []


class Exosphere:
    def __init__(self, auroras=None):
        self.auroras = auroras or []


class Planet(Named):
    def __init__(self, name, moons=None):
        super().__init__(name)
        self.__moons = moons or []
        self.layers = [
            Core(),
            Mantle(),
            Crust(),
            Troposphere(),
            Stratosphere(),
            Mesosphere(),
            Thermosphere(),
            Exosphere(),
        ]

    @property
    def moons(self):
        return self.__moons

    @moons.setter
    def moons(self, value):
        self.__moons = value
