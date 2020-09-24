from genesys.model.model import Model
# from generated.nested_v2.models import Continent, VisitorCity, VisitorInstallation
# from .atmosphere import Atmosphere
# from generated.universe.space.life import Habitat, PlanetCoreLife
# from generated.materials.chemistry import Ice
# from generated.materials import Diamond, Iron, Magma, Rock
# from generated.nested_v2.models.terrain import Ocean


class Orbit(Model):
    # Habitat
    pass


class PlanetCore(Model):
    # Habitat
    minerals = Habitat.children_property(Rock)

    default_name = 'core'

    class Factory(Habitat.Factory):
        @classmethod
        def life(cls):
            yield PlanetCoreLife

        @classmethod
        def minerals(cls):
            yield Iron
            yield Rock
            yield Diamond.probable(2)
            yield Magma

        def children(self):
            yield from self.life()
            yield from self.minerals()


class Plate(Model):
    minerals = Model.children_property(Rock)
    ice = Model.children_property(Ice)

    class Factory(Model.Factory):
        def children(self):
            yield Rock
            yield Ice


class PlanetLike(Orbit):
    # atmosphere = Model.child_property(Atmosphere)
    # biosphere = Model.child_property(Model)
    # core = Model.child_property(PlanetCore)
    # plates = Model.children_property(Plate)
    # # sky = Model.children_property(Sky)
    # land = Model.children_property(Continent)
    # water = Model.children_property(Ocean)
    # visited = Model.children_property(VisitorCity, VisitorInstallation)
    pass
