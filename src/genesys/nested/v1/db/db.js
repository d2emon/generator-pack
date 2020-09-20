new Thing("diamond",["carbon"]);
new Thing("oil",["lipids"]);
new Thing("magma",[".rock"]);
new Thing("rock",["silica","aluminium,30%","iron,20%","potassium,20%","sodium,50%","calcium,50%"]);
new Thing("silica",["silicon","oxygen"]);
new Thing("chitin",["carbon","hydrogen","oxygen","nitrogen"]);
new Thing("salt",["chlorine","sodium"]);
new Thing("water",["hydrogen","oxygen"]);
new Thing("fire",["oxygen","carbon"]);
new Thing("ash",["organic matter","carbon"]);
new Thing("dew",["water"]);
new Thing("ice",["water"]);
new Thing("snow",["snowflakes"]);
new Thing("snowflakes",["water"]);
new Thing("ammonia",["hydrogen","nitrogen"]);
new Thing("methane",["hydrogen","carbon"]);
new Thing("hydrogen",[".hydrogen atom"]);
new Thing("hydrogen atom",["proton","electron"],["atoms"]);
new Thing("plastic",["polymers"]);
new Thing("rubber",["polymers"]);
new Thing("polymers",[".glucids"]);
new Thing("alcohol",[".glucids"]);
new Thing("carbon",[".atom"]);
new Thing("sodium",[".atom"]);
new Thing("chlorine",[".atom"]);
new Thing("oxygen",[".atom"]);
new Thing("helium",[".atom"]);
new Thing("potassium",[".atom"]);
new Thing("aluminium",[".atom"]);
new Thing("iron",[".atom"]);
new Thing("copper",[".atom"]);
new Thing("lead",[".atom"]);
new Thing("steel",["iron","carbon"]);
new Thing("gold",[".atom"]);
new Thing("silver",[".atom"]);
new Thing("silicon",[".atom"]);
new Thing("calcium",[".atom"]);
new Thing("nitrogen",[".atom"]);
new Thing("sulfur",[".atom"]);
new Thing("phosphorus",[".atom"]);
//alright, I'm not doing the whole periodic table.
new Thing("proteins",[".molecule"]);
new Thing("lipids",[".molecule"]);
new Thing("glucids",["carbon","hydrogen","oxygen"],"glucose");
new Thing("organic matter",[["proteins","lipids","glucids"],["proteins","lipids","glucids",""],"salt,30%"]);
new Thing("atom",["proton","neutron","electron"],["atoms"]);
new Thing("molecule",["atom"],["molecules"]);
new Thing("proton",["up quark,2","down quark"]);
new Thing("neutron",["down quark,2","up quark"]);
new Thing("electron",["qwubble"]);
new Thing("up quark",["qwubble"]);
new Thing("down quark",["qwubble"]);
new Thing("qwubble",["multiverse,1-5"]);
new Thing("portal",["universe"]);


//cell stuff
new Thing("cell",["nucleus","cytoplasm"],["cells"]);
new Thing("nucleus",["dna","proteins"]);
new Thing("cytoplasm",["glucids","lipids"]);
new Thing("dna",["genetic code","hydrogen","oxygen","nitrogen","carbon","phosphorus"],"DNA");
new Thing("genetic code",["nucleotide,20-50"]);
new Thing("nucleotide",["molecule"],["A","T","G","C"]);

//body stuff
new Thing("body part",["bacteria,30%","bacteria,10%","skin","blood vessels","bones","fat","muscles"],"body part");
new Thing("soft body part",["bacteria,30%","bacteria,10%","skin","blood vessels","fat","muscles"],"body part");
new Thing("skinless body part",["bacteria,30%","bacteria,10%","blood vessels","bones","fat","muscles"],"body part");
new Thing("skinless soft body part",["bacteria,30%","bacteria,10%","blood vessels","fat","muscles"],"body part");
new Thing("blood vessels",["bacteria,30%","blood"],"blood vessels");
new Thing("blood",["blood cell"],"blood");
new Thing("blood cell",[".cell"],["blood cells"]);
new Thing("skin",["bacteria,1-3","scar,0.5%","pores","skin cell","dead skin","dust,20%","sweat,20%"],"skin");
new Thing("scar",["dead skin"]);
new Thing("pores",["bacteria,1-3","skin cell","dead skin,50%","sweat,40%"],"pores");
new Thing("skin cell",[".cell"],["skin cells"]);
new Thing("dead skin",["skin cell"]);
new Thing("bone",[".bones"],"bone");
new Thing("bones",["bone cell","calcium"],"bones");
new Thing("bone cell",[".cell"],["bone cells"]);
new Thing("muscles",["muscle cell"],"muscles");
new Thing("muscle cell",[".cell"],["muscle cells"]);
new Thing("fat",["lipids"],"fat");
new Thing("mind cell",[".cell"],["mind cells"]);
new Thing("dandruff",["dead skin"]);

new Thing("clothing set",["hat,2%","glasses,20%","pants,98%","shirt,98%","coat,50%","socks,80%","shoes,80%","underwear,99%"],"clothing");
// => Person
new Thing("corpse",["body","clothing set","blood,35%","worm,20%","worm,10%"],"*PERSON*| (dead)");
new Thing("body",["head","torso","arm,99%","arm,99%","leg,99%","leg,99%"],"body");
new Thing("torso",["chest","pelvis",".body part"]);
new Thing("chest",["nipple,2","bellybutton",".body part"]);
new Thing("bellybutton",["skin","lint,0-1"]);
new Thing("nipple",["skin"]);
new Thing("pelvis",["naughty bits","butt",".body part"]);
new Thing("naughty bits",[".soft body part"]);
new Thing("butt",["pasta,0.01%","sweat,50%",".body part"]);
new Thing("arm",["hand","elbow","armpit",".body part"],"arm");
new Thing("hand",["finger,5",".body part"]);
new Thing("finger",["fingernail",".body part"],"finger");
new Thing("fingernail",["dust,30%","keratin"],"fingernail");
new Thing("elbow",[".body part"]);
new Thing("armpit",["armpit hair","sweat,80%",".soft body part"]);
new Thing("armpit hair",[".hair"],"hair");
new Thing("leg",["foot","knee",".body part"],"leg");
new Thing("foot",["toe,5","sweat,30%",".body part"]);
new Thing("toe",["toenail",".body part"],"toe");
new Thing("toenail",["dust,40%","keratin"],"toenail");
new Thing("knee",[".body part"],"knee");
new Thing("head",["mouth","nose","eye,99%","eye,99%","ear,2","skull","head hair,85%",".body part"],"head");
new Thing("eye",["eyelashes","eye flesh","tear,2%"],"eye");
new Thing("eye flesh",["water","blood vessels","fat"],"eyeball");
new Thing("eyelashes",[".hair"],"eyelashes");
new Thing("tear",["water","salt"]);
new Thing("ear",[".soft body part"],"ear");
new Thing("mind",["bacteria,20%","mind cell"],"mind");
new Thing("skull",["mind",".bones"]);
new Thing("head hair",[".hair","dandruff,10%"],[["brown","black","gray","light","blonde","red","dark"],[" hair"]]);
new Thing("hair",["bacteria,30%","keratin"],"hair");
new Thing("nose",["nostril,2",".body part"],"nose");
new Thing("nostril",["nostril hair","boogers,0-1",".soft body part"],"nostril");
new Thing("nostril hair",[".hair"],"nostril hair");
new Thing("boogers",["organic matter"]);
new Thing("mouth",["teeth","tongue"],"mouth");
new Thing("teeth",["calcium","phosphorus"],"teeth");
new Thing("tongue",["muscles"],"tongue");

new Thing("abomination",["abomination body","abomination psyche"],"*PERSON*| (abomination)");//nonononononono
new Thing("abomination psyche",["abomination thoughts","memories"],"psyche");
new Thing("abomination thoughts",["black hole,0.01%","abomination thought"],"thoughts");
new Thing("abomination thought",[],["P-please...","Don't look at me...","Please... kill me...","Kill... me...","Why would I ever ask for this...","I only wish for death.","I only long for death now.","I only demand... death...","End my misery... I beg you...","This is a mockery of existence...","I miss her so much...","I miss him so much...","I miss my family...","Why would they do that to me...","How could they do this to me...","What have I become...","I feel... different...","I can't feel... anything...","I can't... see anything..."]);
new Thing("abomination body",["abomination head","abomination head,5%","abomination torso",["arm,0-8","arm,0-4"],["leg,0-8","leg,0-4"],"crustacean claw,2%","stinger,2%","weird soft organ,10%","weird soft organ,10%","weird hard organ,10%","weird hard organ,10%"],"misshapen body");
new Thing("abomination head",["mouth,0-2","nose,0-2","eye,0-8","ear,0-4","skull,90%","weird soft organ,20%","weird hard organ,20%","head hair,65%",".body part"],"misshapen head");
new Thing("abomination torso",["chest","chest,10%","pelvis","pelvis,10%","weird soft organ,20%","weird hard organ,20%",".body part"],"misshapen torso");

//mind stuff
new Thing("psyche",["thoughts","memories"],"psyche");
new Thing("thoughts",["black hole,0.01%",["sad thought,2-4","happy thought,2-4"]]);
new Thing("sad thought",[],["*SADTHOUGHT*"]);
new Thing("happy thought",[],["*HAPPYTHOUGHT*"]);
new Thing("memories",["memory,2-4"]);
new Thing("memory",[],["*MEMORY*"]);

//cloth stuff
new Thing("cloth",["textile"]);
new Thing("leather",["skin cell"]);
new Thing("textile",["textile fibre"]);
new Thing("textile fibre",["keratin"],["textile fibres"]);
new Thing("keratin",["proteins"]);
new Thing("sweat",["water","salt","glucids"]);
new Thing("clothing",["textile","dead skin,40%","sweat,15%"]);
new Thing("pocket",["dust,20%","crumbs,20%","lint,30%","donut,1%","coin,20%","coin,20%","coin,10%","pen,10%","pen,2%","button,10%","button,5%","button,1%","note,15%","note,5%","handgun,0.4%","pasta,0.2%","textile"]);

new Thing("pants",["pocket,0-4",".clothing"],["pants","trousers","sweatpants","bermuda shorts","shorts","jeans","cargo pants"]);
new Thing("shirt",[".clothing"],["shirt","sweater","t-shirt"]);
new Thing("underwear",[".clothing"]);
new Thing("coat",["pocket,0-4",".clothing","leather,30%"],["coat","jacket","hoodie"]);
new Thing("cozy von pocketworth",["pocket,20-40",".clothing","leather,30%"],["Cozy von Pocketworth"]);//lotsopokkits
new Thing("socks",[".clothing"]);
new Thing("shoes",["leather,40%","plastic"],["shoes","boots","sneakers","sandals"]);//crocs //okay seriously no
new Thing("hat",[".clothing"],["cap","hat","hat","hat","hat","beret","party hat","top-hat"]);
new Thing("glasses",["plastic","glass","metal,10%"],["glasses","glasses","glasses","sunglasses","monocle","ski mask"]);




//vegetation
new Thing("plant cell",[".cell"],["plant cells"]);
new Thing("grass",["grass blade,50-100"]);
new Thing("grass blade",["grass thoughts,2%","dew,6%","worm,3%","insect,6%","plant cell"]);
new Thing("grass thoughts",["grass thought,1"],"thought");
new Thing("grass thought",[],[":D",":O","D:",":|",":]",">:0"]);
new Thing("trees",["tree,20-50"]);
new Thing("tree",["tree thoughts,2%","tree trunk","branches","leaves","nest,5%","nest,2%","fruits,20%","flowers,20%"],["larch","fir","oak","birch","pine","sequoia","cedar","spruce","ash","poplar","elm","sycamore","willow","mahogany","laurel","orange tree","lemon tree","palm tree","coconut tree","pear tree","apple tree","walnut tree","olive tree"]);
new Thing("tree thoughts",["tree thought,1"],"thought");
new Thing("tree thought",[],["Well. What is this all about.","So. What's the hurry?","Whoah. Slow down.","Do like a tree. And go away.","I seen some things.","They're coming.","We know.","We've been watching you for hundreds of years.","Do you have any idea how old I am?","Yes. I remember you. I remember all of you."]);
new Thing("leaves",["leaf,50-100"]);
new Thing("leaf",["dew,6%","insect,6%","plant cell"]);
new Thing("branches",["branch,10-30"]);
new Thing("branch",["insect,6%","leaf,10%","plant cell"]);
new Thing("twig",["plant cell"]);
new Thing("fruits",["worm,5%","plant cell","sugar"]);
new Thing("flowers",["insect,5%","plant cell","pollen"]);
new Thing("pollen",["plant cell","sugar"]);
new Thing("tree trunk",["insect,4%","wood","bark"]);
new Thing("bark",["insect,10%","worm,10%","wood"]);
new Thing("jungle trees",["jungle tree,20-150"],"trees");
new Thing("jungle tree",[".tree"],["tree"]);
new Thing("humus",["insect,0-3","worm,0-3","twig,0-3","leaf,0-6","organic matter","dirt"]);
new Thing("nest",["bird,50%","egg shell,20%","bird egg,0-6","twig,6-12"]);


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


//single-celled organisms
new Thing("bacteria",["bacteria body","bacteria thoughts"],[["pico","nitro","sulfuro","oxy","toxi","micro","nano","proto","archi","ferro","mono","poly","schizo","myxo","hydro","noo","zoo","phyto","aqui","acido","cyano","chloro","chromo","fibro","osteo","spiro","bacillo","flagello","helio","anaero","photo","litho","methano","cerebro","cephalo","brachio","plasmo","ethylo"],["amoeba","bacteria","virus"]]);
new Thing("bacteria body",[".cell"],"body");
new Thing("bacteria thoughts",["bacteria thought,1"],["thoughts"]);
new Thing("bacteria thought",[],["#wow","#wow okay","#i can't even","#okay","#me","#yes","#what","#how","#delicious","#seriously","#but seriously tho","#germ life","#mitosis","#meiosis","#nucleus","#cytoplasm","#single-celled and ready to mingle","#lame","#meh","#i don't wanna talk about it","#eukaryote privilege","#protist scum","#squirm","#protist patriarchy","#osmosis","#one cell of a guy"]);

//sea life
//plankton
new Thing("plankton",["plankton body","plankton thoughts"],["jellyfish larva","coral polyp","diatom","urchin larva","starfish larva","salp","rotifer","pteropod","clione"]);//krill etc in crustaceans
new Thing("plankton body",["simple eye,0-3","simple mouth","exoskeleton","jelly","soft flesh"],"body");
new Thing("plankton thoughts",["plankton thought,1"],["thoughts"]);
new Thing("plankton thought",[],["hello :)","yes hi :)","how are you :)","it's sunny today :)","what a nice day :)","aaah I could just float away :)","I am fine thank you :)","yes I think so :)","how fun :)","do you catch my drift :)","so many cousins :)","I'm a little lost :)","no pressure :)","that's okay :)","what a nice thing to say :)","you should stay over :)","my place or your place :)","why are you still here :)","there's a big world to explore :)","I don't even know where I'm going :)","here I go! :)","am I really going where I decide to go, or am I just being pushed around by the current? :)","oh no :(","can't you feel them coming? :(","they're slowly rising from deep below :(","it's slowly coming this way :(","I'm different :(","ravioli, ravioli :)","give me the formuoli :)","oh,..."]);

//clams
new Thing("clam",["clam body","clam thoughts"],["oyster","mussel","scallop"]);
new Thing("clam body",["clam shell","clam shell","mind","soft flesh"],"body");
new Thing("clam thoughts",["clam thought,1-3"],["thoughts"]);
new Thing("clam thought",[],["what","wait","hold on","wait why","i don't","stay clam and carry on","oh no","why this","that's","no","yes","wait no","but","haha what","please explain","that's not","i'm confused","please why","slurp","okay","okay what","what is this","what's that"]);

//cnidaria
new Thing("cnidaria",["cnidaria body","cnidaria thoughts"],["urchin","starfish","sea cucumber","sea anemon","coral","box jelly","jellyfish","hydra","man'o'war","sponge","sea nettle","siphonophore","ctenophore","tunicate","trichordate"]);//urchins and starfish and sponges are unrelated to cnidarians but I don't really care
new Thing("cnidaria body",["simple mouth","jelly","soft flesh"],"body");
new Thing("cnidaria thoughts",["cnidaria thought"],"thoughts");
new Thing("cnidaria thought",[],[["shhhhl","shhl","schllll","gl","schgl","gbl","swwwl"],["urp","orp","arp","urps","orpsss"]]);

//mollusks
new Thing("mollusk",["mollusk body","mollusk thoughts"],["sea slug","sea snail","squid","octopus","vampire squid","clione","sea angel","cuttlefish","nautilus","giant squid","colossal squid","mimic octopus"]);
new Thing("mollusk body",["simple eye,2","mouth","tentacle,6-8","jelly","soft flesh"],"body");
new Thing("mollusk thoughts",["mollusk thought,2"],["thoughts"]);
new Thing("mollusk thought",[],["party time","is it party time now","party now ok","party's over","okay let's party","ready to party","are you party","they don't look like they want to party","is the party over","this party's so hot it's stupid","this party getting crazy","partyyyyyyy","chug chug chug","we party now","wanna join in","we partyin","okay too much party","I have a secret for you","that's a secret","I kinda like partying","party yes nice","woooo party"]);

//crustaceans
new Thing("crustacean",["crustacean body","crustacean thoughts"],["shrimp","prawn","langoustine","lobster","rock lobster","crab","spider crab","crayfish","krill","triops","copepod"]);
new Thing("crustacean body",["simple eye,2-6","mind","crustacean leg,6-8","crustacean claw,2","crustacean shell","soft flesh"],"body");
new Thing("crustacean thoughts",["crustacean thought,2-3"],["thoughts"]);
new Thing("crustacean thought",[],["skitter skitter","crawl crawl","dig dig","grab grab","gotta eat","gotta skitter","gotta catch food","gotta hide","gotta breed","breed breed","under the sea"]);

//fish; getting those from http://homepages.cwi.nl/~sjoerd/fishlist.html just because I can
new Thing("fish",["fish body","fish thoughts"],["anchovy","sardine","mackerel","tuna","albacore","herring","bream","bass","perch","mullet","brill","plaice","sole","angler","dab","flounder","skate","cod","haddock","pollack","whiting","pike","perch","trout","carp","eel","lamprey","salmon","catfish","dogfish","swordfish","sailfish","pufferfish","sunfish","manta ray","stingray"]);
new Thing("fish body",["simple eye,2","mind","mouth","fish fin,2-6","fish skin","fish tail","flesh","worm,5%"],"body");
new Thing("fish thoughts",["fish thought,2-3"],["thoughts"]);
new Thing("fish thought",[],["blup","bloop","blwap","blep","gotta eat","gotta swim","gotta get food","gotta hide","gotta breed","oooh shiny"]);

//sharks
new Thing("shark",["fish body","shark thoughts"],["shark","bullshark","blue shark","goblin shark","great white shark","hammerhead shark","nurse shark","tiger shark","whale shark","reef shark","angel shark","basking shark","megalodon","megashark","wereshark","bearshark"]);
new Thing("shark thoughts",["shark thought,1-2"],["thoughts"]);
new Thing("shark thought",[],["CHOMP","NOM","THIS LOOKS TASTY","THIS SMELLS DELICIOUS","IS THIS FOOD","OH GOD I LOVE FOOD","MY FOOD IS SCREAMING","MY FOOD IS TRYING TO SWIM AWAY","COME BACK FOOD","I LOVE YOU FOOD","FOOD WHY DO YOU DO THIS","FOOD I MISS YOU","HELLO IS THIS FOOD","YES THIS IS SHARK","FOOD AND I ARE BEST FRIENDS","I AM SO LOST RIGHT NOW","OH HEY ARE YOU FOOD","EXCUSE ME ARE YOU FOOD","OH SORRY I THOUGHT YOU WERE FOOD","HAVE YOU SEEN FOOD","WHAT'S THIS ALL ABOUT","WOULD YOU COME OVER HERE","SO YOU'RE NOT FOOD RIGHT","LET ME TELL YOU ABOUT FOOD","WHY ARE WE YELLING","OOOH SHINY","IT KEEPS HAPPENING","I TOLD YOU ABOUT FOOD BRO","WHY DO I KEEP EATING MY FRIENDS","I DON'T GET IT","I'M A SHARK","IF THEY DIDN'T WANT TO BE EATEN THEY WOULDN'T BE SO DELICIOUS","YOU'RE NOT ONE OF THEM PRANCY FANCY DOLPHINS ARE YOU","FOOD COME BACK I'M SORRY I YELLED","OH FOOD I LOVE YOU SO","I'M SERIOUS","HOLD ON IT'S TIME FOR FOOD"]);

//cetaceans
new Thing("cetacean",["cetacean body","cetacean thoughts"],["dolphin","porpoise","whale","orca","bottlenose dolphin"]);
new Thing("cetacean thoughts",["cetacean thought,1-2"],["thoughts"]);
new Thing("cetacean thought",[],["Oh god. Let me tell you about sharks.","Sigh. Yes, this is dolphin.","Do I look like a goddamn rescue dog to you?","A trick? Do I look like a clown to you?","The blowhole isn't just for show.","There's things. Down there. Deep down.","We've seen them.","They're coming to the surface.","EEK EEK EEK EEK- oh, sorry about that.","EEK UUK","Yes. Charming.","So long, etc.","My god. How long must this go on.","EEEEUUUUUUEEEEEKKKKK","Click noises.","Swimmity.","Yes. No. Go away.","You know. I could catch that fish myself if I wanted to.","I mean, that's fine and all.","That's really all there is to say about it.","I never make puns on porpoise. HUEHUEHUEHUEHUE","Look! Over there! Haha, sucker.","Guess how much I care about sharks? Exactly. I don't."]);
new Thing("cetacean head",["mouth","eye,2","skull","skin"],"head");
new Thing("cetacean body",["cetacean head","skin","cetacean flipper,2","cetacean fin,1-2","tail","flesh"],"body");

//worms
new Thing("worm",["worm body","worm thoughts"],["worm","mealworm","maggot","nightcrawler","flatworm"]);//YES I KNOW MAGGOTS AND WORMS ARE UNRELATED
new Thing("worm body",["simple mouth","soft flesh"],"body");
new Thing("worm thoughts",["worm thought,1-2"],["thoughts"]);
new Thing("worm thought",[],["wiggle wiggle","squirm squirm","crawl crawl","weee","yayyy","hey apple","hey","oh hey","hellooo","oh sorry","so much fun","nevermind"]);

//insects (arachnids etc too)
new Thing("insect",["insect body","insect thoughts"],["ant","bee","wasp","hornet","ladybug","cockroach","termite","beetle","dung beetle","scarab beetle","bumblebee","spider","scorpion","tarantula","praying mantis","butterfly","moth","fly","cricket","mole cricket","cicada","weevil","stick insect","aphid","flea","lice","firefly","gnat","stinkbug","grasshopper","silverfish","locust","earwig"]);
new Thing("insect body",["simple eye,2-8","mind",["insect leg,6","insect leg,8"],["insect claw,2",""],"exoskeleton","stinger,30%",["insect wing,2","insect wing,4","",""],["antenna,2",""],"flesh"],"body");//spiders with wings. because yeah
new Thing("insect thoughts",["insect thought,2-3"],["thoughts"]);
new Thing("insect thought",[],["skitter","skitter skitter","squirm squirm","crawl crawl","buzz","big noisy things","small tasty things","too much sun","not enough sun","need water","need food","need shelter","food please","mating please","must defend nest","intruder detected","must spawn eggs","hey hey","let's be bros","no stomp please","go away"]);
new Thing("social insect",["insect body","social insect thoughts"],["worker","soldier","drone"]);
new Thing("insect queen",["insect body","social insect thoughts"],["queen"]);
new Thing("anthill",["social insect,10-30","insect queen","insect egg,2-10","dirt"],["anthill","termite mound"]);
new Thing("beehive",["social insect,10-30","insect queen","insect egg,2-10","paper"],["beehive","wasp nest","hornet nest"]);
new Thing("insect egg",["egg thoughts","egg shell","soft flesh","organic matter"],"egg");
new Thing("social insect thoughts",["social insect thought,1-2"],["thoughts"]);
new Thing("social insect thought",[],["hello intruder","you should stay away intruder","intruder we may be forced to chop you up into little pieces if you stay here","this is no place for you intruder","why don't you go back to your intruder nest with all the other intruders","we have no need for intruders right now","hey intruder ever heard of personal space","sorry intruder but you're kind of in the way","intruder that's enough now","intruder why don't you come back another time","sorry intruder we're all super-busy here","hey intruder you're like very big so please don't stay here","i trophallaxized a girl and i liked it"]);

//monsters
new Thing("sea monster",["sea monster thoughts",["tentacle,0-6","fish fin,0-4","",""],"stinger,20%",["crustacean claw,0-4",""],["crustacean leg,0-8",""],["crustacean shell","scales","fur","exoskeleton",""],["mouth,1-2","beak,1-2"],"skull,80%",["eye,1-8","simple eye,1-8","",""],"weird soft organ,0-4","weird hard organ,0-4"],[["giant","timeless","colossal","abyssal","forgotten","ancient","gigantic","monstrous"],[" "],["craze","drift","dredge","dread","slumber","dream","wander","frost","magma","stone","slime","ooze","egg","larva","grudge","stride","flail","wail","time","star","crystal","terror","horror","scream","wrath","burst","dark","deep","tickle"],["fin","tail","sinker","sunk","singer","song","polyp","rifter","glider","squirmer","titan","colossus","mind","queen","king","child","guardian","seer","whale","worm","spider","crab","leech","fish","shark","squid","saur","buddy","lord"]]);
new Thing("sea monster thoughts",["sea monster thought,1-2"],["thoughts"]);
new Thing("sea monster thought",[],["IIIIII MUSSST SCREEEAAAM","I AMMMM AWAKENED","ALLLLLL FEAR MEEEEE","NOOOOONE SHALL LIVE","I MUSSSSST EATTTTT","DEEEEEEEEP I SSSSLUMBER","IIIII SHALL CONSSSSUME","IIIII SHALL DEVOUUUUURRRRR","LIFFFFFFE MUSSSSST PERISHHHHH","NNNNNNNNURISHMENT","ALL SHALLLLLLL GO INSSSSSSANE","SSSSSSANITY SHALL YIELDDDDD","EXXXXXILED I WASSSSS","EONSSSSS I HAVE SLUMBERED","EONSSSSS I HAVE WAITED","MORTALSSSSSS BEHOLDDDDD","I COMMMMME FROM DEEP","IMMMMMMOBILE I WATCHHHH","SSSSSKITTER","THEY FFFFFLOAAAAAT"]);

new Thing("space monster",["space monster thoughts",["tentacle,0-6","fish fin,0-4","",""],"stinger,20%",["crustacean claw,0-4",""],["crustacean leg,0-8",""],["crustacean shell","scales","fur","exoskeleton",""],["mouth,1-2","beak,1-2"],"skull,80%",["eye,1-8","simple eye,1-8","",""],"weird soft organ,0-4","weird hard organ,0-4"],[["C'","Vr'","Ksh","Zn'","Sh","Hrl","X","O","Yog","Gorg","Morg","Marg","Magg"],["","","agn","soth","norgn","ngas","alx","orx","rgl","iirn","egw","thulh","t","g","m"],["org","orgon","orgus","orkus","oid","us","u","esth","ath","oth","um","ott","aur"],[""," the Forgotten"," the Entity"," the Ancient"," the Starchild"," the Seeder"," the Leech"," the Timeless"," the Eon"," the Many"," the Countless"," the Boundless"," the Prisoner"," the Child"," the Form"," the Shape"," the Drifter"," the Swarm"," the Vicious"," the Warden"," the Ender"," the Unworldly"," the Unfriendly"," the All-Consumer"]]);
new Thing("space monster thoughts",["space monster thought,1-2"],["thoughts"]);
new Thing("space monster thought",[],["WWWWWWWIDER THAN STARRRRRRS","AWAKENNNN MY CHILDRENNNNNN","GALAXIESSSSS SHALL FALLLLLLL","I AMMMMMM INFFFFFINITE","I SSSSSSSPAN AGESSSS","WWWWWWEEEEE ARE UNDYINGGGGGG","WE COMMMMMMMME","WE ANSSSSSWER THE CALLLLLLL","I TRAVELLLLLLL SLLLLLLUMBERING","FROMMMMMM FARRRRRR I COMMMME","IIIIII MUSSST SCREEEAAAM","I AMMMM AWAKENED","ALLLLLL FEAR MEEEEE","NOOOOONE SHALL LIVE","I MUSSSSST EATTTTT","DEEEEEEEEP I SSSSLUMBER","IIIII SHALL CONSSSSUME","IIIII SHALL DEVOUUUUURRRRR","LIFFFFFFE MUSSSSST PERISHHHHH","NNNNNNNNURISHMENT","ALL SHALLLLLLL GO INSSSSSSANE","SSSSSSANITY SHALL YIELDDDDD","EXXXXXILED I WASSSSS","EONSSSSS I HAVE SLUMBERED","EONSSSSS I HAVE WAITED","MORTALSSSSSS BEHOLDDDDD","I COMMMMME FROM DEEP","IMMMMMMOBILE I WATCHHHH","SSSSSKITTER","HHHHHHHEY HOW YOU DOIN'","AWKWAAAAAAAAARD"]);

new Thing("space animal",["space animal thoughts,85%","space animal body"],[["e","a","o","","","","","",""],["sm","cr","shn","sh","sn","gl","g","m","c","x","h","dr","r","l"],["o","a","u","i","e","ee"],["x","b","rv","z","s","gg","g","k","rf","gl","bl","th","kt","m","sh","l","dr","v","p","nt","nk"],["o","a","i","u","e"],["n","ne","se","b","m","l","s","sh","th","t","sk","zer","bbler","ggler","ddler","ter","nt","r","r","r"]]);
new Thing("space animal body",[["tentacle,0-6","crustacean leg,0-8","fish fin,0-4","mammal leg,1-6","",""],["insect wing,0-6","",""],["crustacean claw,0-4","",""],"flesh,40%","snout,3%","stinger,10%","whiskers,3%",["crustacean shell","scales","fur","exoskeleton",""],["mouth,1-4","beak,1-4",""],"skull,30%","mind,50%",["eye,1-2","eye,1-6","simple eye,1-6",""],"weird soft organ,50%","weird soft organ,20%","weird hard organ,50%","weird hard organ,20%"],["body"]);
new Thing("space animal thoughts",["space animal thought,1-3"],["thoughts"]);
new Thing("space animal thought",[],[
["sk'","mop","nanu","nug","gmap","shmu","dna","no","xle","doda","daia","de",""],["g ","gek ","th ","iap ","glib ","ph ","d't ","neig'","dip ","shna ","sh "],
["sk'","mop","nanu","nug","gmap","shmu","dna","no","xle","doda","daia","de",""],["g ","gek ","th ","iap ","glib ","ph ","d't ","neig'","dip ","shna ","sh "],
["mi","di","glu","dra","shwa","ama",""],["ben","ri","nap","dap","top","gog"],
[".",".",".",".","!","?"]
]);

new Thing("can of nightmare",["space animal,4-12","sea monster,2-6","space monster,2-6"]);//do not open

//amphibians
new Thing("amphibian",["reptile body","amphibian thoughts"],["frog","bull frog","poison frog","treefrog","golden toad","toad","newt","salamander","caecilian","axolotl"]);
new Thing("amphibian thoughts",["amphibian thought,1-2"],["thoughts"]);
new Thing("amphibian thought",[],["h-here i go","r-ribbit?","anyone?","heyyy","helloooo","ribbity","croak","hello my baby","hello my honey","how do you do this","i'm kinda newt to this","well","okay","alright...","why frog do that","toadally"]);

//reptiles
new Thing("reptile",["reptile body","reptile thoughts"],["snapping turtle","sea turtle","turtle","tortoise","chameleon","gecko","iguana","lizard","skink","monitor lizard","goanna","crocodile","alligator","gavial","caiman","komodo dragon"]);
new Thing("snake",["snake body","reptile thoughts"],["boa","coral snake","snake","sea snake","mamba","viper","adder","python"]);
new Thing("reptile thoughts",["reptile thought,1-2"],["thoughts"]);
new Thing("reptile thought",[],["hhhehehe","hehu","haheha","hehuheheho","hohohohe","i cant breathe","hue","br","brbrbrbrbrbrbrbr","gib fud pls","pls","r u a lizard","ehuehuehu","hey","k","sss","ssssssss","hiss etc","ey","ay","ey bb","u wot m8","aeiou","john madden","ereptile dysfunction","confirmed for br","i joke bb","i tease bcuz i care","r u 4 real","i swr m8","ill bop u 1","let's see if you fit in my mouth","wink, wink","but for real tho im absolutely terrified right now","your skin so soft so nice mmh can i wear it","damn right","yes indeed... yes indeed","let's shed light on this mystery","pabongles","bachinkles","zabinga","wapingles","mmh","body massage"]);

//dinosaurs yes
new Thing("dinosaur",["reptile body","dinosaur thoughts"],["ankylosaur","triceratops","protoceratops","pentaceratops","stegosaur","hadrosaur","iguanodon","pachycephalosaur","sauropod","raptor","velociraptor","deinonychus","brachiosaur","apatosaur","therizinosaur","theropod","titanosaur","tyrannosaur","diplodocus","allosaur","ceratosaur","dimetrodon","pterosaur"]);
new Thing("dinosaur thoughts",["dinosaur thought,1-2"],["thoughts"]);
new Thing("dinosaur thought",[],["Dinner. Served.","End. Near.","Protect. Eggs.","Food. Must find.","Need food. Badly.","Scared. Hunted.","Things. Beneath.","Chase. Run.","Food. Nearby.","Sky. Dark.","Limbs. Aching.","Mind. Numb.","Ground. Shaking.","Over. Soon.","Offspring. Safety.","Skin. Burning.","Hostile. Nearby.","Must. Go on.","Must. Remember.","Pack. Lost?","Family. Where?"]);

//dragons why not
new Thing("dragon",["dragon body","dragon thoughts"],[["fire","ice","forst","arcane","ancient","wise","guardian","copper","bronze","steel","obsidian","gem","undead","skeletal","sea","sky","cloud","green","red","white","golden","silver","chrome","rainbow","mist","mother"],[" "],["dragon","wyrm","wyvern","guivre"]]);
new Thing("dragon thoughts",["dragon thought,1-2"],["thoughts"]);
new Thing("dragon thought",[],["You shouldn't be here.","Leave. Now.","You need to leave.","Well well well. What do we have here?","I will make quick work of you.","You smell like food. Are you food?","I will eat your mind before I eat your body.","You'll be dead before you realize what's happening to you.","They... they took my egg...","My treasure. Must protect my treasure!","I guard, undisturbed.","I'm older than most of these mountains.","I've seen things you wouldn't believe.","Leave at once, mortal.","Turn back if you value your life.","Act with great care now, for this is the very last thing you'll ever do.","Knights in armor cook just like canned beans.","People seem to value treasure more than their own life.","There's no honor, no valor nowadays.","I'm on fire today.","Ooooh burn."]);
new Thing("dragon body",["reptile head","pyrolith","scales","reptile leg,4",["reptile wing,2",""],"tail","flesh"],"body");
new Thing("pyrolith",["rock"]);
new Thing("dragon lair",["dragon,98%","medieval servant,10%","dragon nest,40%","pile of treasure,90%","medieval corpse,0-3"]);
new Thing("dragon nest",["egg shell,20%","dragon egg,0-3","pile of treasure"]);
new Thing("dragon egg",["egg thoughts","egg shell","soft flesh","organic matter"],"dragon egg");

//birds
new Thing("bird",["bird body","bird thoughts"],["pigeon","starling","swallow","robin","sparrow","eagle","vulture","hawk","condor","osprey","buzzard","crane","bustard","pheasant","woodpecker","seagull","albatross","petrel","grebe","flamingo","stork","ibis","heron","swan","magpie","crow","raven","jay","chough","quail","grouse","partridge","egret","pelican","cormorant","avocet","lapwing","plover","curlew","gull","tern","skua","guillemot","auk","sandgrouse","dove","parrot","lorikeet","cockatoo","parakeet","macaw","turaco","cuckoo","coucal","owl","snowy owl","frogmouth","nightjar","swift","hummingbird","quetzal","toucan","shrike","wren","oriole","fantail","paradise bird","lark","skylark","warbler","babbler","thrasher","mockingbird","lyrebird","bluebird","thrush","nightingale","sunbird","finch","kingfisher","trogon","pitta","manakin","chickadee","sula"]);//not putting in tits or boobies
new Thing("poultry",["bird body","poultry thoughts"],["chicken","chicken","chicken","duck","duck","mallard","goose","goose","turkey","kiwi","penguin","ostrich","emu","cassowary"]);//All flightless birds are considered poultry. Penguins and kiwis in farms. LIKE I CARE
new Thing("bird thoughts",["bird thought,1-2"],["thoughts"]);
new Thing("bird thought",[],["caw","caw caw",":V",":V caw","you think i care","yeah bring it","like for real","come say that to my face","chirp","so high right now","pooping on people, from far above, doop-dee-doop","do i care, no i don't, doop-dee-doop","me and my mates are gonna ruin your day","can i peck your face","please can i peck at you just a bit","everything i sing is super-lewd","i'm a lewd dude","so yeah","i am bird hi","i'm pretty fly","hey can i steal that","what now","that's not what your mom said last night","yes that's right","yes indeed","see what happens","oh god what happen","riveting","aw yiss","bred crums yisss","i am the birdest","bird and bird accessories","hey have you heard","turns out i'm the word"]);
new Thing("poultry thoughts",["poultry thought,1-2"],["thoughts"]);
new Thing("poultry thought",[],["cluck","bwucluck",":U",":U cluck","i'm gonna strut around a bit while bobbing my head like that","i got weird feet why","you think i care","like for real","yeah bring it","come say that to my face","why do i poop on my feet","oh my god i have the best voice","i'm like super-good at songs okay","let me sing you something plz","so yeah","i am bird hi","this is most fowl","yeah i got laid when i was born, what now gurl","what now","that's not what your mom said last night","yes that's right","yes indeed","see what happens","oh god what happen","riveting","aw yiss","bred crums yisss","i am the birdest","bird and bird accessories","hey have you heard","turns out i'm the word"]);
new Thing("bird egg",["egg thoughts","egg shell","soft flesh","organic matter"],"egg");
new Thing("egg shell",["calcium"],"shell");
new Thing("egg thoughts",["egg thought"],"thought");
new Thing("egg thought",[],[["...","...","...","...","I...","the...","a...","ah..."]]);


//mammals

new Thing("small mammal",["mammal body","small mammal thoughts"],["squirrel","rat","mouse","dormouse","sugar glider","flying squirrel","possum","lemur","weasel","ferret","groundhog","rabbit","hare","vole","hedgehog","shrew","bat","fruit bat","pipistrelle","stoat","polecat","raccoon","badger","honey badger","otter","civet","koala","mongoose","mink","mole","molerat","loris","sloth","aye-aye","prairie dog","chipmunk","gerbil","chinchilla"]);
new Thing("small mammal thoughts",["small mammal thought,2-3"],["thoughts"]);
new Thing("small mammal thought",[],["Hunted.","Somewhere to hide. Now.","Now is not the time.","I need shelter.","I need to burrow somewhere.","This is not good.","I am being stalked.","Something's chasing me.","Don't turn around.","Just keep running.","I need to collect more food.","I'll never get enough food at this rate.","I need to find a mate.","I want offspring.","I can't stay here.","I think I saw something move.","The hunt is on.","This scent is familiar.","I smell food.","This scent is no good.","This smells dangerous.","I need to hurry.","I'm starving.","I'm tired.","I'm cold.","I'm scared."]);

new Thing("herbivorous mammal",["mammal body","herbivorous mammal thoughts"],["ox","buffalo","antelope","impala","gazelle","wild horse","zebra","giraffe","ram","goat","yak","ibex","llama","alpaca","elephant","rhinoceros","deer","moose","elk","kangaroo","walabi"]);
new Thing("predatory mammal",["mammal body","predatory mammal thoughts"],["fox","jackal","boar","wolf","hyena","lynx","lion","leopard","panther","tiger","dropbear"]);
new Thing("bear",["mammal body","bear thoughts"],["bear","brown bear","polar bear","grizzly","panda"]);

new Thing("herbivorous mammal thoughts",["herbivorous mammal thought,1-3"],["thoughts"]);
new Thing("herbivorous mammal thought",[],["Hunted.","Somewhere to hide. Now.","Now is not the time.","I need shelter.","I need to hide somewhere.","This is not good.","I am being stalked.","Something's chasing me.","Don't turn around.","Just keep running.","I need food badly.","I need to find a mate.","I want offspring.","I can't stay here.","I think I saw something move.","This scent is familiar.","I smell food.","This scent is no good.","This smells dangerous.","I need to hurry.","I'm starving.","I'm tired.","I'm cold.","I'm scared."]);

new Thing("predatory mammal thoughts",["predatory mammal thought,1-3"],["thoughts"]);
new Thing("predatory mammal thought",[],["Busy. Hunting.","Now is not the time.","I need shelter.","This is not good.","It grazes, oblivious to my presence.","So nimble on its feet.","Yes. It grazes so peacefully.","It grazes so calmly.","All is quiet.","Why is it in such a hurry?","Aah. Delicious, mindless meat.","I've been stalking this meat for days. I won't give up.","So swift is the meat.","I will toy with the meat and then I will devour it.","The meat is going scarce.","Just as planned.","Something is scaring the meat away.","Do I smell meat?","Graceful, delicious meat.","I smell something. It's not meat.","Something is approaching.","There is something bigger than me.","You think you can outrun me?","Prey or be preyed upon.","Eat. Prey. Eat some more.","Meat awaits.","Don't turn around.","Run. Run for the meat.","I need food badly.","I need to find a mate.","I want offspring.","I don't beat my meat. I just tear it to pieces.","I can't stay here.","I'm bigger than you.","This scent is familiar.","I smell meat.","This scent is no good.","This smells dangerous.","I need to hurry.","I'm starving.","I'm tired.","I'm cold.","I'm scared."]);

new Thing("bear thoughts",["bear thought,1-3"],["thoughts"]);
new Thing("bear thought",[],["I WOULD LIKE TO ENQUIRE ABOUT YOUR FOOD","EXCUSE ME GOOD SIR, WOULD YOU HAPPEN TO BE EDIBLE","I'LL SAY","THIS IS NOT PROPER ETIQUETTE","MAY I ENQUIRE ABOUT YOUR EDIBILITY","ARE YOU ONE OF THOSE EDIBLE FELLOWS","WOULD YOU SAVE BOTH OF US THE TROUBLE AND JUST HOP INTO MY MOUTH","WHY WOULD YOU DO THAT","YES QUITE","YES INDEED","THOUGHTS ARE BETTER CONVEYED BY THINKING THEM EXTRA-LOUDLY","IT WOULD APPEAR SO","YES I AM QUITE DAPPER","WHAT WILL IT BE OLD CHAP","WELL AREN'T YOU A DELICIOUS LITTLE CHAP","SUCH PLEBEIAN UNDERTAKINGS","SUCH GLORIOUS VERBOSITY","HOLD ON TO THAT THOUGHT","HOLD ON I NEED TO STUFF MY FACE INSIDE A BEEHIVE BECAUSE I'M HARDCORE LIKE THAT","DEM BEES MAN","OKAY WHAT","SHHH ONLY SLEEP NOW","IT'S A SECRET TO EVERYBODY","I CERTAINLY DON'T MIND SOME SQUIRMING MEAT","YEAH NOT GOING TO RANT ABOUT FOOD","HELLO THERE TASTY","I DARE YOU MAN","WELL THIS IS JUST SILLY","I'M SECRETELY A HUMAN"]);

new Thing("horse",["mammal body","horse thoughts"],["horse"]);
new Thing("horse thoughts",["horse thought,1-3"],["thoughts"]);
new Thing("horse thought",[],["oh","oh god","what does it mean","it's all around","why","I don't understand","oh god what is that","oh my god","oh dear god","it's so intense","it's so beautiful","this is everything I've ever wanted","this exceeds all my expectations","this is better than everything ever","how did I even get here son","whoah","I just","mom where are you","let's just","...whoah","look at me, I'm amazing","give me a lick","sweet lemonade","not walking into bars again","all those colors","I can taste the colors","the universe tastes amazing","is this real life","I can't even","I can't breathe help","that's the best thing I've ever heard","so then why the long face? because it's melting. my face is melting","why this","I am everything","I am forever","I can't even begin to"]);

new Thing("monkey",["mammal body","monkey thoughts"],["macaque","chimpanzee","gorilla","bonobo","orangutan","howler monkey","capuchin monkey","spider monkey"]);
new Thing("monkey thoughts",["monkey thought,2-3"],["thoughts"]);
new Thing("monkey thought",[],["I need grooming. Anyone?","Oh yeah, that's the spot.","Oh god. The itch.","Yes. I'm a monkey. How are you.","How insensitive of you.","Look what I can do!","Oh hey, look what I found!","Don't make me fling it.","Hey. Pull my finger.","Man, you keep delicious things in your fur.","Am I smelling what I think I'm smelling?","Mind if I sit on you?","You don't know where that finger has been.","A stick, a rock, technology!","This is the last time I raid an anthill.","I don't feel like I'm being taken seriously here.","Do everything they do. That'll do the trick.","Do I smell... coconut?","Can I eat the skin of your face just a little? No? Okay, just making sure.","I could make tools or whatever too, I just don't feel like it."]);

new Thing("cat",["mammal body","cat thoughts"],[["fat","obese","skinny","fluffy","calm","collected","meditative","wistful","quiet","purring","meowing"],[" "],["tabby","calico","striped","spotted","black","grey","white","brown","orange"],[" "],["cat","kitten"]]);
//[["bobtail","abyssinian","balinese","birman","bombay","burmese","chartreux","devon rex","domestic","maine coon","manx","munchkin","oriental","persian","ragamuffin","scottish fold","siamese","sphynx","longhaired","shorthaired","bald","fluffy","obese","white","black","tabby","calico"],[" cat"," kitten"]]);
new Thing("cat thoughts",["cat thought,1-2"],["thoughts"]);
new Thing("cat thought",[],[["meow meow meow meow","we must abolish","we cannot tolerate","I have predicted","as I have predicted","children will be blessed","we are being lied to","they do not fool me","the dirty lying teachers say","soon it will end","adults eat teenagers alive","try my belly-button logic","fraudulent oneness","vilify teachers","nothing more evil than cat educated as 1","safely remove parasites and their eggs","this is some good catnip","hey everybody","4 harmonic corner days rotate simultaneously around squared equator","chapstick chapstick fffshh","wake up sheeple","false prophet","sanity preserve sanity","come to daddy","is it time for","when will it be when","What is this place? Where am","proceed now to","in the next chapter I explain how","and this is how","complete with","if it fits","if you order now","oh no it's happening agai-","one does not simply","I'm so much better off without my meds","Did you know?","I can haz","and that is how I met your","thoughtform of cat coevaluates thoughtform of dog"],[" "],["MEOW MEOW MEOW MEOW","PURR PURR PURR","THE VERY FACE OF TIME","I FEEL THEM IN MY BRAIN","THE INITIAL MOVEMENT","MUST CHANGE THE HOLY BOOK","BURN THE OLD WORLD METHODS","BREATHE THE CONTINUUM","QUANTUM DEMOGRAPHICS","EVIL OF PERSON FROM ANCESTORS","THE SON AND FATHER","THIS PROVES EVERY BELIEVER A LIAR","EVIL OF QUADRANTS","THE BLOOD OF THE IMPURE","SUPPORTERS OF LIES","SUFFERING OF CHILDREN","NO GOD KNOWS ABOUT 4 DAYS","4 SIMULTANEOUS DAYS","4 CORNER DAYS PROVES 1 DAY 1 GOD IS TAUGHT EVIL","IGNORANCE OF CAT SIMPLE MATH IS RETARDATION","THE ONENESS OF GOD IS STILLNESS DEATH","LOVE OF GOD IS HATE OF CHILDREN","DOES YOUR TEACHER KNOW?","2 HALF 4 SELF","1 DAY GOD WAS WRONG","ALL HAIL CAT","NOT GOD NOT GOD FSHHHH","THE BODY, THE BODY OF THE LORD","CORPSES TO CORPSES","UNACCEPTABLE","MUST SURRENDER","CATNIP FOR THE CAT GOD","MORE LITTER FOR THE LITTER-THRONE","LITTERALLY","4 CORNERS MAKES THE WORLD GO ROUND ROUND ROUND","CUBES ALL THE WAY DOWN","QUADRANTS EVERYWHERE","ONE OF ITS SIXTY-THOUSAND NAMES","DO NOT TOUCH THE THETANS","PUNCH MY FACE IN","HELP I AM STUCK IN CAT BODY","I TOLD YOU ABOUT QUADRANTS BRO","SURRENDER NOW AND YOU MAY EARN THE PRIVILEGE OF BEING EATEN FIRST","QUALITY STUFF","THE SWINE MUST PAY","SO HARDCORE","OH LONG JOHNSON","I WILL EAT YOUR SOUL","THEY WILL PAY WITH BLOOD","HE COMES"],[" "],["meow meow meow meow","meow","meow purr","of new world order","of the seven coordinates","now, lick me","into new order","for glorious sacrament","practicing evil","navel connects 4 corner 4s","world will stay the same","lie that corrupts the planet","you educated stupid fools","but it was all joke","it is evil to ignore 4 days","deserve to be spit upon publicly","chunky peanut butter","directly to forehead","spoke to my mind","wrote a book about it","and it's free","proven clinically","immediate results","created all of them","has retarded your opposite rationale mind to a half mind slave","and evil education damnation","just a hoax","just a theory","and shall be exterminated","not very raven","would you like to know more","cat cat cat cat cat cat cat","I'm a kitty-cat","and I dance dance dance and I dance dance dance","nyan","interwebz","series of tubes","whoah what just happened","mondays","(this is what cats actually believe)","church was full of liars","support cat or be cursed","or is it?","copyright fshh fshhh"]]);
//new Thing("cat thought",[],["Meow meow meow meow, meow meow meow meow, meow meow meow meow meow meow meow meow","I'm like, so offended right now?","That's, like, not tasteful at all?","So triggered right now.","Yes. Well. It takes one to know one.","Yeah well. You know what they say.","Uhm, like, hello?","What am I looking at exactly.","That is SO inappropriate.","Uhm, duh? How else would I clean my butthole?","Uhm, not funny."]);//snooty teenager? not very funny

new Thing("dog",["mammal body","dog thoughts"],[["tall","huge","tiny","ridiculously small","comically small","enormous","monstrous","fluffy","obese","malnourished","fat","skinny","slender","curly","hairy","hairless","sort-haired","long-haired","puffy","happy","excited","friendly","ridiculous-looking","barking","panting"],[" "],["yellow","gold","cream","white","grey","black","orange","red","brown","spotted","black and tan","two-color","tricolor"],[" "],["dog","puppy","lapdog","hound"]]);
//[["inu","terrier","malamute","bulldog","spaniel","foxhound","pit bull terrier","mastiff","shepherd","basset","beagle","berger","bichon","collie","boxer","chihuahua","chow chow","dachshund","dalmatian","cocker","coonhound","setter","mountain","spitz","retriever","dane","labrador","husky","maltese","pekingese","pomeranian","poodle","labradoodle","pug","rottweiler","shih tzu"],[" dog"," puppy"]]);
//Wrote all these names and realized it wasn't very funny, plus too many location names for my liking. Ah well.
new Thing("dog thoughts",["dog thought,2-3"],["thoughts"]);
new Thing("dog thought",[],["HAY I'M DOG","I AM DOG HAY","WE DOG NOW???","HEY LET'S DOG OK???","CAN WE DOG NOW OK???","DOG STUFF YAYYYYY","BUTTS COME IN MANY FLAVORS","BUTTS YES","HURRAY!!!!!!!! BUTTS","YOUR BUTT SMELLS LEGIT","WOOF","BWURF","BAWF WOOF","GUESS WHAT?????????? WOOF","MY SPECIALTY. IS ROOFING.","HEY EVERYDOGGY","DOG DOG DOG DOG DOG DOG DOG","MY NAME. IS DOG. AND I HAVE MET YOU. HI!!!","!!!!!!!!!!!!!!!!!!!!!WHOAH","!!!!!!!!!YES NICE","EVERYTHING SO NICE WOW","WE GO MANGLE SQUIRREL NOW????? PLS","WOW!!!!!!!! SO EXCITE","I'M RLY EXCITE RIGHT NOW","DO YOU KNOW JUST HOW EXCITE I AM","DO YOU HAVE. ANY IDEA. JUST HOW EXCITE I AM.","A WALK????? YES WALK LOVE WALKS HURRAY!!!!!!","PEE ON THINGS HURRAY!!!!!!","YIP YIP YIP YIP YIP","YIP","I COULD GO FOR SOME SQUIRREL RIGHT ABOUT NOW","IF TEARING UP SQUIRRELS IS WRONG THEN WOOF WOOF WOOF WOOF WOOF WOOF WOOF","DOG??????????? DOG","I LICK YOUR FACE NOW OK???????","VERI GOOD :DDDDDDDD","I WAS RUNNING BUT I FORGOT WHY I WAS RUNNING SO THEN I STOPPED RUNNING AND NOW I AM NOT RUNNING ANYMORE.","I DON'T UNDERSTAND!!!!! BUT OK","UH","HELP I AM CHOKE ON SQUIRREL HELP","ARE YOU A SQUIRREL","NO WAY","DUDE THERE IS NO WAY","IS THAT, UH, OH NEVERMIND","OHNO WHY","MEOW I MEAN WOOF????? YES","All of this must of course remain absolutely confidenOH HEY WOOF WOOF WOOF","I AM THE DOGGEST","MORE DOG YES DOG","LESS CAT MORE DOG","HAHA I LOVE YOU","ONE DAY I WAKE UP AND I AM DOG WOW","IS THIS REAL LIFE","I AM SO DOG RIGHT NOW","WOW","WHY THIS","THIS IS GREAT"]);



//furniture
new Thing("cabinet",["wood frame","glass,30%",".cabinet content"]);
new Thing("cabinet content",["donut box,4%",["cheese,0-3",""],"water bottle,0-1","juice bottle,0-1","soda bottle,0-1",["can,0-6","cookie box,0-6"],"insect,2%"]);
new Thing("fridge",[".fridge content","plastic","metal grill,1-4","electronics"]);
new Thing("fridge content",["roast,15%","pasta,40%","pasta,10%","can,15%","donut box,5%","cake,3%","pie,3%",["yoghurt,0-6",""],["ice cream,0-6",""],["cheese,0-3",""],"water bottle,0-1","juice bottle,0-2","soda bottle,0-2","milk bottle,0-1","wine bottle,10%"]);
new Thing("oven",[["pie","cake","roast","",""],"plastic","metal grill,1-3","electronics"]);
new Thing("kitchen sink",[".sink"]);
new Thing("sink",[["porcelain","metal"],"organic matter,5%","pipes"]);
new Thing("toilet",["water","organic matter,15%","pasta,0.1%","porcelain","pipes"]);
new Thing("pipes",["metal","dirt"]);
new Thing("nails",["iron"]);
new Thing("metal",["iron"]);
new Thing("metal grill",["metal"]);
new Thing("porcelain",["silica"]);
new Thing("ceramic",["silica"]);
new Thing("chair",[["wood","plastic"],"nails,50%"]);
new Thing("armchair",[".chair","cloth"]);
new Thing("couch",[".armchair","tv remote,5%","coin,5%","pen,5%"],["couch","sofa"]);
new Thing("tv remote",["plastic","electronics"],"TV remote");
new Thing("coin",["organic matter,2%","dirt,2%","copper"]);
new Thing("gold coin",["gold"]);
new Thing("dirt",["organic matter,50%","dust"]);
new Thing("grease",["lipids","dust"]);
new Thing("dust",["molecule"]);
new Thing("crumbs",["organic matter"]);
new Thing("lint",["textile fibre"]);
new Thing("pen",["plastic","ink,80%"]);
new Thing("button",["plastic"]);
new Thing("note",["note writing","paper"]);
new Thing("note writing",[],["*NOTE*"]);
new Thing("bed",[".armchair","pillow,0-3"]);
new Thing("pillow",["feather","cloth"]);
new Thing("feather",["keratin"]);
new Thing("feathers",[".feather"]);
new Thing("mirror",["glass","portal,0.1%"]);
new Thing("glass",["silica"]);
new Thing("desk",["wood frame","drawer,0-6"]);
new Thing("cupboard",["cup,0-6","drinking glass,0-6","bowl,0-4","plate,0-8","wood frame","wood shelf,1-4","drawer,0-2"]);
new Thing("drinking glass",["glass"],"glass");
new Thing("bowl",["ceramic"]);
new Thing("cup",["ceramic"]);
new Thing("plate",["ceramic"]);
new Thing("closet",["portal,0.1%","skeleton,0.1%","hat,30%","hat,15%","pants,0-5","shirt,0-5","underwear,0-6","coat,0-3","socks,0-8","shoes,0-6","button,20%","wood frame","wood shelf,0-2"]);
new Thing("living-room table",[".table","drawer,0-2"],"table");
new Thing("table",[["wood","plastic"],"nails,50%"]);
new Thing("drawer",["note,0-8","office toy,30%","office toy,30%","pen,30%","pen,10%","pen,5%","donut box,4%","can,2%","book,20%","book,20%","book,5%","book,5%","button,10%","button,10%","dust,40%","lint,40%"]);
new Thing("note stack",["note,5-25"]);//lotsonotes
new Thing("bookshelf",["book,5-30",["plastic shelf,3-8","wood shelf,3-8","drawer,0-2"]]);
new Thing("small bookshelf",["book,1-8",["plastic shelf,1-6","wood shelf,1-6"]],["bookshelf"]);
new Thing("wood shelf",["wood","nails"],"shelf");
new Thing("plastic shelf",["plastic","nails,50%"],"shelf");
new Thing("wood frame",["wood","nails"]);
new Thing("book",["page,20-100"],"*BOOK*");
new Thing("page",["paragraph,1-8","paper"]);
new Thing("paper",["cellulose"]);
new Thing("cardboard",["cellulose"]);
new Thing("wood",["cellulose","worm,1%"]);
new Thing("cellulose",["glucids"]);
new Thing("paragraph",["character,50-300"]);
new Thing("character",["ink"],"*CHAR*");
new Thing("ink",["alcohol","oil"]);
new Thing("bathtub",["porcelain","pipes","dirt,30%","insect,5%","hair,30%"]);
new Thing("shower",["porcelain","pipes","dirt,30%","insect,5%","hair,30%"]);
new Thing("tv",["tv show","tv remote,20%","plastic","electronics"],[["plasma","wide-screen","high-resolution","black and white","small","cheap"],[" TV"]]);
new Thing("tv show",[],[["A movie about","A show about","A sitcom about","A TV show about","A cartoon about","A foreign show about","An ad with"],[" "],["stupid people","boring people","uninteresting people","tan people","foreigners","a cute couple","an obnoxious couple","a dysfunctional couple","magic kids","space people","scientists","heroes","antiheroes","superheroes","cavemen","knights","old-timey people","awkward teenagers","hundreds of people","insane people","cool hip kids","a kid and his pet","a kid and his teacher","a boy and a girl","businessmen","an old man and his wife","a young couple","cow-boys","pirates","ninjas","monsters","wizards","cleaning products","aliens","cute talking animals","artists","wacky animated animals","beloved cartoon characters","bears","sharks","small people"],[" "],["struggling with their emotions","trying to express their feelings","and ecology","and friendship","and feelings","and food","talking about stuff","doing things","kicking butt and taking names","in a post-apocalyptic world","running away from zombies","crying helplessly","getting lost in the woods","and their dream of starting a business","trying to achieve their life-long dream","trying to keep their promises","trying to destroy a cursed artifact","in school","looking away from explosions","hacking computers","telling jokes","delivering one-liners","shooting stuff","slaying monsters","going to space","travelling together","learning about life","dancing and singing","doing way gross stuff","learning martial arts","trying to kill each other","doing sports","trying to defeat a government conspiracy","in the century's biggest heist","involving hilarious quiproquos and misunderstandings","getting killed by a sociopath","fighting robots","killing aliens","rescuing baby animals","falling in love","going on a date","slowly turning evil","learning that violence is not the answer","doing magic","coming up with convoluted plans","exploring the sea","saving the world","involved in various mishaps","involved in hilarious pranks","with less-than-stellar writing","with neat visual effects","with a beautiful soundtrack","with an impressive amount of clichés","with a twist at the end","with brilliant acting"],["."]]);
new Thing("video game console",["plastic","electronics"],[["Mega","Ultra","Gene","Se","Ninten","Nin","Play","Game","Next","Retro","Dream","Sun","Kine","3D"],["station","do","sphere","sis","tron","ga","zor","boy","cast","nect","next"]]);

new Thing("machine",["computer keyboard,10%","engine,20%","mechanics","electronics,40%","metal","wood,10%","cables,40%","dirt,10%"],[["valve","pump","terminal","conveyor","forklift","girder","furnace","generator","hydraulics"]]);
new Thing("cables",["plastic","wire"]);
new Thing("wire",["copper"]);

new Thing("engine",["mechanics"]);
new Thing("mechanics",["cog,2-12","push-button,0-3","electronics,30%","cables,75%","wire,0-2","tube,0-3","nails,40%","insect,5%"],"mechanical components");
new Thing("cog",[["copper","plastic","iron","steel","aluminium"]],["cog","gear","spur gear","helical gear","bevel gear","harmonic drive","spring","pump","sprocket","wheel","chain","belt","track","bolts","gizmo","pulley","puffer","smoker","vent"]);
new Thing("push-button",["plastic","cables"],["lever","button","switch"]);
new Thing("tube",[["plastic","metal","glass"]]);

new Thing("electronics",["microchip,1-6","electronic component,1-6","wire,0-2"]);
new Thing("microchip",["electronic component,1-15","plastic,75%","copper,75%","silicon,25%","gold,5%"],["microchip"]);
new Thing("electronic component",["plastic,75%","copper,75%","silicon,25%","gold,5%"],["transistor","inductor","capacitor","diode","metagizmo","transmorpher","beeper"]);


//computers
new Thing("pixel paragraph",["pixel character,50-300"],"paragraph");
new Thing("pixel character",["bit,8"],"*CHAR*");
new Thing("computer",["computer screen","computer keyboard","computer mouse","electronics"],[["P","B","M","N","T","St","Pl","Bl","Gr","Fr","Sht","Fl"],["apple","indows","inux","oogle"],[" computer"]]);
new Thing("laptop",[".computer"],[["P","B","M","N","T","St","Pl","Bl","Gr","Fr","Sht","Fl"],["apple","indows","inux","oogle"],[" laptop"]]);
new Thing("computer keyboard",["plastic","electronics"],"keyboard");
new Thing("computer mouse",["plastic","electronics"],"mouse");
new Thing("computer screen",["internet browser","computer folder,1-4","software,0-4","video game,0-4","computer trashbin","plastic","electronics"],"screen");
new Thing("computer folder",["computer folder,0-2",["computer folder,0-6","disturbing computer image,1-10","stupid computer image,1-10","cute computer image,1-10","software,1-6","video game,1-6"]],[["/"],["my ","My ","misc ","Misc. ","various ","secret ","family ","Family ","shared ","Shared ","important ","Important ","public ","Public ","private ","Private ","","",""],["documents","docs","Documents","Songs","Music","Movies","Pictures","pictures","pics","photos","files","Files","things","stuff","stuff to sort"]]);
new Thing("computer trashbin",["computer folder,0-4","disturbing computer image,0-4"],"Trashbin");
new Thing("video game",[".computer file"],[
["Super ","Mega ","Ultra ","Final ","World of ","","","","",""],
["Bl","B","Fl","Gl","Z","Zw","Dw","M","W","Wh","C","F","G","Pl","Spl"],["ario","antasy","and","astle","ark","ork","org","urg","ink","arf","ine","ar","at","uster","aster","alaxy","ims","ultima","universe","izzard"],
["craft","vania","arria","arium","'s Revenge","'s Quest"," Bros"," Town"," Land"," World"," Party"," Quest"," RPG"," Horses"," Friends"," Girlz"," Online"," Fantasy"," Ultra"," Deluxe"," Fortress"," Racing"," Edit"," Maker"," Beta"," Trial"," Music"," Ultimate"," Resurrection"," The Movie : The Game"," 2"," 3"," II"," III"," 2000"," 3000"," GOTY Edition"," Deluxe Edition"," expansion pack"," [keygen]"," [CRACK]"," HD","","","","","","","","","","",""]
,[".soft"]
]);
new Thing("software",[".computer file"],[
["Photo","Touch","Pic","Morph","Kid","Cosmo","Astro","Ink","Web","Art","Movie","Music","Calc","Math","Phrase","Dictio","World","Bug","Shell","Folder","File","Program","Question","EZ","Easy","Ancestry","History","Encyclo","Sun","Speed","Health","Doc","School","Learn","Lang","Code","Prog","Note","Pixel","Simple","Line","Shape","Name","Phone","Insta","Love","Friend","Assist","Tut","Active","Micro","Macro","Shock","Laser","Disc","Index","Game","Trouble","Hobbie","House","Task","Sports","Car","Money","Finance","Password","Fun","Mail","Virus","Fire","Burn","Diet","Pet","Mission","Hyper","Flower","Biblio","Video","Party","Open","Closed","Magic"],
["shop","pic","pix","draw","thinker","mind","pad","glide","top","artist","words","writer","layer","net","nary","matic","ulator","ula","ulus","ify","izer","crusher","finder","find","sort","reply","info","pro","pedia","helper","creator","card","land","warrior","armor","wall","nova","manager","paint","pixel","namer","call","book","tales","media","wave","mail","-b-gone","care","serve","server","printer","designer","retriever","spy","link","Office","cracker","Edit","Editor"],
[" Pro"," - More Clipart edition"," Assistant"," Fusion"," Easy"," Plus"," Professional"," Gold"," extended edition"," Free"," freeware version"," trial"," shareware"," Web"," Online"," Edit"," Illustrated"," 2.0"," 1.1"," 1.2"," 3.0"," [keygen]"," [CRACK]"," HD","","","","","","","","","","",""]
,[".soft"]
]);
new Thing("computer file",["bit,50-100"],["file"]);
new Thing("bit",[],["0","1"]);
new Thing("cute computer image",[".computer file"],[
["An image of ","A picture of ","A short video of ","A drawing of ","A slideshow of ","A video of "],
["a cat","two cats","cats","kittens","a kitten","a duckling","a duck","ducks","a puppy","a baby seal","a dog","puppies","a squid","a dolphin","a bunny","bunnies","baby bunnies","a parrot","two parrots","a gecko","a chameleon"],[" "],
["playing with a ball","befriending other animals","making cute faces","wearing silly hats","trying to play piano","in various shenanigans","playing with cardboard boxes","being really excited","sneezing","sleeping","waking up","falling asleep"],["."]
]);
new Thing("stupid computer image",[".computer file"],[
["An image of ","A picture of ","An album of ","A short video of ","A video of ","A compilation of "],
["some dude","some girl","a rather unattractive fellow","a rather unattractive lady","a grotesque individual","a clearly drunk guy","a clearly drunk girl","a bunch of kids with popped collars","some muscular guy","a masked guy","some guy with a horse mask","cosplaying kids","orange people","midgets","a midget","a movie star","some celebrity","high school kids","children","a creepy old person","old people"],[" "],
["setting fire to some stuff","involved in a retardedly dangerous prank","trying something extremely dangerous","involved in what was probably a stupid bet","doing stupid stuff","in anatomically questionable shenanigans","getting stupidly injured","stretching the limits of stupidity","in an absurdly dangerous stunt","dancing to some cheesy music","pestering dangerous animals","doing that thing with the stuff","trying too hard to be cool"],["."]
]);
new Thing("disturbing computer image",[".computer file"],[
["An image of ","A possibly illegal image of ","A crude representation of ","A disturbing representation of ","A daring representation of ","A video of "],
["a ¤¤¤¤¤¤","a group of ¤¤¤¤¤¤","several ¤¤¤¤¤¤","a couple of ¤¤¤¤¤¤"],[" "],
["in the process of ¤¤¤¤¤¤","being ¤¤¤¤¤¤ by","trying to ¤¤¤¤¤¤ on","in a ¤¤¤¤¤¤ with","involved in ¤¤¤¤¤¤ with","holding"],[" "],
["another ¤¤¤¤¤¤","two other ¤¤¤¤¤¤","their ¤¤¤¤¤¤","inside a ¤¤¤¤¤¤'s ¤¤¤¤¤¤","a ¤¤¤¤¤¤","a strange-looking ¤¤¤¤¤¤","a bewildered ¤¤¤¤¤¤"],["."]
]);
new Thing("forum post",[".pixel paragraph"],[
["A poll about ","An irate little person ranting about ","A bunch of shut-ins arguing about ","Two people sharing their love for ","Some hipsters chatting about ","Concerned parents discussing ","An inflammatory post about ","A thoughtful comment on ","An insightful post regarding ","A troll post about ","A flame war about ","Some spam about ","A comment on ","A post about ","A discussion about ","An ongoing discussion about ","A heated argument about ","A passionate discussion about ","A single person complaining about ","A group of persons enthusiastic about "],
["politics","countries","cooking","food","favorite foods","pets","religion","religious beliefs","crime","funny videos","music","favorite bands","webcomics","comics","art","video games","movies","dating advice","relationships","favorite books","famous people","astronomy","astrophysics","science","memes","spacetime","physics","foreign countries","cats","aliens","a bunch of nonsense","a controversial book","a controversial movie","friendship","stuff people put in their pockets","computers","cute things","creepy things","stupid things","gardening","cars","crime","youth","illicit substances","knitting","sports","meditation","hobbies","whatever's trendy right now","a debated topic","superheroes","trolling","jimmies being rustled","filenames","an online universe generator"],["."]
]);
new Thing("internet browser",["v1,0.5%","website"],[["Blazewolf","Interweb Discoverer","Bismuth","Savannah","Theatre"],[".soft"]]);
new Thing("website",[["forum post,1-10","disturbing computer image,1-10","cute computer image,1-10","stupid computer image,1-10","website,1-10"],"website,1-3"],[["www."],
["one","4","9","on","live","wiki","re","net","home","neat","fat","free","cool","not","something","everything","dat","my","you","that","this","face","tv","sick","cute","creepy","me","hurr","crap","web","bizz","wrong"],
["chon","speak","news","chat","gog","ddit","bad","nasty","forum","gross","pal","friends","world","rama","search","stick","retarded","tard","ville","town","cat","cats","durr","tube","space","book","music","directory"],
[".com",".com",".com",".net",".org"]]);

//hell, might as well
new Thing("internet",["website,20"],"The Internet");
new Thing("google",[".website"]);
new Thing("wikipedia",[".website"]);
new Thing("4chan",[".website"]);
new Thing("v1",["universe"],"www.orteil.dashnet.org/v1");
new Thing("reddit",[".website"]);
new Thing("facebook",[".website"]);
new Thing("/tg/",[".website"]);
new Thing("/b/",[".website"]);
new Thing("/v/",[".website"]);
new Thing("/x/",[".website"]);



//food
new Thing("milk",["glucids","lipids","calcium"]);
new Thing("bottle",[["glass","plastic","cardboard"],"label"]);
new Thing("glass bottle",["glass"],"bottle");
new Thing("glass jar",["glass"],"jar");
new Thing("label",["paper"]);
new Thing("milk bottle",[".bottle","milk"]);
new Thing("wine bottle",[".bottle","wine"]);
new Thing("wine",["sugar","alcohol"]);
new Thing("water bottle",[".bottle","water"]);
new Thing("juice bottle",[".bottle","juice"]);
new Thing("soda bottle",[".bottle","soda"]);
new Thing("juice",["water","sugar"],[["apple","pear","banana","tomato","pineapple","pumpkin","carrot","grape","orange","papaya","kiwi","mango"],[" juice"," juice"," juice"," smoothie"]]);
new Thing("soda",["water","sugar"],[["apple","pineapple","grape","orange","purple","brown"],[" soda"]]);
new Thing("can",["water","sugar","salt","mold,3%","metal"],[["canned "],["apple bits","pear bits","tomatoes","pineapple","pumpkin","carrots","meat","pork","beef","peas","mushrooms","olives","fish","burger","corn"]]);
new Thing("cookie box",["sugar","salt,70%","mold,3%","cardboard"],[["box of "],["cheesy","cheese","sugar","cream","milk","milky","whole-grain","frosted","glazed","apple","nut","fruit","chocolate","butter","oat","wheat","corn","animal-shaped","meat","crunchy","crispy"],[" "],["puffs","poofs","cookies","biscuits","rolls","pops","snacks","crackers","cereals","pies","tarts"]]);
new Thing("yeast",[".cell"]);
new Thing("yoghurt",["milk","sugar","yeast"],[["strawberry","vanilla","cherry","pear","plain"],[" yoghurt"]]);
new Thing("ice cream",["milk","sugar","ice"],[["strawberry","vanilla","cherry","chocolate"],[" ice cream"]]);
new Thing("cheese",["milk","yeast","mold,30%"],[["roquefort","cheddar","gouda","edam","colby","mozarella","processed cheese","stilton","goat cheese","gorgonzola","brie","camembert"]]);
new Thing("roast",[".meat","spices"],[["chicken","beef","pork","duck","mutton"],[" roast"]]);
new Thing("spices",[".organic matter"],[["pepper","garlic","onions","rosemary","sage","thyme"]]);
new Thing("meat",["blood vessels,5%","bones,5%","fat,50%","muscles","salt"]);
new Thing("tomato sauce",["glucids","meat,20%","salt"]);
new Thing("pasta",["salt","glucids","cheese,5%","tomato sauce,20%"],["spaghetti","noodles","fusilli","fettuccine","fettuce","tagliatelle","cannelloni","penne","rigatoni","farfalle","tortelloni","ravioli","gnocchi"]);
new Thing("pastry",["sugar","salt","dough"],"pastry");
new Thing("pie",[["fruit jam","meat"],".pastry"],"pie");
new Thing("cake",[".pastry"],[["chocolate","white chocolate","chestnut","fruit","huge","impressive","ornate","glazed","colorful","cheese","nut","delicious"],[" cake"]]);
new Thing("fruit jam",["plant cell","sugar"]);
new Thing("donut box",["donut,0-12","cardboard"],"doughnut box");
new Thing("donut",[".pastry"],[["vanilla ","strawberry ","raspberry ","cherry ","chocolate ","coconut ","cream ","cinnamon ","bacon ","sprinkly ","frosted ","glazed ","powdered ",""],["doughnut"]]);
new Thing("sugar",["glucids"]);
new Thing("dough",["glucids","lipids"]);

//visitors
new Thing("visitor",["visitor body","visitor psyche"],"visitor");
new Thing("visitor body",["visitor head","visitor head,2%","visitor torso","visitor arm,99%","visitor arm,2%","visitor arm,99%","visitor leg,99%","visitor leg,99%","visitor leg,2%"],"body");
new Thing("visitor torso",["visitor chest","visitor pelvis",".body part"],"torso");
new Thing("visitor chest",[".body part"],"chest");
new Thing("visitor pelvis",["visitor naughty bits",".body part"],"pelvis");
new Thing("visitor naughty bits",[".soft body part"],["thrusher"]);
new Thing("visitor arm",["visitor hand","visitor elbow,2","visitor armpit",".body part"],"arm");
new Thing("visitor hand",["visitor finger,3",".body part"],"hand");
new Thing("visitor finger",[".body part"],"finger");
new Thing("visitor elbow",[".body part"],"elbow");
new Thing("visitor armpit",["visitor ooze,70%",".soft body part"],"armpit");
new Thing("visitor leg",["visitor foot","visitor knee",".body part"],"leg");
new Thing("visitor foot",["toe,4","visitor ooze,40%",".body part"],"foot");
new Thing("visitor toe",[".body part"],"toe");
new Thing("visitor knee",[".body part"],"knee");
new Thing("visitor head",["visitor mouth","eye,0-4","skull"],"head");
new Thing("visitor eye",["eye flesh","visitor ooze,20%"],"eye");
new Thing("nose",["nostril,2",".body part"],"nose");
new Thing("visitor mouth",["visitor teeth","tongue,2","visitor ooze"],"mouth");
new Thing("visitor teeth",["steel"],"teeth");
new Thing("visitor ooze",["bacteria,40%","organic matter","sulfur"],"ooze");

new Thing("visitor psyche",["visitor thoughts","visitor memories"],"psyche");
new Thing("visitor thoughts",["visitor thought,1-3"],"thoughts");
new Thing("visitor memories",["visitor memory,1-2"],"memories");
new Thing("visitor thought",[],["ACK!!! ACK ACK ACK","ACK ACK AAAACK ACK ACK","ACK, ACKKKKKKKK","AAAAAAAAAACKKKKKKK","Ack.","Ack?","Ack... Ack ack ack.","Ack ack ock ack!","Ack eck.","Ack ACK AAAAACK","AACK, ACK ACK ACK!","AAAAACK ACK ACK ACK","ACKACKACK, ACK!!!","Ackack, ackackackack?","...ack...","Hehuck.","Whoack."]);
new Thing("visitor memory",[],[["Ack ack...","Ack, ack ack...","Ack.","...Ack ack.","Ack ack ack."],["",""," Ack ack ack ack."," Ack."," Ack, ack ack."," Ack ack ack..."," ...ack ack ack."," ...Ack."," Ack."]]);

new Thing("named visitor",[".visitor"],[["B"],["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","!","?",";",",",".",":","/","*","#","¤","+","-","="," "],["rt"],["y","ie","ington","inson","son","","","","","","",""]]);

new Thing("visitor city",["named visitor,0-8",["space animal,0-3",""],"visitor neighborhood,1-8"],"visitor city");
new Thing("visitor neighborhood",["named visitor,0-8",["space animal,0-3",""],"visitor building,2-16"],"neighborhood");
new Thing("visitor building",[["named visitor,0-8",""],"visitor room,1-8"],[["a tall","a wide","a spiralicious","a twisty","a holographic","a composite","a stout","a long","a domed","an underground","a submerged","a gigantic"],[", "],["green","blue","purple","white","gray","translucent","bright","porous","microsthetic","turbified","motorized","hovering","meshed","towered","automated","ridged"],[" "],["glumporium","swapmarket","slickmarket","juicehouse","scienceteria","faceteria","homezone","orbshop","oozeshop","marklorion","hive","holotekt"]]);
new Thing("visitor room",["named visitor,60%","named visitor,30%","named visitor,10%","named visitor,10%","named visitor,10%","space animal,10%","visitor furniture,1-6",".room"],"room");
new Thing("visitor furniture",["abomination,1%","space animal,3%","named visitor,2%","organic matter,5%",["glass","metal","concrete","plastic"]],[["symbio","opto","auto","synchro","thru","ato","ecto","diplo","plasti","pasta","pluta","elu","gubri","capra","lubio","logi","plato","micro","alto","tele","meta","anti","poly","mono","corvo"],["shid","synth","shaver","shist","mizer","mucus","twister","ridger","cutter","mac","maker","ctory","ctamid","chton","leaker","grater","board","frame","table","stand","plug","masher","greeter","mobile","pin","vat","tron","drone","chron","tub","fridge","pool","box","cube","morpher","phraser"]]);
new Thing("visitor installation",["named visitor,0-4",["space animal,0-3",""],"visitor building,1-3"],[["pod","grub","egg","limb","ooze","tendril","bulb","pulp","energy","smoke","hive","moisture","cat"],[" "],["materializer","synthesizer","factory","farm","collector","cultures","pit","fields","crops","barn","vat"]]);
new Thing("visitor ship",["named visitor,1-3","person,20%","space animal,30%","visitor furniture,1-6","metal"],"visitor UFO");


//medieval and ancient
new Thing("medieval continent",["medieval land,1-6","sea,1-5"],["explored continent"]);
new Thing("medieval land",["medieval region,1-10","medieval battlefield,10%",".biome"],[["realm","kingdom","empire","dominion"],[" of "],["G","P","S","St","Sh","B","F","K","Z","Az","Oz"],["","","","r","l"],["u","o","a","e"],["r","sh","nd","st","sd","kl","kt","pl","fr","ck","sh","ff","gg","l","lig","rag","sha","pta","lir","limd","lim","shim","stel"],["i","u","o","oo","e","ee","y","a"],["ll","th","h","k","lm","r","g","gh","n","m","p","s","rg","lg"]]);
new Thing("medieval region",["medieval capital","medieval village,2-6","dungeon,15%","dungeon,5%"],[["hilly","rainy","lush","foggy","desertic","green","tropical","rich","barren","scorched"],[" "],["shire","province","county","parish","pale"]]);

new Thing("ancient continent",["ancient land,1-5","sea,1-5"],["continent"]);
new Thing("ancient land",["ancient plain,0-5",["ancient forest,0-4","ancient jungle,0-4"],"mountain,0-3"],[["hilly","rainy","lush","foggy","desertic","green","tropical","rich","barren","scorched"],[" land"]]);

// => Medieval People

//medieval towns
new Thing("medieval village",["townwall,20%","watchtower,15%","medieval monument,50%","medieval residential area,1-4","medieval commercial area,1-2","medieval temple,0-2","medieval farm,4-8","medieval cemetery,50%","wizard tower,5%"],"village");
new Thing("medieval capital",["castle","townwall","medieval monument,70%","medieval monument,20%","medieval residential area,3-12","medieval mage quarter,50%","medieval mage quarter,20%","medieval temple,1-3","medieval commercial area,2-6","medieval farm,2-6","medieval cemetery"],["stronghold","fortress","fort","hold","palace","main city","citadel"]);

new Thing("castle",["medieval peasant,1-4","medieval noble,0-2","medieval guard,2-8","castle keep","giant monster cage,1%","watchtower,1-6","medieval temple,30%","medieval inn,40%","medieval house,1-4","medieval monument,70%","medieval monument,20%","moat,30%","gatehouse","medieval wall"]);
new Thing("gatehouse",["medieval guard,1-3","portcullis,1-2","wood","medieval wall"]);
new Thing("portcullis",["wood","metal"]);
new Thing("moat",["water,50%","dirt"]);
new Thing("medieval monument",[["stone","marble"]],["fountain","memorial","statue","well","altar"]);
new Thing("townwall",["medieval guard,1-8","watchtower,1-6","medieval wall"]);
new Thing("watchtower",["medieval guard,1-2","medieval chest,30%",".medieval building"]);
new Thing("castle keep",["great hall","noble medieval living quarters,1-3","noble medieval bedroom,2-5",".medieval building"]);
new Thing("great hall",["medieval king,90%","medieval queen,90%","throne,2","wizard,0-3","medieval noble,1-6","medieval guard,1-4","medieval servant,1-4","medieval table","medieval table,60%","medieval chair,3-8","medieval chest,1-4","medieval clutter,0-4","medieval meat,30%","sack of medieval food,0-2","medieval food,0-2","sack of grain,50%","medieval fireplace","medieval fireplace,50%","dog,60%","dog,30%","cat,30%",".medieval room"],"throne room");
new Thing("medieval residential area",["medieval house,3-8"],"housing district");
new Thing("medieval commercial area",["medieval inn,1-2","medieval armor shop,0-2","medieval tool shop,0-2","medieval clothing shop,0-2","medieval butcher shop,0-2","medieval food shop,0-2","medieval apothecary shop,0-2"],"trade district");
new Thing("medieval mage quarter",["wizard tower,1-5","medieval inn,0-1","medieval apothecary shop,0-3"],"mage district");
new Thing("medieval house",["medieval living quarters","medieval bedroom","medieval bedroom,50%",".medieval building"],[["a small","a large","a big","a cozy","a bland","a boring","an old","a new","a freshly-painted","a pretty","an old-fashioned","a creepy","a spooky","a gloomy","a tall","a tiny","a fine","a happy little"],[" hovel"]]);
new Thing("medieval building",["medieval walls","roof"],"building");
new Thing("medieval room",["visitor,0.1%","ghost,0.1%","medieval walls"],"room");
new Thing("medieval walls",["door,1-4","window,0-6",["medieval wall,4","medieval wall,4-8"]],"stone walls");
new Thing("medieval wall",["wood","stone","dirt,20%"],"stone wall");
new Thing("medieval living quarters",["medieval peasant,0-4","medieval pantry","medieval table","medieval table,30%","medieval chair,1-6","medieval chest,0-3","medieval clutter,0-2","medieval meat,30%","sack of medieval food,0-2","medieval food,0-2","sack of grain,50%","medieval fireplace,90%","dog,60%","dog,30%","cat,30%","poultry,10%","insect,70%","insect,40%",".medieval room"],"living quarters");
new Thing("medieval bedroom",["medieval peasant,0-2","medieval bed","medieval bed,20%","medieval table,30%","medieval chair,0-4","medieval chest,0-2","medieval clutter,0-2","medieval fireplace,40%","dog,10%","dog,10%","cat,20%","insect,70%","insect,40%",".medieval room"],"bedroom");
new Thing("medieval pantry",["medieval peasant,10%","medieval meat,0-4","sack of medieval food,0-8","medieval food,0-8","sack of grain,0-6","ale keg,0-3","medieval chest,0-2","medieval clutter,0-2","insect,0-4",".medieval room"],"pantry");
new Thing("noble medieval living quarters",["wizard,10%","medieval noble,0-4","medieval servant,0-3","medieval pantry,0-2","medieval table","medieval table,60%","medieval chair,1-8","medieval chest,1-4","medieval clutter,0-4","medieval meat,30%","sack of medieval food,0-2","medieval food,0-2","sack of grain,50%","medieval fireplace","medieval fireplace,50%","dog,60%","dog,30%","cat,30%",".medieval room"],"living quarters");
new Thing("noble medieval bedroom",["medieval noble,0-2","medieval servant,0-2","medieval bed","medieval bed,20%","medieval table,50%","medieval chair,0-4","medieval chest,1-3","medieval clutter,0-3","medieval fireplace,80%","dog,10%","dog,10%","cat,20%",".medieval room"],"bedroom");
new Thing("medieval fireplace",["fire","ash","wood","stone"],"fireplace");
new Thing("medieval temple",["medieval priest,1-3","medieval noble,0-2","medieval peasant,0-4","medieval altar,1-2","medieval table,70%","medieval bench,2-6","medieval chair,1-3","medieval chest,1-4","medieval clutter,0-4","medieval fireplace,20%",".medieval room"],[["temple of the","church of the","chapel of the","house of the","abbey of the","cathedral of the","shrine of the","sanctuary of the","priory of the"],[" "],["blinding","sacred","holy","unholy","bloody","cursed","marvellous","wondrous","pious","miraculous","endless","unending","undying","infinite","unworldly","worldly","divine","demonic","ghostly","monstrous","tentacled","all-knowing","rational","pretty good","vengeful","hallowed"],[" "],["light","star","beam","sphere","goddess","god","lords","sisterhood","brotherhood","skies","pact","sect","harmony","discord","child","entity","ghost","builders","makers","guide","wit","story","tale","unicorn","flame","fountain","locust","squid","gembaby","father","mother"]]);
new Thing("giant monster cage",[["dragon","sea monster"]],"giant cage");

new Thing("medieval shop",["medieval shopkeeper,1-2","medieval peasant,0-2","medieval noble,40%","medieval table,80%","medieval chair,0-2","medieval chest,0-2","medieval clutter,1-3",".medieval building"],"shop");
new Thing("medieval armor shop",["armor,2-8","medieval weapon,2-8","treasure,30%","anvil",".medieval shop"],[["armors & swords","swords","bows","maces","armor","weapon","blacksmith","forge","equipment","gear"],[" shop"," market"," store"]]);
new Thing("medieval tool shop",["medieval clutter,1-6","medieval chest,1-6",".medieval shop"],[["wares","tools","miscellaneous","utilities","equipment","gear","general"],[" shop"," market"," store"]]);
new Thing("medieval clothing shop",["medieval pants,1-3","medieval shirt,1-3","medieval coat,1-3","medieval underwear,0-2","medieval shoes,1-3","medieval hat,0-3","cloth,1-4","loom",".medieval shop"],[["hat","clothing","outfit","cloth","textiles","coats","cloak","garments","cobbler's"],[" shop"," market"," store"]]);
new Thing("medieval butcher shop",["medieval meat,2-10","medieval food,0-3",".medieval shop"],[["butcher","meat"],[" shop"," market"," store"]]);
new Thing("medieval food shop",["sack of grain,1-6","sack of medieval food,1-6","medieval food,2-5","medieval meat,1-4",".medieval shop"],[["baker's","ingredients","groceries","farmer's","cook's"],[" shop"," market"," store"]]);
new Thing("medieval apothecary shop",["potion,1-8","unusual stone,1-8","unusual plant,1-8","unusual ingredient,0-4","wizard,20%",".medieval shop"],["rare ingredients shop","potion shop","cures and remedies","alchemy essenitals","unusual wares shop","apothecary"]);
new Thing("medieval inn",["medieval innkeeper,1-2","medieval peasant,0-3","medieval guard,0-3","medieval noble,50%","medieval bedroom,2-6","tankard,1-4","ale keg,1-4","medieval table,1-3","medieval chair,2-4","medieval chest,0-2","medieval clutter,1-3",".medieval building"],[["inn of the ","tavern of the "],
["bleeding","smoking","witching","flying","burning","rabid","winking","dead","standing","tasty","meaty","fat","thirsty","hungry","starving","lone","cheerful","singing","dancing","travelling","lost","haunted","cursed","holy","magic","sorcerous","shy","fair","tipsy","drunk","sleeping","snoring","screaming","moaning","iron","resting","sulking","hidden","raving","prancing","filthy","v1","squealing"],[" "],
["walrus","king","queen","princess","prince","bear","witch","wizard","mage","barbarian","shark","dog","cat","castle","fish","rabbit","bull","spider","cake","potion","wanderer","traveller","tree","fairy","pixie","unicorn","dragon","mandrake","tankard","bottle","cobbler","blacksmith","jester","nettle","cookpot","anvil","scholar","monk","idiot","raven","squire","skeleton","beggar","gembaby","pig"]]);
new Thing("wizard tower",["wizard,95%","wizard,20%","medieval servant,30%","unusual ingredient,1-4","medieval table,80%","medieval chair,1-3","medieval chest,1-4","medieval clutter,2-4",".medieval building"]);
new Thing("medieval cemetery",["medieval gravedigger,0-2","medieval person,0-3","medieval grave,10-30","ghost,20%","ghost,10%"],"graveyard");
new Thing("medieval grave",["medieval corpse,98%","ghost,2%","worm,0-3","insect,0-1","rock","dirt"],"grave");


new Thing("medieval chair",["wood","nails,50%"],"chair");
new Thing("medieval bench",["stone"],"bench");
new Thing("tankard",["ale,20%","metal"]);
new Thing("ale keg",["ale,80%","wood","metal"]);
new Thing("medieval altar",["potion,0-3","unusual stone,0-2","unusual ingredient,0-1",["marble","stone"]],"altar");
new Thing("ale",["alcohol"]);
new Thing("loom",["wood frame","metal"],"loom");
new Thing("throne",["cloth","wood","metal"]);
new Thing("medieval table",["wood","nails,50%"],"table");
new Thing("medieval bed",["wood frame","cloth","pillow,0-3"],"bed");
new Thing("medieval chest",[".medieval chest content","wood frame","metal"],["coffer","chest","strongbox"]);
new Thing("medieval chest content",["medieval clutter,0-2",["medieval clutter,0-5","unusual stone,0-2","unusual plant,0-5","unusual ingredient,0-2","potion,0-5","sack of grain,0-3","sack of medieval food,0-3","medieval food,0-5","medieval meat,0-6","treasure,0-2"],"insect,10%","insect,10%"],["chest content"]);
new Thing("medieval clutter",[["metal","wood"]],["spoon","fork","knife","torch","broom","pot","jug","candlestick","goblet","flagon","plate","platter","bowl","ladle","clothes iron","figurine","hammer","tongs","bellows","spigot","axe","pickaxe","saw","hoe","shovel","quill","calipers","oar","paint brush","pitchfork","shears","weight"]);
new Thing("anvil",["steel"]);
new Thing("unusual stone",["rock"],["crystal","bezoar","agate","amber","amethyst","bloodstone","carnelian","garnet","hematite","jade","jasper","lapis","moonstone","obsidian","opal","sapphire","tiger's eye","turquoise","zircon"]);
new Thing("unusual ingredient",["organic matter"],["dragon tooth","dragon claw","dragon scale","unicorn horn","goblin mucus","giant snail shell","troll blood clot","imp nose","fairy fingers","pixie wings","demon tail","behemoth plate","mindsucker lips","slime porridge","ladyfly ocella","spider silk","gold cocoon","silver chrysalis","oaf bladder","angel larva","sugarfey fudge","whale blubber","mummified gembaby","basilisk feather","mage fingernails","screamfiber","brainpod","footface nipple","cephalite eyelashes"]);
new Thing("unusual plant",["plant cell"],["mandrake","myrrh","vervain","lotus","pomegranate","myrtle","blackroot","silkbean","drypod","pigweed","thistle","marigold","mistletoe","spearmint","mugwort","aconite","aloe","amaranth","anise","belladonna","bergamot","bladderwrack","cloves","clover","comphrey","dragonblood","eucalyptus","incense","garlic","ginger","ginseng","hemlock","holly","honeysuckle","licorice","jasmine","juniper","nutmeg","oakmoss","orchid","rue","saffron","sage","vetivert","wormwood","witchgrass","agaric","bolete"]);//http://www.janih.com/lady/herbs/magick/
new Thing("potion",["organic matter","water",["glass bottle","glass jar"]],[["stamina","health","beauty","endurance","strength","energy","lover's","blacksmith's","cook's","queen's","growth","witch's","hunter's","brawler's","knight's","cobbler's","clarity","perception","nimbleness","quickness","squire's","unicorn's","bear's","shark's","moon's","lady's","soldier's","wizard's","rest","sleep","paralysis","stone","shimmer","oil","eloquence","speech","bird's","vapor","void"],[" "],["poultice","salve","potion","elixir","poison","philter","draught","brew","remedy","balm","infusion","tincture","decoction","ointment","cordial","tonic"]]);
new Thing("pile of treasure",["treasure,1-4","gold coin,5-20"]);
new Thing("treasure",["unusual stone,20%","gold"],[["golden","gemmed","ornate","magic","cursed","blessed","enchanted","ancestral","holy","royal","diamond"],[" "],["goblet","cup","ring","necklace","medallion","locket","sword","mirror","shield","crown","trinket","scepter","tiara","casket","helm","figurine","egg","knife","arrow","wand"]]);

new Thing("medieval farm",["medieval house,1-3","medieval peasant,1-4","field,1-8","sack of grain,0-8","dog,50%","cat,10%","horse,30%","horse,30%","horse,30%","poultry,0-3"],"farm");
new Thing("sack of grain",["grain","cloth","worm,5%","worm,5%"],[["sack of "],["oats","wheat","corn","barley","ruined grain","rice","soy beans","rye"]]);
new Thing("sack of medieval food",["organic matter","cloth","worm,5%","worm,5%"],[["sack of "],["tomatoes","potatoes","apples","peanuts","raisins","leeks","dead mice"]]);
new Thing("medieval food",["organic matter","worm,5%"],["tomato","potato","apple","corn cob","roasted leeks","cheese wheel","bread loaf","meat pie","apple pie","peanut pie","fish pie","corn pie","mice pie","sludge pie","honey cake","butter cake","rabbit stew"]);
new Thing("medieval meat",["soft flesh"],[["cured ","prepared ","salted ","smoked ","breaded ","roasted "],["beef","pork","mutton","veal","horse","fish","ham","rabbit","pheasant","chicken","clams","bear"]]);

//dungeons
new Thing("dungeon",["dungeon entrance","dungeon entrance,20%","dungeon entrance,20%","dungeon tower,0-3"],[["sunken","lost","buried","dark","forbidden","unholy","cursed","abandoned","forsaken","forgotten","time-lost","haunted","blood","ghostly","hallowed"],[" "],["catacombs","tomb","pit","tunnels","underground","dungeon","mine","shaft","den","fortress","castle","citadel","temple","cathedral","lair","prison"]]);
new Thing("dungeon building",["dungeon walls"],"building");
new Thing("dungeon walls",["door,20%","door,10%",["dungeon wall,4","dungeon wall,4-8"]],"stone walls");
new Thing("dungeon wall",["stone","dirt,20%"],"stone wall");
new Thing("dungeon clutter",["medieval monument,20%","medieval altar,5%","medieval corpse,3%","medieval corpse,1%","pile of treasure,15%","pile of treasure,10%","treasure,15%","potion,20%","medieval clutter,0-2","medieval chest,0-2","medieval chest,20%","medieval table,5%","medieval table,5%","medieval chair,5%","medieval chair,5%","medieval bed,5%","medieval bed,5%","medieval bench,5%","medieval bench,5%","medieval fireplace,5%"]);
new Thing("dungeon tower",["dungeon life",".dungeon clutter",".dungeon building","roof"],"tower");
new Thing("dungeon passage",["dungeon life",".dungeon clutter","dungeon room,60%","dungeon room,40%","dungeon room,15%",".dungeon building"],[["dark","twisting","damp","hidden","engraved","frozen","submerged"],[" "],["tunnel","corridor","passage","hall"]]);
new Thing("dungeon room",["dungeon life",".dungeon clutter","dungeon passage,60%","dungeon passage,40%","dungeon passage,15%",".dungeon building"],[["dark","tall","damp","engraved","circular","frozen","submerged"],[" "],["hall","room","chamber","alcove","antechamber","cell","gardens","arena"]]);
new Thing("dungeon entrance",["dungeon life,50%",".dungeon clutter","dungeon passage","dungeon passage,20%","dungeon passage,5%",".dungeon building"],["entrance"]);
new Thing("dungeon life",[".dungeon monster","insect,10%"],"life");
new Thing("dungeon monster",[["dragon","ghost,1-3","ghost,1-3","wizard","humanoid creature,1-3","humanoid creature,1-3","fairy,1-3","fairy,1-3","giant bug,1-3","giant bug,1-3","small creature,1-6","small creature,1-6","snake,1-3","bear","space animal,1-3","sea monster"]]);
new Thing("humanoid creature",["medieval weapon,50%","medieval weapon,10%","helmet,30%","armor,40%","armor,20%","armor,10%","medieval clothing set","mammal body","creature thoughts"],[["fel","giant","cursed","undead","decaying","numb","magic-using","steel","obsidian","tribal","berserker","ranger","caster","necromancer","vampiric","master","chieftain","mutated","possessed"],[" "],["goblin","troll","gremlin","gnome","dwarf","catperson","sharkperson","dogperson","footface","cephalite","demon","imp","minotaur","gemperson","zombie"]]);
new Thing("fairy",["fairy body","creature thoughts"],["fairy","pixie","fey","sugarfey","angel","ladyfly"]);
new Thing("fairy body",[["bird wing,2","insect wing,2"],".body"],"body");
new Thing("small creature",["mammal body","creature thoughts"],[["giant","feral","mutated","distorted","rabid","plated","armored","stalking","dashing","mangy"],[" "],["rat","sloth","dog","behemoth","wolf","boar","mindsucker","brainblower","oaf"]]);
new Thing("giant bug",["insect body","creature thoughts"],[["giant","huge","poisonous","mutated","distorted","magic","plated","armored","stalking","dashing"],[" "],["spider","scorpion","mantis","moth","crab","tarantula"]]);
new Thing("creature thoughts",["creature thought,1-2"],["thoughts"]);
new Thing("creature thought",[],["INTRUDER, INTRUDER!","You no get out of here alive.","This one, mine!","I will suck its blood and then feast on its skin.","I will rejoice in its blood!","How skin tears joyfully under my teeth!","Skin, blood, yes!","Flesh. I crave flesh.","Soft, juicy, scrumptious brains!","Dibs on your skull.","Fresh flesh ahead!","None, you get none of the treasure!","I detect you.","Time for a feast.","Adventurers are so rare these days.","I have spotted you. You be dead soon.","Crisp ribcages are the best.","I will suck its eyeballs from their sockets.","I will tear apart its ribs one by one.","I will bathe in its red juice.","I will strip it of its skin.","I will puncture its heart."]);

// => Future
// => Caveman


//meta
new Thing("later",["sorry"],"will do later");
new Thing("error",["sorry"],"Uh oh... It looks like you didn't supply a valid element to create.");
new Thing("sorry",["consolation universe"],"(Sorry!)");
new Thing("consolation universe",[".universe"]);


//this is for the nice people who help support the site.
new Thing("thanks",["can of nightmare","cake","portal"],"Thank you for donating!");