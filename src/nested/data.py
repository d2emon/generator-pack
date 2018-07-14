from .thing import Thing


THINGS = dict()


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


# universe stuff
addThing("multiverse",["universe,10-30"],["multiverse","lasagnaverse","doughnutverse","towelverse","baconverse","sharkverse","nestedverse","tastyverse","upverse","downverse","layerverse","clusterverse","metaverse","quantiverse","paraverse","epiverse","alterverse","hypoverse","dimensioverse","planiverse","pluriverse","polyverse","maniverse","stackoverse","antiverse","superverse","upperverse","maxiverse","megaverse","babyverse","tinyverse","retroverse","ultraverse","topoverse","otherverse","bubbleverse","esreverse","versiverse","'verse","cookieverse","grandmaverse"])
addThing("universe",["supercluster,10-30"])
addThing("supercluster",["galaxy,10-30"],"galactic supercluster")
addThing("galaxy",["galaxy center","galaxy arm,2-6"])
addThing("galaxy arm",["galactic life,5%","dyson sphere,4%","dyson sphere,2%","star system,20-50","nebula,0-12","black hole,20%","black hole,20%"],"arm")
addThing("galaxy center",["black hole","galactic life,10%","dyson sphere,4%","dyson sphere,2%","star system,20-50","nebula,0-12"],"galactic center")
addThing("nebula",["galactic life,15%","star,2%","star,2%","star,2%","interstellar cloud,1-6"])
addThing("interstellar cloud",["helium","hydrogen","carbon,80%","water,5%","ammonia,5%","nitrogen,5%","iron,5%","sulfur,5%","oxygen,15%"],[["a bright pink","a faint","a fading","a pale","a fluo","a glowing","a green","a bright green","a dark brown","a brooding","a magenta","a bright red","a dark red","a blueish","a deep blue","a turquoise","a teal","a golden","a multicolored","a silver","a dramatic","a luminous","a colossal","a purple","a gold-trimmed","an opaline","a silvery","a shimmering"],[" "],["interstellar cloud"]])
addThing("star system",["star","star,3%","visitor planet,5%","future planet,10%","future planet,10%","terraformed planet,50%","terraformed planet,20%","terraformed planet,10%","medieval planet,30%","medieval planet,20%","ancient planet,50%","ancient planet,30%","ancient planet,10%","barren planet,60%","barren planet,40%","barren planet,20%","gas giant,60%","gas giant,40%","gas giant,20%","gas giant,10%","asteroid belt,0-2"])
addThing("dyson sphere",["star","star,3%","dyson surface","future planet,1-8","barren planet,60%","barren planet,40%","barren planet,20%","gas giant,60%","gas giant,40%","gas giant,20%","gas giant,10%","asteroid belt,0-2"])
addThing("star",["ghost,0.1%","space monster,0.2%","hydrogen","helium"],[["white","faint","yellow","red","blue","green","purple","bright","double","twin","triple","old","young","dying","small","giant","large","pale","dark","hell","horrific","twisted","spectral"],[" star"]])
addThing("planet",[".terraformed planet"],"telluric planet")
addThing("barren planet",["galactic life,10%","rock","ice,50%",".planet composition"],"telluric planet")
addThing("visitor planet",["visitor city,1-8","visitor installation,2-6","galactic life","rock","ice,50%",".planet composition"],"telluric planet")
addThing("future planet",["future continent,2-7","ocean,1-7","future sky",".future moon,30%",".planet composition"],"telluric planet")
addThing("terraformed planet",["continent,2-7","ocean,1-7","terraformed sky",".terraformed moon,30%",".planet composition"],"telluric planet")
addThing("medieval planet",["medieval continent,2-4","ancient continent,0-3","ocean,1-7","sky",".planet composition"],"telluric planet")
addThing("ancient planet",["ancient continent,2-7","ocean,1-7","sky",".planet composition"],"telluric planet")
addThing("planet composition",["planet core","moon,40%","moon,20%","moon,10%"],"planet")
addThing("moon",["ghost,0.1%","rock","planet core"],[["young","old","large","small","pale","white","dark","black","old"],[" moon"]])
addThing("terraformed moon",[".planet composition","continent,1-4","ocean,1-4","sky"],[["young","old","large","small","pale","white","dark","black","old","green","lush","blue","city","colonized","life"],[" moon"]])
addThing("asteroid belt",["galactic life,20%","asteroid,10-30"])
addThing("earth",[".asteroid belt"],"Earth")
addThing("asteroid",["space animal,0.5%","rock","ice,30%"],"asteroid")
addThing("gas giant",["gas giant atmosphere","planet core,50%","moon,0-3","terraformed moon,20%","terraformed moon,10%"])
addThing("gas giant atmosphere",["galactic life,10%","helium","hydrogen","water,50%","ammonia,50%","methane,50%"],"atmosphere")
addThing("planet core",["space monster,0.5%","iron","rock","diamond,2%","magma"],"core")

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