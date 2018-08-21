class Terrain():
    name = ""
    speed = 1.0
    allowCharge = True
    allowFormed = True
    allowHeavy = True
    requireHalt = False
    entireMove = True


class Plain(Terrain):
    name = "Plain"


class Hill(Plain):
    name = "Hill"
    speed = 0.5
    downhill = 1.0
    allowCharge = False


class Wood(Hill):
    name = "Wood"
    allowFormed = False


class Marsh(Hill):
    name = "Marsh"
    allowHeavy = False


class Rough(Plain):
    name = "Rough"
    allowCharge = False


class Rampart(Hill):
    name = "Rampart"


class Stream(Plain):
    name = "Stream"
    toCross = 6
    allowCharge = False


class River(Plain):
    name = "River"
    requireHalt = True
    entireMove = True


class Pond(River):
    name = "Pond"


class Gulley(Stream):
    name = "Gulley"


terrainDeck = [
    River(),
    River(),
    Marsh(),
    Pond(),
    Gulley(),
    Wood(),
    Wood(),
    Rough(),
    Hill(),
    Hill(),
    Hill(),
    Hill(),
    Plain(),
    Plain(),
    Plain(),
    Plain(),
    Plain(),
    Plain(),
    Plain(),
    Plain(),
]


def generateTerrain():
    import random
    random.shuffle(terrainDeck)
    terrain = [[Plain() for j in range(8)] for i in range(8)]
    for k in range(8):
        terrain[random.randrange(8)][random.randrange(8)] = terrainDeck[k]
    return terrain
