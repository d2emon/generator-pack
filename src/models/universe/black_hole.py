"""
- EndOfUniverseNote
- Everything (Unused)
- Answer42 (Unused)
- WhiteHole
- InsideTheBlackHole
- BlackHole
"""
from models.nested_model import TreeModel
# from models.v5.life import Life


class Portal(TreeModel):
    universe = property(lambda self: self.children[0] if len(self.children) else None)

    def enter(self):
        return self.universe



class EndOfUniverseNote(TreeModel):
    # contents = Model.children_property(Pasta)

    def read(self):
        return self.name


class Everything(TreeModel):
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


class InsideTheBlackHole(TreeModel):
    # life = TreeModel.child_property(Life)
    note = TreeModel.child_property(EndOfUniverseNote)
    white_hole = TreeModel.child_property(WhiteHole)


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
