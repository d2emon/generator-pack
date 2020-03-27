"""
	Alien
	Amazon
	Angel
	Animal Species
	Animatronic
	Apocalypse/Mutant
	+   Artificial Intelligence
	Bandit

	Banshee
	Barbarian
	Basilisk
	Birdfolk
	+   Bluecap
	Bounty Hunter
	Brownie
	Cat-people/Nekojin

	Cavemen
	Centaur
	Christmas Elf
	Cockatrice
	Code
	Cowboy/girl
	Cyberpunk
	Dark Elf

	Death
	+   Death Worm
	Demon
	Detective
	Dracaenae


    Dragon
    Dragon (Chinese)
    Dragonkin
    Dryad
    Dwarf
    Elemental
    Elf
    Ent/Tree creature

	Evil
	Fairy
	Fantasy Animal
	Fantasy Creature
	Fantasy Race
	Fantasy Surnames
	Fursona
	Futuristic

	Gargoyle
	Genie
	Ghost Classifications
	Ghost/Spirit
	Ghoul
	Giant
	Gnoll
	Gnome

	Goblin
	God &amp; Goddess
	Golem
	Gorgon
	Graeae


	Griffin
	+   Grootslang
	Guardian
	Half-Elf
	+   Half-Orc
	Harpy
	+   Hellhound
	Hobbit

	(Heroic) Horse
	Hydra
	+   Ifrit
	Imp
	Jotunn
	Kaiju
	Killer
	Kitsune

	Knight
	Kobold
	Lamia
	Legendary Creature
	Lich
	Lizardfolk
	+   Mad Scientist
	+   Manananggal

	Manticore
	Mecha
	Medieval
	Mermaid/Merman Names


    Minotaur
    Mirrored Twin
    Monster
    +   Moon Rabbit
    Mutant Species
    Naga
    Necromancer
    Nephilim

    Ninja & Assassin
    Non-Magic User
    Nymph
    Ogre
    Orc
    Pegasus
    Pets / Companions:
        Aliens
        Amphibians
        Bats
        Bears
        Birds
        Birds of Prey
        Cats & Felines
        Cows
        Crabs
        Deer
        Dogs & Canines
        Elephants
        Fish
        Horses

        Insects
        Large Cats
        Marine Mammals
        Mice & Rats
        Monkeys
        Owls
        Parrots<
        Pigs
        Rabbits
        Reptiles
        Rodents
        Sheep
        Turtles
        Wolves
    Phoenix

	Pirate
	+   Prophet
	Puppet
	Quetzalcoatl
	Rakshasa
	Robot
	Roc
	Satyr & Faun

	Sea Creature
	Selkie
	Servant
	Shapeshifter


	Siren
	Slave
	Species
	+   Sphinx
	+   Spiderfolk
	Steampunk
	Succubus
	Superhero

	Superhero Team
	Super Villain
	Sylph
	?   Tauren
	Troll
	Unicorn
	Valkyrie
	Vampire
	Vampire Clan

	Warrior
	Werewolf
	Werewolf Pack
	Witch
	Witch Coven
	Wizard
	World Defender
	World Destroyer

	Wyvern
	Yeti
	Zaratan
	Zombie

    ------

    Amusement Parks
    Antique Store
    Arcade
    Asylum
    Bakery
    Bank
    Battle Arenas
    Beach

    Blacksmith
    Brewery
    Bridge
    Cafe
    Camp
    Casino
    Castle
    Cave

    Circus
    City & Town
    City District


	Civilization
	Cliff & Fjord
	Company
	Continent
	Country/Nation
	+   Craft Store
	Day Care
	Desert/Wasteland

	Dimension
    Dungeon
    Farm
    Film Studio
    Fire Land
    Forest
    +   Galaxy
    Game Studio

	Grassland
	Graveyard
	Harbor


    Headquarters
    Hideout
    Hospital
    Hotel
    Island
    +   Isthmus
    Jungle
    Kingdom

	Laboratory
	Lake
	Library
	Mage Tower
	Magic School
	Magic Shop
	Mansion
	Mining Company

	Mountain
	Museum
	Nightclub


	Norse World Names
	Oasis
	Ocean/Sea
	Orphanage
	Outpost
	Park
	Pet Business
	Pirate Cove

	Pizzeria
	Planet
	Plantation
	Plaza
	Prison
	+   Quasar
	Realm
	Restaurant

	River
	Road (Fantasy)
	Ruin


	School
	Shop & Business
	Sky Island
	Snowland
	+   Spa
	Space Station/Colony
	Stadium
	Star

	+   Steampunk House
	Street
	Swamp
	+   Tattoo Parlors
    Tavern
    Temple
    Theater
    Tower

    Volcano
    Waterfall
    +   World

"""
import random

TOPICS = [
    "Afterlife", "Alien (Race)", "Alliance", "Angel", "Animal", "Animal Group", "Apocalypse",
    "Armor (Leather, Plate, Belts, Boots, Bracers, Chests, Cloaks, Gloves & Gauntlets, Helmets, Legs, Pauldrons, "
    + "Shields) +",
    "Army (Name, Description, Formation +)", "Artifact", "Artwork", "Attack Move", "Attack", "Award", "Backstory",
    "Battle", "Battle Cry", "Battlefield", "Birthday Wish", "Board Game", "Book Titles", "Bouquet", "Boxer",
    "Brand", "Bug Species", "Calendar +", "Candy", "Card Game", "Castle +", "Character", "Character Goal",
    "Chivalric Order", "Chosen One Titles", "City", "Clothing (Fancy, Medieval, Rags)", "Clothing Brand",
    "Clown (Good, Evil)", "Coat of Arms +", "Color", "Computer Virus", "Concept Ideas (Art, Story)", "Console",
    "Constellation (Name, Description +)", "Council", "Country", "Crop", "Currency", "Curse", "Dance", "Date",
    "Demon", "Demonym", "Dice", "Disease (General, Magical, Scientific)", "Dinosaur", "DJ", "Dragon", "Drink",
    "Drug", "Dungeon +", "Dying", "Enchantment", "Enchanted Gear", "Energy Types", "Epithets",
    "Evil Organizations", "Farm", "Familiar Types", "Family Tree +", "Fantasy Plant", "Fantasy Tree",
    "Fantasy Profession", "Flag +", "Food (General, Fantasy)", "Forest", "Fruit & Veg.", "Fungus", "Galaxy",
    "Game Engine", "Game Soundtrack", "Gang / Clan", "Garden", "Gemstone/Mineral (Name, Description)",
    "Ghost Town", "God(dess)", "Graffiti Tags", "Grammar +", "Guild / Clan", "Hacker", "Haiku",
    "Halloween Costume Ideas", "Hand Gesture", "Heist", "Herb & Spice", "Holiday (Name, Description)", "Holy Book",
    "House", "Human Species", "Humanoid", "Idiom", "Instrument", "Invention", "Jewelry", "Language +", "Law",
    "Law Enforcement Agencies", "Love nicknames", "Magazine", "Magic Types", "Magic School Books", "Map +",
    "Martial Art (Name, Description)", "Mascot", "Material", "Medicine", "Metal/Element", "Meteor",
    "Military Division Names", "Military Honor", "Military Operation", "Military Rank", "Mobster", "Molecule",
    "Monster/Spell Card +", "Monument", "Motorcycle Clubs", "Motorsport Races", "Motto", "Music Album",
    "Music Band", "Musician", "Mutant Plant", "Natural Disaster", "Newspaper", "Nicknames", "Noble House",
    "Notice Board +", "Outfit +", "Pain", "Пантеон (Pantheon +)", "Periodic Table +", "Personality", "Pirate Crew",
    "Plague", "Planet", "Planet Interior +", "Plant and Tree (Name, Description)", "Player Class & NPC Types",
    "Plot", "Poison", "Political Party", "Post-Apocalyptic Society", "Potion (Name, Description)", "Prayer",
    "Prophecy", "Quest", "Racer", "Railway", "Random Loot +", "Random Shop +", "Rank", "Realm", "Rebellion",
    "Religion (Name, Description)", "Religious Commandment", "Riddle", "Rune", "Satellite", "School Book (Magic)",
    "School Subject", "School Uniform", "Scientific Bird", "Scientific Creature", "Scientific Plant", "Scroll +",
    "Кораблекрушение (Shipwreck)", "Siege Engine", "Slogan", "Society", "Software", "Solar System +", "Song",
    "Space Base +", "Space Encounter +", "Space Fleet", "Spell (Name, Description)", "Sport", "Sports Team",
    "Squad", "Steampunk Walker", "Summoning Circle +", "Superpowers", "Swear", "Tavern", "Tarot Cards +",
    "Teleportation", "Theme Park Ride", "Throne", "Throne Hall", "Time Period", "Timeline +", "Title",
    "Tool Nicknames", "Town +", "Tradition", "Treaty", "Tribal", "Tribe", "Usernames",
    "Vehicle (Airplane, Airship, Car, Helicopter, Military Vehicle, Pirate Ship, Ship, Spaceship, Submarine, "
    + "Tank, Yacht)",
    "Video Game", "Vocal Group", "Жезл (Wand)", "Weapon Abilities",
    "Weapons (A. Rifles, Battle Axe, Blades, Bombs & Missiles, Bows & Crossbows, Claws, Daggers, Dual Wielding, "
    + "Fist Weapons, Flails & Maces, Magic Books, Magic Weapons, Pistols, Rifles, Sci-Fi Guns, Shields, Shotgun, "
    + "Spears & Halberds, Staves, Swords, Throwing Weapons, War Hammers, War Scythes, Whips & Lassos) +",
    "Web Series", "Wine", "Wisdom Quote", "Wrestler", "Wrestling Move",
]


def get_random_topic():
    return random.choice(TOPICS)
