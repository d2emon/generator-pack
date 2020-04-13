from genesys.nested.models import Model
from genesys.nested.models.mixins import EncounteredMixin
from .life import GalacticLife
from .star import StarSystem, SingleStar
from ..chemistry import Ammonia, Gas, Matter, Steam
from genesys.nested.data import lookups


class InterstellarCloud(Matter):
    gases = Model.children_property(Gas)

    class Factory(Matter.Factory):
        class DataProvider:
            interstellar_cloud = lookups.interstellar_clouds

        name = property(lambda self: self.provider.interstellar_cloud)

        def children(self):
            yield Gas.from_atoms('He')
            yield Gas.from_atoms('H')
            yield Gas.from_atoms('C').probable(80)
            yield Steam.probable(5)
            yield Ammonia.probable(5)
            yield Gas.from_atoms('N').probable(5)
            yield Gas.from_atoms('Fe').probable(5)
            yield Gas.from_atoms('S').probable(5)
            yield Gas.from_atoms('O').probable(15)


class Nebula(Model, EncounteredMixin):
    life = Model.child_property(GalacticLife)
    stars = Model.children_property(StarSystem)
    clouds = Model.children_property(InterstellarCloud)

    class Factory(Model.Factory):
        @classmethod
        def life(cls):
            yield GalacticLife.probable(15)

        @classmethod
        def stars(cls):
            yield SingleStar.probable(2)
            yield SingleStar.probable(2)
            yield SingleStar.probable(2)

        @classmethod
        def clouds(cls):
            yield from InterstellarCloud.multiple(1, 6)

        def children(self):
            yield from self.life()
            yield from self.stars()
            yield from self.clouds()
