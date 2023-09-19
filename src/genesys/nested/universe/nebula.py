from factories.thing.nested_factory import NestedFactory
from models.universe import nebula
from utils.nested import select_item
from ..materials import ELEMENTS, AmmoniaFactory
from ..materials.water import SteamFactory
# from ..life import NebulaLifeFactory
from .data_provider import PROVIDER
from .star import SingleStarFactory


class InterstellarCloudFactory(NestedFactory):
    default_data = PROVIDER
    model = nebula.InterstellarCloud

    def contents(self):
        yield ELEMENTS['He'].one()
        yield ELEMENTS['H'].one()
        yield ELEMENTS['C'].probable(80)
        yield SteamFactory.probable(5)
        yield AmmoniaFactory.probable(5)
        yield ELEMENTS['N'].probable(5),
        yield ELEMENTS['Fe'].probable(5),
        yield ELEMENTS['S'].probable(5),
        yield ELEMENTS['O'].probable(15),

    def name_factory(self):
        return f"{select_item(*self.data.interstellar_cloud)} interstellar cloud"


class NebulaFactory(NestedFactory):
    model = nebula.Nebula

    def life(self):
        # galactic life,15%
        # yield NebulaLifeFactory()
        yield None

    def stars(self):
        yield SingleStarFactory.probable(2)
        yield SingleStarFactory.probable(2)
        yield SingleStarFactory.probable(2)

    def clouds(self):
        yield InterstellarCloudFactory.multiple(1, 6)

    def children(self):
        yield from self.life()
        yield from self.stars()
        yield from self.clouds()
