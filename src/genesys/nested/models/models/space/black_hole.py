from genesys.nested.models.models.unknown import Pasta
from genesys.nested.models import Model
from genesys.nested.models.mixins import EncounteredMixin
# from ..biology import Crustacean
from genesys.nested.data import lookups


class GlobalItem(Model):
    @property
    def universe(self):
        from . import Universe

        return next(self.children_by_class(Universe), None)

    class Factory(Model.Factory):
        def children(self):
            from . import Universe

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
    contents = Model.children_property(Pasta)

    class Factory(Model.Factory):
        class DataProvider:
            end_of_universe_note = lookups.end_of_universe_notes

        name = property(lambda self: self.provider.end_of_universe_note)

        def children(self):
            yield Pasta.probable(0.1)

    def read(self):
        return self.name


class WhiteHole(Portal):
    pass


class BlackHole(Portal, EncounteredMixin):
    white_hole = Portal.child_property(WhiteHole)
    note = Portal.child_property(EndOfUniverseNote)

    class Factory(Model.Factory):
        def children(self):
            yield EndOfUniverseNote.probable(0.5)
            # yield Crustacean.probable(0.2)
            yield WhiteHole

    @property
    def universe(self):
        return self.white_hole and self.white_hole.universe

    def inside(self):
        return self.children

    def enter(self):
        if self.note is not None:
            print(self.note)
        return self.white_hole
