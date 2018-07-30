from ..thing import Thing
from ..children import ChildGenerator

# furniture
# new Thing("cabinet",["wood frame","glass,30%",".cabinet content"]);
# new Thing("cabinet content",["donut box,4%",["cheese,0-3",""],"water bottle,0-1","juice bottle,0-1","soda bottle,0-1",["can,0-6","cookie box,0-6"],"insect,2%"]);
# new Thing("fridge",[".fridge content","plastic","metal grill,1-4","electronics"]);
# new Thing("fridge content",["roast,15%","pasta,40%","pasta,10%","can,15%","donut box,5%","cake,3%","pie,3%",["yoghurt,0-6",""],["ice cream,0-6",""],["cheese,0-3",""],"water bottle,0-1","juice bottle,0-2","soda bottle,0-2","milk bottle,0-1","wine bottle,10%"]);
# new Thing("oven",[["pie","cake","roast","",""],"plastic","metal grill,1-3","electronics"]);
# new Thing("kitchen sink",[".sink"]);


class Sink(Thing):
    child_generators = [
        [
            ChildGenerator("porcelain"),
            ChildGenerator("metal"),
        ],
        ChildGenerator("organic matter", probability=5),
        ChildGenerator("pipes"),
    ]


class Toilet(Thing):
    child_generators = [
        ChildGenerator("water"),
        ChildGenerator("organic matter", probability=15),
        ChildGenerator("pasta", probability=0.1),
        ChildGenerator("porcelain"),
        ChildGenerator("pipes"),
    ]


# new Thing("pipes",["metal","dirt"]);
# new Thing("nails",["iron"]);
# new Thing("metal",["iron"]);
# new Thing("metal grill",["metal"]);
# new Thing("porcelain",["silica"]);
# new Thing("ceramic",["silica"]);


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


# new Thing("coin",["organic matter,2%","dirt,2%","copper"]);
# new Thing("gold coin",["gold"]);
# new Thing("dirt",["organic matter,50%","dust"]);
# new Thing("grease",["lipids","dust"]);
# new Thing("dust",["molecule"]);
# new Thing("crumbs",["organic matter"]);
# new Thing("lint",["textile fibre"]);
# new Thing("pen",["plastic","ink,80%"]);
# new Thing("button",["plastic"]);
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


# new Thing("glass",["silica"]);


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


# new Thing("drinking glass",["glass"],"glass");
# new Thing("bowl",["ceramic"]);
# new Thing("cup",["ceramic"]);
# new Thing("plate",["ceramic"]);


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
    type_name = 'living-room'
    child_generators = [
        ChildGenerator(".table"),
        ChildGenerator("drawer", (0, 2)),
    ]
    names_data = ["table"]


# new Thing("drawer",["note,0-8","office toy,30%","office toy,30%","pen,30%","pen,10%","pen,5%","donut box,4%","can,2%","book,20%","book,20%","book,5%","book,5%","button,10%","button,10%","dust,40%","lint,40%"]);
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


# new Thing("wood shelf",["wood","nails"],"shelf");
# new Thing("plastic shelf",["plastic","nails,50%"],"shelf");
# new Thing("wood frame",["wood","nails"]);
# new Thing("book",["page,20-100"],"*BOOK*");
# new Thing("page",["paragraph,1-8","paper"]);
# new Thing("paper",["cellulose"]);
# new Thing("cardboard",["cellulose"]);
# new Thing("wood",["cellulose","worm,1%"]);
# new Thing("cellulose",["glucids"]);
# new Thing("paragraph",["character,50-300"]);
# new Thing("character",["ink"],"*CHAR*");
# new Thing("ink",["alcohol","oil"]);


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


# new Thing("video game console",["plastic","electronics"],[["Mega","Ultra","Gene","Se","Ninten","Nin","Play","Game","Next","Retro","Dream","Sun","Kine","3D"],["station","do","sphere","sis","tron","ga","zor","boy","cast","nect","next"]]);

# new Thing("machine",["computer keyboard,10%","engine,20%","mechanics","electronics,40%","metal","wood,10%","cables,40%","dirt,10%"],[["valve","pump","terminal","conveyor","forklift","girder","furnace","generator","hydraulics"]]);
# new Thing("cables",["plastic","wire"]);
# new Thing("wire",["copper"]);

# new Thing("engine",["mechanics"]);
# new Thing("mechanics",["cog,2-12","push-button,0-3","electronics,30%","cables,75%","wire,0-2","tube,0-3","nails,40%","insect,5%"],"mechanical components");
# new Thing("cog",[["copper","plastic","iron","steel","aluminium"]],["cog","gear","spur gear","helical gear","bevel gear","harmonic drive","spring","pump","sprocket","wheel","chain","belt","track","bolts","gizmo","pulley","puffer","smoker","vent"]);
# new Thing("push-button",["plastic","cables"],["lever","button","switch"]);
# new Thing("tube",[["plastic","metal","glass"]]);

# new Thing("electronics",["microchip,1-6","electronic component,1-6","wire,0-2"]);
# new Thing("microchip",["electronic component,1-15","plastic,75%","copper,75%","silicon,25%","gold,5%"],["microchip"]);
# new Thing("electronic component",["plastic,75%","copper,75%","silicon,25%","gold,5%"],["transistor","inductor","capacitor","diode","metagizmo","transmorpher","beeper"]);


# ChildGenerator("porcelain"),
# ChildGenerator("metal"),
# ChildGenerator("organic matter", probability=5),
# ChildGenerator("pipes"),
# ChildGenerator("water"),
# ChildGenerator("pasta", probability=0.1),
# ChildGenerator("dirt", probability=30),
# ChildGenerator("insect", probability=5),
# ChildGenerator("hair", probability=30)
# ChildGenerator("glass"),
# ChildGenerator("portal", probability=0.1),
# ChildGenerator("wood"),
# ChildGenerator("nails", probability=50),
# ChildGenerator("cloth"),
# ChildGenerator("keratin")
# ChildGenerator("cup", (0, 6)),
# ChildGenerator("drinking glass", (0, 6)),
# ChildGenerator("bowl", (0, 4)),
# ChildGenerator("plate", (0, 8)),
# ChildGenerator("wood frame"),
# ChildGenerator("wood shelf", (1, 4)),
# ChildGenerator("drawer", (0, 2)),
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
# ChildGenerator("button", probability=20),
# ChildGenerator("plastic shelf", (3, 8)),
# ChildGenerator("coin", probability=5),
# ChildGenerator("pen", probability=5),

CONTENTS = [
    Sink,
    Toilet,

    Chair,
    Armchair,
    Couch,
    TvRemote,

    Bed,
    Pillow,
    Feather,

    Mirror,

    Desk,
    Cupboard,

    Closet,
    LivingRoomTable,
    Table,

    Bookshelf,
    SmallBookshelf,

    Bathtub,
    Shower,
    Tv,
    TvShow,
]
