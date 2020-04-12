from genesys.nested.models import Model
from genesys.nested.models.mixins import EncounteredMixin
# from ...biology import GalacticLife
from ...chemistry import elements, Water, Ammonia, Methane


class Atmosphere(Model, EncounteredMixin):
    gases = Model.children_property(
        elements['He'],
        elements['H'],
        Water,
        Ammonia,
        Methane,
    )

    default_name = 'atmosphere'

    class Factory(Model.Factory):
        def encounters(self):
            yield None

        def gases(self):
            yield None

        def children(self):
            yield from self.encounters()
            yield from self.gases()


class GasGiantAtmosphere(Atmosphere):
    class Factory(Atmosphere.Factory):
        def encounters(self):
            # yield GalacticLife.probable(10)
            yield None

        def gases(self):
            yield elements['He']
            yield elements['H']
            yield Water.probable(50)
            yield Ammonia.probable(50)
            yield Methane.probable(50)
