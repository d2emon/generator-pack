from models.v5 import life
from factories.nested_factory import NestedFactory as Factory
from ....mind import PsycheFactory
# from ....cloth import ClothingSetFactory
from ...animals.animal import AnimalFactory
from ...animal_body.blood import BloodFactory
from ..body import BodyFactory


class PersonFactory(AnimalFactory):
    default_model = life.Person
    default_name = '*PERSON*'

    def generate_name(self):
        return self.default_name

    @property
    def body_factory(self):
        return BodyFactory()

    @property
    def psyche_factory(self):
        return PsycheFactory()

    @property
    def clothing_set_factory(self):
        # return ClothingSetFactory()
        return None

    def children(self):
        yield from super().children()
        yield self.clothing_set_factory()


class ManFactory(PersonFactory):
    default_name = '*MAN*'


class WomanFactory(PersonFactory):
    default_name = '*WOMAN*'


class CorpseFactory(PersonFactory):
    default_model = life.Corpse

    @property
    def psyche_factory(self):
        return None

    def children(self):
        yield from super().children()
        yield BloodFactory().probable(35)
        # yield Worm.probable(20)
        # yield Worm.probable(10)
