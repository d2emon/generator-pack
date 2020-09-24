from generated import universe
from ..factory import Factory
from ..materials import MoleculeFactory


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
        # yield VisitorPlanet.probable(5)
        # yield FuturePlanet.probable(10)
        # yield FuturePlanet.probable(10)
        # yield TerraformedPlanet.probable(50)
        # yield TerraformedPlanet.probable(20)
        # yield TerraformedPlanet.probable(10)
        # yield MedievalPlanet.probable(30)
        # yield MedievalPlanet.probable(20)
        # yield AncientPlanet.probable(50)
        # yield AncientPlanet.probable(30)
        # yield AncientPlanet.probable(10)
        yield None

    def orbits(self):
        yield from self.inhabited()
        # yield BarrenPlanet.probable(60)
        # yield BarrenPlanet.probable(40)
        # yield BarrenPlanet.probable(20)
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
        # yield from FuturePlanet.multiple(1, 8)
        yield None
