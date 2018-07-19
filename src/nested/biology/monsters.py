from ..thing import Thing
from ..children import ChildGenerator


# new Thing("sea monster",["sea monster thoughts",["tentacle,0-6","fish fin,0-4","",""],"stinger,20%",["crustacean claw,0-4",""],["crustacean leg,0-8",""],["crustacean shell","scales","fur","exoskeleton",""],["mouth,1-2","beak,1-2"],"skull,80%",["eye,1-8","simple eye,1-8","",""],"weird soft organ,0-4","weird hard organ,0-4"],[["giant","timeless","colossal","abyssal","forgotten","ancient","gigantic","monstrous"],[" "],["craze","drift","dredge","dread","slumber","dream","wander","frost","magma","stone","slime","ooze","egg","larva","grudge","stride","flail","wail","time","star","crystal","terror","horror","scream","wrath","burst","dark","deep","tickle"],["fin","tail","sinker","sunk","singer","song","polyp","rifter","glider","squirmer","titan","colossus","brain","queen","king","child","guardian","seer","whale","worm","spider","crab","leech","fish","shark","squid","saur","buddy","lord"]]);
# new Thing("sea monster thoughts",["sea monster thought,1-2"],["thoughts"]);
# new Thing("sea monster thought",[],["IIIIII MUSSST SCREEEAAAM","I AMMMM AWAKENED","ALLLLLL FEAR MEEEEE","NOOOOONE SHALL LIVE","I MUSSSSST EATTTTT","DEEEEEEEEP I SSSSLUMBER","IIIII SHALL CONSSSSUME","IIIII SHALL DEVOUUUUURRRRR","LIFFFFFFE MUSSSSST PERISHHHHH","NNNNNNNNURISHMENT","ALL SHALLLLLLL GO INSSSSSSANE","SSSSSSANITY SHALL YIELDDDDD","EXXXXXILED I WASSSSS","EONSSSSS I HAVE SLUMBERED","EONSSSSS I HAVE WAITED","MORTALSSSSSS BEHOLDDDDD","I COMMMMME FROM DEEP","IMMMMMMOBILE I WATCHHHH","SSSSSKITTER","THEY FFFFFLOAAAAAT"]);


class SpaceMonster(Thing):
    type_name = "space monster"
    child_generators = [
        ChildGenerator("space monster thoughts"),
        [
            ChildGenerator("tentacle", (0, 6)),
            ChildGenerator("fish fin", (0, 4)),
            ChildGenerator(),
            ChildGenerator(),
        ],
        ChildGenerator("stinger", probability=20),
        [
            ChildGenerator("crustacean claw", (0, 4)),
            ChildGenerator(),
        ],
        [
            ChildGenerator("crustacean leg", (0, 8)),
            ChildGenerator()
        ],
        [
            ChildGenerator("crustacean shell"),
            ChildGenerator("scales"),
            ChildGenerator("fur"),
            ChildGenerator("exoskeleton"),
            ChildGenerator(),
        ],
        [
            ChildGenerator("mouth", (1, 2)),
            ChildGenerator("beak", (1, 2))
        ],
        ChildGenerator("skull", probability=80),
        [
            ChildGenerator("eye", (1, 8)),
            ChildGenerator("simple eye", (1, 8)),
            ChildGenerator(),
            ChildGenerator()
        ],
        ChildGenerator("weird soft organ", (0, 4)),
        ChildGenerator("weird hard organ", (0, 4)),
    ]
    names_data = [
        ["C'","Vr'","Ksh","Zn'","Sh","Hrl","X","O","Yog","Gorg","Morg","Marg","Magg"],
        ["","","agn","soth","norgn","ngas","alx","orx","rgl","iirn","egw","thulh","t","g","m"],
        ["org","orgon","orgus","orkus","oid","us","u","esth","ath","oth","um","ott","aur"],
        [""," the Forgotten"," the Entity"," the Ancient"," the Starchild"," the Seeder"," the Leech"," the Timeless"," the Eon"," the Many"," the Countless"," the Boundless"," the Prisoner"," the Child"," the Form"," the Shape"," the Drifter"," the Swarm"," the Vicious"," the Warden"," the Ender"," the Unworldly"," the Unfriendly"," the All-Consumer"]
    ]


class SpaceMonsterThoughts(Thing):
    type_name = "space monster thoughts"
    child_generators = [ChildGenerator("space monster thought", (1, 2))]
    names_data = ["thoughts"]


class SpaceMonsterThought(Thing):
    type_name = "space monster thought"
    names_data = [
        "WWWWWWWIDER THAN STARRRRRRS",
        "AWAKENNNN MY CHILDRENNNNNN",
        "GALAXIESSSSS SHALL FALLLLLLL",
        "I AMMMMMM INFFFFFINITE",
        "I SSSSSSSPAN AGESSSS",
        "WWWWWWEEEEE ARE UNDYINGGGGGG",
        "WE COMMMMMMMME",
        "WE ANSSSSSWER THE CALLLLLLL",
        "I TRAVELLLLLLL SLLLLLLUMBERING",
        "FROMMMMMM FARRRRRR I COMMMME",
        "IIIIII MUSSST SCREEEAAAM",
        "I AMMMM AWAKENED",
        "ALLLLLL FEAR MEEEEE",
        "NOOOOONE SHALL LIVE",
        "I MUSSSSST EATTTTT",
        "DEEEEEEEEP I SSSSLUMBER",
        "IIIII SHALL CONSSSSUME",
        "IIIII SHALL DEVOUUUUURRRRR",
        "LIFFFFFFE MUSSSSST PERISHHHHH",
        "NNNNNNNNURISHMENT",
        "ALL SHALLLLLLL GO INSSSSSSANE",
        "SSSSSSANITY SHALL YIELDDDDD",
        "EXXXXXILED I WASSSSS",
        "EONSSSSS I HAVE SLUMBERED",
        "EONSSSSS I HAVE WAITED",
        "MORTALSSSSSS BEHOLDDDDD",
        "I COMMMMME FROM DEEP",
        "IMMMMMMOBILE I WATCHHHH",
        "SSSSSKITTER",
        "HHHHHHHEY HOW YOU DOIN'",
        "AWKWAAAAAAAAARD"
    ]


class SpaceAnimal(Thing):
    type_name = "space animal"
    child_generators = [
        ChildGenerator("space animal thoughts", probability=85),
        ChildGenerator("space animal body"),
    ]
    names_data = [
        ["e", "a", "o", "", "", "", "", "", ""],
        ["sm", "cr", "shn", "sh", "sn", "gl", "g", "m", "c", "x", "h", "dr", "r", "l"],
        ["o", "a", "u", "i", "e", "ee"],
        ["x", "b", "rv", "z", "s", "gg", "g", "k", "rf", "gl", "bl", "th", "kt", "m", "sh", "l", "dr", "v", "p", "nt","nk"],
        ["o", "a", "i", "u", "e"],
        ["n", "ne", "se", "b", "m", "l", "s", "sh", "th", "t", "sk", "zer", "bbler", "ggler", "ddler", "ter", "nt", "r","r","r"],
    ]


class SpaceAnimalBody(Thing):
    type_name = "space animal body"
    child_generators = [
        [
            ChildGenerator("tentacle", (0, 6)),
            ChildGenerator("crustacean leg", (0, 8)),
            ChildGenerator("fish fin", (0, 4)),
            ChildGenerator("mammal leg", (1, 6)),
            ChildGenerator(),
            ChildGenerator(),
        ],
        [
            ChildGenerator("insect wing", (0, 6)),
            ChildGenerator(),
            ChildGenerator(),
        ],
        [
            ChildGenerator("crustacean claw", (0, 4)),
            ChildGenerator(),
            ChildGenerator(),
        ],
        ChildGenerator("flesh", probability=40),
        ChildGenerator("snout", probability=3),
        ChildGenerator("stinger", probability=10),
        ChildGenerator("whiskers", probability=10),
        [
            ChildGenerator("crustacean shell"),
            ChildGenerator("scales"),
            ChildGenerator("fur"),
            ChildGenerator("exoskeleton"),
            ChildGenerator(),
        ],
        [
            ChildGenerator("mouth", (1, 4)),
            ChildGenerator("beak", (1, 4)),
            ChildGenerator(),
        ],
        ChildGenerator("skull", probability=30),
        ChildGenerator("brain", probability=50),
        [
            ChildGenerator("eye", (1, 2)),
            ChildGenerator("eye", (1, 6)),
            ChildGenerator("simple eye", (1, 6)),
            ChildGenerator(),
        ],
        ChildGenerator("weird soft organ", probability=50),
        ChildGenerator("weird soft organ", probability=20),
        ChildGenerator("weird hard organ", probability=50),
        ChildGenerator("weird hard organ", probability=20),
    ]
    names_data = ["body"]


class SpaceAnimalThoughts(Thing):
    type_name = "space animal thoughts"
    child_generators = [ChildGenerator("space animal thought", (1, 3))]
    names_data = ["thoughts"]


class SpaceAnimalThought(Thing):
    type_name = "space animal thought"
    names_data = [
        ["sk'","mop","nanu","nug","gmap","shmu","dna","no","xle","doda","daia","de",""],["g ","gek ","th ","iap ","glib ","ph ","d't ","neig'","dip ","shna ","sh "],
        ["sk'","mop","nanu","nug","gmap","shmu","dna","no","xle","doda","daia","de",""],["g ","gek ","th ","iap ","glib ","ph ","d't ","neig'","dip ","shna ","sh "],
        ["mi","di","glu","dra","shwa","ama",""],["ben","ri","nap","dap","top","gog"],
        [".",".",".",".","!","?"],
    ]



# new Thing("can of nightmare",["space animal,4-12","sea monster,2-6","space monster,2-6"]);//do not open


CONTENTS = [
    SpaceMonster,
    SpaceMonsterThoughts,
    SpaceMonsterThought,
    SpaceAnimal,
    SpaceAnimalBody,
    SpaceAnimalThoughts,
    SpaceAnimalThought,
]
