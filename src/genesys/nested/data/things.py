from ..factories import Things

from .chemistry import CONTENTS as CHEMISTRY_CONTENTS
from .particles import CONTENTS as PARTICLES_CONTENTS
from .space import CONTENTS as SPACE_CONTENTS
from .biology.life import CONTENTS as LIFE_CONTENTS
from .biology.monsters import CONTENTS as MONSTERS_CONTENTS
from .terrain import CONTENTS as TERRAIN_CONTENTS
from .state import CONTENTS as STATE_CONTENTS
from .room import CONTENTS as ROOM_CONTENTS
from .furniture import CONTENTS as FURNITURE_CONTENTS

from .person import CONTENTS as PERSON_CONTENTS

from .medieval import CONTENTS as MEDIEVAL_CONTENTS


Things.add_thing("diamond",["carbon"])
# new Thing("oil",["lipids"]);
Things.add_thing("magma",[".rock"])
Things.add_thing("rock",["silica","aluminium,30%","iron,20%","potassium,20%","sodium,50%","calcium,50%"])
Things.add_thing("silica",["silicon","oxygen"]);
# new Thing("chitin",["carbon","hydrogen","oxygen","nitrogen"]);
Things.add_thing("salt",["chlorine","sodium"])
Things.add_thing("water",["hydrogen","oxygen"])
# Things.add_thing("fire",["oxygen","carbon"])
# Things.add_thing("ash",["organic matter","carbon"])
# Things.add_thing("dew",["water"])
Things.add_thing("ice",["water"])
# Things.add_thing("snow",["snowflakes"])
# Things.add_thing("snowflakes",["water"])

Things.from_contents(CHEMISTRY_CONTENTS)
# alright, I'm not doing the whole periodic table.
# Things.add_thing("proteins",[".molecule"])
# Things.add_thing("lipids",[".molecule"])
# Things.add_thing("glucids",["carbon","hydrogen","oxygen"],"glucose")
# Things.add_thing("organic matter",[["proteins","lipids","glucids"],["proteins","lipids","glucids",""],"salt,30%"])

Things.from_contents(PARTICLES_CONTENTS)
# Things.add_thing("portal",["universe"])

# universe stuff
Things.from_contents(SPACE_CONTENTS)

Things.from_contents(LIFE_CONTENTS)
Things.from_contents(TERRAIN_CONTENTS)
Things.from_contents(MONSTERS_CONTENTS)
Things.from_contents(STATE_CONTENTS)
Things.from_contents(ROOM_CONTENTS)
Things.from_contents(PERSON_CONTENTS)
Things.from_contents(FURNITURE_CONTENTS)
Things.from_contents(MEDIEVAL_CONTENTS)


Things.add_thing("ectoplasm",["proton,3-7"],[["purple","fetid","green","yellow","blood-red","shiny","wispy","sparkly"],[" "],["ectoplasm"]])
Things.add_thing("ghost",["ghost body","ghost thoughts"],[["depressed","sad","lonely","wailing","screaming","stretching","clinking","sneezing","breathing","screeching","spinning","gasping","moaning","regretful","remorseful","vengeful","friendly neighborhood","skeletal","tentacled","conjoined","grasping","slimy","floating","mournful"],[" "],["ghost","spirit","apparition","phantom","poltergeist","specter","hauntling"]])
Things.add_thing("ghost body",["ectoplasm"],["\"body\""])
Things.add_thing("ghost thoughts",["ghost thought","ghost thought,20%"],["thoughts"])
Things.add_thing("ghost thought",[],["if only - she could hear me -","he needs to know - I'm sorry -","alone - I - wait -","I am so - very lonely -","when - will it end -","will it be - over soon -","do I - deserve this -","I regret - so much -","I miss you - so much -","please - never - ever die -","I must - wait here -","how many - centuries -","such is - my burden -","I cannot - feel a thing -","I have lost - all hope -","abandoned -","I float - forever -","I wander - for how long -","so spooky - right now -","that slime - isn't mine -","I rest - at last -","let's - be pals -","I sense - a presence -","you can - see me?","who you - gonna call -","can you - hear me now -"])


# meta
Things.add_thing("later", ["sorry"], "will do later")
Things.add_thing("error", ["sorry"], "Uh oh... It looks like you didn't supply a valid element to create.")
Things.add_thing("sorry", ["consolation universe"], "(Sorry!)")
Things.add_thing("consolation universe", [".universe"])

# for t in THINGS.items():
#     print(t)
# print(THINGS['universe'])
