# new Thing(
#   "mote",
#   1,
#   ["float|You float slowly in the wind.", "aggregate/become:lint|You join other motes and form a mass of dust."],
#   [["mote", "mote of dust"], [""]],
#   ["drop"]
# );
# new Thing(
#   "drop",
#   2,
#   ["drip|You drip from an unknown surface to another unknown surface.", "evaporate/become:steam|You turn into a gas !"],
#   [["waterdrop", "droplet", "raindrop"], [""]],
#   ["bubble"]
# );
# new Thing(
#   "bubble",
#   2,
#   ["float|You float up."],
#   [["big ", "small ", "tiny ", ""], ["bubble"]],
#   ["virus"]
# );
# new Thing(
#   "steam",
#   3,
#   ["float|You float slowly in the wind.", "condensate/become:drop|You turn into a mist of waterdrops."],
#   [["vapor", "gas", "cloud", "steam", "fog"], [""]],
#   []
# );
# new Thing(
#   "lint",
#   2,
#   ["float|You float slowly in the wind.", "aggregate/become:pebble|You harden into a solid pebble."],
#   ["piece of lint"],
#   []
# );
# new Thing(
#   "virus",
#   3,
#   ["drift|You drift aimlessly in the ooze.", "infect/become:virus|You spread to a new host."],
#   [["virus"], [" (infecting "], ["a fish", "a person", "a dog", "a cow", "an insect", "a cat", "a bird", "a plant"], [")"]],
#   ["bacteria"]
# );
# new Thing(
#   "bacteria",
#   5,
#   ["drift|You drift aimlessly in the ooze.", "feed|You feed on some smaller organisms."],
#   [["bacteria", "amoeba"], [""]],
#   ["clam", "seed"]
# );
# new Thing(
#   "pebble",
#   3,
#   ["roll|You tumble down./You roll around.", "aggregate/become:rock|With the help of nearby pebbles, you turn into a bigger rock."],
#   [["shiny ", "smooth ", "old ", "small ", "weathered ", ""], ["pebble"]]
# );
# new Thing(
#   "rock",
#   4,
#   ["roll|You fall heavily down the slope of a mountain.", "aggregate/become:mountain|You blend with the bigger rocks around you. You turn into a GODDAMN MOUNTAIN."],
#   [["shiny ", "smooth ", "old ", "big ", "weathered ", ""], ["rock", "stone"]]
# );
# new Thing(
#   "mountain",
#   10,
#   ["be a mountain|YOU'RE A GODDAMN MOUNTAIN.", "aggregate/become:continent|You dig yourself into the ground and expand as much as you can."],
#   [["old ", "tall ", "snowy ", "jagged ", ""], ["mountain"]]
# );
# new Thing(
#   "continent",
#   13,
#   ["be a continent|Well. You're pretty wide and stuff."],
#   [["continent of "], ["Europe", "Asia", "Africa", "Oceania", "North America", "South America", "Antartica"], [""]]
# );
# new Thing(
#   "clam",
#   7,
#   ["open|You open your shell and let some water in.", "build up a pearl|You produce a shiny pearl./You only produce a botched aggregate."],
#   [["clam", "oyster", "scallop", "mussel"], [""]],
#   ["coral", "crustacean"]
# );
# new Thing(
#   "coral",
#   6,
#   ["grow|You extend your polyps."],
#   ["coral"]
# );
# new Thing(
#   "crustacean",
#   9,
#   ["feed|You hunt some small fishes.", "hide|You retreat under a rock."],
#   [["crab", "crayfish", "lobster", "spider crab", "shrimp", "prawn"], [""]],
#   ["fish"]
# );
# new Thing(
#   "fish",
#   10,
#   ["feed|You prey on some smaller fishes.", "hide|You retreat under a rock./You swim swiftly behind some algaes./You bury into the sand."],
#   [["salmon", "trout", "swordfish", "minnow", "anchovy", "sardeen", "eel", "herring", "seahorse", "manta ray", "catfish"], [""]],
#   ["shark", "amphibian"]
# );
# new Thing(
#   "shark",
#   12,
#   ["feed|You eat a fisherman./You swallow some children./You eat a careless swimmer."],
#   [["shark", "hammershark", "basking shark", "tiger shark"], [""]]
# );
# new Thing(
#   "amphibian",
#   12,
#   ["feed|You prey on some flies."],
#   [["frog", "dartfrog", "axolotl", "tree frog", "toad", "bull toad", "salamander"], [""]],
#   ["reptile"]
# );
# new Thing(
#   "reptile",
#   13,
#   ["feed|You hunt some fresh meat.", "bask|You bask in the sun./The sun warms up your scales."],
#   [["lizard", "snake", "komodo dragon", "gecko", "chameleon", "iguana"], [""]],
#   ["dinosaur", "rodent"]
# );
# new Thing(
#   "dinosaur",
#   16,
#   ["feed|You don't care if it runs around screaming or if it's green and leafy. Whatever it is, it's going to be delicious.", "do dino stuff|You ponder about your existence./What is that in the sky ?"],
#   [["tyranosaurus rex", "diplodocus", "brontosaurus", "velociraptor", "iguanodon", "stegosaurus", "pteranodon"], [""]],
#   ["bird"]
# );
# new Thing(
#   "bird",
#   15,
#   ["feed|Oh boy, worms !/Hurray, seeds !", "do bird stuff|Your wings. They're so cool./Your feathers are, like, so pretty."],
#   [["sparrow", "eagle", "seagull", "starling", "crow", "raven", "chicken", "duck", "swan", "flamingo"], [""]]
# );
# new Thing(
#   "rodent",
#   14,
#   ["feed|You eat on various edible-looking things.", "hide|You find shelter in an old tree./You burrow in the earth."],
#   [["hamster", "rat", "mouse", "hare", "rabbit", "shrew", "squirrel"], [""]],
#   ["ungulate", "felid", "canid", "lemur"]
# );
# new Thing(
#   "lemur",
#   16,
#   ["feed|You hunt some bugs./You eat a juicy fruit.", "rest|You fall asleep in a tree."],
#   [["lemur", "aye-aye"], [""]],
#   ["monkey"]
# );
# new Thing(
#   "monkey",
#   18,
#   ["feed|You form a hunt party and bring back some fresh meat./You collect fruits.", "do monkey stuff|You engage in some social networking. Fleas are so delicious./You hit a bunch of stones together. Yeah, that'll never catch on."],
#   [["ape", "monkey", "gorilla", "chimp", "orang-outang"], [""]],
#   ["human"]
# );
# new Thing(
#   "human",
#   20,
#   ["eat|You eat some crisps./You eat a burger./You eat some pizza./You eat a birthday cake./You treat yourself to a fancy restaurant in town./You throw a massive feast with 6 main courses and 4 desserts.", "poop|You use the opportunity to read a mightily enlightening comic strip.", "work|You go to work and spend your day pressing buttons.", "sleep|You find it hard to fall asleep./You close your eyes and try not to think about anything until the sun sets./You had a nightmare./You wonder about the meaning of your life, and then fall asleep.", "have some kids/unlock:child|Alright, you have kids now.", "die/become:corpse|You're dead !"],
#   [["young ", "middle-aged ", "grumpy ", "boring ", "nice ", "ugly ", "bored ", "frustrated ", "stupid ", "average "], ["man", "woman"]]
# );
# new Thing(
#   "corpse",
#   10,
#   ["rot|You decay slowly."],
#   ["corpse"]
# );
# new Thing(
#   "seed",
#   6,
#   ["grow/become:tree,flower,grass/unlock:tree,flower,grass|You make yourself cozy in the surrounding dirt."],
#   ["seed"]
# );
# new Thing(
#   "flower",
#   8,
#   ["grow|You grow some petals./You bask in the sun."],
#   [["flower", "dandelion", "daisy", "rose", "sunflower", "tulip", "daffodil"], [""]]
# );
# new Thing(
#   "grass",
#   8,
#   ["grow|You grow some more blades./You bask in the sun."],
#   [["grass", "weed"], [""]]
# );
# new Thing("tree",25,["grow/unlock:leaf,fruit|You grow some leaves./You gain a few centimeters./You grow a layer of bark./You try to reach the sky with your branches./You produce some flowers./You produce a number of fruits.", "die/become:dead tree|Your heavy fall echoes through the forest."],[["maple tree", "apple tree", "banana tree", "durian tree", "pear tree", "orange tree", "oak", "birch", "pine tree", "sequoia"], [""]]);
# new Thing("fruit",10,["do fruit stuff|You feel something wiggling in you. Silly worm ! Get out of here./You try your best to look tasty, hoping to attract a passerby.", "fall/become:seed|You fall to the ground and start rotting."],[["apple", "banana", "pear", "durian", "orange"], [""]]);
# new Thing("leaf",7,["do leaf stuff|You swing gently in the breeze."],["leaf"]);
# new Thing("dead tree",10,["rot/become:humus|You decay slowly in the humus."],["dead tree"],[]);
# new Thing("humus",7,["do humus stuff|You're feeling pretty humid and moldy today."],["humus"],["insect", "mushroom"]);
# new Thing("insect",9,["feed|You eat a bunch of smaller, stupider bugs./You suck some sap out of a plant.", "get social/become:social insect|You gather with some buddies of yours and form an insect community !"],[["horned", "big", "hairy", "", ""], ["scarab", "aphid", "caterpillar", "flea", "beetle", "fly", "roach", "cicada", "grasshopper", "cricket"], []],[]);
# new Thing("social insect",11,["gather food|You and your squad collect various bits of meats and plants.", "build town|You shape a gigantic city out of mostly digested materials."],[["ant", "wasp", "bee", "hornet", "termite"], []],[]);
