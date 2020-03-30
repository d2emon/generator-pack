from factories.factory.name import NameFactory, random_generator


second_names = ["Aardvark", "Abyssinian", "Addax", "Affenpinscher", "Akbash", "Akita", "Albatross", "Alligator",
                "Alpaca", "Anemone Fish", "Angelfish", "Angora", "Anole", "Ant", "Anteater", "Antelope", "Aoudad",
                "Ape", "Argali", "Armadillo", "Avocet", "Axolot", "Baboon", "Badger", "Balinese", "Bandicoot", "Barb",
                "Barnacle", "Barracuda", "Basilisk", "Bat", "Beagle", "Bear", "Bearded Dragon", "Beaver", "Bee",
                "Beetle", "Bighorn", "Binturong", "Bird", "Birman", "Bison", "Bloodhound", "Boa", "Boar", "Bobcat",
                "Bombay", "Bongo", "Bonobo", "Booby", "Borer", "Budgerigar", "Buffalo", "Bull", "Bull Terrier",
                "Bulldog", "Bullfrog", "Bunny", "Burmese", "Burro", "Butterfly", "Caiman", "Camel", "Canary",
                "Capuchin", "Capybara", "Caracal", "Cardinal", "Caribou", "Cassowary", "Cat", "Caterpillar", "Catfish",
                "Centipede", "Chameleon", "Chamois", "Cheetah", "Chicken", "Chihuahua", "Chimpanzee", "Chinchilla",
                "Chinook", "Chipmunk", "Cichlid", "Civet", "Coati", "Cockroach", "Collie", "Colt", "Cony", "Coral",
                "Cougar", "Cow", "Coyote", "Crab", "Crane", "Crocodile", "Crow", "Cuscus", "Cuttlefish", "Dachshund",
                "Dalmatian", "Darter", "Deer", "Dhole", "Dingo", "Discus", "Dodo", "Doe", "Dog", "Dogfish", "Dolphin",
                "Donkey", "Dormouse", "Dragon", "Dragonfly", "Drever", "Dromedary", "Duck", "Duckbill", "Dugong",
                "Dunker", "Eagle", "Earwig", "Echidna", "Eel", "Egret", "Eland", "Elephant", "Eleuth", "Elk", "Emu",
                "Ermine", "Ewe", "Falcon", "Fawn", "Ferret", "Finch", "Firefinch", "Fish", "Flamingo", "Flounder",
                "Fly", "Fossa", "Fox", "Frigatebird", "Frog", "Fulgorid", "Gar", "Gazelle", "Gecko", "Gemsbok",
                "Gerbil", "Gharial", "Gibbon", "Gila monster", "Giraffe", "Gnu", "Goat", "Goatfish", "Goose", "Gopher",
                "Gorilla", "Grasshopper", "Greyhound", "Grizzly bear", "Ground hog", "Grouse", "Guanaco", "Guinea Pig",
                "Guinea pig", "Guppy", "Hamlet", "Hamster", "Hare", "Harrier", "Hartebeest", "Havanese", "Hedgehog",
                "Heron", "Himalayan", "Hippo", "Hippopotamus", "Hog", "Hornbill", "Hornet", "Horse", "Hound", "Human",
                "Hummingbird", "Hyena", "Ibex", "Ibis", "Iguana", "Impala", "Indri", "Insect", "Jackal", "Jackrabbit",
                "Jaguar", "Javanese", "Jay", "Jellyfish", "Jerboa", "Kakapo", "Kangaroo", "Katydid", "Kid",
                "Kingfisher", "Kinkajou", "Kitten", "Kiwi", "Koala", "Komodo", "Koodoo", "Kookaburra", "Kudu",
                "Labradoodle", "Ladybird", "Lamb", "Lechwe", "Lemming", "Lemur", "Leopard", "Liger", "Lion", "Lionfish",
                "Lizard", "Llama", "Lobster", "Locust", "Longclaw", "Lovebird", "Lynx", "Macaw", "Magpie", "Maltese",
                "Mammoth", "Manatee", "Mandrill", "Mantis", "Mare", "Markhor", "Marmoset", "Marmot", "Marten",
                "Mastiff", "Mastigodryas", "Mayfly", "Meerkat", "Millipede", "Mink", "Mole", "Molly", "Mongoose",
                "Mongrel", "Monkey", "Moorhen", "Moose", "Moth", "Mountain goat", "Mouse", "Mule", "Musk deer",
                "Musk-ox", "Muskrat", "Mustang", "Mynah bird", "Neanderthal", "Newfoundland", "Newt", "Nightingale",
                "Numbat", "Ocelot", "Octopus", "Oedemera", "Okapi", "Olm", "Opossum", "Orang-utan", "Orangutan", "Orca",
                "Oryx", "Ostrich", "Otter", "Owl", "Ox", "Oyster", "Pademelon", "Panda", "Panther", "Parakeet",
                "Parrot", "Peacock", "Peccary", "Pekingese", "Pelican", "Penguin", "Persian", "Pheasant", "Pig", "Pika",
                "Pike", "Piranha", "Platypus", "Pointer", "Polar bear", "Pony", "Poodle", "Porcupine", "Porpoise",
                "Possum", "Prairie dog", "Prawn", "Pronghorn", "Puffin", "Pug", "Puma", "Puppy", "Quagga", "Quail",
                "Quetzal", "Quokka", "Quoll", "Rabbit", "Raccoon", "Ragdoll", "Ram", "Rat", "Rattlesnake", "Raven",
                "Reindeer", "Reptile", "Retriever", "Rhino", "Rhinoceros", "Robin", "Roebuck", "Rottweiler",
                "Salamander", "Saola", "Scorpion", "Seahorse", "Seal", "Serval", "Shark", "Sheep", "Sheepdog", "Shrew",
                "Shrimp", "Siamese", "Siberian", "Silver fox", "Skink", "Skunk", "Sloth", "Slug", "Snail", "Snake",
                "Snowshoe", "Somali", "Spaniel", "Spanish Flag", "Sparrow", "Sparrowhawk", "Spider", "Sponge",
                "Springbok", "Squid", "Squirrel", "Stallion", "Starfish", "Starling", "Steer", "Stingray", "Stoat",
                "Stork", "Sunfish", "Swan", "Tamarin", "Tang", "Tapir", "Tarantula", "Tarsier", "Tayra", "Termite",
                "Terrier", "Tetra", "Tiffany", "Tiger", "Toad", "Tortoise", "Toucan", "Triggerfish", "Tropicbird",
                "Trunkfish", "Tuatara", "Turkey", "Turtle", "Uakari", "Uguisu", "Umbrellabird", "Urchin", "Vicuna",
                "Vole", "Vulture", "Wallaby", "Walrus", "Wapiti", "Warthog", "Wasp", "Waterbuck", "Weasel", "Weaver",
                "Whale", "Whippet", "Wildcat", "Wildebeest", "Wolf", "Wolfhound", "Wolverine", "Wombat", "Woodchuck",
                "Woodlouse", "Woodpecker", "Wrasse", "Yak", "Zebra", "Zebu", "Zonkey", "Zorse"]


class AnimalSpeciesNameGenerator(NameFactory):
    glue = " "


class AnimalSpecies1NameGenerator(AnimalSpeciesNameGenerator):
    data = [
        ["Adelie", "Ainu", "Airedale", "Aldabra", "Almond", "Alpine", "Amazon", "Amber", "Ambush", "Amphibian",
         "Anatolian", "Antler", "Aqua", "Arctic", "Army", "Ash", "Assassin", "Autumn", "Awkward", "Aye", "Azure",
         "Bactrian", "Banded", "Barb-Tailed", "Barn", "Basenji", "Basking", "Basset", "Bavarian", "Bearded",
         "Bedlington", "Beige", "Bernese", "Bichon", "Black", "Blind", "Blizzard", "Blond", "Blonde", "Blue",
         "Bluetick", "Blushing", "Bog", "Bolognese", "Border", "Bornean", "Borneo", "Bottle", "Boxer", "Boykin",
         "Brass", "Bright", "Brilliant", "Bronze", "Brown", "Bull", "Bumble", "Burnt", "Burrowing", "Cairn",
         "Camouflaged", "Carnivorous", "Cavalier", "Cesky", "Charcoal", "Cherry", "Chesapeake", "Chestnut", "Chinstrap",
         "Chocolate", "Cinnamon", "Citrine", "Citron", "Clouded", "Clown", "Clumber", "Coastal", "Cobalt", "Coiled",
         "Collared", "Common", "Copper", "Coral", "Cottontop", "Crab-Eating", "Cream", "Crested", "Crimson", "Cross",
         "Crossed", "Crown", "Crowned", "Curly", "Cyan", "Daffodil", "Dandelion", "Dark", "Deaf", "Desert", "Diamond",
         "Dire", "Doctor", "Dotted", "Dread", "Dreaming", "Dusky", "Dwarf", "Eastern", "Ebony", "Edible", "Eerie",
         "Electric", "Elegant", "Emerald", "Emperor", "Eucalyptus", "Exalted", "Fake", "Fat", "Feathered", "Field",
         "Fire", "Fire-Bellied", "Fishing", "Flame", "Flaming", "Flat", "Flat-Eared", "Flat-Tailed", "Floral",
         "Fluffy-Tailed", "Fluorescent", "Flying", "Forest green", "Foxy", "Frigid", "Frilled", "Fuchsia", "Furry",
         "Fuzzy", "Gentoo", "Ghost", "Giant", "Gilded", "Ginger", "Glacial", "Glass", "Glimmer", "Glorious", "Glow",
         "Gold", "Golden", "Graceful", "Gracious", "Grand", "Gray", "Great", "Greater", "Green", "Grey", "Grizzly",
         "Groaning", "Growling", "Guinea", "Hairless", "Hairy", "Hammerhead", "Harlequin", "Hell", "Herbivorous",
         "Hercules", "Hermit", "Highland", "Honey", "Honeydew", "Hooting", "Horn", "Horned", "Horseshoe", "Howler",
         "Humpback", "Hunting", "Husky", "Ice", "Imperial", "Indigo", "Inferior", "Iris", "Iron", "Ivory", "Jade",
         "Jasmine", "Jasper", "Jester", "Jumbo", "Jungle", "Keel", "Khaki", "Killer", "King", "Komodo", "Lake", "Land",
         "Laughing", "Lava", "Lavender", "Leaf-Tailed", "Lemon", "Leopard", "Liberty", "Light", "Lilac", "Lime",
         "Little", "Livid", "Lonely", "Long-Eared", "Long-Horned", "Long-Tailed", "Lusting", "Magellanic", "Magenta",
         "Magnolia", "Mahogany", "Maine", "Majestic", "Malachite", "Mammoth", "Manatee", "Manta", "Mantis", "Marine",
         "Maritime", "Maroon", "Marsh", "Masked", "Matriarch", "Mauve", "Mellow", "Metallic", "Midget", "Mimic", "Mini",
         "Mint", "Mire", "Mirror", "Moaning", "Mocking", "Monitor", "Moon", "Moray", "Moss", "Mossy", "Mountain", "Mud",
         "Muddy", "Navy", "Noble", "Northern", "Nurse", "Ocean", "Ochre", "Old", "Olive", "Onyx", "Orange", "Orchid",
         "Pack", "Painted", "Pale", "Paradise", "Passive", "Pastel", "Patriarch", "Peach", "Pear", "Pearl", "Pied",
         "Pigmy", "Pine", "Pineapple", "Pink", "Pistachio", "Pixy", "Platinum", "Plum", "Plump", "Poison", "Poisonous",
         "Polar", "Pond", "Pool", "Preying", "Proud", "Prune", "Puffer", "Pumpkin", "Purple", "Puss", "Pygmy", "Quartz",
         "Quiet", "Rainbow", "Raspberry", "Razzmatazz", "Red", "Redwood", "Regal", "Rigid", "River", "Roaring", "Rock",
         "Rockhopper", "Rose", "Rosewood", "Royal", "Royal blue", "Ruby", "Rufous", "Rust", "Sabre-Toothed", "Saffron",
         "Sage", "Saint", "Sand", "Sandy", "Sapphire", "Scarlet", "Scorpion", "Sea", "Sea blue", "Sea green",
         "Seashell", "Sepia", "Shadow", "Shadow blue", "Shaggy", "Shocked", "Shocking", "Shore", "Short-Eared",
         "Short-Horned", "Short-Tailed", "Siamese", "Siberian", "Sienna", "Silent", "Silver", "Single-Horned",
         "Sky blue", "Slayer", "Slender", "Slow", "Smitten", "Smokey", "Snapping", "Snow", "Snowy", "Soldier",
         "Solitary", "Southern", "Spadefooted", "Spear-Tailed", "Spectacled", "Spider", "Spiny", "Spring", "Stag",
         "Stalking", "Star", "Starred", "Steel blue", "Stellers", "Stick", "Storm", "Stormcloud", "Stormy", "Straw",
         "Strawberry", "Striped", "Stunning", "Sumatran", "Summer", "Sun", "Sunglow", "Sunray", "Sunset", "Superior",
         "Supple", "Supreme", "Swamp", "Tan", "Tangelo", "Tangerine", "Tasmanian", "Taupe", "Tawny", "Tea green",
         "Teal", "Terra cotta", "Terror", "Thistle", "Thorny", "Tiger's eye", "Timberwolf", "Titan", "Titanic",
         "Titanium", "Topaz", "Towering", "Tree", "Tulip", "Tundra", "Tuscan", "Tuscany", "Ultramarine", "Umber",
         "Vampire", "Vanilla", "Venomous", "Verdigris", "Vermilion", "Vervet", "Violet", "Violet-blue", "Violet-red",
         "Viridian", "Water", "Wavy", "Weeping", "Western", "Wetland", "Wheat", "Whimpering", "Whiskered", "Whistling",
         "White", "Wild", "Wine", "Winter", "Wisteria", "Wood brown", "Woolly", "Xanadu", "Yellow", "Yellow Orange",
         "Yellow rose", "Yellow-green", "Yelping"],
        second_names,
    ]


class AnimalSpecies2NameGenerator(AnimalSpeciesNameGenerator):
    data = [
        ["Almond-Eared", "Almond-Eyed", "Almond-Bellied", "Almond-Dotted", "Almond-Furred", "Almond-Nosed",
         "Almond-Scaled", "Almond-Striped", "Almond-Tailed", "Amazon-Eared", "Amazon-Eyed", "Amazon-Bellied",
         "Amazon-Dotted", "Amazon-Furred", "Amazon-Nosed", "Amazon-Scaled", "Amazon-Striped", "Amazon-Tailed",
         "Amber-Eared", "Amber-Eyed", "Amber-Bellied", "Amber-Dotted", "Amber-Furred", "Amber-Nosed", "Amber-Scaled",
         "Amber-Striped", "Amber-Tailed", "Ash-Eared", "Ash-Eyed", "Ash-Bellied", "Ash-Dotted", "Ash-Furred",
         "Ash-Nosed", "Ash-Scaled", "Ash-Striped", "Ash-Tailed", "Azure-Eared", "Azure-Eyed", "Azure-Bellied",
         "Azure-Dotted", "Azure-Furred", "Azure-Nosed", "Azure-Scaled", "Azure-Striped", "Azure-Tailed", "Beige-Eared",
         "Beige-Eyed", "Beige-Bellied", "Beige-Dotted", "Beige-Furred", "Beige-Nosed", "Beige-Scaled", "Beige-Striped",
         "Beige-Tailed", "Black-Eared", "Black-Eyed", "Black-Bellied", "Black-Dotted", "Black-Furred", "Black-Nosed",
         "Black-Scaled", "Black-Striped", "Black-Tailed", "Blond-Eared", "Blond-Eyed", "Blond-Bellied", "Blond-Dotted",
         "Blond-Furred", "Blond-Nosed", "Blond-Scaled", "Blond-Striped", "Blond-Tailed", "Blue-Eared", "Blue-Eyed",
         "Blue-Bellied", "Blue-Dotted", "Blue-Furred", "Blue-Nosed", "Blue-Scaled", "Blue-Striped", "Blue-Tailed",
         "Brass-Eared", "Brass-Eyed", "Brass-Bellied", "Brass-Dotted", "Brass-Furred", "Brass-Nosed", "Brass-Scaled",
         "Brass-Striped", "Brass-Tailed", "Bright-Eared", "Bright-Eyed", "Bright-Bellied", "Bright-Dotted",
         "Bright-Furred", "Bright-Nosed", "Bright-Scaled", "Bright-Striped", "Bright-Tailed", "Brilliant-Eared",
         "Brilliant-Eyed", "Brilliant-Bellied", "Brilliant-Dotted", "Brilliant-Furred", "Brilliant-Nosed",
         "Brilliant-Scaled", "Brilliant-Striped", "Brilliant-Tailed", "Bronze-Eared", "Bronze-Eyed", "Bronze-Bellied",
         "Bronze-Dotted", "Bronze-Furred", "Bronze-Nosed", "Bronze-Scaled", "Bronze-Striped", "Bronze-Tailed",
         "Brown-Eared", "Brown-Eyed", "Brown-Bellied", "Brown-Dotted", "Brown-Furred", "Brown-Nosed", "Brown-Scaled",
         "Brown-Striped", "Brown-Tailed", "Charcoal-Eared", "Charcoal-Eyed", "Charcoal-Bellied", "Charcoal-Dotted",
         "Charcoal-Furred", "Charcoal-Nosed", "Charcoal-Scaled", "Charcoal-Striped", "Charcoal-Tailed", "Cherry-Eared",
         "Cherry-Eyed", "Cherry-Bellied", "Cherry-Dotted", "Cherry-Furred", "Cherry-Nosed", "Cherry-Scaled",
         "Cherry-Striped", "Cherry-Tailed", "Chestnut-Eared", "Chestnut-Eyed", "Chestnut-Bellied", "Chestnut-Dotted",
         "Chestnut-Furred", "Chestnut-Nosed", "Chestnut-Scaled", "Chestnut-Striped", "Chestnut-Tailed",
         "Chocolate-Eared", "Chocolate-Eyed", "Chocolate-Bellied", "Chocolate-Dotted", "Chocolate-Furred",
         "Chocolate-Nosed", "Chocolate-Scaled", "Chocolate-Striped", "Chocolate-Tailed", "Cinnamon-Eared",
         "Cinnamon-Eyed", "Cinnamon-Bellied", "Cinnamon-Dotted", "Cinnamon-Furred", "Cinnamon-Nosed", "Cinnamon-Scaled",
         "Cinnamon-Striped", "Cinnamon-Tailed", "Citrine-Eared", "Citrine-Eyed", "Citrine-Bellied", "Citrine-Dotted",
         "Citrine-Furred", "Citrine-Nosed", "Citrine-Scaled", "Citrine-Striped", "Citrine-Tailed", "Citron-Eared",
         "Citron-Eyed", "Citron-Bellied", "Citron-Dotted", "Citron-Furred", "Citron-Nosed", "Citron-Scaled",
         "Citron-Striped", "Citron-Tailed", "Cobalt-Eared", "Cobalt-Eyed", "Cobalt-Bellied", "Cobalt-Dotted",
         "Cobalt-Furred", "Cobalt-Nosed", "Cobalt-Scaled", "Cobalt-Striped", "Cobalt-Tailed", "Copper-Eared",
         "Copper-Eyed", "Copper-Bellied", "Copper-Dotted", "Copper-Furred", "Copper-Nosed", "Copper-Scaled",
         "Copper-Striped", "Copper-Tailed", "Coral-Eared", "Coral-Eyed", "Coral-Bellied", "Coral-Dotted",
         "Coral-Furred", "Coral-Nosed", "Coral-Scaled", "Coral-Striped", "Coral-Tailed", "Cream-Eared", "Cream-Eyed",
         "Cream-Bellied", "Cream-Dotted", "Cream-Furred", "Cream-Nosed", "Cream-Scaled", "Cream-Striped",
         "Cream-Tailed", "Crimson-Eared", "Crimson-Eyed", "Crimson-Bellied", "Crimson-Dotted", "Crimson-Furred",
         "Crimson-Nosed", "Crimson-Scaled", "Crimson-Striped", "Crimson-Tailed", "Cyan-Eared", "Cyan-Eyed",
         "Cyan-Bellied", "Cyan-Dotted", "Cyan-Furred", "Cyan-Nosed", "Cyan-Scaled", "Cyan-Striped", "Cyan-Tailed",
         "Daffodil-Eared", "Daffodil-Eyed", "Daffodil-Bellied", "Daffodil-Dotted", "Daffodil-Furred", "Daffodil-Nosed",
         "Daffodil-Scaled", "Daffodil-Striped", "Daffodil-Tailed", "Dandelion-Eared", "Dandelion-Eyed",
         "Dandelion-Bellied", "Dandelion-Dotted", "Dandelion-Furred", "Dandelion-Nosed", "Dandelion-Scaled",
         "Dandelion-Striped", "Dandelion-Tailed", "Dark-Eared", "Dark-Eyed", "Dark-Bellied", "Dark-Dotted",
         "Dark-Furred", "Dark-Nosed", "Dark-Scaled", "Dark-Striped", "Dark-Tailed", "Diamond-Eared", "Diamond-Eyed",
         "Diamond-Bellied", "Diamond-Dotted", "Diamond-Furred", "Diamond-Nosed", "Diamond-Scaled", "Diamond-Striped",
         "Diamond-Tailed", "Ebony-Eared", "Ebony-Eyed", "Ebony-Bellied", "Ebony-Dotted", "Ebony-Furred", "Ebony-Nosed",
         "Ebony-Scaled", "Ebony-Striped", "Ebony-Tailed", "Eerie-Eared", "Eerie-Eyed", "Eerie-Bellied", "Eerie-Dotted",
         "Eerie-Furred", "Eerie-Nosed", "Eerie-Scaled", "Eerie-Striped", "Eerie-Tailed", "Electric-Eared",
         "Electric-Eyed", "Electric-Bellied", "Electric-Dotted", "Electric-Furred", "Electric-Nosed", "Electric-Scaled",
         "Electric-Striped", "Electric-Tailed", "Emerald-Eared", "Emerald-Eyed", "Emerald-Bellied", "Emerald-Dotted",
         "Emerald-Furred", "Emerald-Nosed", "Emerald-Scaled", "Emerald-Striped", "Emerald-Tailed", "Eucalyptus-Eared",
         "Eucalyptus-Eyed", "Eucalyptus-Bellied", "Eucalyptus-Dotted", "Eucalyptus-Furred", "Eucalyptus-Nosed",
         "Eucalyptus-Scaled", "Eucalyptus-Striped", "Eucalyptus-Tailed", "Flame-Eared", "Flame-Eyed", "Flame-Bellied",
         "Flame-Dotted", "Flame-Furred", "Flame-Nosed", "Flame-Scaled", "Flame-Striped", "Flame-Tailed", "Floral-Eared",
         "Floral-Eyed", "Floral-Bellied", "Floral-Dotted", "Floral-Furred", "Floral-Nosed", "Floral-Scaled",
         "Floral-Striped", "Floral-Tailed", "Forest green-Eared", "Forest green-Eyed", "Forest green-Bellied",
         "Forest green-Dotted", "Forest green-Furred", "Forest green-Nosed", "Forest green-Scaled",
         "Forest green-Striped", "Forest green-Tailed", "Fuchsia-Eared", "Fuchsia-Eyed", "Fuchsia-Bellied",
         "Fuchsia-Dotted", "Fuchsia-Furred", "Fuchsia-Nosed", "Fuchsia-Scaled", "Fuchsia-Striped", "Fuchsia-Tailed",
         "Ginger-Eared", "Ginger-Eyed", "Ginger-Bellied", "Ginger-Dotted", "Ginger-Furred", "Ginger-Nosed",
         "Ginger-Scaled", "Ginger-Striped", "Ginger-Tailed", "Golden-Eared", "Golden-Eyed", "Golden-Bellied",
         "Golden-Dotted", "Golden-Furred", "Golden-Nosed", "Golden-Scaled", "Golden-Striped", "Golden-Tailed",
         "Gray-Eared", "Gray-Eyed", "Gray-Bellied", "Gray-Dotted", "Gray-Furred", "Gray-Nosed", "Gray-Scaled",
         "Gray-Striped", "Gray-Tailed", "Green-Eared", "Green-Eyed", "Green-Bellied", "Green-Dotted", "Green-Furred",
         "Green-Nosed", "Green-Scaled", "Green-Striped", "Green-Tailed", "Harlequin-Eared", "Harlequin-Eyed",
         "Harlequin-Bellied", "Harlequin-Dotted", "Harlequin-Furred", "Harlequin-Nosed", "Harlequin-Scaled",
         "Harlequin-Striped", "Harlequin-Tailed", "Honeydew-Eared", "Honeydew-Eyed", "Honeydew-Bellied",
         "Honeydew-Dotted", "Honeydew-Furred", "Honeydew-Nosed", "Honeydew-Scaled", "Honeydew-Striped",
         "Honeydew-Tailed", "Indigo-Eared", "Indigo-Eyed", "Indigo-Bellied", "Indigo-Dotted", "Indigo-Furred",
         "Indigo-Nosed", "Indigo-Scaled", "Indigo-Striped", "Indigo-Tailed", "Iris-Eared", "Iris-Eyed", "Iris-Bellied",
         "Iris-Dotted", "Iris-Furred", "Iris-Nosed", "Iris-Scaled", "Iris-Striped", "Iris-Tailed", "Ivory-Eared",
         "Ivory-Eyed", "Ivory-Bellied", "Ivory-Dotted", "Ivory-Furred", "Ivory-Nosed", "Ivory-Scaled", "Ivory-Striped",
         "Ivory-Tailed", "Jade-Eared", "Jade-Eyed", "Jade-Bellied", "Jade-Dotted", "Jade-Furred", "Jade-Nosed",
         "Jade-Scaled", "Jade-Striped", "Jade-Tailed", "Jasmine-Eared", "Jasmine-Eyed", "Jasmine-Bellied",
         "Jasmine-Dotted", "Jasmine-Furred", "Jasmine-Nosed", "Jasmine-Scaled", "Jasmine-Striped", "Jasmine-Tailed",
         "Jasper-Eared", "Jasper-Eyed", "Jasper-Bellied", "Jasper-Dotted", "Jasper-Furred", "Jasper-Nosed",
         "Jasper-Scaled", "Jasper-Striped", "Jasper-Tailed", "Khaki-Eared", "Khaki-Eyed", "Khaki-Bellied",
         "Khaki-Dotted", "Khaki-Furred", "Khaki-Nosed", "Khaki-Scaled", "Khaki-Striped", "Khaki-Tailed", "Lava-Eared",
         "Lava-Eyed", "Lava-Bellied", "Lava-Dotted", "Lava-Furred", "Lava-Nosed", "Lava-Scaled", "Lava-Striped",
         "Lava-Tailed", "Lavender-Eared", "Lavender-Eyed", "Lavender-Bellied", "Lavender-Dotted", "Lavender-Furred",
         "Lavender-Nosed", "Lavender-Scaled", "Lavender-Striped", "Lavender-Tailed", "Lemon-Eared", "Lemon-Eyed",
         "Lemon-Bellied", "Lemon-Dotted", "Lemon-Furred", "Lemon-Nosed", "Lemon-Scaled", "Lemon-Striped",
         "Lemon-Tailed", "Light-Eared", "Light-Eyed", "Light-Bellied", "Light-Dotted", "Light-Furred", "Light-Nosed",
         "Light-Scaled", "Light-Striped", "Light-Tailed", "Lilac-Eared", "Lilac-Eyed", "Lilac-Bellied", "Lilac-Dotted",
         "Lilac-Furred", "Lilac-Nosed", "Lilac-Scaled", "Lilac-Striped", "Lilac-Tailed", "Lime-Eared", "Lime-Eyed",
         "Lime-Bellied", "Lime-Dotted", "Lime-Furred", "Lime-Nosed", "Lime-Scaled", "Lime-Striped", "Lime-Tailed",
         "Livid-Eared", "Livid-Eyed", "Livid-Bellied", "Livid-Dotted", "Livid-Furred", "Livid-Nosed", "Livid-Scaled",
         "Livid-Striped", "Livid-Tailed", "Magenta-Eared", "Magenta-Eyed", "Magenta-Bellied", "Magenta-Dotted",
         "Magenta-Furred", "Magenta-Nosed", "Magenta-Scaled", "Magenta-Striped", "Magenta-Tailed", "Magnolia-Eared",
         "Magnolia-Eyed", "Magnolia-Bellied", "Magnolia-Dotted", "Magnolia-Furred", "Magnolia-Nosed", "Magnolia-Scaled",
         "Magnolia-Striped", "Magnolia-Tailed", "Mahogany-Eared", "Mahogany-Eyed", "Mahogany-Bellied",
         "Mahogany-Dotted", "Mahogany-Furred", "Mahogany-Nosed", "Mahogany-Scaled", "Mahogany-Striped",
         "Mahogany-Tailed", "Malachite-Eared", "Malachite-Eyed", "Malachite-Bellied", "Malachite-Dotted",
         "Malachite-Furred", "Malachite-Nosed", "Malachite-Scaled", "Malachite-Striped", "Malachite-Tailed",
         "Manatee-Eared", "Manatee-Eyed", "Manatee-Bellied", "Manatee-Dotted", "Manatee-Furred", "Manatee-Nosed",
         "Manatee-Scaled", "Manatee-Striped", "Manatee-Tailed", "Mantis-Eared", "Mantis-Eyed", "Mantis-Bellied",
         "Mantis-Dotted", "Mantis-Furred", "Mantis-Nosed", "Mantis-Scaled", "Mantis-Striped", "Mantis-Tailed",
         "Maroon-Eared", "Maroon-Eyed", "Maroon-Bellied", "Maroon-Dotted", "Maroon-Furred", "Maroon-Nosed",
         "Maroon-Scaled", "Maroon-Striped", "Maroon-Tailed", "Mauve-Eared", "Mauve-Eyed", "Mauve-Bellied",
         "Mauve-Dotted", "Mauve-Furred", "Mauve-Nosed", "Mauve-Scaled", "Mauve-Striped", "Mauve-Tailed", "Mellow-Eared",
         "Mellow-Eyed", "Mellow-Bellied", "Mellow-Dotted", "Mellow-Furred", "Mellow-Nosed", "Mellow-Scaled",
         "Mellow-Striped", "Mellow-Tailed", "Metallic-Eared", "Metallic-Eyed", "Metallic-Bellied", "Metallic-Dotted",
         "Metallic-Furred", "Metallic-Nosed", "Metallic-Scaled", "Metallic-Striped", "Metallic-Tailed", "Mint-Eared",
         "Mint-Eyed", "Mint-Bellied", "Mint-Dotted", "Mint-Furred", "Mint-Nosed", "Mint-Scaled", "Mint-Striped",
         "Mint-Tailed", "Moss-Eared", "Moss-Eyed", "Moss-Bellied", "Moss-Dotted", "Moss-Furred", "Moss-Nosed",
         "Moss-Scaled", "Moss-Striped", "Moss-Tailed", "Navy-Eared", "Navy-Eyed", "Navy-Bellied", "Navy-Dotted",
         "Navy-Furred", "Navy-Nosed", "Navy-Scaled", "Navy-Striped", "Navy-Tailed", "Ocean-Eared", "Ocean-Eyed",
         "Ocean-Bellied", "Ocean-Dotted", "Ocean-Furred", "Ocean-Nosed", "Ocean-Scaled", "Ocean-Striped",
         "Ocean-Tailed", "Ochre-Eared", "Ochre-Eyed", "Ochre-Bellied", "Ochre-Dotted", "Ochre-Furred", "Ochre-Nosed",
         "Ochre-Scaled", "Ochre-Striped", "Ochre-Tailed", "Olive-Eared", "Olive-Eyed", "Olive-Bellied", "Olive-Dotted",
         "Olive-Furred", "Olive-Nosed", "Olive-Scaled", "Olive-Striped", "Olive-Tailed", "Onyx-Eared", "Onyx-Eyed",
         "Onyx-Bellied", "Onyx-Dotted", "Onyx-Furred", "Onyx-Nosed", "Onyx-Scaled", "Onyx-Striped", "Onyx-Tailed",
         "Orange-Eared", "Orange-Eyed", "Orange-Bellied", "Orange-Dotted", "Orange-Furred", "Orange-Nosed",
         "Orange-Scaled", "Orange-Striped", "Orange-Tailed", "Orchid-Eared", "Orchid-Eyed", "Orchid-Bellied",
         "Orchid-Dotted", "Orchid-Furred", "Orchid-Nosed", "Orchid-Scaled", "Orchid-Striped", "Orchid-Tailed",
         "Pale-Eared", "Pale-Eyed", "Pale-Bellied", "Pale-Dotted", "Pale-Furred", "Pale-Nosed", "Pale-Scaled",
         "Pale-Striped", "Pale-Tailed", "Paradise-Eared", "Paradise-Eyed", "Paradise-Bellied", "Paradise-Dotted",
         "Paradise-Furred", "Paradise-Nosed", "Paradise-Scaled", "Paradise-Striped", "Paradise-Tailed", "Pastel-Eared",
         "Pastel-Eyed", "Pastel-Bellied", "Pastel-Dotted", "Pastel-Furred", "Pastel-Nosed", "Pastel-Scaled",
         "Pastel-Striped", "Pastel-Tailed", "Patriarch-Eared", "Patriarch-Eyed", "Patriarch-Bellied",
         "Patriarch-Dotted", "Patriarch-Furred", "Patriarch-Nosed", "Patriarch-Scaled", "Patriarch-Striped",
         "Patriarch-Tailed", "Peach-Eared", "Peach-Eyed", "Peach-Bellied", "Peach-Dotted", "Peach-Furred",
         "Peach-Nosed", "Peach-Scaled", "Peach-Striped", "Peach-Tailed", "Pear-Eared", "Pear-Eyed", "Pear-Bellied",
         "Pear-Dotted", "Pear-Furred", "Pear-Nosed", "Pear-Scaled", "Pear-Striped", "Pear-Tailed", "Pearl-Eared",
         "Pearl-Eyed", "Pearl-Bellied", "Pearl-Dotted", "Pearl-Furred", "Pearl-Nosed", "Pearl-Scaled", "Pearl-Striped",
         "Pearl-Tailed", "Pine-Eared", "Pine-Eyed", "Pine-Bellied", "Pine-Dotted", "Pine-Furred", "Pine-Nosed",
         "Pine-Scaled", "Pine-Striped", "Pine-Tailed", "Pineapple-Eared", "Pineapple-Eyed", "Pineapple-Bellied",
         "Pineapple-Dotted", "Pineapple-Furred", "Pineapple-Nosed", "Pineapple-Scaled", "Pineapple-Striped",
         "Pineapple-Tailed", "Pink-Eared", "Pink-Eyed", "Pink-Bellied", "Pink-Dotted", "Pink-Furred", "Pink-Nosed",
         "Pink-Scaled", "Pink-Striped", "Pink-Tailed", "Pistachio-Eared", "Pistachio-Eyed", "Pistachio-Bellied",
         "Pistachio-Dotted", "Pistachio-Furred", "Pistachio-Nosed", "Pistachio-Scaled", "Pistachio-Striped",
         "Pistachio-Tailed", "Platinum-Eared", "Platinum-Eyed", "Platinum-Bellied", "Platinum-Dotted",
         "Platinum-Furred", "Platinum-Nosed", "Platinum-Scaled", "Platinum-Striped", "Platinum-Tailed", "Plum-Eared",
         "Plum-Eyed", "Plum-Bellied", "Plum-Dotted", "Plum-Furred", "Plum-Nosed", "Plum-Scaled", "Plum-Striped",
         "Plum-Tailed", "Prune-Eared", "Prune-Eyed", "Prune-Bellied", "Prune-Dotted", "Prune-Furred", "Prune-Nosed",
         "Prune-Scaled", "Prune-Striped", "Prune-Tailed", "Pumpkin-Eared", "Pumpkin-Eyed", "Pumpkin-Bellied",
         "Pumpkin-Dotted", "Pumpkin-Furred", "Pumpkin-Nosed", "Pumpkin-Scaled", "Pumpkin-Striped", "Pumpkin-Tailed",
         "Purple-Eared", "Purple-Eyed", "Purple-Bellied", "Purple-Dotted", "Purple-Furred", "Purple-Nosed",
         "Purple-Scaled", "Purple-Striped", "Purple-Tailed", "Quartz-Eared", "Quartz-Eyed", "Quartz-Bellied",
         "Quartz-Dotted", "Quartz-Furred", "Quartz-Nosed", "Quartz-Scaled", "Quartz-Striped", "Quartz-Tailed",
         "Raspberry-Eared", "Raspberry-Eyed", "Raspberry-Bellied", "Raspberry-Dotted", "Raspberry-Furred",
         "Raspberry-Nosed", "Raspberry-Scaled", "Raspberry-Striped", "Raspberry-Tailed", "Razzmatazz-Eared",
         "Razzmatazz-Eyed", "Razzmatazz-Bellied", "Razzmatazz-Dotted", "Razzmatazz-Furred", "Razzmatazz-Nosed",
         "Razzmatazz-Scaled", "Razzmatazz-Striped", "Razzmatazz-Tailed", "Red-Eared", "Red-Eyed", "Red-Bellied",
         "Red-Dotted", "Red-Furred", "Red-Nosed", "Red-Scaled", "Red-Striped", "Red-Tailed", "Redwood-Eared",
         "Redwood-Eyed", "Redwood-Bellied", "Redwood-Dotted", "Redwood-Furred", "Redwood-Nosed", "Redwood-Scaled",
         "Redwood-Striped", "Redwood-Tailed", "Rose-Eared", "Rose-Eyed", "Rose-Bellied", "Rose-Dotted", "Rose-Furred",
         "Rose-Nosed", "Rose-Scaled", "Rose-Striped", "Rose-Tailed", "Rosewood-Eared", "Rosewood-Eyed",
         "Rosewood-Bellied", "Rosewood-Dotted", "Rosewood-Furred", "Rosewood-Nosed", "Rosewood-Scaled",
         "Rosewood-Striped", "Rosewood-Tailed", "Royal blue-Eared", "Royal blue-Eyed", "Royal blue-Bellied",
         "Royal blue-Dotted", "Royal blue-Furred", "Royal blue-Nosed", "Royal blue-Scaled", "Royal blue-Striped",
         "Royal blue-Tailed", "Ruby-Eared", "Ruby-Eyed", "Ruby-Bellied", "Ruby-Dotted", "Ruby-Furred", "Ruby-Nosed",
         "Ruby-Scaled", "Ruby-Striped", "Ruby-Tailed", "Rufous-Eared", "Rufous-Eyed", "Rufous-Bellied", "Rufous-Dotted",
         "Rufous-Furred", "Rufous-Nosed", "Rufous-Scaled", "Rufous-Striped", "Rufous-Tailed", "Rust-Eared", "Rust-Eyed",
         "Rust-Bellied", "Rust-Dotted", "Rust-Furred", "Rust-Nosed", "Rust-Scaled", "Rust-Striped", "Rust-Tailed",
         "Saffron-Eared", "Saffron-Eyed", "Saffron-Bellied", "Saffron-Dotted", "Saffron-Furred", "Saffron-Nosed",
         "Saffron-Scaled", "Saffron-Striped", "Saffron-Tailed", "Sage-Eared", "Sage-Eyed", "Sage-Bellied",
         "Sage-Dotted", "Sage-Furred", "Sage-Nosed", "Sage-Scaled", "Sage-Striped", "Sage-Tailed", "Sapphire-Eared",
         "Sapphire-Eyed", "Sapphire-Bellied", "Sapphire-Dotted", "Sapphire-Furred", "Sapphire-Nosed", "Sapphire-Scaled",
         "Sapphire-Striped", "Sapphire-Tailed", "Scarlet-Eared", "Scarlet-Eyed", "Scarlet-Bellied", "Scarlet-Dotted",
         "Scarlet-Furred", "Scarlet-Nosed", "Scarlet-Scaled", "Scarlet-Striped", "Scarlet-Tailed", "Sea blue-Eared",
         "Sea blue-Eyed", "Sea blue-Bellied", "Sea blue-Dotted", "Sea blue-Furred", "Sea blue-Nosed", "Sea blue-Scaled",
         "Sea blue-Striped", "Sea blue-Tailed", "Sea green-Eared", "Sea green-Eyed", "Sea green-Bellied",
         "Sea green-Dotted", "Sea green-Furred", "Sea green-Nosed", "Sea green-Scaled", "Sea green-Striped",
         "Sea green-Tailed", "Seashell-Eared", "Seashell-Eyed", "Seashell-Bellied", "Seashell-Dotted",
         "Seashell-Furred", "Seashell-Nosed", "Seashell-Scaled", "Seashell-Striped", "Seashell-Tailed", "Sepia-Eared",
         "Sepia-Eyed", "Sepia-Bellied", "Sepia-Dotted", "Sepia-Furred", "Sepia-Nosed", "Sepia-Scaled", "Sepia-Striped",
         "Sepia-Tailed", "Shadow blue-Eared", "Shadow blue-Eyed", "Shadow blue-Bellied", "Shadow blue-Dotted",
         "Shadow blue-Furred", "Shadow blue-Nosed", "Shadow blue-Scaled", "Shadow blue-Striped", "Shadow blue-Tailed",
         "Shadow-Eared", "Shadow-Eyed", "Shadow-Bellied", "Shadow-Dotted", "Shadow-Furred", "Shadow-Nosed",
         "Shadow-Scaled", "Shadow-Striped", "Shadow-Tailed", "Sienna-Eared", "Sienna-Eyed", "Sienna-Bellied",
         "Sienna-Dotted", "Sienna-Furred", "Sienna-Nosed", "Sienna-Scaled", "Sienna-Striped", "Sienna-Tailed",
         "Silver-Eared", "Silver-Eyed", "Silver-Bellied", "Silver-Dotted", "Silver-Furred", "Silver-Nosed",
         "Silver-Scaled", "Silver-Striped", "Silver-Tailed", "Sky blue-Eared", "Sky blue-Eyed", "Sky blue-Bellied",
         "Sky blue-Dotted", "Sky blue-Furred", "Sky blue-Nosed", "Sky blue-Scaled", "Sky blue-Striped",
         "Sky blue-Tailed", "Smitten-Eared", "Smitten-Eyed", "Smitten-Bellied", "Smitten-Dotted", "Smitten-Furred",
         "Smitten-Nosed", "Smitten-Scaled", "Smitten-Striped", "Smitten-Tailed", "Smokey-Eared", "Smokey-Eyed",
         "Smokey-Bellied", "Smokey-Dotted", "Smokey-Furred", "Smokey-Nosed", "Smokey-Scaled", "Smokey-Striped",
         "Smokey-Tailed", "Snow-Eared", "Snow-Eyed", "Snow-Bellied", "Snow-Dotted", "Snow-Furred", "Snow-Nosed",
         "Snow-Scaled", "Snow-Striped", "Snow-Tailed", "Steel blue-Eared", "Steel blue-Eyed", "Steel blue-Bellied",
         "Steel blue-Dotted", "Steel blue-Furred", "Steel blue-Nosed", "Steel blue-Scaled", "Steel blue-Striped",
         "Steel blue-Tailed", "Stormcloud-Eared", "Stormcloud-Eyed", "Stormcloud-Bellied", "Stormcloud-Dotted",
         "Stormcloud-Furred", "Stormcloud-Nosed", "Stormcloud-Scaled", "Stormcloud-Striped", "Stormcloud-Tailed",
         "Straw-Eared", "Straw-Eyed", "Straw-Bellied", "Straw-Dotted", "Straw-Furred", "Straw-Nosed", "Straw-Scaled",
         "Straw-Striped", "Straw-Tailed", "Strawberry-Eared", "Strawberry-Eyed", "Strawberry-Bellied",
         "Strawberry-Dotted", "Strawberry-Furred", "Strawberry-Nosed", "Strawberry-Scaled", "Strawberry-Striped",
         "Strawberry-Tailed", "Sunglow-Eared", "Sunglow-Eyed", "Sunglow-Bellied", "Sunglow-Dotted", "Sunglow-Furred",
         "Sunglow-Nosed", "Sunglow-Scaled", "Sunglow-Striped", "Sunglow-Tailed", "Sunray-Eared", "Sunray-Eyed",
         "Sunray-Bellied", "Sunray-Dotted", "Sunray-Furred", "Sunray-Nosed", "Sunray-Scaled", "Sunray-Striped",
         "Sunray-Tailed", "Sunset-Eared", "Sunset-Eyed", "Sunset-Bellied", "Sunset-Dotted", "Sunset-Furred",
         "Sunset-Nosed", "Sunset-Scaled", "Sunset-Striped", "Sunset-Tailed", "Tan-Eared", "Tan-Eyed", "Tan-Bellied",
         "Tan-Dotted", "Tan-Furred", "Tan-Nosed", "Tan-Scaled", "Tan-Striped", "Tan-Tailed", "Tangelo-Eared",
         "Tangelo-Eyed", "Tangelo-Bellied", "Tangelo-Dotted", "Tangelo-Furred", "Tangelo-Nosed", "Tangelo-Scaled",
         "Tangelo-Striped", "Tangelo-Tailed", "Tangerine-Eared", "Tangerine-Eyed", "Tangerine-Bellied",
         "Tangerine-Dotted", "Tangerine-Furred", "Tangerine-Nosed", "Tangerine-Scaled", "Tangerine-Striped",
         "Tangerine-Tailed", "Taupe-Eared", "Taupe-Eyed", "Taupe-Bellied", "Taupe-Dotted", "Taupe-Furred",
         "Taupe-Nosed", "Taupe-Scaled", "Taupe-Striped", "Taupe-Tailed", "Tea green-Eared", "Tea green-Eyed",
         "Tea green-Bellied", "Tea green-Dotted", "Tea green-Furred", "Tea green-Nosed", "Tea green-Scaled",
         "Tea green-Striped", "Tea green-Tailed", "Teal-Eared", "Teal-Eyed", "Teal-Bellied", "Teal-Dotted",
         "Teal-Furred", "Teal-Nosed", "Teal-Scaled", "Teal-Striped", "Teal-Tailed", "Terra cotta-Eared",
         "Terra cotta-Eyed", "Terra cotta-Bellied", "Terra cotta-Dotted", "Terra cotta-Furred", "Terra cotta-Nosed",
         "Terra cotta-Scaled", "Terra cotta-Striped", "Terra cotta-Tailed", "Thistle-Eared", "Thistle-Eyed",
         "Thistle-Bellied", "Thistle-Dotted", "Thistle-Furred", "Thistle-Nosed", "Thistle-Scaled", "Thistle-Striped",
         "Thistle-Tailed", "Tiger's eye-Eared", "Tiger's eye-Eyed", "Tiger's eye-Bellied", "Tiger's eye-Dotted",
         "Tiger's eye-Furred", "Tiger's eye-Nosed", "Tiger's eye-Scaled", "Tiger's eye-Striped", "Tiger's eye-Tailed",
         "Timberwolf-Eared", "Timberwolf-Eyed", "Timberwolf-Bellied", "Timberwolf-Dotted", "Timberwolf-Furred",
         "Timberwolf-Nosed", "Timberwolf-Scaled", "Timberwolf-Striped", "Timberwolf-Tailed", "Titanium-Eared",
         "Titanium-Eyed", "Titanium-Bellied", "Titanium-Dotted", "Titanium-Furred", "Titanium-Nosed", "Titanium-Scaled",
         "Titanium-Striped", "Titanium-Tailed", "Topaz-Eared", "Topaz-Eyed", "Topaz-Bellied", "Topaz-Dotted",
         "Topaz-Furred", "Topaz-Nosed", "Topaz-Scaled", "Topaz-Striped", "Topaz-Tailed", "Tulip-Eared", "Tulip-Eyed",
         "Tulip-Bellied", "Tulip-Dotted", "Tulip-Furred", "Tulip-Nosed", "Tulip-Scaled", "Tulip-Striped",
         "Tulip-Tailed", "Tuscan-Eared", "Tuscan-Eyed", "Tuscan-Bellied", "Tuscan-Dotted", "Tuscan-Furred",
         "Tuscan-Nosed", "Tuscan-Scaled", "Tuscan-Striped", "Tuscan-Tailed", "Tuscany-Eared", "Tuscany-Eyed",
         "Tuscany-Bellied", "Tuscany-Dotted", "Tuscany-Furred", "Tuscany-Nosed", "Tuscany-Scaled", "Tuscany-Striped",
         "Tuscany-Tailed", "Ultramarine-Eared", "Ultramarine-Eyed", "Ultramarine-Bellied", "Ultramarine-Dotted",
         "Ultramarine-Furred", "Ultramarine-Nosed", "Ultramarine-Scaled", "Ultramarine-Striped", "Ultramarine-Tailed",
         "Umber-Eared", "Umber-Eyed", "Umber-Bellied", "Umber-Dotted", "Umber-Furred", "Umber-Nosed", "Umber-Scaled",
         "Umber-Striped", "Umber-Tailed", "Vanilla-Eared", "Vanilla-Eyed", "Vanilla-Bellied", "Vanilla-Dotted",
         "Vanilla-Furred", "Vanilla-Nosed", "Vanilla-Scaled", "Vanilla-Striped", "Vanilla-Tailed", "Verdigris-Eared",
         "Verdigris-Eyed", "Verdigris-Bellied", "Verdigris-Dotted", "Verdigris-Furred", "Verdigris-Nosed",
         "Verdigris-Scaled", "Verdigris-Striped", "Verdigris-Tailed", "Vermilion-Eared", "Vermilion-Eyed",
         "Vermilion-Bellied", "Vermilion-Dotted", "Vermilion-Furred", "Vermilion-Nosed", "Vermilion-Scaled",
         "Vermilion-Striped", "Vermilion-Tailed", "Violet-Eared", "Violet-Eyed", "Violet-Bellied", "Violet-Blue-Eared",
         "Violet-Blue-Eyed", "Violet-Blue-Bellied", "Violet-Blue-Dotted", "Violet-Blue-Furred", "Violet-Blue-Nosed",
         "Violet-Blue-Scaled", "Violet-Blue-Striped", "Violet-Blue-Tailed", "Violet-Dotted", "Violet-Furred",
         "Violet-Nosed", "Violet-red-Eared", "Violet-red-Eyed", "Violet-red-Bellied", "Violet-red-Dotted",
         "Violet-red-Furred", "Violet-red-Nosed", "Violet-red-Scaled", "Violet-red-Striped", "Violet-red-Tailed",
         "Violet-Scaled", "Violet-Striped", "Violet-Tailed", "Viridian-Eared", "Viridian-Eyed", "Viridian-Bellied",
         "Viridian-Dotted", "Viridian-Furred", "Viridian-Nosed", "Viridian-Scaled", "Viridian-Striped",
         "Viridian-Tailed", "Wheat-Eared", "Wheat-Eyed", "Wheat-Bellied", "Wheat-Dotted", "Wheat-Furred", "Wheat-Nosed",
         "Wheat-Scaled", "Wheat-Striped", "Wheat-Tailed", "White-Eared", "White-Eyed", "White-Bellied", "White-Dotted",
         "White-Furred", "White-Nosed", "White-Scaled", "White-Striped", "White-Tailed", "Wine-Eared", "Wine-Eyed",
         "Wine-Bellied", "Wine-Dotted", "Wine-Furred", "Wine-Nosed", "Wine-Scaled", "Wine-Striped", "Wine-Tailed",
         "Wisteria-Eared", "Wisteria-Eyed", "Wisteria-Bellied", "Wisteria-Dotted", "Wisteria-Furred", "Wisteria-Nosed",
         "Wisteria-Scaled", "Wisteria-Striped", "Wisteria-Tailed", "Wood brown-Eared", "Wood brown-Eyed",
         "Wood brown-Bellied", "Wood brown-Dotted", "Wood brown-Furred", "Wood brown-Nosed", "Wood brown-Scaled",
         "Wood brown-Striped", "Wood brown-Tailed", "Xanadu-Eared", "Xanadu-Eyed", "Xanadu-Bellied", "Xanadu-Dotted",
         "Xanadu-Furred", "Xanadu-Nosed", "Xanadu-Scaled", "Xanadu-Striped", "Xanadu-Tailed", "Yellow Orange-Eared",
         "Yellow Orange-Eyed", "Yellow Orange-Bellied", "Yellow Orange-Dotted", "Yellow Orange-Furred",
         "Yellow Orange-Nosed", "Yellow Orange-Scaled", "Yellow Orange-Striped", "Yellow Orange-Tailed",
         "Yellow rose-Eared", "Yellow rose-Eyed", "Yellow rose-Bellied", "Yellow rose-Dotted", "Yellow rose-Furred",
         "Yellow rose-Nosed", "Yellow rose-Scaled", "Yellow rose-Striped", "Yellow rose-Tailed", "Yellow-Eared",
         "Yellow-Eyed", "Yellow-Bellied", "Yellow-Dotted", "Yellow-Furred", "Yellow-green-Eared", "Yellow-green-Eyed",
         "Yellow-green-Bellied", "Yellow-green-Dotted", "Yellow-green-Furred", "Yellow-green-Nosed",
         "Yellow-green-Scaled", "Yellow-green-Striped", "Yellow-green-Tailed", "Yellow-Nosed", "Yellow-Scaled",
         "Yellow-Striped", "Yellow-Tailed"],
        second_names,
    ]


class AnimalSpecies3NameGenerator(AnimalSpeciesNameGenerator):
    glue = "-"
    data = [
        second_names,
        second_names,
    ]


def animal_species_selector(generator_id):
    if generator_id < 4:
        return AnimalSpecies1NameGenerator
    elif generator_id < 6:
        return AnimalSpecies2NameGenerator
    return AnimalSpecies3NameGenerator


def animal_species_generate(generator_id=None):
    return random_generator(animal_species_selector, generator_id=generator_id).generate()
