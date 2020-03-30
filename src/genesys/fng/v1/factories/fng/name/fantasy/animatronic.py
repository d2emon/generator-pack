import random
from factories.name import NameFactory


class AnimatronicNameGenerator(NameFactory):
    glue = " "
    data = {
        GENDER_MALE: [
            [
                ["Abalone", "Ace the", "Achilles", "Acro the", "Acrobat", "Admiral", "Ajax the", "Alfie",
                 "Alistair", "Alpha", "Ammo the", "Angel", "Anger the", "Apache the", "Apollo the", "Apple",
                 "Aragog the", "Archer the", "Arrow the", "Artemis", "Artic", "Ash the", "Ashes", "Aslan the",
                 "Asterix", "Astro the", "Athene the", "Atlas", "Aura the", "Avalanche", "Avalon the", "Axe the",
                 "Axel the", "Axis the", "Azrael the"],
                ["Angel", "Astronaut", "Alligator", "Ant", "Ape", "Anaconda"]
            ],
            [
                ["Babbit", "Bacon the", "Badger the", "Bailey", "Baltazar the", "Bambam", "Bandit the",
                 "Bane the", "Baron", "Barry", "Basil", "Batista", "Baxter", "Bay the", "Bazal the",
                 "Beacon the", "Beaker the", "Belch the", "Belcher", "Bingo", "Berry", "Beta the",
                 "Big B the", "Bigglesworth", "Biggs the", "Biggy", "Bilbo", "Bing the", "Binky the",
                 "Biscuit the", "Blackjack the", "Blade the", "Blaze the", "Blazer", "Bleach the",
                 "Blight the", "Blister the", "Blitz the", "Blizz the", "Bloats the", "Blob the", "Blood the",
                 "Blue the", "Bluster the", "Bob the", "Bolt the", "Bones the", "Booboo", "Booger the",
                 "Boogy the", "Booker the", "Boomboom", "Boomer the", "Boomerang the", "Booth the",
                 "Boots the", "Bosco the", "Boulder the", "Bounce th", "Bowser the", "Brawn the", "Brock the",
                 "Brownie the", "Bruce the", "Brutus", "Bubba the", "Bubbles the", "Buck the", "Bud the",
                 "Buddy", "Buff the", "Buffles the", "Bullet the", "Bully", "Bumble the", "Buster the",
                 "Butch the", "Butters the", "Button", "Buttons the", "Buzz the"],
                ["Baboon", "Badger", "Bandicoot", "Bandit", "Bat", "Bear", "Beaver", "Bee", "Bigfoot", "Bird",
                 "Bison", "Boar", "Buffalo"]
            ],
            [
                ["Caine the", "Calvin the", "Camelot", "Captain", "Casanova the", "Cashew the", "Casper the",
                 "Caspian the", "Catastrophe", "Caveman", "Chaos the", "Clacker the", "Claw the",
                 "Clawde the", "Clawdius", "Clawford the", "Claws the", "Clawz the", "Clicker the",
                 "Clipper the", "Cloud the", "Clyde the", "Coal the", "Cole the", "Coloss the", "Colt the",
                 "Comet the", "Conan the", "Cookie the", "Cosmo the", "Cotton the", "Count", "Courage the",
                 "Cozmo", "Crack the", "Crackle the", "Crash the", "Crazy", "Cream the", "Crook the",
                 "Crooked", "Cruise the", "Crunch the", "Cruncher the", "Crunchy", "Crust the", "Crusty",
                 "Cuddles the", "Cupcake the", "Cupid the", "Kaine the", "Kane the", "Kargo", "Khan the",
                 "Killer", "Kindle the", "King"],
                ["Camel", "Cat", "Chameleon", "Cobra", "Cockroach", "Cougar", "Cow", "Coyote", "Crab",
                 "Crane", "Croc", "Crow", "Kangaroo", "Koala", "Kobold", "Komodo"]
            ],
            [
                ["Dagger the", "Dancer the", "Dane the", "Danger the", "Dapper the", "Darby the", "Darcy the",
                 "Darkness the", "Dart the", "Darth the", "Dash the", "Dawson the", "Deacon", "Delta",
                 "Deuce the", "Dexter the", "Diablo the", "Digger the", "Dillon the", "Dimitri the", "Ding",
                 "Ding the", "Dipper the", "Diver the", "Doctor", "Doc te", "Doc", "Dodge the", "Dodger the",
                 "Domino", "Doodle", "Doom", "Doom the", "Dova the", "Dover the", "Dozer the", "Drac the",
                 "Dracula", "Drake the", "Dread the", "Dread", "Drummer the", "Dude the", "Duffy", "Duke",
                 "Dune the", "Dusk the", "Dust the", "Dusty"],
                ["Dingo", "Demon", "Dwarf", "Deer", "Dino", "Dodo", "Dog", "Donkey", "Dragon", "Duck"]
            ],
            [
                ["Echo the", "Eclipse the", "Edge the", "Elmo the", "Elwood the", "Equinox the", "Ernie the",
                 "Excalibur the"], ["Elf", "Eagle", "Elephant"]
            ],
            [
                ["Fable the", "Fang the", "Fangs the", "Farkas the", "Fatty", "Fetch the", "Fiddles the",
                 "Fire", "Fizzle the", "Flapper the", "Flappy", "Flash the", "Flopsie the", "Fluff the",
                 "Fluffy", "Flynn the", "Force", "Forest the", "Forester", "Frankenstein", "Freaky",
                 "Freckles the", "Frenzy the", "Friskie the", "Frisky the", "Frosty the", "Fudge", "Fury",
                 "Fury the", "Fuzz the", "Fuzzy", "Fyre the"],
                ["Phantom", "Falcon", "Ferret", "Fish", "Flamingo", "Fairy", "Fly", "Fox", "Frog", "Phoenix",
                 "Pheasant"]
            ],
            [
                ["Gadget the", "Gale the", "Gallop the", "Gambit the", "Garry", "Gargle the", "Gargoyle the",
                 "Genghis", "George the", "Ghost", "Giggle the", "Giggles the", "Gil the", "Gillian",
                 "Gizmo the", "Gloom the", "Glutton the", "Glyde the", "Gnaw the", "Gobbles the", "Goble the",
                 "Godzilla", "Golem the", "Goliath the", "Gouge the", "Grand", "Gray the", "Grayson the",
                 "Griffin the", "Grim the", "Grinch the", "Grog the", "Grouch the", "Grouchy", "Grave",
                 "Grover the", "Grumpy", "Grump the", "Grunt the", "Gumball the", "Gunner the", "Gus the"],
                ["Gibbon", "Goat", "Goblin", "Ghost", "Griffin", "Goose", "Gopher", "Gator", "Gorilla"]
            ],
            [
                ["Hades the", "Hambo the", "Hamilton", "Hamlet the", "Hammer the", "Handsome", "Hank the",
                 "Hannibal", "Hardy the", "Harry", "Haven the", "Havoc the", "Havock the", "Hawke the",
                 "Haze the", "Hector", "Hercules the", "Herman the", "Hermit the", "Hershel the",
                 "Hogger the", "Hooch the", "Hopper the", "Hopscotch the", "Houdini", "Hudini", "Hulk",
                 "Hunter the", "Hurley the", "Hyde the", "Hyperion the"],
                ["Hamster", "Hare", "Hawk", "Hedgehog", "Hippo", "Hog", "Horse", "Hunter", "Hound", "Human",
                 "Hyena"]
            ],
            [
                ["Jabba the", "Jackson the", "Jaffa the", "Jaws the", "Jax", "Jeckyll the", "Jet the",
                 "Jethro the", "Jingle", "Jitters the", "Judge", "Jumbo the", "Junior", "Juno the"],
                ["Jackal", "Jaguar", "Giant"]
            ], [
                ["Lad the", "Laddy the", "Laika the", "Lance the", "Lancelot the", "Lash the", "Leaps the",
                 "Leapy the", "Lecter", "Legend the", "Leo the", "Leon the", "Licorice", "Lightning",
                 "Lionel", "Lockhart the", "Lockjaw the", "Logan the", "Loki the", "Lucifer", "Lucky the",
                 "Lupin the", "Lupus the", "Lycan the"],
                ["Lemming", "Lemur", "Lord", "Leopard", "Lion", "Lizard", "Llama", "Lobster", "Locust",
                 "Lynx"]
            ], [
                ["Macho", "Macho the", "Maddock the", "Madeye", "Magma", "Magnum the", "Magnus the",
                 "Mako the", "Mambo the", "Mammoth", "Marble", "Marlin the", "Marlow the", "Mason the",
                 "Matrix", "Maverick", "Max the", "Maximus", "Mayhem the", "Mello", "Mellow", "Menace the",
                 "Mercury", "Merlin the", "Midas the", "Midnight the", "Miles the", "Mirage the",
                 "Mittens the", "Moe the", "Mohawk", "Momo the", "Monty", "Mort the", "Muds the",
                 "Muffin the", "Murdoch the", "Murky", "Muse the", "Myst the"],
                ["Macaw", "Mandrill", "Mantis", "Meerkat", "Mage", "Mobster", "Mutant", "Mole", "Mongoose",
                 "Mongrel", "Monkey", "Monster", "Moose", "Moth", "Mouse", "Mule"]
            ], [
                ["Nacho the", "Nanook the", "Nemesis the", "Nemo the", "Nemoo the", "Neo the", "Neptune the",
                 "Nero the", "Newton the", "Nibbler the", "Nibbles the", "Nightmare", "Nightmare the",
                 "Nightshade the", "Nightwing the", "Niles the", "Nocturn the", "Noodle the", "Norbert the",
                 "Norton the", "Nova the", "Nugget the", "Nukem the", "Nyx the"],
                ["Gnoll", "Gnome", "Numbat", "Nightingale", "Neanderthal", "Knight", "Ninja", "Nymph",
                 "Newt"]
            ], [
                ["Oak the", "Obsidian", "Odin the", "Omega the", "Omega", "Omen the", "Onyx", "Onyx the",
                 "Oreo the", "Orion the", "Otis the", "Outlaw", "Owen the", "Ozzy the"],
                ["Ocelot", "Oracle", "Orc", "Octopus", "Ogre", "Orc", "Ostrich", "Owl"]
            ], [
                ["Pace the", "Paddington", "Paladin", "Pandora the", "Patch the", "Patches the", "Patriot",
                 "Patton the", "Payne the", "Peanut the", "Pebble the", "Pebbles the", "Pepper the",
                 "Piccolo", "Pickles the", "Pitch the", "Plunge the", "Pogo the", "Poison the", "Popcorn the",
                 "Popeye the", "Poppers the", "Poseidon the", "Pounce the", "Prancer the", "Predator",
                 "Pride the", "Prince", "Prometheus", "Puddle the", "Puddles the", "Pudge the", "Puff the",
                 "Puggy", "Punky", "Pyre the", "Pyro the"],
                ["Panda", "Panther", "Pirate", "Parrot", "Peacock", "Pelican", "Penguin", "Pig", "Pigeon",
                 "Piranha", "Pony", "Porcupine", "Possum", "Puma"]
            ], [
                ["Rabies the", "Rage", "Ragget the", "Rain the", "Rainbow the", "Ralph the", "Rambo",
                 "Rampage the", "Ranger", "Rascal", "Ray the", "Razor the", "Reaper the", "Rebel", "Rex the",
                 "Rhonin the", "Riggs the", "Ripley the", "Rocky the", "Rogue", "Rogue the", "Rohan the",
                 "Romulus", "Rosco the", "Rover the", "Rowan the", "Rowdy the", "Ruff the", "Rufus the",
                 "Rumble the", "Russell the", "Rusty the", "Rusty"],
                ["Rabbit", "Ranger", "Rogue", "Raccoon", "Ram", "Rat", "Raven", "Rhino"]
            ], [
                ["Sabath the", "Saber the", "Salt the", "Salty", "Satin the", "Saul the", "Savage the",
                 "Sawyer the", "Scamper the", "Scandal the", "Scar the", "Scooter the", "Scourge the",
                 "Scratches the", "Scratchy the", "Screech the", "Psych the", "Psyche the", "Psycho the",
                 "Scruffy the", "Sebastion", "Shade the", "Shadow the", "Shamrock the", "Shawn the",
                 "Shepherd the", "Sherlock the", "Shimmy the", "Shmooch the", "Shrapnel the", "Shredder the",
                 "Sid the", "Sidney", "Silver the", "Skinner the", "Skipper the", "Skittles the", "Slate the",
                 "Slick the", "Slimes the", "Slinky the", "Sly the", "Smeagol the", "Smiles the",
                 "Smokey the", "Smooch the", "Smudge the", "Snapper the", "Snookums the", "Snowball the",
                 "Snowflake the", "Snuffles the", "Snyder the", "Solace the", "Soots the", "Sparks the",
                 "Sparky the", "Spartacus the", "Spartan the", "Spectre the", "Speedy the", "Spike the",
                 "Spitfire", "Splinter the", "Sprite the", "Spudnik the", "Steele the", "Stitches the",
                 "Summit the", "Sunny the", "Storm the"],
                ["Salamander", "Satyr", "Scorpion", "Centipede", "Seal", "Shark", "Sheep", "Skunk", "Sloth",
                 "Slug", "Snail", "Snake", "Sparrow", "Centaur", "Scout", "Spy", "Spider", "Squid",
                 "Squirrel", "Stork", "Swallow", "Swan"]
            ], [
                ["Taboo the", "Tad the", "Tango the", "Tank the", "Terror", "Thor the", "Thunder the",
                 "Thunder", "Tiberius", "Tickles the", "Timber the", "Tiny", "Titan the", "Titanium",
                 "Tooth the", "Torment the", "Trace the", "Tremor the", "Triton the", "Triumph the",
                 "Trouble the", "Troy the", "Tumble the", "Tumnus the", "Tweedle the", "Twitch the",
                 "Tyde the", "Tyson the"],
                ["Tarantula", "Tiger", "Toad", "Tortoise", "Toucan", "Troll", "Turkey", "Turtle"]
            ],
            [
                ["Vamp the", "Vanilla", "Vapor the", "Vegas the", "Venom the", "Victor", "Vlad the", "Vladimir"],
                ["Vampire", "Viper", "Vulture"]
            ],
            [
                ["Waddle the", "Waddles the", "Walnut the", "Ward the", "Warpath the", "Wasabi the",
                 "Wayde the", "Wayne the", "Weirdo the", "Wellington", "Whisper the", "Wicked", "Wiggles the",
                 "Wilburt", "Willow the", "Wolfgang the", "Woods the", "Woody", "Wrath the"],
                ["Walrus", "Warthog", "Wasp", "Weasel", "Wolf", "Wolverine", "Wombat", "Werewolf", "Wizard",
                 "Woodpecker", "Worm"]
            ],
            [
                ["Yoghi the", "Yoghurt the", "Yogi the"],
                ["Yak"]
            ],
            [
                ["Ziggy the", "Zion the", "Zug the"],
                ["Zebra"]
            ]
        ],
        GENDER_FEMALE: [
            [
                ["Abalone", "Abby", "Acadia the", "Aerial the", "Aggie", "Aggy", "Agnes the", "Alexi",
                 "Alexia", "Alexis", "Algee", "Alibi the", "Alize the", "Alpine the", "Amazone the",
                 "Amazonia the", "Amber", "Amethyst the", "Angel the", "Angi", "Angie", "Annabella",
                 "Aphrodite the", "Apple the", "April the", "Aqua", "Ares the", "Aria", "Arial the",
                 "Ariel the", "Arizona", "Artica the", "Ash the", "Ashelia", "Ashes the", "Ashley",
                 "Aspen the", "Astral", "Athena the", "Atilla the", "Atolle the", "Aura", "Aurora the",
                 "Autumn", "Azraelle the", "Azura the", "Azure the", "Azurys the"],
                ["Angel", "Astronaut", "Alligator", "Ant", "Anaconda", "Ape"]
            ], [
                ["Barbara", "Babe the", "Babes the", "Babette the", "Baby", "Badge the", "Bambi the",
                 "Bambino", "Bandetta the", "Banshee the", "Bash the", "Bashful the", "Bashy the", "Batsy",
                 "Batty", "Beauty the", "Becky", "Belchy the", "Bella", "Belle", "Bernice the",
                 "Bertha the", "Bessy", "Beth the", "Betsy the", "Betty", "Biscuit the", "Bitsy the",
                 "Blaze the", "Blinks the", "Blinky", "Blitz the", "Blitze the", "Blitzen the",
                 "Bloats the", "Blossom the", "Blush the", "Bones the", "Bonnie", "Booboo", "Booboo the",
                 "Boots the", "Boubou", "Bounce the", "Bouncy the", "Brandy", "Breeze the", "Breezy",
                 "Brew the", "Brizzie", "Brooke the", "Brownie the", "Bubble the", "Bubbles the",
                 "Buffy the", "Bullette the", "Bumble the", "Bumbles the", "Bunny the", "Buttercup",
                 "Button the", "Buttons the"],
                ["Baboon", "Badger", "Bandicoot", "Bandit", "Bat", "Bear", "Beaver", "Bee", "Bigfoot",
                 "Bird", "Bison", "Boar", "Buffalo"]
            ], [
                ["Cake the", "Cakes the", "Calico the", "Calypso the", "Cami the", "Candy", "Capri the",
                 "Cara the", "Caramel", "Caramelle", "Carapace", "Carmen the", "Cascade the", "Clacks the",
                 "Clacky the", "Clarabella", "Clarice the", "Clarity", "Clawdia", "Claws the",
                 "Clemency the", "Clementine", "Cleo the", "Cleopatra", "Clippy the", "Clips the",
                 "Cloe the", "Clover the", "Cobbles the", "Coco the", "Codex the", "Comette the",
                 "Cookie the", "Cora", "Coral the", "Coralia", "Coraline", "Corona", "Cosmo the",
                 "Cotton the", "Crackle the", "Crackles the", "Crash the", "Creepette the", "Crunchey",
                 "Crystal", "Cuddle the", "Cuddles thes", "Cupcake the", "Cushion the", "Cutie",
                 "Karma the", "Kat the", "Kate the", "Kathy", "Kiss the", "Kisses the", "Kitty",
                 "Kylla the"],
                ["Camel", "Cat", "Chameleon", "Cobra", "Cockroach", "Cougar", "Cow", "Coyote", "Crab",
                 "Crane", "Croc", "Crow", "Kangaroo", "Koala", "Kobold", "Komodo"]
            ], [
                ["Daahling the", "Daffodil the", "Dahlia", "Daisy the", "Dakota the", "Dandy", "Daphne the",
                 "Darla the", "Darling", "Dash the", "Dashful the", "Dawn the", "Dawne the", "Dawnstar the",
                 "Dazzle", "Dee the", "Deedee the", "Delilah the", "Delta the", "Destiny", "Dew the",
                 "Dharma the", "Dirty", "Diva", "Diva the", "Dixie", "Dodger the", "Dolly", "Dora the",
                 "Doris the", "Dot the", "Dots the", "Dottie the", "Dotty the", "Draculette", "Dream the",
                 "Duchess", "Duchess the", "Duffy"],
                ["Dingo", "Dino", "Dodo", "Demon", "Dwarf", "Deer", "Dog", "Donkey", "Dragon", "Duck"]
            ], [
                ["Ebony", "Echo the", "Eclipse the", "Eek the", "Eep the", "Elain the", "Eleanor",
                 "Ember the", "Enigma the", "Enya the", "Equina the", "Equinox the", "Eve the"],
                ["Elf", "Eagle", "Elephant"]
            ], [
                ["Faith the", "Fancy", "Fang the", "Fangie the", "Fangs the", "Faune the", "Faye the",
                 "Fiddle the", "Fierra the", "Fire the", "Fizzle the", "Flame", "Flappy", "Flopsy the",
                 "Flower the", "Flubby the", "Fluffy", "Fluffy the", "Flufkins the", "Flutters the",
                 "Fortuna the", "Fortune the", "Frazzle", "Freakey", "Freckles the", "Frizzle the",
                 "Fuzzles the", "Fuzzy", "Fye the", "Fyre the"],
                ["Phantom", "Falcon", "Ferret", "Fish", "Flamingo", "Fly", "Fox", "Frog", "Phoenix",
                 "Fairy", "Pheasant"]
            ], [
                ["Gadget the", "Gambles the", "Gargles the", "Gemini", "Gemma the", "Geo the",
                 "Gertrude the", "Gia the", "Gidget the", "Giggles the", "Ginger the", "Ginny the",
                 "Gloria", "Gobbles the", "Goldilocks", "Gooey", "Gorgeous the", "Grace the", "Gracie the",
                 "Granny", "Gripes the", "Gummy the", "Gwen"],
                ["Gibbon", "Ghost", "Griffin", "Goat", "Goblin", "Goose", "Gopher", "Gator", "Gorilla"]
            ], [
                ["Hailey the", "Happy the", "Happy", "Harley", "Harmony the", "Haze the", "Hazel the",
                 "Heather the", "Heiress", "Helen the", "Helena", "Hermi the", "Hermine", "Hermione",
                 "Hinda the", "Hippity", "Hipscotch the", "Honey the", "Hope the", "Hoppity", "Hugsie the",
                 "Huntress the", "Hydris the", "Hymn the", "Hynde the", "Hyve the"],
                ["Hamster", "Hare", "Hawk", "Hedgehog", "Hippo", "Hog", "Hunter", "Horse", "Hound", "Human",
                 "Hyena"]
            ], [
                ["Jade the", "Jaffa the", "Jasmin the", "Jasmine the", "Jazzy", "Jess the", "Jewel the",
                 "Jinx the", "Jitters the", "Juno the", "Jynx the"],
                ["Jackal", "Jaguar", "Giant"]
            ], [
                ["Labyrinth the", "Lace the", "Lacy the", "Lady", "Laguna the", "Laika the", "Lana the",
                 "Lane the", "Lavender", "Leaps the", "Leapy the", "Legs the", "Levi", "Lexis the",
                 "Libby the", "Liberty", "Lilly the", "Linsey the", "Lola the", "Lore the", "Lotus the",
                 "Lucky the", "Lucy the", "Lullaby", "Lulu the", "Lumina", "Luna the", "Lyla the",
                 "Lyric the"],
                ["Lemming", "Lemur", "Leopard", "Lion", "Lizard", "Llama", "Lobster", "Locust", "Lynx"]
            ], [
                ["Mable the", "Mae the", "Maggie", "Magnolia", "Maiden", "Malibu", "Mango the", "Maple the",
                 "Marbles the", "Marigold", "Marinna", "Marsha the", "Martha the", "Maryn the", "Maxima",
                 "Meadow the", "Medusa the", "Melancholy", "Melanie", "Mello", "Mellow", "Melody",
                 "Mercy the", "Midnight the", "Mila the", "Milo the", "Mime the", "Minty the",
                 "Mischief the", "Missy", "Mistress", "Misty the", "Mittens the", "Mocha", "Molly the",
                 "Momma", "Mona the", "Momo the", "Moonbeam the", "Morticia the", "Muffin the", "Muriel",
                 "Mysti the", "Mystique the", "Myth the"],
                ["Macaw", "Mandrill", "Mage", "Mutant", "Mantis", "Meerkat", "Mole", "Mongoose", "Mongrel",
                 "Monkey", "Monster", "Moose", "Moth", "Mouse", "Mule"]
            ], [
                ["Nahla the", "Nala the", "Nanook the", "Nebula", "Neko the", "Nell the", "Nemo the",
                 "Nemoo the", "Neptuna the", "Nibbles the", "Nighte the", "Nipsey the", "Nixie the",
                 "Noodle the", "Noodles the", "Nora", "Nova the", "Nugget the", "Nutmeg the", "Nymph the",
                 "Nyx the"],
                ["Gnoll", "Gnome", "Numbat", "Nightingale", "Knight", "Ninja", "Nymph", "Neanderthal",
                 "Newt"]
            ], [
                ["Oasis", "Oasis the", "Oceana the", "Oceane the", "Olive the", "Olympia", "Omen the",
                 "Onyxia the", "Opal the", "Oracle", "Orbit the", "Orchid the", "Oreo the", "Ozone the"],
                ["Oracle", "Orc", "Ocelot", "Octopus", "Ogre", "Orc", "Ostrich", "Owl"]
            ], [
                ["Pace the", "Pandora the", "Paprika", "Patches the", "Patience the", "Paws the",
                 "Peaches the", "Pearl the", "Pebble the", "Pebbles the", "Peeps the", "Penelope",
                 "Penny the", "Pepper the", "Petunia", "Pickles the", "Pinky the", "Pitch the", "Pixie the",
                 "Poison the", "Pookie the", "Popcorn the", "Poppy the", "Precious the", "Princess",
                 "Prudence the", "Pudge the", "Pudgy the", "Puds the", "Puffy", "Pumpkin the", "Pyro the"],
                ["Panda", "Panther", "Pirate", "Parrot", "Peacock", "Pelican", "Penguin", "Pig", "Pigeon",
                 "Piranha", "Polar Bear", "Pony", "Porcupine", "Possum", "Puma"]
            ], [
                ["Rags the", "Raidrop the", "Rainbow the", "Raine the", "Raisin the", "Raleigh the",
                 "Razzle the", "Rebel", "Rebel the", "Rhyme the", "Ria", "Ribbon the", "Ripley the",
                 "Ripple", "Ripples the", "Riva", "River the", "Robin", "Rogue the", "Rogue", "Rose the",
                 "Rosemary", "Rosie the", "Roxy", "Ruby the", "Rune the", "Ruth the"],
                ["Rabbit", "Ranger", "Rogue", "Raccoon", "Ram", "Rat", "Raven", "Rhino"]
            ], [
                ["Sable the", "Sabre the", "Sabrina", "Sade the", "Saffron the", "Sage the", "Sally",
                 "Salmone the", "Sandy the", "Sanguine the", "Sapphire", "Satin the", "Savanah the",
                 "Scarlet the", "Psyche the", "Scratches the", "Scruffles the", "Selena", "Serenity",
                 "Shade the", "Shadow the", "Shaye the", "Shelob the", "Shiba the", "Shmooches the",
                 "Shye the", "Siera the", "Silver the", "Siren the", "Sirena", "Skylar the", "Sludges the",
                 "Smooches the", "Smudges the", "Snappy the", "Snickers the", "Snoots the", "Snowball the",
                 "Snuffles the", "Snuggles the", "Sona", "Sora the", "Sparkles the", "Speckles the",
                 "Spice the", "Spindle the", "Squiggles the", "Stitches the", "Storme the", "Strawberry",
                 "Stripes the", "Stuffles the", "Sugar", "Summer", "Sweetie", "Sweetpea the"],
                ["Salamander", "Satyr", "Scorpion", "Centipede", "Seal", "Shark", "Sheep", "Skunk", "Sloth",
                 "Slug", "Snail", "Snake", "Centaur", "Scout", "Spy", "Sparrow", "Spider", "Squid",
                 "Squirrel", "Stork", "Swallow", "Swan"]
            ], [
                ["Tabby the", "Tabitha", "Tawny the", "Teeny the", "Termina the", "Thistle the",
                 "Tibby the", "Tickles the", "Tiggles the", "Tilly the", "Tinkerbell", "Tinkerbelle",
                 "Tiny", "Theresa", "Toffee the", "Toots the", "Tootsie the", "Trixie the", "Trixy the",
                 "Truffles the", "Tulip the", "Twiggy the", "Twinkie the", "Twinkles the", "Tyra the"],
                ["Tarantula", "Tiger", "Toad", "Tortoise", "Toucan", "Troll", "Turkey", "Turtle"]
            ], [
                ["Valentine", "Vanilla the", "Vanity", "Vapor the", "Velvet the", "Venom the", "Venus the",
                 "Victoria", "Viola", "Violet the", "Vixen the"], ["Viper", "Vampire", "Vulture"]
            ], [
                ["Waddles the", "Waffles the", "Wendy", "Whisper the", "Wiggles the", "Wilde the",
                 "Willow the", "Winter the", "Wobbles the"],
                ["Walrus", "Warthog", "Wasp", "Weasel", "Wolf", "Wolverine", "Wombat", "Werewolf", "Witch",
                 "Woodpecker", "Worm"]
            ], [
                ["Yoghi the", "Yoghurt the", "Yogi the"],
                ["Yak"]
            ],
            [
                ["Zelda the", "Ziggy the", "Zippy the", "Zoe the"],
                ["Zebra"]
            ]
        ],
    }

    @classmethod
    def generate_parts(cls, gender=GENDER_MALE):
        return [random.choice(parts) for parts in random.choice(cls.data[gender])]


def animatronic_names_generate(gender=GENDER_MALE):
    return AnimatronicNameGenerator.generate(gender)
