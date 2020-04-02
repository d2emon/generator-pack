from ....unknown import Psyche, Worm
from .people.clothing import Hat, Glasses, Pants, Shirt, Coat, Socks, Shoes, Underwear
from genesys.nested.models import Model
from ..blood import Blood
from ..body import Body


class ClothingSet(Model):
    hat = Model.child_property(Hat)
    glasses = Model.child_property(Glasses)
    pants = Model.child_property(Pants)
    shirt = Model.child_property(Shirt)
    coat = Model.child_property(Coat)
    socks = Model.child_property(Socks)
    shoes = Model.child_property(Shoes)
    underwear = Model.child_property(Underwear)

    class NameFactory(Model.NameFactory):
        default = 'clothing'

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield Hat.probable(2)
            yield Glasses.probable(20)
            yield Pants.probable(98)
            yield Shirt.probable(98)
            yield Coat.probable(50)
            yield Socks.probable(80)
            yield Shoes.probable(80)
            yield Underwear.probable(99)


class Person(Model):
    body = Model.child_property(Body)
    psyche = Model.child_property(Psyche)
    clothing = Model.child_property(ClothingSet)

    class NameFactory(Model.NameFactory):
        default = '*PERSON*'

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield Body
            yield Psyche
            yield ClothingSet

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
    class NameFactory(Model.NameFactory):
        default = '*MAN*'


class Woman(Person):
    class NameFactory(Model.NameFactory):
        default = '*WOMAN*'


class Corpse(Person):
    blood = Model.child_property(Blood)
    worms = Model.children_property(Worm)

    class NameFactory(Model.NameFactory):
        default = '*PERSON*| (dead)'

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield Body
            yield ClothingSet
            yield Blood.probable(35)
            yield Worm.probable(20)
            yield Worm.probable(10)


# future stuff


# class FutureClothingSet(ClothingSet):
#     child_generators = [
#         ChildGenerator("future gizmo", probability=10),
#         ChildGenerator("future gizmo", probability=10),
#         ChildGenerator("future gizmo", probability=10),
#         ChildGenerator("future hat", probability=10),
#         ChildGenerator("future outfit", probability=99.8),
#     ]
#     names_data = ["clothing"]


# class FutureMan(Man):
#     child_generators = [
#         ChildGenerator(".future person")
#     ]
#     names_data = ["*FUTURE MAN*"]


# class FutureWoman(Man):
#     child_generators = [
#         ChildGenerator(".future person")
#     ]
#     names_data = ["*FUTURE WOMAN*"]


# class FuturePerson(Person):
#     child_generators = [
#         ChildGenerator("body"),
#         ChildGenerator("future psyche"),
#         ChildGenerator("future clothing set")
#     ]
#     names_data = "*FUTURE PERSON*"


# new Thing("future psyche",["future thoughts","future memories"],"psyche");
# new Thing("future thoughts",["black hole,0.01%",["future thought,2-3"]],"thoughts");
# new Thing("future thought",[],["*FUTURE THOUGHT*"]);
# new Thing("future memories",["future memory,2-4"],"memories");
# new Thing("future memory",[],["*FUTURE MEMORY*"]);


# class Tourist(Person):
#     child_generators = [ChildGenerator(".person"),]
#     names_data = "*PERSON*| (tourist)"
