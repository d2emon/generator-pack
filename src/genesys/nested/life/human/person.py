from genesys.nested.factories.nested_factory import NestedFactory
from models.v5 import life
from ..body.blood import BloodFactory
from .body import BodyFactory

from ...unsorted_cloth import ClothingSetFactory
from ...unsorted_mind import PsycheFactory
from ...unsorted_life import WormFactory


class PersonFactory(NestedFactory):
    # TODO: Make child of AnimalFactory
    default_name = '*PERSON*'
    # model = life.Person

    def name_factory(self, data, *args, **kwargs):
        return self.default_name

    def body(self):
        yield BodyFactory.one()

    def psyche(self):
        yield PsycheFactory.one()

    def clothing_set(self):
        yield ClothingSetFactory.one()

    def children(self):
        yield from self.body()
        yield from self.psyche()
        yield from self.clothing_set()


class ManFactory(PersonFactory):
    default_name = '*MAN*'


class WomanFactory(PersonFactory):
    default_name = '*WOMAN*'


class CorpseFactory(PersonFactory):
    # model = life.Corpse

    def psyche(self):
        return None

    def children(self):
        yield from super().children()

        yield BloodFactory.probable(35)
        yield WormFactory.probable(20)
        yield WormFactory.probable(10)
