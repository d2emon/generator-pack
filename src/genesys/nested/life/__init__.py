from .body import FACTORIES as BODY_FACTORIES
from .cell import FACTORIES as CELL_FACTORIES
from .human import FACTORIES as HUMAN_FACTORIES
from .vegetation import *
from .life import *


FACTORIES = {
    **CELL_FACTORIES,
    **BODY_FACTORIES,
    **HUMAN_FACTORIES,
}


"""
new Thing("abomination",["abomination body", "abomination psyche"],"*PERSON*| (abomination)");
//nonononononono
new Thing("abomination psyche",["abomination thoughts", "memories"],"psyche");
new Thing("abomination thoughts",[
    BlackHole.Factory.probable(0.01),
    "abomination thought"],"thoughts");
new Thing("abomination thought",[],["P-please...", "Don't look at me...", "Please... kill me...", "Kill... me...", "Why would I ever ask for this...", "I only wish for death.", "I only long for death now.", "I only demand... death...", "End my misery... I beg you...", "This is a mockery of existence...", "I miss her so much...", "I miss him so much...", "I miss my family...", "Why would they do that to me...", "How could they do this to me...", "What have I become...", "I feel... different...", "I can't feel... anything...", "I can't... see anything..."]);
new Thing("abomination body",["abomination head", "abomination head,5%", "abomination torso", ["arm,0-8", "arm,0-4"], ["leg,0-8", "leg,0-4"], "crustacean claw,2%", "stinger,2%", "weird soft organ,10%", "weird soft organ,10%", "weird hard organ,10%", "weird hard organ,10%"],"misshapen body");
new Thing("abomination head",["mouth,0-2", "nose,0-2", "eye,0-8", "ear,0-4", "skull,90%", "weird soft organ,20%", "weird hard organ,20%", "head hair,65%",
    (BodyPatFactory)
    ],"misshapen head");
new Thing("abomination torso",["chest", "chest,10%", "pelvis", "pelvis,10%", "weird soft organ,20%", "weird hard organ,20%",
    (BodyPatFactory)
    ],"misshapen torso");

//brain stuff
new Thing("psyche",["thoughts", "memories"],"psyche");
new Thing("thoughts",[
    BlackHole.Factory.probable(0.01),
    ["sad thought,2-4", "happy thought,2-4"]]);
new Thing("sad thought",[],["*SADTHOUGHT*"]);
new Thing("happy thought",[],["*HAPPYTHOUGHT*"]);
new Thing("memories",["memory,2-4"]);
new Thing("memory",[],["*MEMORY*"]);

//cloth stuff
new Thing("cloth",["textile"]);
new Thing("leather",[
    SkinCellFactory.one(),
    ]);
new Thing("textile",["textile fibre"]);
new Thing("textile fibre",["keratin"],["textile fibres"]);
new Thing("keratin",[
    ProteinsFactory.one(),
]);
new Thing("sweat",[
    WaterFactory.one(),
    SaltFactory.one(),
    GlucidsFactory.one(),
]);
new Thing("clothing",["textile",
    DeadSkinFactory.probable(40),
    "sweat,15%"]);
new Thing("pocket",["dust,20%", "crumbs,20%", "lint,30%", "donut,1%", "coin,20%", "coin,20%", "coin,10%", "pen,10%", "pen,2%", "button,10%", "button,5%", "button,1%", "note,15%", "note,5%", "handgun,0.4%", "pasta,0.2%", "textile"]);

new Thing("pants",["pocket,0-4", ".clothing"],["pants", "trousers", "sweatpants", "bermuda shorts", "shorts", "jeans", "cargo pants"]);
new Thing("shirt",[".clothing"],["shirt", "sweater", "t-shirt"]);
new Thing("underwear",[".clothing"]);
new Thing("coat",["pocket,0-4", ".clothing", "leather,30%"],["coat", "jacket", "hoodie"]);
new Thing("cozy von pocketworth",["pocket,20-40", ".clothing", "leather,30%"],["Cozy von Pocketworth"]);
//lotsopokkits
new Thing("socks",[".clothing"]);
new Thing("shoes",["leather,40%",
    PlasticFactory.one(),
],["shoes", "boots", "sneakers", "sandals"]);
//crocs //okay seriously no
new Thing("hat",[".clothing"],["cap", "hat", "hat", "hat", "hat", "beret", "party hat", "top-hat"]);
new Thing("glasses",[
    PlasticFactory.one(),
    "glass", "metal,10%"],["glasses", "glasses", "glasses", "sunglasses", "monocle", "ski mask"]);

//terrain stuff
new Thing("ocean",["sea water", "sea life", "beach,10-20", ["iceberg,2-6", "", "", "", ""], "abyss"]);
new Thing("sea",["sea water", "sea life", "beach,2-6"],[["great", "wide", "big", "old", "young", "large", "small", "dead", "shallow", "deep", "red", "yellow", "green", "blue", "orange", "brown", "grey", "black", "white", "purple", "shady", "bright", "silver"], [" sea"]]);
new Thing("sea water",[
    WaterFactory.one(),
    SaltFactory.one(),
]);
new Thing("iceberg",["bear,30%", "bear,10%",
    IceFactory.one(),
]);
new Thing("beach",["beach life", "sand"]);
new Thing("abyss",["sand", "abyss life"]);
new Thing("sand",[
    SilicaFactory.one(),
    ]);
new Thing("soil",[["worm,0-2", "", ""], ["insect,0-2", "", ""],
    SilicaFactory.one(),
    ],"dirt");
new Thing("mud",[["worm,0-2", "", ""], ["insect,0-2", "", ""],
    WaterFactory.one(),
    SilicaFactory.one(),
]);

new Thing("river",["river life",
    WaterFactory.one(),
    "soil", "mud"],["river", "stream", "brook", "creek"]);
new Thing("lake",["lake life",
    WaterFactory.one(),
    "soil", "mud"],["lake", "lagoon", "pond", "marsh", "creek", "cove"]);
new Thing("plain",[
    FireFactory.probable(0.3),
    "land life", "river,0-3", "lake,0-1", "grass", "soil",
    SnowFactory.probable(5),
],["plain", "steppe", "valley", "canyon", "flatland", "moor", "grassland", "prairie", "desert", "savannah", "tundra", "wasteland"]);
new Thing("forest",[
    FireFactory.probable(0.5),
    "forest life", "river,0-2", "trees", "grass", "humus", "soil",
    SnowFactory.probable(5),
],["forest", "woods", "copse"]);
new Thing("jungle",[
    FireFactory.probable(0.5),
    "jungle life", "river,0-2", "jungle trees", "grass", "humus", "soil"],["jungle", "rainforest"]);
new Thing("mountain",["mountain life", "river,0-3", "lake,0-1", "cave,30%", "cave,30%", "cave,20%", "trees", "soil",
    RockFactory.one(),
    SnowFactory.probable(40),
],["mountain", "peak", "hill", "volcano", "bluff", "cliff", "mesa", "plateau"]);
new Thing("cave",["cave life", "dragon lair,1%", "river,20%", "lake,10%",
    RockFactory.one(),
    IronFactory.one().probable(2),
],["cave", "cavern", "grotto"]);

new Thing("ancient plain",[
    FireFactory.probable(0.3),
    "caveman settlement,40%", "ancient land life", "river,0-3", "lake,0-1", "grass", "soil",
    SnowFactory.probable(5),
],["plain", "steppe", "valley", "canyon", "flatland", "moor", "grassland", "prairie", "desert", "savannah", "tundra", "wasteland"]);
new Thing("ancient forest",[
    FireFactory.probable(0.5),
    "caveman settlement,40%", "ancient forest life", "river,0-2", "trees", "grass", "humus", "soil",
    SnowFactory.probable(5),
],["forest", "woods", "copse"]);
new Thing("ancient jungle",[
    FireFactory.probable(0.5),
    "caveman settlement,40%", "ancient jungle life", "river,0-2", "jungle trees", "grass", "humus", "soil"],["jungle", "rainforest"]);
new Thing("ancient mountain",["caveman settlement,40%", "ancient mountain life", "ancient cave,30%", "ancient cave,20%", "ancient cave,10%", "river,0-3", "lake,0-1", "trees", "soil",,
    RockFactory.one(),
    SnowFactory.probable(40),
],["mountain", "peak", "hill", "volcano", "bluff", "cliff", "mesa", "plateau"]);
new Thing("ancient cave",["caveman settlement,65%", "wall painting,50%", "wall painting,30%", "wall painting,30%", ".cave"],["cave", "cavern", "grotto"]);

new Thing("future sky",["sprowseship,4-12", ".sky"],"sky");
new Thing("terraformed sky",["plane,1-8", "rocketship,20%", ".sky"],"sky");
new Thing("sky",["visitor ship,10%", "meteorite,3%", "sky life", "precipitation,50%", "cloud,2-8",
    ELEMENTS['O'].one(),
    CarbonFactory.one(),
    "ozone"],"sky");
new Thing("meteorite",["space animal,6%",
    IceFactory.probable(60),
    RockFactory.one(),
    IronFactory.one().probable(40),
],"meteorite");
new Thing("ozone",[
    ELEMENTS['O'].one(),
]);
new Thing("cloud",[
    WaterFactory.one(),
]);
new Thing("precipitation",[
    WaterFactory.one(),
],["rain", "snow", "hail", "mist", "fog", "drizzle", "storm"]);

//vegetation
new Thing("plant cell",[".cell"],["plant cells"]);
new Thing("grass",["grass blade,50-100"]);
new Thing("grass blade",["grass thoughts,2%",
    DewFactory.probable(6),
    "worm,3%", "insect,6%", "plant cell"]);
new Thing("grass thoughts",["grass thought,1"],"thought");
new Thing("grass thought",[],[":D", ":O", "D:", ":|", ":]", ">:0"]);
new Thing("trees",["tree,20-50"]);
new Thing("tree",["tree thoughts,2%", "tree trunk", "branches", "leaves", "nest,5%", "nest,2%", "fruits,20%", "flowers,20%"],["larch", "fir", "oak", "birch", "pine", "sequoia", "cedar", "spruce", "ash", "poplar", "elm", "sycamore", "willow", "mahogany", "laurel", "orange tree", "lemon tree", "palm tree", "coconut tree", "pear tree", "apple tree", "walnut tree", "olive tree"]);
new Thing("tree thoughts",["tree thought,1"],"thought");
new Thing("tree thought",[],["Well. What is this all about.", "So. What's the hurry?", "Whoah. Slow down.", "Do like a tree. And go away.", "I seen some things.", "They're coming.", "We know.", "We've been watching you for hundreds of years.", "Do you have any idea how old I am?", "Yes. I remember you. I remember all of you."]);
new Thing("leaves",["leaf,50-100"]);
new Thing("leaf",[
    DewFactory.probable(6),
    "insect,6%", "plant cell"]);
new Thing("branches",["branch,10-30"]);
new Thing("branch",["insect,6%", "leaf,10%", "plant cell"]);
new Thing("twig",["plant cell"]);
new Thing("fruits",["worm,5%", "plant cell", "sugar"]);
new Thing("flowers",["insect,5%", "plant cell", "pollen"]);
new Thing("pollen",["plant cell", "sugar"]);
new Thing("tree trunk",["insect,4%", "wood", "bark"]);
new Thing("bark",["insect,10%", "worm,10%", "wood"]);
new Thing("jungle trees",["jungle tree,20-150"],"trees");
new Thing("jungle tree",[".tree"],["tree"]);
new Thing("humus",["insect,0-3", "worm,0-3", "twig,0-3", "leaf,0-6",
    OrganicFactory.one(),
"dirt"]);
new Thing("nest",["bird,50%", "egg shell,20%", "bird egg,0-6", "twig,6-12"]);

//life
new Thing("life",[["bird", "poultry", "fish", "shark", "crustacean", "cnidaria", "worm", "mollusk", "clam", "plankton", "reptile", "amphibian", "snake", "small mammal", "herbivorous mammal", "predatory mammal", "monkey", "bear", "horse", "cat", "dog", "dinosaur", "medieval person", "caveman", "dragon", "person", "space animal", "insect", "tree", "grass blade"]],"Life");
new Thing("sea life",["sea monster,0.5%", "fish,5-10", "cetacean,0-4", "shark,0-4", "crustacean,1-4", "cnidaria,1-4", "mollusk,1-4", "clam,1-4", "plankton,2-8"],"life");
new Thing("abyss life",["sea monster,2%", "fish,3-6", "cetacean,0-2", "shark,0-2", "crustacean,2-5", "cnidaria,2-5", "mollusk,2-5", "clam,2-5", "plankton,2-8"],"life");
new Thing("beach life",["bird,0-3", "herbivorous mammal,5%", "amphibian,2%", "reptile,2%", "snake,2%", "predatory mammal,5%", "small mammal,2-5", "insect,3-10", "clam,3-8"],"life");
new Thing("river life",["fish,5-15", "crustacean,0-10", "plankton,2-8", "bird,0-5", "small mammal,0-2", "amphibian,0-5", "reptile,0-1", "snake,0-1", "insect,3-10"],"life");
new Thing("lake life",["sea monster,1%", "fish,5-15", "amphibian,0-5", "crustacean,0-10", "bird,0-5", "plankton,5-15", "small mammal,0-2", "reptile,0-1", "snake,0-1", "insect,3-10"],"life");
new Thing("land life",["herbivorous mammal,2-8", "horse,5%", "predatory mammal,0-4", "small mammal,5-10", "amphibian,0-2", "reptile,0-2", "snake,0-2", "bird,0-5", "anthill,30%", "insect,5-10"],"life");
new Thing("forest life",["herbivorous mammal,2-8", "predatory mammal,0-4", "bear,0-5", "small mammal,5-10", "amphibian,0-3", "reptile,0-3", "snake,0-3", "bird,2-10", "beehive,30%", "anthill,30%", "insect,5-10"],"life");
new Thing("jungle life",["herbivorous mammal,1-5", "predatory mammal,0-4", "monkey,1-5", "small mammal,5-10", "amphibian,0-3", "reptile,0-3", "snake,0-6", "bird,2-10", "beehive,30%", "anthill,30%", "insect,5-10"],"life");
new Thing("mountain life",["herbivorous mammal,1-6", "predatory mammal,0-4", "bear,2-6", "small mammal,5-10", "amphibian,0-2", "reptile,0-2", "snake,0-2", "bird,2-10", "beehive,30%", "anthill,30%", "insect,5-10"],"life");
new Thing("cave life",["herbivorous mammal,10%", "predatory mammal,10%", "bear,20%", "small mammal,20%", "small mammal,20%", "small mammal,20%", "amphibian,20%", "reptile,20%", "snake,10%", "bird,15%", "bird,5%", "insect,5-10"],"life");
new Thing("ancient land life",["dinosaur,0-8", ".land life"],"life");
new Thing("ancient forest life",["dinosaur,0-5", ".forest life"],"life");
new Thing("ancient jungle life",["dinosaur,0-5", ".jungle life"],"life");
new Thing("ancient mountain life",["dinosaur,0-3", ".mountain life"],"life");
new Thing("urban life",["bird,0-8", "small mammal,5-10", "anthill,30%", "insect,10-20"],"life");
new Thing("sky life",["shark,1%", "bird,5-20", "insect,0-2"],"life");
new Thing("galactic life",["space monster,1%", "space animal,1-12"],"life");

new Thing("skeleton",[
    BonesFactory.one(),
    ],"skeleton");
new Thing("flesh",[
    (SkinlessBodyPartFactory)
    ],"flesh");
new Thing("soft flesh",[
    (SkinlessSoftBodyPartFactory)
    ],"flesh");
new Thing("scales",["keratin"]);
new Thing("fish fin",[
    MusclesFactory.one(),
    "scales"],"fin");
new Thing("fish tail",[
    MusclesFactory.one(),
    "scales"],"tail");
new Thing("fish skin",["scales"],"skin");
new Thing("cetacean flipper",[
    MusclesFactory.one(),
    SkinFactory.one(),
    ],"flipper");
new Thing("cetacean fin",[
    MusclesFactory.one(),
    SkinFactory.one(),
    ],"fin");
new Thing("crustacean claw",[
    ChitinFactory.one(),
    MusclesFactory.one(),
    FatFactory.one(),
    ],"claw");
new Thing("crustacean leg",[
    ChitinFactory.one(),
    MusclesFactory.one(),
    FatFactory.one(),
    ],"leg");
new Thing("crustacean shell",[
    ChitinFactory.one(),
    ],"shell");
new Thing("clam shell",[
    ELEMENTS['Ca'].one(),
],"shell");
new Thing("simple eye",[".eye flesh"],"eye");
new Thing("exoskeleton",[
    ChitinFactory.one(),
    ],"exoskeleton");
new Thing("insect leg",[
    ChitinFactory.one(),
    MusclesFactory.one(),
    FatFactory.one(),
    ],"leg");
new Thing("insect claw",[
    ChitinFactory.one(),
    MusclesFactory.one(),
    FatFactory.one(),
    ],"claw");
new Thing("stinger",[
    ChitinFactory.one(),
    "venom"],"stinger");
new Thing("antenna",[
    ChitinFactory.one(),
    ],"antenna");
new Thing("insect wing",[[
    ChitinFactory.one(),
    "scales"],
    DewFactory.probable(2),
],"wing");
new Thing("wing",["feathers",
    (BodyPatFactory)
    ],"wing");
new Thing("reptile wing",["scales",
    (BodyPatFactory)
    ],"wing");
new Thing("bird wing",["feathers",
    (BodyPatFactory)
    ],"wing");
new Thing("bird leg",["feathers",
    (BodyPatFactory)
    ],"leg");
new Thing("bird tail",["feathers",
    (BodyPatFactory)
    ],"tail");
new Thing("venom",[
    ProteinsFactory.one(),
    LipidsFactory.one().probable(40),
    ELEMENTS['N'].one().probable(40),
    ELEMENTS['Na'].one().probable(40),
    ELEMENTS['Cl'].one().probable(40),
],"venom");
new Thing("jelly",[
    WaterFactory.one(),
]);

new Thing("weird soft organ",[
    (SkinlessSoftBodyPartFactory)
    ],[["fleshy", "thick", "slimy", "scaly", "furry", "fuzzy", "feathery", "sharp", "pointy", "thorny", "bulbous", "leathery", "hidden", "soft", "bubbling", "distorted", "shapeless", "porous", "spongiform", "liquid-filled", "foamy", "smoking", "oozing", "drooling", "shivering", "quivering", "pulsing"], [" "], ["grasper", "tendril", "stinger", "claw", "tentacle", "sac", "egg sac", "pouch", "organ", "specialized organ", "bulb", "brain bulb", "gland", "epiderm", "sucker", "pod", "pseudolimb", "nervous bulb", "external muscle", "structure", "orifice", "proboscis", "tail"]]);
new Thing("weird hard organ",[
    (SkinlessBodyPartFactory)
    ],[["fleshy", "thick", "slimy", "scaly", "furry", "fuzzy", "sharp", "pointy", "thorny", "bulbous", "hidden", "flexible", "plated", "armored", "metallic", "distorted", "shapeless", "porous", "spongiform", "liquid-filled", "foamy", "smoking", "oozing", "drooling"], [" "], ["carapace", "shell", "bone structure", "skull", "grasper", "stinger", "claw", "organ", "specialized organ", "sucker", "pod", "pseudolimb", "structure"]]);

new Thing("tentacle",[
    (SkinlessSoftBodyPartFactory)
    ],"tentacle");
new Thing("simple mouth",["teeth", 
    (SkinlessSoftBodyPartFactory)
    ],"mouth");

new Thing("beak",[
    (BonesFactory),
    ],"beak");

new Thing("reptile head",["scales",
    (BodyPatFactory)
    ],"head");
new Thing("reptile leg",["scales",
    (BodyPatFactory)
    ],"leg");

new Thing("fur",["keratin"],"fur");
new Thing("snout",[".nose"],"snout");
new Thing("whiskers",["keratin"],"whiskers");
new Thing("mammal leg",["fur",
    (BodyPatFactory)
    ],"leg");
new Thing("tail",[
    (BodyPatFactory)
    ],"tail");
new Thing("mammal head",["mouth", "snout", "whiskers", "eye,2", "ear,2", "skull", "fur"],"head");
new Thing("mammal body",["mammal head", "fur", "mammal leg,4", "tail", "flesh"],"body");
new Thing("bird body",["bird head", "feathers", "bird leg,2", "bird wing,2", "bird tail", "flesh"],"body");
new Thing("bird head",["beak", "eye,2", "skull", "feathers"],"head");
new Thing("reptile body",["reptile head", "scales", "reptile leg,4", "tail", "flesh"],"body");
new Thing("snake body",["reptile head", "scales", "tail", "flesh"],"body");

//oh my god writing animal thoughts is so much fun

//single-celled organisms
new Thing("bacteria",["bacteria body", "bacteria thoughts"],[["pico", "nitro", "sulfuro", "oxy", "toxi", "micro", "nano", "proto", "archi", "ferro", "mono", "poly", "schizo", "myxo", "hydro", "noo", "zoo", "phyto", "aqui", "acido", "cyano", "chloro", "chromo", "fibro", "osteo", "spiro", "bacillo", "flagello", "helio", "anaero", "photo", "litho", "methano", "cerebro", "cephalo", "brachio", "plasmo", "ethylo"], ["amoeba", "bacteria", "virus"]]);
new Thing("bacteria body",[".cell"],"body");
new Thing("bacteria thoughts",["bacteria thought,1"],["thoughts"]);
new Thing("bacteria thought",[],["#wow", "#wow okay", "#i can't even", "#okay", "#me", "#yes", "#what", "#how", "#delicious", "#seriously", "#but seriously tho", "#germ life", "#mitosis", "#meiosis", "#nucleus", "#cytoplasm", "#single-celled and ready to mingle", "#lame", "#meh", "#i don't wanna talk about it", "#eukaryote privilege", "#protist scum", "#squirm", "#protist patriarchy", "#osmosis", "#one cell of a guy"]);

//sea life
//plankton
new Thing("plankton",["plankton body", "plankton thoughts"],["jellyfish larva", "coral polyp", "diatom", "urchin larva", "starfish larva", "salp", "rotifer", "pteropod", "clione"]);
//krill etc in crustaceans
new Thing("plankton body",["simple eye,0-3", "simple mouth", "exoskeleton", "jelly", "soft flesh"],"body");
new Thing("plankton thoughts",["plankton thought,1"],["thoughts"]);
new Thing("plankton thought",[],["hello :)", "yes hi :)", "how are you :)", "it's sunny today :)", "what a nice day :)", "aaah I could just float away :)", "I am fine thank you :)", "yes I think so :)", "how fun :)", "do you catch my drift :)", "so many cousins :)", "I'm a little lost :)", "no pressure :)", "that's okay :)", "what a nice thing to say :)", "you should stay over :)", "my place or your place :)", "why are you still here :)", "there's a big world to explore :)", "I don't even know where I'm going :)", "here I go! :)", "am I really going where I decide to go, or am I just being pushed around by the current? :)", "oh no :(", "can't you feel them coming? :(", "they're slowly rising from deep below :(", "it's slowly coming this way :(", "I'm different :(", "ravioli, ravioli :)", "give me the formuoli :)", "oh,..."]);

//clams
new Thing("clam",["clam body", "clam thoughts"],["oyster", "mussel", "scallop"]);
new Thing("clam body",["clam shell", "clam shell", "brain", "soft flesh"],"body");
new Thing("clam thoughts",["clam thought,1-3"],["thoughts"]);
new Thing("clam thought",[],["what", "wait", "hold on", "wait why", "i don't", "stay clam and carry on", "oh no", "why this", "that's", "no", "yes", "wait no", "but", "haha what", "please explain", "that's not", "i'm confused", "please why", "slurp", "okay", "okay what", "what is this", "what's that"]);

//cnidaria
new Thing("cnidaria",["cnidaria body", "cnidaria thoughts"],["urchin", "starfish", "sea cucumber", "sea anemon", "coral", "box jelly", "jellyfish", "hydra", "man'o'war", "sponge", "sea nettle", "siphonophore", "ctenophore", "tunicate", "trichordate"]);
//urchins and starfish and sponges are unrelated to cnidarians but I don't really care
new Thing("cnidaria body",["simple mouth", "jelly", "soft flesh"],"body");
new Thing("cnidaria thoughts",["cnidaria thought"],"thoughts");
new Thing("cnidaria thought",[],[["shhhhl", "shhl", "schllll", "gl", "schgl", "gbl", "swwwl"], ["urp", "orp", "arp", "urps", "orpsss"]]);

//mollusks
new Thing("mollusk",["mollusk body", "mollusk thoughts"],["sea slug", "sea snail", "squid", "octopus", "vampire squid", "clione", "sea angel", "cuttlefish", "nautilus", "giant squid", "colossal squid", "mimic octopus"]);
new Thing("mollusk body",["simple eye,2", "mouth", "tentacle,6-8", "jelly", "soft flesh"],"body");
new Thing("mollusk thoughts",["mollusk thought,2"],["thoughts"]);
new Thing("mollusk thought",[],["party time", "is it party time now", "party now ok", "party's over", "okay let's party", "ready to party", "are you party", "they don't look like they want to party", "is the party over", "this party's so hot it's stupid", "this party getting crazy", "partyyyyyyy", "chug chug chug", "we party now", "wanna join in", "we partyin", "okay too much party", "I have a secret for you", "that's a secret", "I kinda like partying", "party yes nice", "woooo party"]);

//crustaceans
new Thing("crustacean",["crustacean body", "crustacean thoughts"],["shrimp", "prawn", "langoustine", "lobster", "rock lobster", "crab", "spider crab", "crayfish", "krill", "triops", "copepod"]);
new Thing("crustacean body",["simple eye,2-6", "brain", "crustacean leg,6-8", "crustacean claw,2", "crustacean shell", "soft flesh"],"body");
new Thing("crustacean thoughts",["crustacean thought,2-3"],["thoughts"]);
new Thing("crustacean thought",[],["skitter skitter", "crawl crawl", "dig dig", "grab grab", "gotta eat", "gotta skitter", "gotta catch food", "gotta hide", "gotta breed", "breed breed", "under the sea"]);

//fish; getting those from http://homepages.cwi.nl/~sjoerd/fishlist.html just because I can
new Thing("fish",["fish body", "fish thoughts"],["anchovy", "sardine", "mackerel", "tuna", "albacore", "herring", "bream", "bass", "perch", "mullet", "brill", "plaice", "sole", "angler", "dab", "flounder", "skate", "cod", "haddock", "pollack", "whiting", "pike", "perch", "trout", "carp", "eel", "lamprey", "salmon", "catfish", "dogfish", "swordfish", "sailfish", "pufferfish", "sunfish", "manta ray", "stingray"]);
new Thing("fish body",["simple eye,2", "brain", "mouth", "fish fin,2-6", "fish skin", "fish tail", "flesh", "worm,5%"],"body");
new Thing("fish thoughts",["fish thought,2-3"],["thoughts"]);
new Thing("fish thought",[],["blup", "bloop", "blwap", "blep", "gotta eat", "gotta swim", "gotta get food", "gotta hide", "gotta breed", "oooh shiny"]);

//sharks
new Thing("shark",["fish body", "shark thoughts"],["shark", "bullshark", "blue shark", "goblin shark", "great white shark", "hammerhead shark", "nurse shark", "tiger shark", "whale shark", "reef shark", "angel shark", "basking shark", "megalodon", "megashark", "wereshark", "bearshark"]);
new Thing("shark thoughts",["shark thought,1-2"],["thoughts"]);
new Thing("shark thought",[],["CHOMP", "NOM", "THIS LOOKS TASTY", "THIS SMELLS DELICIOUS", "IS THIS FOOD", "OH GOD I LOVE FOOD", "MY FOOD IS SCREAMING", "MY FOOD IS TRYING TO SWIM AWAY", "COME BACK FOOD", "I LOVE YOU FOOD", "FOOD WHY DO YOU DO THIS", "FOOD I MISS YOU", "HELLO IS THIS FOOD", "YES THIS IS SHARK", "FOOD AND I ARE BEST FRIENDS", "I AM SO LOST RIGHT NOW", "OH HEY ARE YOU FOOD", "EXCUSE ME ARE YOU FOOD", "OH SORRY I THOUGHT YOU WERE FOOD", "HAVE YOU SEEN FOOD", "WHAT'S THIS ALL ABOUT", "WOULD YOU COME OVER HERE", "SO YOU'RE NOT FOOD RIGHT", "LET ME TELL YOU ABOUT FOOD", "WHY ARE WE YELLING", "OOOH SHINY", "IT KEEPS HAPPENING", "I TOLD YOU ABOUT FOOD BRO", "WHY DO I KEEP EATING MY FRIENDS", "I DON'T GET IT", "I'M A SHARK", "IF THEY DIDN'T WANT TO BE EATEN THEY WOULDN'T BE SO DELICIOUS", "YOU'RE NOT ONE OF THEM PRANCY FANCY DOLPHINS ARE YOU", "FOOD COME BACK I'M SORRY I YELLED", "OH FOOD I LOVE YOU SO", "I'M SERIOUS", "HOLD ON IT'S TIME FOR FOOD"]);

//cetaceans
new Thing("cetacean",["cetacean body", "cetacean thoughts"],["dolphin", "porpoise", "whale", "orca", "bottlenose dolphin"]);
new Thing("cetacean thoughts",["cetacean thought,1-2"],["thoughts"]);
new Thing("cetacean thought",[],["Oh god. Let me tell you about sharks.", "Sigh. Yes, this is dolphin.", "Do I look like a goddamn rescue dog to you?", "A trick? Do I look like a clown to you?", "The blowhole isn't just for show.", "There's things. Down there. Deep down.", "We've seen them.", "They're coming to the surface.", "EEK EEK EEK EEK- oh, sorry about that.", "EEK UUK", "Yes. Charming.", "So long, etc.", "My god. How long must this go on.", "EEEEUUUUUUEEEEEKKKKK", "Click noises.", "Swimmity.", "Yes. No. Go away.", "You know. I could catch that fish myself if I wanted to.", "I mean, that's fine and all.", "That's really all there is to say about it.", "I never make puns on porpoise. HUEHUEHUEHUEHUE", "Look! Over there! Haha, sucker.", "Guess how much I care about sharks? Exactly. I don't."]);
new Thing("cetacean head",["mouth", "eye,2", "skull",
    SkinFactory.one(),
    ],"head");
new Thing("cetacean body",["cetacean head",
    SkinFactory.one(),
    "cetacean flipper,2", "cetacean fin,1-2", "tail", "flesh"],"body");

//worms
new Thing("worm",["worm body", "worm thoughts"],["worm", "mealworm", "maggot", "nightcrawler", "flatworm"]);
//YES I KNOW MAGGOTS AND WORMS ARE UNRELATED
new Thing("worm body",["simple mouth", "soft flesh"],"body");
new Thing("worm thoughts",["worm thought,1-2"],["thoughts"]);
new Thing("worm thought",[],["wiggle wiggle", "squirm squirm", "crawl crawl", "weee", "yayyy", "hey apple", "hey", "oh hey", "hellooo", "oh sorry", "so much fun", "nevermind"]);

//insects (arachnids etc too)
new Thing("insect",["insect body", "insect thoughts"],["ant", "bee", "wasp", "hornet", "ladybug", "cockroach", "termite", "beetle", "dung beetle", "scarab beetle", "bumblebee", "spider", "scorpion", "tarantula", "praying mantis", "butterfly", "moth", "fly", "cricket", "mole cricket", "cicada", "weevil", "stick insect", "aphid", "flea", "lice", "firefly", "gnat", "stinkbug", "grasshopper", "silverfish", "locust", "earwig"]);
new Thing("insect body",["simple eye,2-8", "brain", ["insect leg,6", "insect leg,8"], ["insect claw,2", ""], "exoskeleton", "stinger,30%", ["insect wing,2", "insect wing,4", "", ""], ["antenna,2", ""], "flesh"],"body");
//spiders with wings. because yeah
new Thing("insect thoughts",["insect thought,2-3"],["thoughts"]);
new Thing("insect thought",[],["skitter", "skitter skitter", "squirm squirm", "crawl crawl", "buzz", "big noisy things", "small tasty things", "too much sun", "not enough sun", "need water", "need food", "need shelter", "food please", "mating please", "must defend nest", "intruder detected", "must spawn eggs", "hey hey", "let's be bros", "no stomp please", "go away"]);
new Thing("social insect",["insect body", "social insect thoughts"],["worker", "soldier", "drone"]);
new Thing("insect queen",["insect body", "social insect thoughts"],["queen"]);
new Thing("anthill",["social insect,10-30", "insect queen", "insect egg,2-10", "dirt"],["anthill", "termite mound"]);
new Thing("beehive",["social insect,10-30", "insect queen", "insect egg,2-10", "paper"],["beehive", "wasp nest", "hornet nest"]);
new Thing("insect egg",["egg thoughts", "egg shell", "soft flesh",
    OrganicFactory.one(),
],"egg");
new Thing("social insect thoughts",["social insect thought,1-2"],["thoughts"]);
new Thing("social insect thought",[],["hello intruder", "you should stay away intruder", "intruder we may be forced to chop you up into little pieces if you stay here", "this is no place for you intruder", "why don't you go back to your intruder nest with all the other intruders", "we have no need for intruders right now", "hey intruder ever heard of personal space", "sorry intruder but you're kind of in the way", "intruder that's enough now", "intruder why don't you come back another time", "sorry intruder we're all super-busy here", "hey intruder you're like very big so please don't stay here", "i trophallaxized a girl and i liked it"]);

//monsters
new Thing("sea monster",["sea monster thoughts", ["tentacle,0-6", "fish fin,0-4", "", ""], "stinger,20%", ["crustacean claw,0-4", ""], ["crustacean leg,0-8", ""], ["crustacean shell", "scales", "fur", "exoskeleton", ""], ["mouth,1-2", "beak,1-2"], "skull,80%", ["eye,1-8", "simple eye,1-8", "", ""], "weird soft organ,0-4", "weird hard organ,0-4"],[["giant", "timeless", "colossal", "abyssal", "forgotten", "ancient", "gigantic", "monstrous"], [" "], ["craze", "drift", "dredge", "dread", "slumber", "dream", "wander", "frost", "magma", "stone", "slime", "ooze", "egg", "larva", "grudge", "stride", "flail", "wail", "time", "star", "crystal", "terror", "horror", "scream", "wrath", "burst", "dark", "deep", "tickle"], ["fin", "tail", "sinker", "sunk", "singer", "song", "polyp", "rifter", "glider", "squirmer", "titan", "colossus", "brain", "queen", "king", "child", "guardian", "seer", "whale", "worm", "spider", "crab", "leech", "fish", "shark", "squid", "saur", "buddy", "lord"]]);
new Thing("sea monster thoughts",["sea monster thought,1-2"],["thoughts"]);
new Thing("sea monster thought",[],["IIIIII MUSSST SCREEEAAAM", "I AMMMM AWAKENED", "ALLLLLL FEAR MEEEEE", "NOOOOONE SHALL LIVE", "I MUSSSSST EATTTTT", "DEEEEEEEEP I SSSSLUMBER", "IIIII SHALL CONSSSSUME", "IIIII SHALL DEVOUUUUURRRRR", "LIFFFFFFE MUSSSSST PERISHHHHH", "NNNNNNNNURISHMENT", "ALL SHALLLLLLL GO INSSSSSSANE", "SSSSSSANITY SHALL YIELDDDDD", "EXXXXXILED I WASSSSS", "EONSSSSS I HAVE SLUMBERED", "EONSSSSS I HAVE WAITED", "MORTALSSSSSS BEHOLDDDDD", "I COMMMMME FROM DEEP", "IMMMMMMOBILE I WATCHHHH", "SSSSSKITTER", "THEY FFFFFLOAAAAAT"]);

new Thing("space monster",["space monster thoughts", ["tentacle,0-6", "fish fin,0-4", "", ""], "stinger,20%", ["crustacean claw,0-4", ""], ["crustacean leg,0-8", ""], ["crustacean shell", "scales", "fur", "exoskeleton", ""], ["mouth,1-2", "beak,1-2"], "skull,80%", ["eye,1-8", "simple eye,1-8", "", ""], "weird soft organ,0-4", "weird hard organ,0-4"],[["C'", "Vr'", "Ksh", "Zn'", "Sh", "Hrl", "X", "O", "Yog", "Gorg", "Morg", "Marg", "Magg"], ["", "", "agn", "soth", "norgn", "ngas", "alx", "orx", "rgl", "iirn", "egw", "thulh", "t", "g", "m"], ["org", "orgon", "orgus", "orkus", "oid", "us", "u", "esth", "ath", "oth", "um", "ott", "aur"], ["", " the Forgotten", " the Entity", " the Ancient", " the Starchild", " the Seeder", " the Leech", " the Timeless", " the Eon", " the Many", " the Countless", " the Boundless", " the Prisoner", " the Child", " the Form", " the Shape", " the Drifter", " the Swarm", " the Vicious", " the Warden", " the Ender", " the Unworldly", " the Unfriendly", " the All-Consumer"]]);
new Thing("space monster thoughts",["space monster thought,1-2"],["thoughts"]);
new Thing("space monster thought",[],["WWWWWWWIDER THAN STARRRRRRS", "AWAKENNNN MY CHILDRENNNNNN", "GALAXIESSSSS SHALL FALLLLLLL", "I AMMMMMM INFFFFFINITE", "I SSSSSSSPAN AGESSSS", "WWWWWWEEEEE ARE UNDYINGGGGGG", "WE COMMMMMMMME", "WE ANSSSSSWER THE CALLLLLLL", "I TRAVELLLLLLL SLLLLLLUMBERING", "FROMMMMMM FARRRRRR I COMMMME", "IIIIII MUSSST SCREEEAAAM", "I AMMMM AWAKENED", "ALLLLLL FEAR MEEEEE", "NOOOOONE SHALL LIVE", "I MUSSSSST EATTTTT", "DEEEEEEEEP I SSSSLUMBER", "IIIII SHALL CONSSSSUME", "IIIII SHALL DEVOUUUUURRRRR", "LIFFFFFFE MUSSSSST PERISHHHHH", "NNNNNNNNURISHMENT", "ALL SHALLLLLLL GO INSSSSSSANE", "SSSSSSANITY SHALL YIELDDDDD", "EXXXXXILED I WASSSSS", "EONSSSSS I HAVE SLUMBERED", "EONSSSSS I HAVE WAITED", "MORTALSSSSSS BEHOLDDDDD", "I COMMMMME FROM DEEP", "IMMMMMMOBILE I WATCHHHH", "SSSSSKITTER", "HHHHHHHEY HOW YOU DOIN'", "AWKWAAAAAAAAARD"]);

new Thing("space animal",["space animal thoughts,85%", "space animal body"],[["e", "a", "o", "", "", "", "", "", ""], ["sm", "cr", "shn", "sh", "sn", "gl", "g", "m", "c", "x", "h", "dr", "r", "l"], ["o", "a", "u", "i", "e", "ee"], ["x", "b", "rv", "z", "s", "gg", "g", "k", "rf", "gl", "bl", "th", "kt", "m", "sh", "l", "dr", "v", "p", "nt", "nk"], ["o", "a", "i", "u", "e"], ["n", "ne", "se", "b", "m", "l", "s", "sh", "th", "t", "sk", "zer", "bbler", "ggler", "ddler", "ter", "nt", "r", "r", "r"]]);
new Thing("space animal body",[["tentacle,0-6", "crustacean leg,0-8", "fish fin,0-4", "mammal leg,1-6", "", ""], ["insect wing,0-6", "", ""], ["crustacean claw,0-4", "", ""], "flesh,40%", "snout,3%", "stinger,10%", "whiskers,3%", ["crustacean shell", "scales", "fur", "exoskeleton", ""], ["mouth,1-4", "beak,1-4", ""], "skull,30%", "brain,50%", ["eye,1-2", "eye,1-6", "simple eye,1-6", ""], "weird soft organ,50%", "weird soft organ,20%", "weird hard organ,50%", "weird hard organ,20%"],["body"]);
new Thing("space animal thoughts",["space animal thought,1-3"],["thoughts"]);
new Thing("space animal thought",[],[["sk'", "mop", "nanu", "nug", "gmap", "shmu", "dna", "no", "xle", "doda", "daia", "de", ""], ["g ", "gek ", "th ", "iap ", "glib ", "ph ", "d't ", "neig'", "dip ", "shna ", "sh "], ["sk'", "mop", "nanu", "nug", "gmap", "shmu", "dna", "no", "xle", "doda", "daia", "de", ""], ["g ", "gek ", "th ", "iap ", "glib ", "ph ", "d't ", "neig'", "dip ", "shna ", "sh "], ["mi", "di", "glu", "dra", "shwa", "ama", ""], ["ben", "ri", "nap", "dap", "top", "gog"], [".", ".", ".", ".", "!", "?"]]);

new Thing("can of nightmare",["space animal,4-12", "sea monster,2-6", "space monster,2-6"]);
//do not open

//amphibians
new Thing("amphibian",["reptile body", "amphibian thoughts"],["frog", "bull frog", "poison frog", "treefrog", "golden toad", "toad", "newt", "salamander", "caecilian", "axolotl"]);
new Thing("amphibian thoughts",["amphibian thought,1-2"],["thoughts"]);
new Thing("amphibian thought",[],["h-here i go", "r-ribbit?", "anyone?", "heyyy", "helloooo", "ribbity", "croak", "hello my baby", "hello my honey", "how do you do this", "i'm kinda newt to this", "well", "okay", "alright...", "why frog do that", "toadally"]);

//reptiles
new Thing("reptile",["reptile body", "reptile thoughts"],["snapping turtle", "sea turtle", "turtle", "tortoise", "chameleon", "gecko", "iguana", "lizard", "skink", "monitor lizard", "goanna", "crocodile", "alligator", "gavial", "caiman", "komodo dragon"]);
new Thing("snake",["snake body", "reptile thoughts"],["boa", "coral snake", "snake", "sea snake", "mamba", "viper", "adder", "python"]);
new Thing("reptile thoughts",["reptile thought,1-2"],["thoughts"]);
new Thing("reptile thought",[],["hhhehehe", "hehu", "haheha", "hehuheheho", "hohohohe", "i cant breathe", "hue", "br", "brbrbrbrbrbrbrbr", "gib fud pls", "pls", "r u a lizard", "ehuehuehu", "hey", "k", "sss", "ssssssss", "hiss etc", "ey", "ay", "ey bb", "u wot m8", "aeiou", "john madden", "ereptile dysfunction", "confirmed for br", "i joke bb", "i tease bcuz i care", "r u 4 real", "i swr m8", "ill bop u 1", "let's see if you fit in my mouth", "wink, wink", "but for real tho im absolutely terrified right now", "your skin so soft so nice mmh can i wear it", "damn right", "yes indeed... yes indeed", "let's shed light on this mystery", "pabongles", "bachinkles", "zabinga", "wapingles", "mmh", "body massage"]);

//dinosaurs yes
new Thing("dinosaur",["reptile body", "dinosaur thoughts"],["ankylosaur", "triceratops", "protoceratops", "pentaceratops", "stegosaur", "hadrosaur", "iguanodon", "pachycephalosaur", "sauropod", "raptor", "velociraptor", "deinonychus", "brachiosaur", "apatosaur", "therizinosaur", "theropod", "titanosaur", "tyrannosaur", "diplodocus", "allosaur", "ceratosaur", "dimetrodon", "pterosaur"]);
new Thing("dinosaur thoughts",["dinosaur thought,1-2"],["thoughts"]);
new Thing("dinosaur thought",[],["Dinner. Served.", "End. Near.", "Protect. Eggs.", "Food. Must find.", "Need food. Badly.", "Scared. Hunted.", "Things. Beneath.", "Chase. Run.", "Food. Nearby.", "Sky. Dark.", "Limbs. Aching.", "Mind. Numb.", "Ground. Shaking.", "Over. Soon.", "Offspring. Safety.", "Skin. Burning.", "Hostile. Nearby.", "Must. Go on.", "Must. Remember.", "Pack. Lost?", "Family. Where?"]);

//dragons why not
new Thing("dragon",["dragon body", "dragon thoughts"],[["fire", "ice", "forst", "arcane", "ancient", "wise", "guardian", "copper", "bronze", "steel", "obsidian", "gem", "undead", "skeletal", "sea", "sky", "cloud", "green", "red", "white", "golden", "silver", "chrome", "rainbow", "mist", "mother"], [" "], ["dragon", "wyrm", "wyvern", "guivre"]]);
new Thing("dragon thoughts",["dragon thought,1-2"],["thoughts"]);
new Thing("dragon thought",[],["You shouldn't be here.", "Leave. Now.", "You need to leave.", "Well well well. What do we have here?", "I will make quick work of you.", "You smell like food. Are you food?", "I will eat your mind before I eat your body.", "You'll be dead before you realize what's happening to you.", "They... they took my egg...", "My treasure. Must protect my treasure!", "I guard, undisturbed.", "I'm older than most of these mountains.", "I've seen things you wouldn't believe.", "Leave at once, mortal.", "Turn back if you value your life.", "Act with great care now, for this is the very last thing you'll ever do.", "Knights in armor cook just like canned beans.", "People seem to value treasure more than their own life.", "There's no honor, no valor nowadays.", "I'm on fire today.", "Ooooh burn."]);
new Thing("dragon body",["reptile head", "pyrolith", "scales", "reptile leg,4", ["reptile wing,2", ""], "tail", "flesh"],"body");
new Thing("pyrolith",[,
    RockFactory.one(),
    ]);
new Thing("dragon lair",["dragon,98%", "medieval servant,10%", "dragon nest,40%", "pile of treasure,90%", "medieval corpse,0-3"]);
new Thing("dragon nest",["egg shell,20%", "dragon egg,0-3", "pile of treasure"]);
new Thing("dragon egg",["egg thoughts", "egg shell", "soft flesh",
    OrganicFactory.one(),
],"dragon egg");

//birds
new Thing("bird",["bird body", "bird thoughts"],["pigeon", "starling", "swallow", "robin", "sparrow", "eagle", "vulture", "hawk", "condor", "osprey", "buzzard", "crane", "bustard", "pheasant", "woodpecker", "seagull", "albatross", "petrel", "grebe", "flamingo", "stork", "ibis", "heron", "swan", "magpie", "crow", "raven", "jay", "chough", "quail", "grouse", "partridge", "egret", "pelican", "cormorant", "avocet", "lapwing", "plover", "curlew", "gull", "tern", "skua", "guillemot", "auk", "sandgrouse", "dove", "parrot", "lorikeet", "cockatoo", "parakeet", "macaw", "turaco", "cuckoo", "coucal", "owl", "snowy owl", "frogmouth", "nightjar", "swift", "hummingbird", "quetzal", "toucan", "shrike", "wren", "oriole", "fantail", "paradise bird", "lark", "skylark", "warbler", "babbler", "thrasher", "mockingbird", "lyrebird", "bluebird", "thrush", "nightingale", "sunbird", "finch", "kingfisher", "trogon", "pitta", "manakin", "chickadee", "sula"]);
//not putting in tits or boobies
new Thing("poultry",["bird body", "poultry thoughts"],["chicken", "chicken", "chicken", "duck", "duck", "mallard", "goose", "goose", "turkey", "kiwi", "penguin", "ostrich", "emu", "cassowary"]);
//All flightless birds are considered poultry. Penguins and kiwis in farms. LIKE I CARE
new Thing("bird thoughts",["bird thought,1-2"],["thoughts"]);
new Thing("bird thought",[],["caw", "caw caw", ":V", ":V caw", "you think i care", "yeah bring it", "like for real", "come say that to my face", "chirp", "so high right now", "pooping on people, from far above, doop-dee-doop", "do i care, no i don't, doop-dee-doop", "me and my mates are gonna ruin your day", "can i peck your face", "please can i peck at you just a bit", "everything i sing is super-lewd", "i'm a lewd dude", "so yeah", "i am bird hi", "i'm pretty fly", "hey can i steal that", "what now", "that's not what your mom said last night", "yes that's right", "yes indeed", "see what happens", "oh god what happen", "riveting", "aw yiss", "bred crums yisss", "i am the birdest", "bird and bird accessories", "hey have you heard", "turns out i'm the word"]);
new Thing("poultry thoughts",["poultry thought,1-2"],["thoughts"]);
new Thing("poultry thought",[],["cluck", "bwucluck", ":U", ":U cluck", "i'm gonna strut around a bit while bobbing my head like that", "i got weird feet why", "you think i care", "like for real", "yeah bring it", "come say that to my face", "why do i poop on my feet", "oh my god i have the best voice", "i'm like super-good at songs okay", "let me sing you something plz", "so yeah", "i am bird hi", "this is most fowl", "yeah i got laid when i was born, what now gurl", "what now", "that's not what your mom said last night", "yes that's right", "yes indeed", "see what happens", "oh god what happen", "riveting", "aw yiss", "bred crums yisss", "i am the birdest", "bird and bird accessories", "hey have you heard", "turns out i'm the word"]);
new Thing("bird egg",["egg thoughts", "egg shell", "soft flesh",
    OrganicFactory.one(),
],"egg");
new Thing("egg shell",[
    ELEMENTS['Ca'].one(),
],"shell");
new Thing("egg thoughts",["egg thought"],"thought");
new Thing("egg thought",[],[["...", "...", "...", "...", "I...", "the...", "a...", "ah..."]]);

//mammals

new Thing("small mammal",["mammal body", "small mammal thoughts"],["squirrel", "rat", "mouse", "dormouse", "sugar glider", "flying squirrel", "possum", "lemur", "weasel", "ferret", "groundhog", "rabbit", "hare", "vole", "hedgehog", "shrew", "bat", "fruit bat", "pipistrelle", "stoat", "polecat", "raccoon", "badger", "honey badger", "otter", "civet", "koala", "mongoose", "mink", "mole", "molerat", "loris", "sloth", "aye-aye", "prairie dog", "chipmunk", "gerbil", "chinchilla"]);
new Thing("small mammal thoughts",["small mammal thought,2-3"],["thoughts"]);
new Thing("small mammal thought",[],["Hunted.", "Somewhere to hide. Now.", "Now is not the time.", "I need shelter.", "I need to burrow somewhere.", "This is not good.", "I am being stalked.", "Something's chasing me.", "Don't turn around.", "Just keep running.", "I need to collect more food.", "I'll never get enough food at this rate.", "I need to find a mate.", "I want offspring.", "I can't stay here.", "I think I saw something move.", "The hunt is on.", "This scent is familiar.", "I smell food.", "This scent is no good.", "This smells dangerous.", "I need to hurry.", "I'm starving.", "I'm tired.", "I'm cold.", "I'm scared."]);

new Thing("herbivorous mammal",["mammal body", "herbivorous mammal thoughts"],["ox", "buffalo", "antelope", "impala", "gazelle", "wild horse", "zebra", "giraffe", "ram", "goat", "yak", "ibex", "llama", "alpaca", "elephant", "rhinoceros", "deer", "moose", "elk", "kangaroo", "walabi"]);
new Thing("predatory mammal",["mammal body", "predatory mammal thoughts"],["fox", "jackal", "boar", "wolf", "hyena", "lynx", "lion", "leopard", "panther", "tiger", "dropbear"]);
new Thing("bear",["mammal body", "bear thoughts"],["bear", "brown bear", "polar bear", "grizzly", "panda"]);

new Thing("herbivorous mammal thoughts",["herbivorous mammal thought,1-3"],["thoughts"]);
new Thing("herbivorous mammal thought",[],["Hunted.", "Somewhere to hide. Now.", "Now is not the time.", "I need shelter.", "I need to hide somewhere.", "This is not good.", "I am being stalked.", "Something's chasing me.", "Don't turn around.", "Just keep running.", "I need food badly.", "I need to find a mate.", "I want offspring.", "I can't stay here.", "I think I saw something move.", "This scent is familiar.", "I smell food.", "This scent is no good.", "This smells dangerous.", "I need to hurry.", "I'm starving.", "I'm tired.", "I'm cold.", "I'm scared."]);

new Thing("predatory mammal thoughts",["predatory mammal thought,1-3"],["thoughts"]);
new Thing("predatory mammal thought",[],["Busy. Hunting.", "Now is not the time.", "I need shelter.", "This is not good.", "It grazes, oblivious to my presence.", "So nimble on its feet.", "Yes. It grazes so peacefully.", "It grazes so calmly.", "All is quiet.", "Why is it in such a hurry?", "Aah. Delicious, mindless meat.", "I've been stalking this meat for days. I won't give up.", "So swift is the meat.", "I will toy with the meat and then I will devour it.", "The meat is going scarce.", "Just as planned.", "Something is scaring the meat away.", "Do I smell meat?", "Graceful, delicious meat.", "I smell something. It's not meat.", "Something is approaching.", "There is something bigger than me.", "You think you can outrun me?", "Prey or be preyed upon.", "Eat. Prey. Eat some more.", "Meat awaits.", "Don't turn around.", "Run. Run for the meat.", "I need food badly.", "I need to find a mate.", "I want offspring.", "I don't beat my meat. I just tear it to pieces.", "I can't stay here.", "I'm bigger than you.", "This scent is familiar.", "I smell meat.", "This scent is no good.", "This smells dangerous.", "I need to hurry.", "I'm starving.", "I'm tired.", "I'm cold.", "I'm scared."]);

new Thing("bear thoughts",["bear thought,1-3"],["thoughts"]);
new Thing("bear thought",[],["I WOULD LIKE TO ENQUIRE ABOUT YOUR FOOD", "EXCUSE ME GOOD SIR, WOULD YOU HAPPEN TO BE EDIBLE", "I'LL SAY", "THIS IS NOT PROPER ETIQUETTE", "MAY I ENQUIRE ABOUT YOUR EDIBILITY", "ARE YOU ONE OF THOSE EDIBLE FELLOWS", "WOULD YOU SAVE BOTH OF US THE TROUBLE AND JUST HOP INTO MY MOUTH", "WHY WOULD YOU DO THAT", "YES QUITE", "YES INDEED", "THOUGHTS ARE BETTER CONVEYED BY THINKING THEM EXTRA-LOUDLY", "IT WOULD APPEAR SO", "YES I AM QUITE DAPPER", "WHAT WILL IT BE OLD CHAP", "WELL AREN'T YOU A DELICIOUS LITTLE CHAP", "SUCH PLEBEIAN UNDERTAKINGS", "SUCH GLORIOUS VERBOSITY", "HOLD ON TO THAT THOUGHT", "HOLD ON I NEED TO STUFF MY FACE INSIDE A BEEHIVE BECAUSE I'M HARDCORE LIKE THAT", "DEM BEES MAN", "OKAY WHAT", "SHHH ONLY SLEEP NOW", "IT'S A SECRET TO EVERYBODY", "I CERTAINLY DON'T MIND SOME SQUIRMING MEAT", "YEAH NOT GOING TO RANT ABOUT FOOD", "HELLO THERE TASTY", "I DARE YOU MAN", "WELL THIS IS JUST SILLY", "I'M SECRETELY A HUMAN"]);

new Thing("horse",["mammal body", "horse thoughts"],["horse"]);
new Thing("horse thoughts",["horse thought,1-3"],["thoughts"]);
new Thing("horse thought",[],["oh", "oh god", "what does it mean", "it's all around", "why", "I don't understand", "oh god what is that", "oh my god", "oh dear god", "it's so intense", "it's so beautiful", "this is everything I've ever wanted", "this exceeds all my expectations", "this is better than everything ever", "how did I even get here son", "whoah", "I just", "mom where are you", "let's just", "...whoah", "look at me, I'm amazing", "give me a lick", "sweet lemonade", "not walking into bars again", "all those colors", "I can taste the colors", "the universe tastes amazing", "is this real life", "I can't even", "I can't breathe help", "that's the best thing I've ever heard", "so then why the long face? because it's melting. my face is melting", "why this", "I am everything", "I am forever", "I can't even begin to"]);

new Thing("monkey",["mammal body", "monkey thoughts"],["macaque", "chimpanzee", "gorilla", "bonobo", "orangutan", "howler monkey", "capuchin monkey", "spider monkey"]);
new Thing("monkey thoughts",["monkey thought,2-3"],["thoughts"]);
new Thing("monkey thought",[],["I need grooming. Anyone?", "Oh yeah, that's the spot.", "Oh god. The itch.", "Yes. I'm a monkey. How are you.", "How insensitive of you.", "Look what I can do!", "Oh hey, look what I found!", "Don't make me fling it.", "Hey. Pull my finger.", "Man, you keep delicious things in your fur.", "Am I smelling what I think I'm smelling?", "Mind if I sit on you?", "You don't know where that finger has been.", "A stick, a rock, technology!", "This is the last time I raid an anthill.", "I don't feel like I'm being taken seriously here.", "Do everything they do. That'll do the trick.", "Do I smell... coconut?", "Can I eat the skin of your face just a little? No? Okay, just making sure.", "I could make tools or whatever too, I just don't feel like it."]);

new Thing("cat",["mammal body", "cat thoughts"],[["fat", "obese", "skinny", "fluffy", "calm", "collected", "meditative", "wistful", "quiet", "purring", "meowing"], [" "], ["tabby", "calico", "striped", "spotted", "black", "grey", "white", "brown", "orange"], [" "], ["cat", "kitten"]]);
//[["bobtail","abyssinian","balinese","birman","bombay","burmese","chartreux","devon rex","domestic","maine coon","manx","munchkin","oriental","persian","ragamuffin","scottish fold","siamese","sphynx","longhaired","shorthaired","bald","fluffy","obese","white","black","tabby","calico"],[" cat"," kitten"]]);
new Thing("cat thoughts",["cat thought,1-2"],["thoughts"]);
new Thing("cat thought",[],[["meow meow meow meow", "we must abolish", "we cannot tolerate", "I have predicted", "as I have predicted", "children will be blessed", "we are being lied to", "they do not fool me", "the dirty lying teachers say", "soon it will end", "adults eat teenagers alive", "try my belly-button logic", "fraudulent oneness", "vilify teachers", "nothing more evil than cat educated as 1", "safely remove parasites and their eggs", "this is some good catnip", "hey everybody", "4 harmonic corner days rotate simultaneously around squared equator", "chapstick chapstick fffshh", "wake up sheeple", "false prophet", "sanity preserve sanity", "come to daddy", "is it time for", "when will it be when", "What is this place? Where am", "proceed now to", "in the next chapter I explain how", "and this is how", "complete with", "if it fits", "if you order now", "oh no it's happening agai-", "one does not simply", "I'm so much better off without my meds", "Did you know?", "I can haz", "and that is how I met your", "thoughtform of cat coevaluates thoughtform of dog"], [" "], ["MEOW MEOW MEOW MEOW", "PURR PURR PURR", "THE VERY FACE OF TIME", "I FEEL THEM IN MY BRAIN", "THE INITIAL MOVEMENT", "MUST CHANGE THE HOLY BOOK", "BURN THE OLD WORLD METHODS", "BREATHE THE CONTINUUM", "QUANTUM DEMOGRAPHICS", "EVIL OF PERSON FROM ANCESTORS", "THE SON AND FATHER", "THIS PROVES EVERY BELIEVER A LIAR", "EVIL OF QUADRANTS", "THE BLOOD OF THE IMPURE", "SUPPORTERS OF LIES", "SUFFERING OF CHILDREN", "NO GOD KNOWS ABOUT 4 DAYS", "4 SIMULTANEOUS DAYS", "4 CORNER DAYS PROVES 1 DAY 1 GOD IS TAUGHT EVIL", "IGNORANCE OF CAT SIMPLE MATH IS RETARDATION", "THE ONENESS OF GOD IS STILLNESS DEATH", "LOVE OF GOD IS HATE OF CHILDREN", "DOES YOUR TEACHER KNOW?", "2 HALF 4 SELF", "1 DAY GOD WAS WRONG", "ALL HAIL CAT", "NOT GOD NOT GOD FSHHHH", "THE BODY, THE BODY OF THE LORD", "CORPSES TO CORPSES", "UNACCEPTABLE", "MUST SURRENDER", "CATNIP FOR THE CAT GOD", "MORE LITTER FOR THE LITTER-THRONE", "LITTERALLY", "4 CORNERS MAKES THE WORLD GO ROUND ROUND ROUND", "CUBES ALL THE WAY DOWN", "QUADRANTS EVERYWHERE", "ONE OF ITS SIXTY-THOUSAND NAMES", "DO NOT TOUCH THE THETANS", "PUNCH MY FACE IN", "HELP I AM STUCK IN CAT BODY", "I TOLD YOU ABOUT QUADRANTS BRO", "SURRENDER NOW AND YOU MAY EARN THE PRIVILEGE OF BEING EATEN FIRST", "QUALITY STUFF", "THE SWINE MUST PAY", "SO HARDCORE", "OH LONG JOHNSON", "I WILL EAT YOUR SOUL", "THEY WILL PAY WITH BLOOD", "HE COMES"], [" "], ["meow meow meow meow", "meow", "meow purr", "of new world order", "of the seven coordinates", "now, lick me", "into new order", "for glorious sacrament", "practicing evil", "navel connects 4 corner 4s", "world will stay the same", "lie that corrupts the planet", "you educated stupid fools", "but it was all joke", "it is evil to ignore 4 days", "deserve to be spit upon publicly", "chunky peanut butter", "directly to forehead", "spoke to my brain", "wrote a book about it", "and it's free", "proven clinically", "immediate results", "created all of them", "has retarded your opposite rationale brain to a half brain slave", "and evil education damnation", "just a hoax", "just a theory", "and shall be exterminated", "not very raven", "would you like to know more", "cat cat cat cat cat cat cat", "I'm a kitty-cat", "and I dance dance dance and I dance dance dance", "nyan", "interwebz", "series of tubes", "whoah what just happened", "mondays", "(this is what cats actually believe)", "church was full of liars", "support cat or be cursed", "or is it?", "copyright fshh fshhh"]]);
//new Thing("cat thought",[],["Meow meow meow meow, meow meow meow meow, meow meow meow meow meow meow meow meow","I'm like, so offended right now?","That's, like, not tasteful at all?","So triggered right now.","Yes. Well. It takes one to know one.","Yeah well. You know what they say.","Uhm, like, hello?","What am I looking at exactly.","That is SO inappropriate.","Uhm, duh? How else would I clean my butthole?","Uhm, not funny."]);//snooty teenager? not very funny

new Thing("dog",["mammal body", "dog thoughts"],[["tall", "huge", "tiny", "ridiculously small", "comically small", "enormous", "monstrous", "fluffy", "obese", "malnourished", "fat", "skinny", "slender", "curly", "hairy", "hairless", "sort-haired", "long-haired", "puffy", "happy", "excited", "friendly", "ridiculous-looking", "barking", "panting"], [" "], ["yellow", "gold", "cream", "white", "grey", "black", "orange", "red", "brown", "spotted", "black and tan", "two-color", "tricolor"], [" "], ["dog", "puppy", "lapdog", "hound"]]);
//[["inu","terrier","malamute","bulldog","spaniel","foxhound","pit bull terrier","mastiff","shepherd","basset","beagle","berger","bichon","collie","boxer","chihuahua","chow chow","dachshund","dalmatian","cocker","coonhound","setter","mountain","spitz","retriever","dane","labrador","husky","maltese","pekingese","pomeranian","poodle","labradoodle","pug","rottweiler","shih tzu"],[" dog"," puppy"]]);
//Wrote all these names and realized it wasn't very funny, plus too many location names for my liking. Ah well.
new Thing("dog thoughts",["dog thought,2-3"],["thoughts"]);
new Thing("dog thought",[],["HAY I'M DOG", "I AM DOG HAY", "WE DOG NOW???", "HEY LET'S DOG OK???", "CAN WE DOG NOW OK???", "DOG STUFF YAYYYYY", "BUTTS COME IN MANY FLAVORS", "BUTTS YES", "HURRAY!!!!!!!! BUTTS", "YOUR BUTT SMELLS LEGIT", "WOOF", "BWURF", "BAWF WOOF", "GUESS WHAT?????????? WOOF", "MY SPECIALTY. IS ROOFING.", "HEY EVERYDOGGY", "DOG DOG DOG DOG DOG DOG DOG", "MY NAME. IS DOG. AND I HAVE MET YOU. HI!!!", "!!!!!!!!!!!!!!!!!!!!!WHOAH", "!!!!!!!!!YES NICE", "EVERYTHING SO NICE WOW", "WE GO MANGLE SQUIRREL NOW????? PLS", "WOW!!!!!!!! SO EXCITE", "I'M RLY EXCITE RIGHT NOW", "DO YOU KNOW JUST HOW EXCITE I AM", "DO YOU HAVE. ANY IDEA. JUST HOW EXCITE I AM.", "A WALK????? YES WALK LOVE WALKS HURRAY!!!!!!", "PEE ON THINGS HURRAY!!!!!!", "YIP YIP YIP YIP YIP", "YIP", "I COULD GO FOR SOME SQUIRREL RIGHT ABOUT NOW", "IF TEARING UP SQUIRRELS IS WRONG THEN WOOF WOOF WOOF WOOF WOOF WOOF WOOF", "DOG??????????? DOG", "I LICK YOUR FACE NOW OK???????", "VERI GOOD :DDDDDDDD", "I WAS RUNNING BUT I FORGOT WHY I WAS RUNNING SO THEN I STOPPED RUNNING AND NOW I AM NOT RUNNING ANYMORE.", "I DON'T UNDERSTAND!!!!! BUT OK", "UH", "HELP I AM CHOKE ON SQUIRREL HELP", "ARE YOU A SQUIRREL", "NO WAY", "DUDE THERE IS NO WAY", "IS THAT, UH, OH NEVERMIND", "OHNO WHY", "MEOW I MEAN WOOF????? YES", "All of this must of course remain absolutely confidenOH HEY WOOF WOOF WOOF", "I AM THE DOGGEST", "MORE DOG YES DOG", "LESS CAT MORE DOG", "HAHA I LOVE YOU", "ONE DAY I WAKE UP AND I AM DOG WOW", "IS THIS REAL LIFE", "I AM SO DOG RIGHT NOW", "WOW", "WHY THIS", "THIS IS GREAT"]);
"""
