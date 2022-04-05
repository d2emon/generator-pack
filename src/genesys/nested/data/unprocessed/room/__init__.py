from genesys.nested.child_generator import ChildGenerator
from genesys.nested.factories import Thing


# rooms
class Building(Thing):
    child_generators = [
        ChildGenerator("walls"),
        ChildGenerator("roof"),
    ]


class Roof(Thing):
    child_generators = [
        ChildGenerator("cat", probability=2),
        ChildGenerator("bird", probability=10),
        ChildGenerator("bird", probability=10),
        ChildGenerator("nest", probability=2),
        ChildGenerator("roof tiles"),
    ]


class RoofTiles(Thing):
    child_generators = [ChildGenerator("ceramic"), ]
    names_data = "tiles"


class Room(Thing):
    child_generators = [
        ChildGenerator("visitor", probability=0.1),
        ChildGenerator("ghost", probability=0.1),
        ChildGenerator("walls"),
    ]


class Walls(Thing):
    child_generators = [
        ChildGenerator("door", (1, 4)),
        ChildGenerator("window", (0, 6)),
        [
            ChildGenerator("wall", (4, )),
            ChildGenerator("wall", (4, 8)),
        ]
    ]


class Wall(Thing):
    child_generators = [
        [
            ChildGenerator("plaster"),
            ChildGenerator("wood")
        ],
        ChildGenerator("dirt", probability=5),
    ]


class Plaster(Thing):
    child_generators = [
        ChildGenerator("calcium"),
        ChildGenerator("sulfur"),
    ]


class Door(Thing):
    child_generators = [
        ChildGenerator("wood frame"),
        ChildGenerator("glass", probability=10),
    ]


class Window(Thing):
    child_generators = [
        ChildGenerator("wood frame"),
        ChildGenerator("glass"),
    ]


# new Thing("marble",["calcium"]);
# new Thing("stone",["rock"]);
# new Thing("concrete",["rock","cement","water"]);
# new Thing("cement",["calcium"]);
# new Thing("marble",["calcium"]);


class Attic(Room):
    pass


class LivingRoom(Room):
    type_name = 'living-room'
    child_generators = [
        ChildGenerator(".room"),
        ChildGenerator("person", (0, 4)),
        ChildGenerator("cat", probability=10),
        ChildGenerator("cat", probability=10),
        ChildGenerator("stuff box", probability=5),
        ChildGenerator("tv", probability=95),
        ChildGenerator("armchair", probability=50),
        ChildGenerator("armchair", probability=50),
        ChildGenerator("couch", probability=90),
        ChildGenerator("living-room table", probability=50),
        ChildGenerator("chair", (1, 6)),
        ChildGenerator("painting", probability=70),
        ChildGenerator("painting", probability=20),
        ChildGenerator("mirror", probability=2),
        ChildGenerator("bookshelf", (0, 3)),
        ChildGenerator("small bookshelf", (0, 2)),
        ChildGenerator("desk", probability=40),
        ChildGenerator("computer", probability=40),
    ]


class Kitchen(Room):
    child_generators = [
        ChildGenerator(".room"),
        ChildGenerator("person", probability=40),
        ChildGenerator("person", probability=20),
        ChildGenerator("tv", probability=40),
        ChildGenerator("kitchen sink"),
        ChildGenerator("cabinet", (1, 5)),
        ChildGenerator("fridge"),
        ChildGenerator("oven"),
        ChildGenerator("chair", (0, 3)),
        ChildGenerator("computer", probability=5),
        ChildGenerator("small bookshelf", probability=5),
        ChildGenerator("painting", probability=30),
        ChildGenerator("painting", probability=10),
    ]


class Bedroom(Room):
    child_generators = [
        ChildGenerator(".room"),
        ChildGenerator("person", probability=40),
        ChildGenerator("person", probability=10),
        ChildGenerator("cat", probability=5),
        ChildGenerator("stuff box", probability=5),
        ChildGenerator("tv", probability=60),
        ChildGenerator("bed"),
        ChildGenerator("chair", (0, 4)),
        [
            ChildGenerator("cupboard", probability=90),
            ChildGenerator("closet", probability=90),
        ],
        ChildGenerator("mirror", probability=50),
        ChildGenerator("bookshelf", (0, 2)),
        ChildGenerator("small bookshelf", (0, 3)),
        ChildGenerator("desk", probability=40),
        ChildGenerator("computer", probability=40),
        ChildGenerator("painting", probability=60),
        ChildGenerator("painting", probability=20),
    ]


class Bathroom(Room):
    child_generators = [
        ChildGenerator(".room"),
        ChildGenerator("person", probability=10),
        ChildGenerator("person", probability=1),
        ChildGenerator("cat", probability=1),
        ChildGenerator("sink", probability=95),
        [
            ChildGenerator("bathtub"),
            ChildGenerator("shower")
        ],
        ChildGenerator("toilet"),
        ChildGenerator("painting", probability=20),
        ChildGenerator("mirror", probability=80),
    ]


class Study(Room):
    child_generators = [
        ChildGenerator(".room"),
        ChildGenerator("person", probability=30),
        ChildGenerator("person", probability=5),
        ChildGenerator("stuff box", probability=20),
        ChildGenerator("tv", probability=20),
        ChildGenerator("desk", probability=95),
        ChildGenerator("computer", probability=90),
        ChildGenerator("chair", (1, 4)),
        ChildGenerator("bookshelf", (0, 6)),
        ChildGenerator("painting", probability=70),
        ChildGenerator("painting", probability=20),
        ChildGenerator("mirror", probability=5),
    ]


class Garden(Room):
    child_generators = [
        ChildGenerator("person", probability=40),
        ChildGenerator("person", probability=10),
        ChildGenerator("dog", probability=20),
        ChildGenerator("dog", probability=5),
        ChildGenerator("cat", probability=15),
        ChildGenerator("grass"),
        ChildGenerator("tree", probability=50),
        ChildGenerator("tree", probability=50),
        ChildGenerator("tree", probability=20),
        ChildGenerator("tree", probability=5),
        ChildGenerator("flowers", probability=30),
        ChildGenerator("hole", probability=1),
        ChildGenerator("hole", probability=1),
        ChildGenerator("hole", probability=1),
        ChildGenerator("poultry", probability=1),
        ChildGenerator("bird", probability=20),
        ChildGenerator("bird", probability=10),
    ]
    names_data = ["garden", "lawn", "backyard"]


class Garage(Room):
    child_generators = [
        ChildGenerator("person", probability=20),
        ChildGenerator("cat", probability=2),
        ChildGenerator("stuff box", probability=30),
        ChildGenerator("stuff box", probability=20),
        ChildGenerator("chair", (0, 3)),
        ChildGenerator("car", probability=90),
        ChildGenerator("car", probability=40),
        ChildGenerator("car", probability=5),
        ChildGenerator("bike", probability=40),
        ChildGenerator("bike", probability=30),
        ChildGenerator("bike", probability=10),
        ChildGenerator("computer", probability=5),
        ChildGenerator("small bookshelf", probability=30),
        ChildGenerator("hole", probability=1),
        ChildGenerator("hole", probability=0.5),
        ChildGenerator("small mammal", probability=5),
        ChildGenerator("insect", probability=15),
        ChildGenerator("insect", probability=15),
        ChildGenerator("dirt", probability=50),
    ]


class Hole(Room):
    child_generators = [
        ChildGenerator("corpse", probability=20),
        ChildGenerator("corpse", probability=5),
        ChildGenerator("blood", probability=20),
        ChildGenerator("shovel", probability=20),
        ChildGenerator("hole", probability=0.5),
        ChildGenerator("insect", probability=25),
        ChildGenerator("insect", probability=15),
        ChildGenerator("dirt"),
    ]


# ChildGenerator("cat", probability=2),
# ChildGenerator("bird", probability=10),
# ChildGenerator("nest", probability=2),
# ChildGenerator("ceramic"),
# ChildGenerator("visitor", probability=0.1),
# ChildGenerator("ghost", probability=0.1),
# ChildGenerator("wood")
# ChildGenerator("dirt", probability=5),
# ChildGenerator("calcium"),
# ChildGenerator("sulfur"),
# ChildGenerator("wood frame"),
# ChildGenerator("glass", probability=10),

# ChildGenerator("person", (0, 4)),
# ChildGenerator("stuff box", probability=5),
# ChildGenerator("painting", probability=70),
# ChildGenerator("computer", probability=40),
# ChildGenerator("kitchen sink"),
# ChildGenerator("cabinet", (1, 5)),
# ChildGenerator("fridge"),
# ChildGenerator("oven"),
# ChildGenerator("dog", probability=20),
# ChildGenerator("grass"),
# ChildGenerator("tree", probability=5),
# ChildGenerator("flowers", probability=30),
# ChildGenerator("poultry", probability=1),
# ChildGenerator("car", probability=5),
# ChildGenerator("bike", probability=10),
# ChildGenerator("small mammal", probability=5),
# ChildGenerator("insect", probability=15),
# ChildGenerator("dirt", probability=50),
# ChildGenerator("corpse", probability=20),
# ChildGenerator("blood", probability=20),
# ChildGenerator("shovel", probability=20),


CONTENTS = [
    Building,
    Roof,
    RoofTiles,
    Room,
    Walls,
    Wall,
    Plaster,

    Door,
    Window,
    LivingRoom,
    Kitchen,
    Bedroom,
    Bathroom,
    Study,
    Garden,
    Garage,
    Hole,

    Attic
]
