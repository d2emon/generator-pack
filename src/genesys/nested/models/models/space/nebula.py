from genesys.nested.models import Model
from genesys.nested.models.mixins import EncounteredMixin
from .star import StarSystem, SingleStar
from ..chemistry import elements, Matter, Atom, Water, Ammonia
# from ..biology import GalacticLife
from genesys.nested.data import lookups


class InterstellarCloud(Matter):
    contents = Model.children_property(Matter, Atom)

    class Factory(Matter.Factory):
        class DataProvider:
            interstellar_cloud = lookups.interstellar_clouds

        name = property(lambda self: self.provider.interstellar_cloud)

        def children(self):
            yield elements['He']
            yield elements['H']
            yield elements['C'].probable(80)
            yield Water.probable(5)
            yield Ammonia.probable(5)
            yield elements['N'].probable(5)
            yield elements['Fe'].probable(5)
            yield elements['S'].probable(5)
            yield elements['O'].probable(15)


class Nebula(Model, EncounteredMixin):
    stars = Model.children_property(StarSystem)
    clouds = Model.children_property(InterstellarCloud)

    class Factory(Model.Factory):
        def children(self):
            # yield GalacticLife.probable(15)
            yield SingleStar.probable(2)
            yield SingleStar.probable(2)
            yield SingleStar.probable(2)
            yield from InterstellarCloud.multiple(1, 6)
