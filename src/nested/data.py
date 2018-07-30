import random


from .thing import Thing
from .chemistry import CONTENTS as CHEMISTRY_CONTENTS
from .particles import CONTENTS as PARTICLES_CONTENTS
from .space import CONTENTS as SPACE_CONTENTS
from .biology.life import CONTENTS as LIFE_CONTENTS
from .biology.monsters import CONTENTS as MONSTERS_CONTENTS
from .terrain import CONTENTS as TERRAIN_CONTENTS
from .state import CONTENTS as STATE_CONTENTS
from .room import  CONTENTS as ROOM_CONTENTS

from .person import CONTENTS as PERSON_CONTENTS

from .medieval import CONTENTS as MEDIEVAL_CONTENTS


THINGS = dict()


def addFromContents(content):
    for c in content:
        i = c()
        THINGS[i.name] = i


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
        if isinstance(g, list):
            generators.append(random.choice(g))
            continue
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


addThing("diamond",["carbon"])
# new Thing("oil",["lipids"]);
addThing("magma",[".rock"])
addThing("rock",["silica","aluminium,30%","iron,20%","potassium,20%","sodium,50%","calcium,50%"])
addThing("silica",["silicon","oxygen"]);
# new Thing("chitin",["carbon","hydrogen","oxygen","nitrogen"]);
addThing("salt",["chlorine","sodium"])
addThing("water",["hydrogen","oxygen"])
# addThing("fire",["oxygen","carbon"])
# addThing("ash",["organic matter","carbon"])
# addThing("dew",["water"])
addThing("ice",["water"])
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

addFromContents(LIFE_CONTENTS)
addFromContents(TERRAIN_CONTENTS)
addFromContents(MONSTERS_CONTENTS)
addFromContents(STATE_CONTENTS)
addFromContents(ROOM_CONTENTS)
addFromContents(PERSON_CONTENTS)
addFromContents(MEDIEVAL_CONTENTS)


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

# for t in THINGS.items():
#     print(t)
# print(THINGS['universe'])