"""
//life
new Thing("life",[["bird","poultry","fish","shark","crustacean","cnidaria","worm","mollusk","clam","plankton","reptile","amphibian","snake","small mammal","herbivorous mammal","predatory mammal","monkey","bear","horse","cat","dog","dinosaur","medieval person","caveman","dragon","person","space animal","insect","tree","grass blade"]],"Life");
new Thing("sea life",["sea monster,0.5%","fish,5-10","cetacean,0-4","shark,0-4","crustacean,1-4","cnidaria,1-4","mollusk,1-4","clam,1-4","plankton,2-8"],"life");
new Thing("abyss life",["sea monster,2%","fish,3-6","cetacean,0-2","shark,0-2","crustacean,2-5","cnidaria,2-5","mollusk,2-5","clam,2-5","plankton,2-8"],"life");
new Thing("beach life",["bird,0-3","herbivorous mammal,5%","amphibian,2%","reptile,2%","snake,2%","predatory mammal,5%","small mammal,2-5","insect,3-10","clam,3-8"],"life");
new Thing("river life",["fish,5-15","crustacean,0-10","plankton,2-8","bird,0-5","small mammal,0-2","amphibian,0-5","reptile,0-1","snake,0-1","insect,3-10"],"life");
new Thing("lake life",["sea monster,1%","fish,5-15","amphibian,0-5","crustacean,0-10","bird,0-5","plankton,5-15","small mammal,0-2","reptile,0-1","snake,0-1","insect,3-10"],"life");
new Thing("land life",["herbivorous mammal,2-8","horse,5%","predatory mammal,0-4","small mammal,5-10","amphibian,0-2","reptile,0-2","snake,0-2","bird,0-5","anthill,30%","insect,5-10"],"life");
new Thing("forest life",["herbivorous mammal,2-8","predatory mammal,0-4","bear,0-5","small mammal,5-10","amphibian,0-3","reptile,0-3","snake,0-3","bird,2-10","beehive,30%","anthill,30%","insect,5-10"],"life");
new Thing("jungle life",["herbivorous mammal,1-5","predatory mammal,0-4","monkey,1-5","small mammal,5-10","amphibian,0-3","reptile,0-3","snake,0-6","bird,2-10","beehive,30%","anthill,30%","insect,5-10"],"life");
new Thing("mountain life",["herbivorous mammal,1-6","predatory mammal,0-4","bear,2-6","small mammal,5-10","amphibian,0-2","reptile,0-2","snake,0-2","bird,2-10","beehive,30%","anthill,30%","insect,5-10"],"life");
new Thing("cave life",["herbivorous mammal,10%","predatory mammal,10%","bear,20%","small mammal,20%","small mammal,20%","small mammal,20%","amphibian,20%","reptile,20%","snake,10%","bird,15%","bird,5%","insect,5-10"],"life");
new Thing("ancient land life",["dinosaur,0-8",".land life"],"life");
new Thing("ancient forest life",["dinosaur,0-5",".forest life"],"life");
new Thing("ancient jungle life",["dinosaur,0-5",".jungle life"],"life");
new Thing("ancient mountain life",["dinosaur,0-3",".mountain life"],"life");
new Thing("urban life",["bird,0-8","small mammal,5-10","anthill,30%","insect,10-20"],"life");
new Thing("sky life",["shark,1%","bird,5-20","insect,0-2"],"life");
new Thing("galactic life",["space monster,1%","space animal,1-12"],"life");


new Thing("skeleton",["bones"],"skeleton");
new Thing("flesh",[".skinless body part"],"flesh");
new Thing("soft flesh",[".skinless soft body part"],"flesh");
new Thing("scales",["keratin"]);
new Thing("fish fin",["muscles","scales"],"fin");
new Thing("fish tail",["muscles","scales"],"tail");
new Thing("fish skin",["scales"],"skin");
new Thing("cetacean flipper",["muscles","skin"],"flipper");
new Thing("cetacean fin",["muscles","skin"],"fin");
new Thing("crustacean claw",["chitin","muscles","fat"],"claw");
new Thing("crustacean leg",["chitin","muscles","fat"],"leg");
new Thing("crustacean shell",["chitin"],"shell");
new Thing("clam shell",["calcium"],"shell");
new Thing("simple eye",[".eye flesh"],"eye");
new Thing("exoskeleton",["chitin"],"exoskeleton");
new Thing("insect leg",["chitin","muscles","fat"],"leg");
new Thing("insect claw",["chitin","muscles","fat"],"claw");
new Thing("stinger",["chitin","venom"],"stinger");
new Thing("antenna",["chitin"],"antenna");
new Thing("insect wing",[["chitin","scales"],"dew,2%"],"wing");
new Thing("wing",["feathers",".body part"],"wing");
new Thing("reptile wing",["scales",".body part"],"wing");
new Thing("bird wing",["feathers",".body part"],"wing");
new Thing("bird leg",["feathers",".body part"],"leg");
new Thing("bird tail",["feathers",".body part"],"tail");
new Thing("venom",["proteins","lipids,40%","nitrogen,40%","sodium,40%","chlorine,40%"],"venom");
new Thing("jelly",["water"]);

new Thing("weird soft organ",[".skinless soft body part"],[["fleshy","thick","slimy","scaly","furry","fuzzy","feathery","sharp","pointy","thorny","bulbous","leathery","hidden","soft","bubbling","distorted","shapeless","porous","spongiform","liquid-filled","foamy","smoking","oozing","drooling","shivering","quivering","pulsing"],[" "],["grasper","tendril","stinger","claw","tentacle","sac","egg sac","pouch","organ","specialized organ","bulb","mind bulb","gland","epiderm","sucker","pod","pseudolimb","nervous bulb","external muscle","structure","orifice","proboscis","tail"]]);
new Thing("weird hard organ",[".skinless body part"],[["fleshy","thick","slimy","scaly","furry","fuzzy","sharp","pointy","thorny","bulbous","hidden","flexible","plated","armored","metallic","distorted","shapeless","porous","spongiform","liquid-filled","foamy","smoking","oozing","drooling"],[" "],["carapace","shell","bone structure","skull","grasper","stinger","claw","organ","specialized organ","sucker","pod","pseudolimb","structure"]]);

new Thing("tentacle",[".skinless soft body part"],"tentacle");
new Thing("simple mouth",["teeth",".skinless soft body part"],"mouth");

new Thing("beak",[".bones"],"beak");

new Thing("reptile head",["scales",".body part"],"head");
new Thing("reptile leg",["scales",".body part"],"leg");

new Thing("fur",["keratin"],"fur");
new Thing("snout",[".nose"],"snout");
new Thing("whiskers",["keratin"],"whiskers");
new Thing("mammal leg",["fur",".body part"],"leg");
new Thing("tail",[".body part"],"tail");
new Thing("mammal head",["mouth","snout","whiskers","eye,2","ear,2","skull","fur"],"head");
new Thing("mammal body",["mammal head","fur","mammal leg,4","tail","flesh"],"body");
new Thing("bird body",["bird head","feathers","bird leg,2","bird wing,2","bird tail","flesh"],"body");
new Thing("bird head",["beak","eye,2","skull","feathers"],"head");
new Thing("reptile body",["reptile head","scales","reptile leg,4","tail","flesh"],"body");
new Thing("snake body",["reptile head","scales","tail","flesh"],"body");


//oh my god writing animal thoughts is so much fun
"""
