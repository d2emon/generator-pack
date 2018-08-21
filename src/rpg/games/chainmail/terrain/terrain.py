class Terrain():
    name = ""
    weight = 1
    speed = 1.0
    forbiddenArmyTypes = []
    requireHalt = False
    entireMove = True

    @classmethod
    def allowArmyType(cls, army_type):
        return army_type not in cls.forbiddenArmyTypes


class Plain(Terrain):
    name = "Plain"
    weight = 6


class Hill(Plain):
    name = "Hill"
    weight = 4
    speed = 0.5
    downhill = 1.0
    forbiddenArmyTypes = ["Charge"]


class Wood(Hill):
    name = "Wood"
    weight = 2
    forbiddenArmyTypes = ["Charge", "Formed"]


class Marsh(Hill):
    name = "Marsh"
    weight = 1
    forbiddenArmyTypes = ["Charge", "Heavy"]


class Rough(Plain):
    name = "Rough"
    weight = 1
    forbiddenArmyTypes = ["Charge"]


class Rampart(Hill):
    name = "Rampart"
    weight = 1


class Stream(Plain):
    name = "Stream"
    weight = 1
    toCross = 6
    forbiddenArmyTypes = ["Charge"]


class River(Plain):
    name = "River"
    weight = 2
    requireHalt = True
    entireMove = True


class Pond(River):
    name = "Pond"
    weight = 1


class Gulley(Stream):
    name = "Gulley"
    weight = 1
