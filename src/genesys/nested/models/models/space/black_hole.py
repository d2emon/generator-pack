from genesys.nested.models.models.unknown import Pasta, Crustacean
from genesys.nested.models import Model
from genesys.nested.models.mixins import EncounteredMixin
from genesys.nested.data import lookups


class GlobalItem(Model):
    universe = Model.child_property(Model)

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            from genesys.nested.models.models.space import Universe

            yield Universe


class Answer42(GlobalItem):
    def answer(self):
        return self.universe


class Everything(GlobalItem):
    def get_everything(self):
        return self.universe


class Portal(GlobalItem):
    def enter(self):
        return self.universe


class EndOfUniverseNote(Model):
    contents = Model.children_property(Model)

    class BaseFactory(Model.BaseFactory):
        default = lookups.end_of_universe_notes

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield Pasta.probable(0.1)

    def read(self):
        return self.BaseFactory.next()


class WhiteHole(Portal):
    pass


class BlackHole(Portal, EncounteredMixin):
    white_hole = Portal.child_property(WhiteHole)

    class ChildrenFactory(Portal.ChildrenFactory):
        def children_classes(self):
            yield EndOfUniverseNote.probable(0.5)
            yield Crustacean.probable(0.2)
            yield WhiteHole

    @property
    def universe(self):
        return self.white_hole and self.white_hole.universe

    def inside(self):
        return self.children

    def enter(self):
        return self.white_hole