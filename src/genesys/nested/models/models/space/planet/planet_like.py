from genesys.nested.models.models.unknown import Continent, VisitorCity, VisitorInstallation
from genesys.nested.models import Model
from genesys.nested.models.mixins import EncounteredMixin
from .atmosphere import Atmosphere
from ...biology import SpaceMonster
from ...chemistry import elements, Rock, Ice, Diamond, Magma
from ...terrain import Ocean


class Orbit(Model, EncounteredMixin):
    pass


class PlanetCore(Model, EncounteredMixin):
    contents = Model.children_property(
        elements['Fe'],
        Rock,
        Diamond,
        Magma,
    )

    class NameFactory(Model.NameFactory):
        default = 'core'

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            # Encounters
            yield SpaceMonster.probable(0.5)
            # Contents
            yield elements['Fe']
            yield Rock
            yield Diamond.probable(2)
            yield Magma


class PlanetLike(Orbit):
    atmosphere = Model.child_property(Atmosphere)
    core = Model.child_property(PlanetCore)
    land = Model.children_property(Rock, Continent)
    water = Model.children_property(Ice, Ocean)
    visited = Model.children_property(VisitorCity, VisitorInstallation)

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield PlanetCore
