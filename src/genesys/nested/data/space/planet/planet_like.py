from ... import unknown
from genesys.nested.models import Model
from genesys.nested.models.mixins import EncounteredMixin
from .atmosphere import Atmosphere
from ...chemistry import elements, Rock, Ice, Diamond, Magma


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
            yield unknown.SpaceMonster.probable(0.5)
            # Contents
            yield elements['Fe']
            yield Rock
            yield Diamond.probable(2)
            yield Magma


class PlanetLike(Orbit):
    atmosphere = Model.child_property(Atmosphere)
    core = Model.child_property(PlanetCore)
    land = Model.children_property(Rock, unknown.Continent)
    water = Model.children_property(Ice, unknown.Ocean)
    visited = Model.children_property(unknown.VisitorCity, unknown.VisitorInstallation)

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield PlanetCore
