from .thing import Thing
from .chemistry import CONTENTS as CHEMISTRY_CONTENTS
from .particles import CONTENTS as PARTICLES_CONTENTS
from .space import CONTENTS as SPACE_CONTENTS


THINGS = dict()


def addFromContents(content):
    for c in content:
        if isinstance(c, type):
            name = c.type_name
        else:
            name = c.name
        THINGS[name] = c()


def addThing(name, children, namegen=None):
    global THINGS
    THINGS[name] = Thing.from_str(name, children, namegen)


def get_thing(key):
    global THINGS
    return THINGS.get(key)


def clean_things():
    global THINGS
    for key, thing in THINGS.items():
        thing.clear()


def get_generators(thing_name):
    def dotted_generators(gen):
        sub_name = gen.value[1:]
        sub = get_thing(sub_name)
        return get_generators(sub_name)

    t = get_thing(thing_name)
    if t is None:
        return None
    to_concat = []
    generators = []
    for i, g in enumerate(t.generators):
        if not isinstance(g.value, str):
            generators.append(g)
            continue
        if g.value[0] == ".":
            sub = dotted_generators(g)
            if sub is not None:
                to_concat += sub
            # self.type.generators[i] = None
        else:
            generators.append(g)
    # return list(filter(lambda item: item is not None, self.type.generators + to_concat))
    return list(filter(lambda item: item is not None, generators + to_concat))


addThing("water",["hydrogen","oxygen"])
# addThing("fire",["oxygen","carbon"])
# addThing("ash",["organic matter","carbon"])
# addThing("dew",["water"])
# addThing("ice",["water"])
# addThing("snow",["snowflakes"])
# addThing("snowflakes",["water"])
addFromContents(CHEMISTRY_CONTENTS)
# alright, I'm not doing the whole periodic table.
# addThing("proteins",[".molecule"])
# addThing("lipids",[".molecule"])
# addThing("glucids",["carbon","hydrogen","oxygen"],"glucose")
# addThing("organic matter",[["proteins","lipids","glucids"],["proteins","lipids","glucids",""],"salt,30%"])

addFromContents(PARTICLES_CONTENTS)
# addThing("portal",["universe"])

# universe stuff
addFromContents(SPACE_CONTENTS)


addThing("black hole",["inside the black hole"])
addThing("inside the black hole",["end of universe note,0.5%","crustacean,0.2%","white hole"])
addThing("white hole",["universe"])

addThing("galactic life",["space monster,1%","space animal,1-12"],"life")

# monsters
addThing("space monster",["space monster thoughts",["tentacle,0-6","fish fin,0-4","",""],"stinger,20%",["crustacean claw,0-4",""],["crustacean leg,0-8",""],["crustacean shell","scales","fur","exoskeleton",""],["mouth,1-2","beak,1-2"],"skull,80%",["eye,1-8","simple eye,1-8","",""],"weird soft organ,0-4","weird hard organ,0-4"],[["C'","Vr'","Ksh","Zn'","Sh","Hrl","X","O","Yog","Gorg","Morg","Marg","Magg"],["","","agn","soth","norgn","ngas","alx","orx","rgl","iirn","egw","thulh","t","g","m"],["org","orgon","orgus","orkus","oid","us","u","esth","ath","oth","um","ott","aur"],[""," the Forgotten"," the Entity"," the Ancient"," the Starchild"," the Seeder"," the Leech"," the Timeless"," the Eon"," the Many"," the Countless"," the Boundless"," the Prisoner"," the Child"," the Form"," the Shape"," the Drifter"," the Swarm"," the Vicious"," the Warden"," the Ender"," the Unworldly"," the Unfriendly"," the All-Consumer"]])
addThing("space monster thoughts",["space monster thought,1-2"],["thoughts"])
addThing("space monster thought",[],["WWWWWWWIDER THAN STARRRRRRS","AWAKENNNN MY CHILDRENNNNNN","GALAXIESSSSS SHALL FALLLLLLL","I AMMMMMM INFFFFFINITE","I SSSSSSSPAN AGESSSS","WWWWWWEEEEE ARE UNDYINGGGGGG","WE COMMMMMMMME","WE ANSSSSSWER THE CALLLLLLL","I TRAVELLLLLLL SLLLLLLUMBERING","FROMMMMMM FARRRRRR I COMMMME","IIIIII MUSSST SCREEEAAAM","I AMMMM AWAKENED","ALLLLLL FEAR MEEEEE","NOOOOONE SHALL LIVE","I MUSSSSST EATTTTT","DEEEEEEEEP I SSSSLUMBER","IIIII SHALL CONSSSSUME","IIIII SHALL DEVOUUUUURRRRR","LIFFFFFFE MUSSSSST PERISHHHHH","NNNNNNNNURISHMENT","ALL SHALLLLLLL GO INSSSSSSANE","SSSSSSANITY SHALL YIELDDDDD","EXXXXXILED I WASSSSS","EONSSSSS I HAVE SLUMBERED","EONSSSSS I HAVE WAITED","MORTALSSSSSS BEHOLDDDDD","I COMMMMME FROM DEEP","IMMMMMMOBILE I WATCHHHH","SSSSSKITTER","HHHHHHHEY HOW YOU DOIN'","AWKWAAAAAAAAARD"])

addThing("ectoplasm",["proton,3-7"],[["purple","fetid","green","yellow","blood-red","shiny","wispy","sparkly"],[" "],["ectoplasm"]])
addThing("ghost",["ghost body","ghost thoughts"],[["depressed","sad","lonely","wailing","screaming","stretching","clinking","sneezing","breathing","screeching","spinning","gasping","moaning","regretful","remorseful","vengeful","friendly neighborhood","skeletal","tentacled","conjoined","grasping","slimy","floating","mournful"],[" "],["ghost","spirit","apparition","phantom","poltergeist","specter","hauntling"]])
addThing("ghost body",["ectoplasm"],["\"body\""])
addThing("ghost thoughts",["ghost thought","ghost thought,20%"],["thoughts"])
addThing("ghost thought",[],["if only - she could hear me -","he needs to know - I'm sorry -","alone - I - wait -","I am so - very lonely -","when - will it end -","will it be - over soon -","do I - deserve this -","I regret - so much -","I miss you - so much -","please - never - ever die -","I must - wait here -","how many - centuries -","such is - my burden -","I cannot - feel a thing -","I have lost - all hope -","abandoned -","I float - forever -","I wander - for how long -","so spooky - right now -","that slime - isn't mine -","I rest - at last -","let's - be pals -","I sense - a presence -","you can - see me?","who you - gonna call -","can you - hear me now -"])


# meta
addThing("later", ["sorry"], "will do later")
addThing("error", ["sorry"], "Uh oh... It looks like you didn't supply a valid element to create.")
addThing("sorry", ["consolation universe"], "(Sorry!)")
addThing("consolation universe", [".universe"])