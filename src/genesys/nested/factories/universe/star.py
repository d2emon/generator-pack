from generated import universe
from ..factory import Factory
from ..temporary import StarLifeFactory, DysonSurfaceFactory
from ..materials import MoleculeFactory
from .orbit import BarrenOrbitFactory, VisitorOrbitFactory, FutureOrbitFactory, TerraformedOrbitFactory, \
    MedievalOrbitFactory, AncientOrbitFactory, AsteroidBeltFactory, GasGiantOrbitFactory


class StarFactory(Factory):
    default_model = universe.Star
    names = [
        "white", "faint", "yellow", "red", "blue", "green", "purple", "bright", "double", "twin", "triple", "old",
        "young", "dying", "small", "giant", "large", "pale", "dark", "hell", "horrific", "twisted", "spectral",
    ]

    def generate_name(self):
        return f"{self.select_item(*self.names)} star"

    def life(self):
        yield StarLifeFactory()

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
        yield VisitorOrbitFactory().probable(5)
        yield FutureOrbitFactory().probable(10)
        yield FutureOrbitFactory().probable(10)
        yield TerraformedOrbitFactory().probable(50)
        yield TerraformedOrbitFactory().probable(20)
        yield TerraformedOrbitFactory().probable(10)
        yield MedievalOrbitFactory().probable(30)
        yield MedievalOrbitFactory().probable(20)
        yield AncientOrbitFactory().probable(50)
        yield AncientOrbitFactory().probable(30)
        yield AncientOrbitFactory().probable(10)

    def orbits(self):
        yield from self.inhabited()
        yield BarrenOrbitFactory().probable(60)
        yield BarrenOrbitFactory().probable(40)
        yield BarrenOrbitFactory().probable(20)
        yield GasGiantOrbitFactory().probable(60)
        yield GasGiantOrbitFactory().probable(40)
        yield GasGiantOrbitFactory().probable(20)
        yield GasGiantOrbitFactory().probable(10)
        yield from AsteroidBeltFactory().multiple(0, 2)

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
        yield DysonSurfaceFactory()
        yield from FutureOrbitFactory().multiple(1, 8)
