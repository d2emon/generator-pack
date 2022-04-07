from models.universe.star import Star, StarSystem
from factories.nested_factory import NestedFactory
# from ..temporary import DysonSurfaceFactory
# from ..life import StarLifeFactory
# from ..materials import MoleculeFactory
# from .orbit import BarrenOrbitFactory, VisitorOrbitFactory, FutureOrbitFactory, TerraformedOrbitFactory, \
#     MedievalOrbitFactory, AncientOrbitFactory, AsteroidBeltFactory, GasGiantOrbitFactory


# StarSystem
# DysonSphere
# Star


class StarSystemFactory(NestedFactory):
    default_model = StarSystem

    def stars(self):
        yield StarFactory.as_child()
        yield StarFactory.probable(3)

    def inhabited(self):
        # yield VisitorOrbitFactory().probable(5)
        # yield FutureOrbitFactory().probable(10)
        # yield FutureOrbitFactory().probable(10)
        # yield TerraformedOrbitFactory().probable(50)
        # yield TerraformedOrbitFactory().probable(20)
        # yield TerraformedOrbitFactory().probable(10)
        # yield MedievalOrbitFactory().probable(30)
        # yield MedievalOrbitFactory().probable(20)
        # yield AncientOrbitFactory().probable(50)
        # yield AncientOrbitFactory().probable(30)
        # yield AncientOrbitFactory().probable(10)
        yield None

    def orbits(self):
        yield from self.inhabited()
        # yield BarrenOrbitFactory().probable(60)
        # yield BarrenOrbitFactory().probable(40)
        # yield BarrenOrbitFactory().probable(20)
        # yield GasGiantOrbitFactory().probable(60)
        # yield GasGiantOrbitFactory().probable(40)
        # yield GasGiantOrbitFactory().probable(20)
        # yield GasGiantOrbitFactory().probable(10)
        # yield from AsteroidBeltFactory().multiple(0, 2)

    def children(self):
        yield from self.stars()
        yield from self.orbits()


class DysonSphereFactory(StarSystemFactory):
    # default_model = DysonSphere

    def inhabited(self):
        # yield DysonSurfaceFactory()
        # yield from FutureOrbitFactory().multiple(1, 8)
        yield None


class StarFactory(NestedFactory):
    default_model = Star
    names = [
        "white", "faint", "yellow", "red", "blue", "green", "purple", "bright", "double", "twin", "triple", "old",
        "young", "dying", "small", "giant", "large", "pale", "dark", "hell", "horrific", "twisted", "spectral",
    ]

    def name_factory(self, *args, **kwargs):
        return f"{self.select_item(*self.names)} star"

    def life(self):
        # yield StarLifeFactory()
        yield None

    def matter(self):
        # yield MoleculeFactory.from_elements('H')
        # yield MoleculeFactory.from_elements('He')
        yield None

    def children(self):
        yield from self.life()
        yield from self.matter()


####


class SingleStarFactory(StarSystemFactory):
    def stars(self):
        yield StarFactory()

    def inhabited(self):
        yield None

    def orbits(self):
        yield None


"""
new Thing("star system",[
    "star",
    "star,3%",
    ####
    "visitor planet,5%",
    "future planet,10%",
    "future planet,10%",
    "terraformed planet,50%",
    "terraformed planet,20%",
    "terraformed planet,10%",
    "medieval planet,30%",
    "medieval planet,20%",
    "ancient planet,50%",
    "ancient planet,30%",
    "ancient planet,10%",
    "barren planet,60%",
    "barren planet,40%",
    "barren planet,20%",
    "gas giant,60%",
    "gas giant,40%",
    "gas giant,20%",
    "gas giant,10%",
    "asteroid belt,0-2",
]);
new Thing("dyson sphere",[
    "star",
    "star,3%",
    ####
    "dyson surface",
    "future planet,1-8",
    "barren planet,60%",
    "barren planet,40%",
    "barren planet,20%",
    "gas giant,60%",
    "gas giant,40%",
    "gas giant,20%",
    "gas giant,10%",
    "asteroid belt,0-2",
]);
new Thing("star",[
    "ghost,0.1%",
    "space monster,0.2%",
    "hydrogen",
    "helium"
],[
    [
        "white","faint","yellow","red","blue","green","purple","bright","double","twin","triple","old","young",
        "dying","small","giant","large","pale","dark","hell","horrific","twisted","spectral"
    ],[
        " star"
    ]
]);
"""