from models.universe.black_hole import EndOfUniverseNote, Everything, Answer42, BlackHole, WhiteHole, InsideTheBlackHole
from factories.thing.nested_factory import NestedFactory
# from ..life import BlackHoleLifeFactory
# from ..temporary import PastaFactory


class EndOfUniverseNoteFactory(NestedFactory):
    default_model = EndOfUniverseNote
    notes = [
        "Help! I'm trapped in a universe factory!", "Okay, you can stop clicking now.",
        "I want to get off Mr Orteil's Wild Ride", "my sides"
    ]

    def generate_name(self):
        return self.select_item(*self.notes)

    def children(self):
        # yield PastaFactory.probable(0.1)
        yield None


class EverythingFactory(NestedFactory):
    default_model = Everything

    def children(self):
        # from . import UniverseFactory

        # yield UniverseFactory
        yield None


class Answer42Factory(EverythingFactory):
    default_model = Answer42


class WhiteHoleFactory(EverythingFactory):
    default_model = WhiteHole


class InsideTheBlackHoleFactory(NestedFactory):
    default_model = InsideTheBlackHole

    def children(self):
        # yield EndOfUniverseNoteFactory.probable(0.5)
        # yield BlackHoleLifeFactory
        # yield WhiteHoleFactory
        yield None


class BlackHoleFactory(NestedFactory):
    default_model = BlackHole

    def children(self):
        yield InsideTheBlackHoleFactory.as_child()


"""
"""
