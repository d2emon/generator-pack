from genesys.nested.models.models.unknown import Continent, VisitorCity, VisitorInstallation
from genesys.nested.models import Model
from genesys.nested.models.mixins import EncounteredMixin
# from .atmosphere import Atmosphere
# from ...biology import SpaceMonster
from ...chemistry import elements, Atom
# from ...chemistry import elements, Rock, Ice, Diamond, Magma, Atom
# from ...terrain import Ocean


class Orbit(Model, EncounteredMixin):
    pass


class PlanetCore(Model, EncounteredMixin):
    contents = Model.children_property(
        Atom,
        # Rock,
        # Diamond,
        # Magma,
    )

    default_name = 'core'

    class Factory(Orbit.Factory):
        def life(self):
            # yield SpaceMonster.probable(0.5)
            yield None

        def rocks(self):
            yield elements['Fe']
            # yield Rock
            # yield Diamond.probable(2)
            # yield Magma

        def children(self):
            yield from self.life()
            yield from self.rocks()


class PlanetLike(Orbit):
    # atmosphere = Model.child_property(Atmosphere)
    core = Model.child_property(PlanetCore)
    # land = Model.children_property(Rock, Continent)
    # water = Model.children_property(Ice, Ocean)
    # visited = Model.children_property(VisitorCity, VisitorInstallation)

    class Factory(Orbit.Factory):
        def atmosphere(self):
            yield None

        def biosphere(self):
            yield None

        def children(self):
            yield PlanetCore
            yield from self.atmosphere()
            yield from self.biosphere()
