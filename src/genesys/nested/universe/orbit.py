from factories.thing.nested_factory import NestedFactory
from models.v5 import universe
# from ..life import AsteroidBeltLifeFactory
from .planet.body import AsteroidFactory
from .planet import BarrenPlanetFactory, VisitorPlanetFactory, FuturePlanetFactory, TerraformedPlanetFactory, \
    MedievalPlanetFactory, AncientPlanetFactory, GasGiantFactory


class OrbitFactory(NestedFactory):
    model = universe.Orbit

    def life(self):
        yield None

    def planets(self):
        yield None

    def children(self):
        yield from self.life()
        yield from self.planets()


class PlanetOrbitFactory(OrbitFactory):
    pass


class BarrenOrbitFactory(PlanetOrbitFactory):
    def planets(self):
        yield BarrenPlanetFactory.one()


class VisitorOrbitFactory(PlanetOrbitFactory):
    def planets(self):
        yield VisitorPlanetFactory.one()


class FutureOrbitFactory(PlanetOrbitFactory):
    def planets(self):
        yield FuturePlanetFactory.one()


class TerraformedOrbitFactory(PlanetOrbitFactory):
    def planets(self):
        yield TerraformedPlanetFactory.one()


class MedievalOrbitFactory(PlanetOrbitFactory):
    def planets(self):
        yield MedievalPlanetFactory.one()


class AncientOrbitFactory(PlanetOrbitFactory):
    def planets(self):
        yield AncientPlanetFactory.one()


class GasGiantOrbitFactory(PlanetOrbitFactory):
    def planets(self):
        yield GasGiantFactory.one()


class AsteroidBeltFactory(OrbitFactory):
    # TODO: Refactor It
    model = universe.AsteroidBelt

    def life(self):
        # yield AsteroidBeltLifeFactory()
        yield None

    def planets(self):
        yield from AsteroidFactory.multiple(10, 30)


class EarthFactory(AsteroidBeltFactory):
    # TODO: Refactor It
    default_name = 'Earth'
