from generated import life
from ....factory import Factory
from ..cloth import ClothingSetFactory
from ..blood import BloodFactory
from ..body import BodyFactory


class PersonFactory(Factory):
    default_model = life.Person

    def children(self):
        yield BodyFactory()
        # yield Psyche
        yield ClothingSetFactory()


class ManFactory(PersonFactory):
    default_name = '*MAN*'


class WomanFactory(PersonFactory):
    default_name = '*WOMAN*'


class CorpseFactory(PersonFactory):
    default_model = life.Corpse

    def children(self):
        yield BodyFactory()
        yield ClothingSetFactory()
        yield BloodFactory().probable(35)
        # yield Worm.probable(20)
        # yield Worm.probable(10)
