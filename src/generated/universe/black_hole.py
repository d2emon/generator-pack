from genesys.model.model import Model
from generated.nested_v2.models import Pasta
from generated.universe.space.life import BlackHoleLife, Habitat
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


class BlackHole(Portal, Habitat):
    note = Portal.child_property(EndOfUniverseNote)
    white_hole = Portal.child_property(WhiteHole)

    class Factory(Model.Factory):
        def children(self):
            yield EndOfUniverseNote.probable(0.5)
            yield BlackHoleLife
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
