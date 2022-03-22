"""
- Person
    - Man (Unused)
    - Woman
- Corpse
"""
from genesys.model.model import Model
# TODO: Fix circular and remove
# from ....cloth import ClothingSet
from ...animals import Animal
from ...animal_body.blood import Blood


# TODO: Remove it
class ClothingSet:
    pass


class Person(Animal):
    default_name = '*PERSON*'

    clothing = Model.child_property(ClothingSet)

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


class Corpse(Person):
    default_name = '*PERSON*| (dead)'

    blood = Model.child_property(Blood)
    # worms = Model.children_property(Worm)


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
