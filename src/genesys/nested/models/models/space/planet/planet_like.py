from genesys.nested.models.models.unknown import Continent, VisitorCity, VisitorInstallation
from genesys.nested.models import Model
from genesys.nested.models.mixins import EncounteredMixin
from .atmosphere import Atmosphere
# from ...biology import SpaceMonster
from ...chemistry import elements, Atom, Diamond, Ice, Magma, Rock
# from ...terrain import Ocean


class Orbit(Model, EncounteredMixin):
    pass


class PlanetCore(Model, EncounteredMixin):
    contents = Model.children_property(
        Atom,
        Rock,
    )

    default_name = 'core'

    class Factory(Orbit.Factory):
        def life(self):
            # yield SpaceMonster.probable(0.5)
            yield None

        def rocks(self):
            yield elements['Fe']
            yield Rock
            yield Diamond.probable(2)
            yield Magma

        def children(self):
            yield from self.life()
            yield from self.rocks()


class Plate(Model):
    class Factory(Model.Factory):
        def children(self):
            yield Rock
            yield Ice


class PlanetLike(Orbit):
    atmosphere = Model.child_property(Atmosphere)
    core = Model.child_property(PlanetCore)
    plates = Model.children_property(Plate)
    land = Model.children_property(Continent)
    # water = Model.children_property(Ocean)
    visited = Model.children_property(VisitorCity, VisitorInstallation)

    class Factory(Orbit.Factory):
        def atmosphere(self):
            yield None

        def biosphere(self):
            yield None

        def core(self):
            yield PlanetCore

        def plates(self):
            yield from Plate.multiple(2, 7)
            yield from Plate.multiple(1, 7)

        def sky(self):
            yield None

        def visited(self):
            yield None

        def children(self):
            yield from self.core()
            yield from self.atmosphere()
            yield from self.biosphere()
            yield from self.plates()
            yield from self.sky()
            yield from self.visited()
