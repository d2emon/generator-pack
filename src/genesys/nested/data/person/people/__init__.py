from nestedg.data import unknown
from nestedg.model import Model
from .body import Body, Blood
from .clothing import ClothingSet


class Person(Model):
    @classmethod
    def children_classes(cls):
        yield Body
        yield unknown.Psyche
        yield ClothingSet

    @classmethod
    def _generate_name(cls):
        return '*PERSON*'

    @property
    def clothing(self):
        return next(self.filter_children(ClothingSet))

    @property
    def hat(self):
        return self.clothing.hat

    @property
    def glasses(self):
        return self.clothing.glasses

    @property
    def pants(self):
        return self.clothing.pants

    @property
    def shirt(self):
        return self.clothing.shirt

    @property
    def coat(self):
        return self.clothing.coat

    @property
    def socks(self):
        return self.clothing.socks

    @property
    def shoes(self):
        return self.clothing.shoes

    @property
    def underwear(self):
        return self.clothing.underwear


class Man(Person):
    @classmethod
    def _generate_name(cls):
        return '*MAN*'


class Woman(Person):
    @classmethod
    def _generate_name(cls):
        return '*WOMAN*'


class Corpse(Person):
    @classmethod
    def children_classes(cls):
        yield Body
        yield ClothingSet
        yield Blood.probable(35)
        yield unknown.Worm.probable(20)
        yield unknown.Worm.probable(10)

    @classmethod
    def _generate_name(cls):
        return '*PERSON*| (dead)'
