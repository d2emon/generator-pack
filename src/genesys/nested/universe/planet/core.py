from models.planet.core import PlanetCore
from factories.nested_factory import NestedFactory
# from ...life import PlanetCoreLifeFactory
# from ...materials import RockFactory, IronFactory, DiamondFactory, MagmaFactory


class PlanetCoreFactory(NestedFactory):
    default_model = PlanetCore
    default_name = "core"

    def life(self):
        # yield PlanetCoreLifeFactory()
        # space monster,0.5%
        yield None

    def contents(self):
        # yield IronFactory()
        # yield RockFactory()
        # yield DiamondFactory().probable(2)
        # yield MagmaFactory()
        # iron
        # rock
        # diamond,2%
        # magma
        yield None


"""
new Thing("planet core",[
    "space monster,0.5%",
    "iron",
    "rock",
    "diamond,2%",
    "magma"
],"core");
"""
