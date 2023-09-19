from genesys.nested.factories.child_factory import ChildFactory as ChildGenerator
from genesys.nested.factories.nested_factory import NestedFactory as Thing

# furniture
class Cabinet(Thing):
    child_generators = [
        ChildGenerator("wood frame"),
        ChildGenerator("glass", probability=30),
        ChildGenerator(".cabinet content"),
    ]


class CabinetContent(Thing):
    child_generators = [
        ChildGenerator("donut box", probability=4),
        [ChildGenerator("cheese", (0, 3)), None],
        ChildGenerator("water bottle", (0, 1)),
        ChildGenerator("juice bottle", (0, 1)),
        ChildGenerator("soda bottle", (0, 1)),
        [
            ChildGenerator("can", (0, 6)),
            ChildGenerator("cookie box", (0, 6)),
        ],
        ChildGenerator("insect", probability=2),
    ]


class Fridge(Thing):
    child_generators = [
        ChildGenerator(".fridge content"),
        ChildGenerator("plastic"),
        ChildGenerator("metal grill", (1, 4)),
        ChildGenerator("electronics"),
    ]


class FridgeContent(Thing):
    child_generators = [
        ChildGenerator("roast", probability=15),
        ChildGenerator("pasta", probability=40),
        ChildGenerator("pasta", probability=10),
        ChildGenerator("can", probability=15),
        ChildGenerator("donut box", probability=5),
        ChildGenerator("cake", probability=3),
        ChildGenerator("pie", probability=3),
        [ChildGenerator("yoghurt", (0, 6)), None],
        [ChildGenerator("ice cream", (0, 6)), None],
        [ChildGenerator("cheese", (0, 3)), None],
        ChildGenerator("water bottle", (0, 1)),
        ChildGenerator("juice bottle", (0, 2)),
        ChildGenerator("soda bottle", (0, 2)),
        ChildGenerator("milk bottle", (0, 1)),
        ChildGenerator("wine bottle", probability=10),
    ]


class Oven(Thing):
    child_generators = [
        [
            ChildGenerator("pie"),
            ChildGenerator("cake"),
            ChildGenerator("roast"),
            None,
            None
        ],
        ChildGenerator("plastic"),
        ChildGenerator("metal grill", (1, 3)),
        ChildGenerator("electronics"),
    ]


class Sink(Thing):
    child_generators = [
        [
            ChildGenerator("porcelain"),
            ChildGenerator("metal"),
        ],
        ChildGenerator("organic matter", probability=5),
        ChildGenerator("pipes"),
    ]


class KitchenSink(Sink):
    child_generators = [ChildGenerator(".sink")]


class Toilet(Thing):
    child_generators = [
        ChildGenerator("water"),
        ChildGenerator("organic matter", probability=15),
        ChildGenerator("pasta", probability=0.1),
        ChildGenerator("porcelain"),
        ChildGenerator("pipes"),
    ]


class Pipes(Thing):
    child_generators = [
        ChildGenerator("metal"),
        ChildGenerator("dirt")
    ]


class Nails(Thing):
    child_generators = [ChildGenerator("iron")]


class Metal(Thing):
    child_generators = [ChildGenerator("iron")]


class MetalGrill(Thing):
    child_generators = [ChildGenerator("metal")]


class Porcelain(Thing):
    child_generators = [ChildGenerator("silica")]


class Ceramic(Thing):
    child_generators = [ChildGenerator("silica")]


class Chair(Thing):
    child_generators = [
        [
            ChildGenerator("wood"),
            ChildGenerator("plastic"),
        ],
        ChildGenerator("nails", probability=50),
    ]


class Armchair(Chair):
    child_generators = [
        ".chair",
        "cloth"
    ]


class Couch(Armchair):
    child_generators = [
        ChildGenerator(".armchair"),
        ChildGenerator("tv remote", probability=5),
        ChildGenerator("coin", probability=5),
        ChildGenerator("pen", probability=5),
    ]
    names_data = ["couch", "sofa"]


class TvRemote(Thing):
    child_generators = [
        ChildGenerator("plastic"),
        ChildGenerator("electronics"),
    ]
    names_data = ["TV remote"]


class Coin(Thing):
    child_generators = [
        ChildGenerator("organic matter", probability=2),
        ChildGenerator("dirt", probability=2),
        ChildGenerator("copper"),
    ]


# new Thing("gold coin", element_factories['Au'].one());


class Dirt(Thing):
    child_generators = [
        ChildGenerator("organic matter", probability=50),
        ChildGenerator("dust"),
    ]


# new Thing("grease",[LipidsFactory.one(), "dust"]);


class Dust(Thing):
    child_generators = [ChildGenerator("molecule")]


# new Thing("crumbs",["organic matter"]);
# new Thing("lint",["textile fibre"]);


class Pen(Thing):
    child_generators = [
        ChildGenerator("plastic"),
        ChildGenerator("ink", probability=80),
    ]


class Button(Thing):
    child_generators = [ChildGenerator("plastic")]


# new Thing("note",["note writing","paper"]);
# new Thing("note writing",[],["*NOTE*"]);


class Bed(Thing):
    child_generators = [
        ChildGenerator(".armchair"),
        ChildGenerator("pillow", (0, 3)),
    ]


class Pillow(Thing):
    child_generators = [
        ChildGenerator("feather"),
        ChildGenerator("cloth"),
    ]


class Feather(Thing):
    child_generators = [ChildGenerator("keratin")]


# new Thing("feathers",[".feather"]);


class Mirror(Thing):
    child_generators = [
        ChildGenerator("glass"),
        ChildGenerator("portal", probability=0.1),
    ]


class Glass(Thing):
    child_generators = [ChildGenerator("silica")]


class Desk(Thing):
    child_generators = [
        ChildGenerator("wood frame"),
        ChildGenerator("drawer", (0, 6)),
    ]


class Cupboard(Thing):
    child_generators = [
        ChildGenerator("cup", (0, 6)),
        ChildGenerator("drinking glass", (0, 6)),
        ChildGenerator("bowl", (0, 4)),
        ChildGenerator("plate", (0, 8)),
        ChildGenerator("wood frame"),
        ChildGenerator("wood shelf", (1, 4)),
        ChildGenerator("drawer", (0, 2)),
    ]


class DrinkingGlass(Thing):
    child_generators = [ChildGenerator("glass")]
    names_data = "glass"


class Bowl(Thing):
    child_generators = [ChildGenerator("ceramic")]


class Cup(Thing):
    child_generators = [ChildGenerator("ceramic")]


class Plate(Thing):
    child_generators = [ChildGenerator("ceramic")]


class Closet(Thing):
    child_generators = [
        ChildGenerator("portal", probability=0.1),
        ChildGenerator("skeleton", probability=0.1),
        ChildGenerator("hat", probability=30),
        ChildGenerator("hat", probability=15),
        ChildGenerator("pants", (0, 5)),
        ChildGenerator("shirt", (0, 5)),
        ChildGenerator("underwear", (0, 6)),
        ChildGenerator("coat", (0, 3)),
        ChildGenerator("socks", (0, 8)),
        ChildGenerator("shoes", (0, 6)),
        ChildGenerator("button", probability=20),
        ChildGenerator("wood frame"),
        ChildGenerator("wood shelf", (0, 2)),
    ]


class Table(Thing):
    child_generators = [
        [
            ChildGenerator("wood"),
            ChildGenerator("plastic"),
        ],
        ChildGenerator("nails", probability=50)
    ]


class LivingRoomTable(Table):
    type_name = 'living-room table'
    child_generators = [
        ChildGenerator(".table"),
        ChildGenerator("drawer", (0, 2)),
    ]
    names_data = ["table"]


class Drawer(Thing):
    child_generators = [
        ChildGenerator("note", (0, 8)),
        ChildGenerator("office toy", probability=30),
        ChildGenerator("office toy", probability=30),
        ChildGenerator("pen", probability=30),
        ChildGenerator("pen", probability=10),
        ChildGenerator("pen", probability=5),
        ChildGenerator("donut box", probability=4),
        ChildGenerator("can", probability=2),
        ChildGenerator("book", probability=20),
        ChildGenerator("book", probability=20),
        ChildGenerator("book", probability=5),
        ChildGenerator("book", probability=5),
        ChildGenerator("button", probability=10),
        ChildGenerator("button", probability=10),
        ChildGenerator("dust", probability=40),
        ChildGenerator("lint", probability=40),
    ]


# new Thing("note stack",["note,5-25"]);//lotsonotes


class Bookshelf(Thing):
    child_generators = [
        ChildGenerator("book", (5, 30)),
        [
            ChildGenerator("plastic shelf", (3, 8)),
            ChildGenerator("wood shelf", (3, 8)),
            ChildGenerator("drawer", (0, 2)),
        ],
    ]


class SmallBookshelf(Bookshelf):
    child_generators = [
        ChildGenerator("book", (1, 8)),
        [
            ChildGenerator("plastic shelf", (1, 6)),
            ChildGenerator("wood shelf", (1, 6)),
        ],
    ]
    names_data = ["bookshelf"]


class WoodShelf(Thing):
    child_generators = [
        ChildGenerator("wood"),
        ChildGenerator("nails")
    ]
    names_data = ["shelf"]


class PlasticShelf(Thing):
    child_generators = [
        ChildGenerator("plastic"),
        ChildGenerator("nails", probability=50)
    ]
    names_data = ["shelf"]


class WoodFrame(Thing):
    child_generators = [
        ChildGenerator("wood"),
        ChildGenerator("nails")
    ]


# new Thing("book",["page,20-100"],"*BOOK*");
# new Thing("page",["paragraph,1-8","paper"]);
# new Thing("paper",["cellulose"]);
# new Thing("cardboard",["cellulose"]);
# new Thing("wood",["cellulose","worm,1%"]);
# new Thing("cellulose",[GlucidsFactory.one()]);
# new Thing("paragraph",["character,50-300"]);
# new Thing("character",["ink"],"*CHAR*");
# new Thing("ink",[AlcoholFactory.one(), "oil"]);


class Bathtub(Thing):
    child_generators = [
        ChildGenerator("porcelain"),
        ChildGenerator("pipes"),
        ChildGenerator("dirt", probability=30),
        ChildGenerator("insect", probability=5),
        ChildGenerator("hair", probability=30)
    ]


class Shower(Thing):
    child_generators = [
        ChildGenerator("porcelain"),
        ChildGenerator("pipes"),
        ChildGenerator("dirt", probability=30),
        ChildGenerator("insect", probability=5),
        ChildGenerator("hair", probability=30)
    ]


class Tv(Thing):
    child_generators = [
        ChildGenerator("tv show"),
        ChildGenerator("tv remote", probability=20),
        ChildGenerator("plastic"),
        ChildGenerator("electronics"),
    ]
    names_data = [
        ["plasma", "wide-screen", "high-resolution", "black and white", "small", "cheap"],
        [" TV"]
    ]


class TvShow(Thing):
    names_data = [
        [
            "A movie about","A show about","A sitcom about","A TV show about","A cartoon about","A foreign show about",
            "An ad with"
        ],
        [" "],
        [
            "stupid people", "boring people", "uninteresting people", "tan people", "foreigners", "a cute couple",
            "an obnoxious couple", "a dysfunctional couple", "magic kids", "space people", "scientists", "heroes",
            "antiheroes", "superheroes", "cavemen", "knights", "old-timey people", "awkward teenagers",
            "hundreds of people", "insane people", "cool hip kids", "a kid and his pet", "a kid and his teacher",
            "a boy and a girl", "businessmen", "an old man and his wife", "a young couple", "cow-boys", "pirates",
            "ninjas", "monsters", "wizards", "cleaning products", "aliens", "cute talking animals", "artists",
            "wacky animated animals", "beloved cartoon characters", "bears", "sharks", "small people"
        ],
        [" "],
        [
            "struggling with their emotions", "trying to express their feelings", "and ecology", "and friendship",
            "and feelings", "and food", "talking about stuff", "doing things", "kicking butt and taking names",
            "in a post-apocalyptic world", "running away from zombies", "crying helplessly",
            "getting lost in the woods", "and their dream of starting a business",
            "trying to achieve their life-long dream", "trying to keep their promises",
            "trying to destroy a cursed artifact", "in school", "looking away from explosions", "hacking computers",
            "telling jokes", "delivering one-liners", "shooting stuff", "slaying monsters", "going to space",
            "travelling together", "learning about life", "dancing and singing", "doing way gross stuff",
            "learning martial arts", "trying to kill each other", "doing sports",
            "trying to defeat a government conspiracy", "in the century's biggest heist",
            "involving hilarious quiproquos and misunderstandings", "getting killed by a sociopath",
            "fighting robots", "killing aliens", "rescuing baby animals", "falling in love", "going on a date",
            "slowly turning evil", "learning that violence is not the answer", "doing magic",
            "coming up with convoluted plans", "exploring the sea", "saving the world", "involved in various mishaps",
            "involved in hilarious pranks", "with less-than-stellar writing", "with neat visual effects",
            "with a beautiful soundtrack", "with an impressive amount of clichés", "with a twist at the end",
            "with brilliant acting"
        ],
        ["."]
    ]


# new Thing("video game console",[PlasticFactory.one(), "electronics"],[["Mega","Ultra","Gene","Se","Ninten","Nin","Play","Game","Next","Retro","Dream","Sun","Kine","3D"],["station","do","sphere","sis","tron","ga","zor","boy","cast","nect","next"]]);

# new Thing("machine",["computer keyboard,10%","engine,20%","mechanics","electronics,40%","metal","wood,10%","cables,40%","dirt,10%"],[["valve","pump","terminal","conveyor","forklift","girder","furnace","generator","hydraulics"]]);
# new Thing("cables",[PlasticFactory.one(), "wire"]);
# new Thing("wire",[element_factories['Cu'].one()]);

# new Thing("engine",["mechanics"]);
# new Thing("mechanics",["cog,2-12","push-button,0-3","electronics,30%","cables,75%","wire,0-2","tube,0-3","nails,40%","insect,5%"],"mechanical components");
# new Thing("cog",[[element_factories['Cu'].one(), PlasticFactory.one(), IronFactory.one(), SteelFactory.one(), element_factory['Al'].one()]],["cog","gear","spur gear","helical gear","bevel gear","harmonic drive","spring","pump","sprocket","wheel","chain","belt","track","bolts","gizmo","pulley","puffer","smoker","vent"]);
# new Thing("push-button",[PlasticFactory.one(), "cables"],["lever","button","switch"]);
# new Thing("tube",[[PlasticFactory.one(), "metal","glass"]]);

# new Thing("electronics",["microchip,1-6","electronic component,1-6","wire,0-2"]);
# new Thing("microchip",["electronic component,1-15", PlasticFactory.probable(75), element_factories['Cu'].one().probable(75),element_factories['Si'].one().probable(25),element_factories['Au'].one().probable(5)],["microchip"]);
# new Thing("electronic component",[PlasticFactory.probable(75), element_factories['Cu'].one().probable(75),element_factories['Si'].one().probable(25),element_factories['Au'].one().probable(5)],["transistor","inductor","capacitor","diode","metagizmo","transmorpher","beeper"]);


# ChildGenerator("organic matter", probability=5),
# ChildGenerator("pasta", probability=0.1),
# ChildGenerator("insect", probability=5),
# ChildGenerator("hair", probability=30)
# ChildGenerator("portal", probability=0.1),
# ChildGenerator("wood"),
# ChildGenerator("cloth"),
# ChildGenerator("keratin")
# ChildGenerator("plastic"),
# ChildGenerator("electronics"),
# ChildGenerator("skeleton", probability=0.1),
# ChildGenerator("hat", probability=30),
# ChildGenerator("pants", (0, 5)),
# ChildGenerator("shirt", (0, 5)),
# ChildGenerator("underwear", (0, 6)),
# ChildGenerator("coat", (0, 3)),
# ChildGenerator("socks", (0, 8)),
# ChildGenerator("shoes", (0, 6)),
# ChildGenerator("copper"),
# [ChildGenerator("molecule")]
# ChildGenerator("ink", probability=80),
# ChildGenerator("note", (0, 8)),
# ChildGenerator("office toy", probability=30),
# ChildGenerator("book", probability=20),
# ChildGenerator("lint", probability=40),

# ChildGenerator("donut box", probability=4),
# ChildGenerator("cheese", (0, 3)),
# ChildGenerator("water bottle", (0, 1)),
# ChildGenerator("juice bottle", (0, 1)),
# ChildGenerator("soda bottle", (0, 1)),
# ChildGenerator("can", (0, 6)),
# ChildGenerator("cookie box", (0, 6)),
# ChildGenerator("insect", probability=2),
# ChildGenerator("roast", probability=15),
# ChildGenerator("cake", probability=3),
# ChildGenerator("pie", probability=3),
# [ChildGenerator("yoghurt", (0, 6)), None],
# [ChildGenerator("ice cream", (0, 6)), None],
# [ChildGenerator("cheese", (0, 3)), None],
# ChildGenerator("milk bottle", (0, 1)),
# ChildGenerator("wine bottle", probability=10),

CONTENTS = [
    Cabinet,
    CabinetContent,
    Fridge,
    FridgeContent,
    Oven,
    KitchenSink,
    Sink,
    Toilet,
    Pipes,
    Nails,
    Metal,
    MetalGrill,
    Porcelain,
    Ceramic,
    Chair,
    Armchair,
    Couch,
    TvRemote,
    Coin,

    Dirt,

    Dust,

    Pen,
    Button,

    Bed,
    Pillow,
    Feather,

    Mirror,
    Glass,
    Desk,
    Cupboard,
    DrinkingGlass,
    Bowl,
    Cup,
    Plate,
    Closet,
    LivingRoomTable,
    Table,
    Drawer,

    Bookshelf,
    SmallBookshelf,
    WoodShelf,
    PlasticShelf,
    WoodFrame,

    Bathtub,
    Shower,
    Tv,
    TvShow,
]
