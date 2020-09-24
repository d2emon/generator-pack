from generated import universe
from ..factory import Factory
from ..materials import MoleculeFactory
from .planet import BarrenPlanetFactory, VisitorPlanetFactory, FuturePlanetFactory, TerraformedPlanetFactory, \
    MedievalPlanetFactory, AncientPlanetFactory


class StarFactory(Factory):
    default_model = universe.Star

    # class DataProvider:
    #     star = lookups.stars

    # name = property(lambda self: self.provider.star)

    # ["white","faint","yellow","red","blue","green","purple","bright","double","twin","triple","old","young","dying",
    # "small","giant","large","pale","dark","hell","horrific","twisted","spectral"],
    # [" star"]

    def life(self):
        # "ghost,0.1%"
        # "space monster,0.2%"
        # yield StarLife
        yield None

    def matter(self):
        yield MoleculeFactory.from_elements('H')
        yield MoleculeFactory.from_elements('He')

    def children(self):
        yield from self.life()
        yield from self.matter()


class StarSystemFactory(Factory):
    default_model = universe.StarSystem

    def stars(self):
        yield StarFactory()
        yield StarFactory().probable(3)

    def inhabited(self):
        yield VisitorPlanetFactory().probable(5)
        yield FuturePlanetFactory().probable(10)
        yield FuturePlanetFactory().probable(10)
        yield TerraformedPlanetFactory().probable(50)
        yield TerraformedPlanetFactory().probable(20)
        yield TerraformedPlanetFactory().probable(10)
        yield MedievalPlanetFactory().probable(30)
        yield MedievalPlanetFactory().probable(20)
        yield AncientPlanetFactory().probable(50)
        yield AncientPlanetFactory().probable(30)
        yield AncientPlanetFactory().probable(10)

    def orbits(self):
        yield from self.inhabited()
        yield BarrenPlanetFactory().probable(60)
        yield BarrenPlanetFactory().probable(40)
        yield BarrenPlanetFactory().probable(20)
        # yield GasGiant.probable(60)
        # yield GasGiant.probable(40)
        # yield GasGiant.probable(20)
        # yield GasGiant.probable(10)
        # yield from AsteroidBelt.multiple(0, 2)

    def children(self):
        yield from self.stars()
        yield from self.orbits()


class SingleStarFactory(StarSystemFactory):
    def stars(self):
        yield StarFactory()

    def inhabited(self):
        yield None

    def orbits(self):
        yield None


class DysonSphereFactory(StarSystemFactory):
    def inhabited(self):
        # yield DysonSurface
        yield from FuturePlanetFactory().multiple(1, 8)
