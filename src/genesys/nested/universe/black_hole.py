from genesys.nested.factories.nested_factory import NestedFactory
from models.universe import black_hole
from utils.nested import select_item
from .unsorted_life import CrustaceanFactory, PastaFactory


class EndOfUniverseNoteFactory(NestedFactory):
    model = black_hole.EndOfUniverseNote

    def name_factory(self, data, *args, **kwargs):
        return select_item(*data.end_of_universe_note)

    def children(self):
        yield PastaFactory.probable(0.1)


class EverythingFactory(NestedFactory):
    model = black_hole.Everything

    def children(self):
        from . import UniverseFactory

        yield UniverseFactory.one()


class Answer42Factory(EverythingFactory):
    model = black_hole.Answer42


class WhiteHoleFactory(EverythingFactory):
    model = black_hole.WhiteHole


class InsideTheBlackHoleFactory(NestedFactory):
    model = black_hole.InsideTheBlackHole

    def children(self):
        yield EndOfUniverseNoteFactory.probable(0.5)
        yield CrustaceanFactory.probable(0.2)
        yield WhiteHoleFactory


class BlackHoleFactory(NestedFactory):
    model = black_hole.BlackHole

    def children(self):
        yield InsideTheBlackHoleFactory.one()
