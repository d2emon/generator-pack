from genesys.nested.models.models.unknown import Ghost
from genesys.nested.models import Model
# from ..biology import Crustacean, GalacticLife, SpaceMonster


class BlackHoleLife(Model):
    life = Model.child_property(Model)

    class Factory(Model.Factory):
        def children(self):
            # yield Crustacean.probable(0.2)
            yield None


class GalacticLife(Model):
    life = Model.child_property(Model)

    class Factory(Model.Factory):
        def children(self):
            # yield GalacticLife
            yield None


class StarLife(Model):
    life = Model.child_property(Model)

    class Factory(Model.Factory):
        def children(self):
            yield Ghost.probable(0.1)
            # yield SpaceMonster.probable(0.2)


class PlanetCoreLife(Model):
    life = Model.child_property(Model)

    class Factory(Model.Factory):
        def children(self):
            # yield SpaceMonster.probable(0.5)
            yield None


class GasGiantLife(Model):
    life = Model.child_property(Model)

    class Factory(Model.Factory):
        def children(self):
            # yield GalacticLife.probable(10)
            yield None


class BarrenPlanetLife(Model):
    life = Model.child_property(Model)

    class Factory(Model.Factory):
        def children(self):
            # yield GalacticLife.probable(10)
            yield None


class VisitorPlanetLife(Model):
    life = Model.child_property(Model)

    class Factory(Model.Factory):
        def children(self):
            # yield GalacticLife.probable(100)
            yield None


class MoonLife(Model):
    life = Model.child_property(Model)

    class Factory(Model.Factory):
        def children(self):
            yield Ghost.probable(0.1)


class AsteroidLife(Model):
    life = Model.child_property(Model)

    class Factory(Model.Factory):
        def children(self):
            # yield SpaceAnimal.probable(0.5)
            yield None


class AsteroidBeltLife(Model):
    life = Model.child_property(Model)

    class Factory(Model.Factory):
        def children(self):
            # yield GalacticLife.probable(20)
            yield None
