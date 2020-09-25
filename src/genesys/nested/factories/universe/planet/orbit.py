from generated import universe
from ...factory import Factory
from .body import AsteroidFactory
from .planet import BarrenPlanetFactory, VisitorPlanetFactory, FuturePlanetFactory, TerraformedPlanetFactory, \
    MedievalPlanetFactory, AncientPlanetFactory, GasGiantFactory


class OrbitFactory(Factory):
    default_model = universe.Orbit

    def life(self):
        yield None

    def planets(self):
        yield None

    def children(self):
        yield from self.life()
        yield from self.planets()


class PlanetOrbitFactory(OrbitFactory):
    default_model = universe.Orbit


class BarrenOrbitFactory(PlanetOrbitFactory):
    def planets(self):
        yield BarrenPlanetFactory()


class VisitorOrbitFactory(PlanetOrbitFactory):
    def planets(self):
        yield VisitorPlanetFactory()


class FutureOrbitFactory(PlanetOrbitFactory):
    def planets(self):
        yield FuturePlanetFactory()


class TerraformedOrbitFactory(PlanetOrbitFactory):
    def planets(self):
        yield TerraformedPlanetFactory()


class MedievalOrbitFactory(PlanetOrbitFactory):
    def planets(self):
        yield MedievalPlanetFactory()


class AncientOrbitFactory(PlanetOrbitFactory):
    def planets(self):
        yield AncientPlanetFactory()


class GasGiantOrbitFactory(PlanetOrbitFactory):
    def planets(self):
        yield GasGiantFactory()


class AsteroidBeltFactory(OrbitFactory):
    default_model = universe.AsteroidBelt

    def life(self):
        # "galactic life,20%"
        # yield AsteroidBeltLife
        yield None

    def planets(self):
        yield from AsteroidFactory().multiple(10, 30)


class EarthFactory(AsteroidBeltFactory):
    default_name = 'Earth'
