from generated import universe
from ...factory import Factory


class PlanetFactory(Factory):
    # PlanetLike
    default_model = universe.Planet

    def visited(self):
        yield None

    @classmethod
    def moons(cls):
        # yield Moon.probable(40)
        # yield Moon.probable(20)
        # yield Moon.probable(10)
        yield None

    def children(self):
        # ".terraformed planet"
        yield from super().children()
        yield from self.moons()


class BarrenPlanetFactory(PlanetFactory):
    def biosphere(self):
        # "galactic life,10%"
        # yield BarrenPlanetLife
        yield None

    def children(self):
        yield from self.visited()
        yield from self.biosphere()
        # "Rock"
        # "Ice,50%"
        # ".planet composition"


class VisitorPlanetFactory(BarrenPlanetFactory):
    def biosphere(self):
        # "galactic life"
        # yield VisitorPlanetLife
        yield None

    def visited(self):
        # yield from VisitorCity.multiple(1, 8)
        # yield from VisitorInstallation.multiple(2, 6)
        yield None

    def children(self):
        yield from self.visited()
        yield from self.biosphere()
        # "Rock"
        # "Ice,50%"
        # ".planet composition"


class PlanetCompositionFactory(BarrenPlanetFactory):
    default_name = 'planet'

    def children(self):
        # "planet core"
        # "moon,40%"
        # "moon,20%"
        # "moon,10%"
        yield None


class TelluricPlanetFactory(PlanetCompositionFactory):
    def atmosphere(self):
        # yield Atmosphere
        yield None

    def biosphere(self):
        yield None

    def continents(self):
        # yield from Continent.multiple(2, 7)
        yield None

    def oceans(self):
        # yield from Ocean.multiple(1, 7)
        yield None

    def plates(self):
        yield from self.continents()
        yield from self.oceans()

    def sky(self):
        # yield Sky
        yield None

    def moons(self):
        yield None

    def children(self):
        yield from self.visited()
        yield from self.atmosphere()
        yield from self.biosphere()
        yield from self.plates()
        yield from self.sky()
        yield from self.moons()
        yield from super().children()


class FuturePlanetFactory(TelluricPlanetFactory):
    def continents(self):
        # yield from FutureContinent.multiple(2, 7)
        yield None

    def sky(self):
        # yield FutureSky
        yield None

    def moons(self):
        # ".future moon,30%"
        yield from super().moons()
        # yield FutureMoon.probable(30)


class TerraformedPlanetFactory(TelluricPlanetFactory):
    def continents(self):
        # "continent,2-7"
        yield None

    def sky(self):
        # yield TerraformedSky
        yield None

    def moons(self):
        # ".terraformed moon,30%"
        yield from super().moons()
        # yield TerraformedMoon.probable(30)


class MedievalPlanetFactory(TelluricPlanetFactory):
    def continents(self):
        # yield from MedievalContinent.multiple(2, 4)
        # yield from AncientContinent.multiple(0, 3)
        yield None


class AncientPlanetFactory(TelluricPlanetFactory):
    def continents(self):
        # yield from AncientContinent.multiple(2, 7)
        yield None
