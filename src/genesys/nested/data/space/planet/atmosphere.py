from ...unknown import GalacticLife
from genesys.nested.models import Model
from genesys.nested.models.mixins import EncounteredMixin
from ...chemistry import elements, Water, Ammonia, Methane


class Atmosphere(Model, EncounteredMixin):
    contents = Model.children_property(
        elements['He'],
        elements['H'],
        Water,
        Ammonia,
        Methane,
    )

    class NameFactory(Model.NameFactory):
        default = 'atmosphere'


class GasGiantAtmosphere(Atmosphere):
    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            # Encounters
            yield GalacticLife.probable(10)
            # Contents
            yield elements['He']
            yield elements['H']
            yield Water.probable(50)
            yield Ammonia.probable(50)
            yield Methane.probable(50)
