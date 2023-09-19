from factories.thing.nested_factory import NestedFactory
from models.v5 import universe
from .planet import AncientPlanetFactory, BarrenPlanetFactory, FuturePlanetFactory, MedievalPlanetFactory, VisitorPlanetFactory, \
    TerraformedPlanetFactory    
from .planet.body import AsteroidFactory
from .planet.gas_giant import GasGiantFactory
from .unsorted_life import GalacticLifeFactory


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


class AsteroidBeltFactory(NestedFactory):
    model = universe.AsteroidBelt

    def life(self):
        yield GalacticLifeFactory.probable(20)

    def planets(self):
        yield AsteroidFactory.multiple(10, 30)


class EarthFactory(AsteroidBeltFactory):
    default_name = 'Earth'
