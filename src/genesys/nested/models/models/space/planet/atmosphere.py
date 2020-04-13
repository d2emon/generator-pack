from genesys.nested.models import Model
from genesys.nested.models.mixins import EncounteredMixin
from ..life import GasGiantLife
# from ...biology import GalacticLife
from ...chemistry import elements, Ammonia, Gas, Steam, Water, Methane


class Atmosphere(Model, EncounteredMixin):
    life = Model.child_property(GasGiantLife)
    gases = Model.children_property(Gas)

    default_name = 'atmosphere'

    class Factory(Model.Factory):
        @classmethod
        def life(cls):
            yield None

        @classmethod
        def gases(cls):
            yield None

        def children(self):
            yield from self.life()
            yield from self.gases()


class GasGiantAtmosphere(Atmosphere):
    class Factory(Atmosphere.Factory):
        @classmethod
        def life(cls):
            yield GasGiantLife

        @classmethod
        def gases(cls):
            yield Gas.from_atoms('He')
            yield Gas.from_atoms('H')
            yield Steam.probable(50)
            yield Ammonia.probable(50)
            yield Methane.probable(50)
