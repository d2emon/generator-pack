"""
- EndOfUniverseNote
- Everything (Unused)
- Answer42 (Unused)
- WhiteHole
- InsideTheBlackHole
- BlackHole
"""
from models.nested_model import NestedModel
from models.v5.materials import Portal
from models.v5.life import Life


class EndOfUniverseNote(NestedModel):
    # contents = Model.children_property(Pasta)

    def read(self):
        return self.name


class Everything(NestedModel):
    @property
    def universe(self):
        from . import Universe

        return next(self.children_by_class(Universe), None)

    def get_everything(self):
        return self.universe


class Answer42(Everything):
    def answer(self):
        return self.get_everything()


class WhiteHole(Portal):
    pass


class InsideTheBlackHole(NestedModel):
    life = NestedModel.child_property(Life)
    note = NestedModel.child_property(EndOfUniverseNote)
    white_hole = NestedModel.child_property(WhiteHole)


class BlackHole(Portal):
    inside = Portal.child_property(InsideTheBlackHole)

    @property
    def note(self):
        return self.inside and self.inside.note

    @property
    def white_hole(self):
        return self.inside and self.inside.white_hole

    @property
    def universe(self):
        return self.white_hole and self.white_hole.universe

    def enter(self):
        if self.note is not None:
            print(self.note)
        return self.white_hole
