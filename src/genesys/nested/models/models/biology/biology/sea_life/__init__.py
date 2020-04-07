"""
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
"""
