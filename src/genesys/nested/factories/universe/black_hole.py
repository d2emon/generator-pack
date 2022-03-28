from generated import universe
from factories.nested_factory import NestedFactory as Factory
from ..life import BlackHoleLifeFactory
from ..temporary import PastaFactory


class EndOfUniverseNoteFactory(Factory):
    default_model = universe.EndOfUniverseNote
    notes = [
        "Help! I'm trapped in a universe factory!", "Okay, you can stop clicking now.",
        "I want to get off Mr Orteil's Wild Ride", "my sides"
    ]

    def generate_name(self):
        return self.select_item(*self.notes)

    def children(self):
        yield PastaFactory().probable(0.1)


class EverythingFactory(Factory):
    default_model = universe.Everything

    def children(self):
        from .universe import UniverseFactory

        yield UniverseFactory()


class Answer42Factory(EverythingFactory):
    default_model = universe.Answer42


class WhiteHoleFactory(EverythingFactory):
    default_model = universe.WhiteHole


class InsideTheBlackHoleFactory(Factory):
    default_model = universe.InsideTheBlackHole

    def children(self):
        yield EndOfUniverseNoteFactory().probable(0.5)
        yield BlackHoleLifeFactory()
        yield WhiteHoleFactory()


class BlackHoleFactory(Factory):
    default_model = universe.BlackHole

    def children(self):
        yield InsideTheBlackHoleFactory()
