from genesys.nested.factories.nested_factory import NestedFactory
from models.universe import orbit
from .planet import AncientPlanetFactory, BarrenPlanetFactory, FuturePlanetFactory, MedievalPlanetFactory, VisitorPlanetFactory, \
    TerraformedPlanetFactory    
from .planet.body import AsteroidFactory
from .planet.gas_giant import GasGiantFactory

from ..unsorted_life import GalacticLifeFactory


class OrbitFactory(NestedFactory):
    model = orbit.Orbit

    def life(self):
        yield None

    def planets(self):
        yield None

    def children(self):
        yield from self.life()
        yield from self.planets()


class BarrenOrbitFactory(OrbitFactory):
    def planets(self):
        yield BarrenPlanetFactory.one()


class VisitorOrbitFactory(OrbitFactory):
    def planets(self):
        yield VisitorPlanetFactory.one()


class FutureOrbitFactory(OrbitFactory):
    def planets(self):
        yield FuturePlanetFactory.one()


class TerraformedOrbitFactory(OrbitFactory):
    def planets(self):
        yield TerraformedPlanetFactory.one()


class MedievalOrbitFactory(OrbitFactory):
    def planets(self):
        yield MedievalPlanetFactory.one()


class AncientOrbitFactory(OrbitFactory):
    def planets(self):
        yield AncientPlanetFactory.one()


class GasGiantOrbitFactory(OrbitFactory):
    def planets(self):
        yield GasGiantFactory.one()


class AsteroidBeltFactory(OrbitFactory):
    model = orbit.AsteroidBelt

    def life(self):
        yield GalacticLifeFactory.probable(20)

    def planets(self):
        yield AsteroidFactory.multiple(10, 30)


class EarthFactory(AsteroidBeltFactory):
    default_name = 'Earth'
