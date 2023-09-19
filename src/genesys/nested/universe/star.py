from factories.thing.nested_factory import NestedFactory
from models.universe import star
from utils.nested import select_item
from ..materials import ELEMENTS
from .data_provider import PROVIDER
from .orbit import AncientOrbitFactory, AsteroidBeltFactory, BarrenOrbitFactory, FutureOrbitFactory, GasGiantOrbitFactory, \
    MedievalOrbitFactory, TerraformedOrbitFactory, VisitorOrbitFactory
# from ..temporary import DysonSurfaceFactory
# from ..life import StarLifeFactory


class StarFactory(NestedFactory):
    default_data = PROVIDER
    model = star.Star

    def life(self):
        # ghost,0.1%
        # space monster,0.2%
        # yield StarLifeFactory()
        yield None

    def matter(self):
        yield ELEMENTS['He'].one()
        yield ELEMENTS['H'].one()

    def contents(self):
        yield from self.matter()

    def name_factory(self, *args, **kwargs):
        return f"{select_item(*self.names)} star"


class StarSystemFactory(NestedFactory):
    model = star.StarSystem

    def stars(self):
        yield StarFactory.one()
        yield StarFactory.probable(3)

    def orbits(self):
        yield VisitorOrbitFactory.probable(5)

        yield FutureOrbitFactory.probable(10)
        yield FutureOrbitFactory.probable(10)

        yield TerraformedOrbitFactory.probable(50)
        yield TerraformedOrbitFactory.probable(20)
        yield TerraformedOrbitFactory.probable(10)

        yield MedievalOrbitFactory.probable(30)
        yield MedievalOrbitFactory.probable(20)

        yield AncientOrbitFactory.probable(50)
        yield AncientOrbitFactory.probable(30)
        yield AncientOrbitFactory.probable(10)

        yield BarrenOrbitFactory.probable(60)
        yield BarrenOrbitFactory.probable(40)
        yield BarrenOrbitFactory.probable(20)

        yield GasGiantOrbitFactory.probable(60)
        yield GasGiantOrbitFactory.probable(40)
        yield GasGiantOrbitFactory.probable(20)
        yield GasGiantOrbitFactory.probable(10)

        yield AsteroidBeltFactory.multiple(0, 2)

    def children(self):
        yield from self.stars()
        yield from self.orbits()


class DysonSphereFactory(StarSystemFactory):
    model = star.DysonSphere

    def orbits(self):
        # yield DysonSurfaceFactory.one()

        yield FutureOrbitFactory.multiple(1, 8)

        yield BarrenOrbitFactory.probable(60)
        yield BarrenOrbitFactory.probable(40)
        yield BarrenOrbitFactory.probable(20)

        yield GasGiantOrbitFactory.probable(60)
        yield GasGiantOrbitFactory.probable(40)
        yield GasGiantOrbitFactory.probable(20)
        yield GasGiantOrbitFactory.probable(10)

        yield AsteroidBeltFactory.multiple(0, 2)


class SingleStarFactory(StarSystemFactory):
    def stars(self):
        yield StarFactory.one()

    def orbits(self):
        yield None
