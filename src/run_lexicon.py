"""
Лексикон
--------

Основная идея игры состоит в том, что каждый её участник берёт себе роль учёного — в общем средневековом смысле этого
слова, до возникновения деления на узкие профессиональные области интересов или после его исчезновения. Как всякий
истинный учёный, персонаж каждого игрока упрям, вреден, самоуверен, предвзят и эксцентричен. Игра посвящена тому, как
несколько таких учёных объединяются в единой попытке создания энциклопедии, которая будет всесторонне описывать
какой-то исторический период (в более общем случае — любую часть сеттинга).
"""
import random


class Game:
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

    ---------

	Afterlife
	Alliance
	Animal Group
	Apocalypse
	Armor:
	    Belts
	    Boots
	    Bracers
	    Chests
	    Cloaks
	    Gloves & Gauntlets
	    Helmets
	    Legs
	    Pauldrons
	    Shields
    Army:
        Army
        (Dwarf)
        (Elf)
        (Orc)
        (Troll)
        (Undead)
    Artifact
    Artwork

	Attack Move
	Attack
	Award
	Battle
	Board Game
	Book Titles
	Bouquet
	Boxer

    Brand
    Bug Species
    Candy
    +   Card Game
    Chivalric Order
    +   Chosen One Titles
    Clothing Brand
    Clown

    +   Clown (Evil)
    Color
    Computer Virus
    Console
    Constellation
    Council


	Crop
	Currency
	Curse
	Dance
	Date
	Disease
	Disease (Magical)
	Disease (Scientific)

	Dinosaur
	+   DJ
	Drink
	Drug
	Enchantment
	Enchanted Gear
	Energy Types
	Epithets

	Evil Organizations
	+   Familiar Types
	Fantasy Plant
	Fantasy Tree
	Fantasy Profession
	Food
	Food (Fantasy)
	Fruit & Veg. Names

	Fungus
	?   Galaxy
	Game Engine
	Game Soundtrack
	Gang / Clan
	Gemstone/Mineral


	Graffiti Tags
	Guild / Clan
	Hacker
	Heist
	Herb & Spice
	Holiday
	Holy Book
	Human Species

	Instrument
	Invention
	Jewelry
	Language
	+   Law Enforcement Agencies
	Love nicknames
	Magazine
	Magic Types

	+   Magic School Books
	Martial Arts
	Mascot
	Material
	Medicine
	Metal/Element
	+   Meteor
	Military Division Names

	Military Honor
	Military Operation
	Military Rank
	Mobster
	Molecule


	Motorcycle Clubs
	Motorsport Races
	Music Album
	Music Band
	Musician
	Mutant Plant
	Natural Disaster
	Newspaper

	Nicknames
	Noble House
	Pirate Crew
	Plague
	Plant and Tree
	Player Class & NPC Types
	Poison
	Political Party

	Post-Apocalyptic Society
	Potion
	Racer
	Railway
	Rank
	+   Rebellion
	Religion
	+   Rune

	Satellite
	Scientific Bird
	Scientific Creature
	Scientific Plant
	School Book (Magic)


	Siege Engine
	Software
	Song
	Space Fleet
	Spell
	Sport
	Sports Team
	Squad

	Steampunk Walker
	Superpowers
	Teleportation
	Theme Park Ride
	Throne
	Time Period
	Title
	Tool Nicknames

	Treaty
	Tribal
	Tribe
	Usernames
	Vehicle:
	    Airplane
	    Airship
	    Car
	    Helicopter
	    Military Vehicle
	    Pirate Ship
	    Ship
	    Spaceship
	    Submarine
	    Tank
	    Vehicle Names</a></li>
	    +   Yacht
    Video Game
    Vocal Group
    Weapon Abilities

    Weapon:
        Battle Axe
        Bombs & Missiles
        Bows & Crossbows
        Claws
        Daggers
        Dual Wielding
        Fist Weapons
        Flails & Maces
        Magic Books
        Magic Weapons
        Pistols
        Rifles
        Sci-Fi Guns
        Shotguns
        Spears & Halberds
        Staves
        Swords
        Throwing Weapons
        War Hammers
        War Scythes
        Whips & Lassos
    Web Series
    Wine
    Wrestler
    Wrestling Move

    --------------

	Alien (Race)
	+   Angel
	Animal
	Armor (Leather)
	Armor (Plate)
	Army
	Backstory
	Battlefield

	Castle
	Character
	City
	Clothing (Fancy)
	Clothing (Medieval)


	Clothing (Rags)
	Coat of Arms
	Constellation
	Country
	Demon
	Disease
	Dragon
	Dungeon

	Dying
	Farm
	Flag
	Forest
	+   Garden


	Gem
	Ghost Town
	God(dess)
	Hand Gesture
	Holiday
	House
	Humanoid
	Law

	Martial Art
	Monument
	Pain
	Personality


	Planet
	Plant
	Plot
	Potion
	Prophecy
	Quest
	+   Realm
	+   Religion

	School Uniform
	+   Shipwreck
	Society
	Spell


    Tavern
    Throne Hall
    Town
    Tradition
    Wand
    Weapons (A. Rifles)
    Weapons (Blades)
    Weapons (Bows)

    Weapons (Pistol)
    Weapons (Shields)
    Weapons (Shotgun)
    Weapons (Staves)

    ----------------

    Ascii Face Generator
    Battle Cry
    Birthday Wish
    Character Goal

    Concept Ideas (Art)
    Concept Ideas (Story)
    Demonym
    Haiku

    +   Halloween Costume Ideas
    Idiom
    Motto
    Prayer

    Religious Commandment
    Riddle
    School Subject

    Slogan
    Swear
    Wisdom Quote

    ------------

    RollForFantasy.com

    Armor Creator
    Army Formation Creator
    Calendar Creator
    Castle Creator
    Coat Of Arms Creator
    Constellation Map Creator

    Dice Generator
    Dungeon Creator
    Family Tree Creator
    Flag Creator
    Grammar Creator
    Language Generator

    Map Creator
    Monster/Spell Card Creator
    Notice Board Creator
    Outfit Creator
    Pantheon Creator
    Periodic Table Creator

    Planet Interior Creator
    Random Loot Generator
    Random Shop Inventory
    Scroll Creator
    Solar System Creator
    Space Base Creator

    Space Encounter
    Summoning Circle
    Tarot Cards
    Timeline Creator
    Town Creator
    Weapon Creator

    # Emblem/Logo Creator
    """
    LETTERS = [chr(c) for c in range(ord('А'), ord('Я') + 1)]

    def __init__(self, random_letter=False):
        """
        Первым ходом каждый игрок пишет энциклопедическую статью на букву A. Он придумывает название статьи и пишет
        100—200 слов на заданную тему. В конце статьи ставится подпись учёного и две ссылки на труды его коллег (то
        есть другие статьи той же энциклопедии). Так как игра только начинается, эти ссылки будут ненастоящими — у них
        будут названия, но содержимое будет определено только на одном из следующих ходов. В энциклопедии на каждую
        букву должно быть ровно столько статей, сколько игроков, так что все ссылки на первом ходу должны начинаться с
        любой буквы, кроме A.

        :return:
        """
        self.random_letter = random_letter
        self.letter_id = 0
        self.turn()

    def next(self):
        """
        На втором, третьем и последующих ходах игроки продолжают создавать статьи на буквы B, C и так далее вплоть до
        Z.

        В академической среде не принято ссылаться на самого себя, так что и игроки в Лексикон не имеют право
        цитировать написанные ими статьи. На метаигровом уровне это заставит игроков плотнее сотрудничать и постоянно
        основывать свои статьи на чужих фактах.

        Несмотря на то, что коллеги персонажа — узколобые болваны с раздутым самомнением, они честные учёные. Как бы
        натянуты ни были трактовки фактов, которые они позволяют в своих работах, сами факты сомнению не подлежат и
        всегда точны, как только может быть точна история. Следовательно, при цитировании чужих трудов любой учёный
        обязан исходить из того, что изложенные там факты действительно имели место. Разумеется, это может и не
        помешать искренне возмутиться неверной интерпретации и ввести в игру новые факты, ставящие исходное
        истолкование происходящего под сомнение.

        :return:
        """
        self.letter_id += 1
        if self.letter_id >= len(self.LETTERS):
            self.letter_id = 0
        self.turn()

    @property
    def prev_letters(self):
        if self.random_letter:
            return self.LETTERS
        if self.letter_id > 0:
            return self.LETTERS[:self.letter_id]
        return None

    def prev_links(self):
        letters = self.prev_letters
        if not letters:
            return []
        return [random.choice(letters), ]

    @property
    def links_count(self):
        if self.random_letter:
            return 2
        if self.letter_id == len(self.LETTERS) - 2:
            return 1
        elif self.letter_id > len(self.LETTERS) - 2:
            return 0
        return 2

    def new_links(self, letter):
        if self.random_letter:
            letter = None
        for i in range(self.links_count):
            link = letter
            while link == letter:
                link = random.choice(self.LETTERS)
            yield link

    def turn(self):
        """
        На каждом ходу каждая новая статья должна ссылаться на три других: одну уже существующую и две ненаписанных.
        На 25-м ходу можно сослаться только на одну будущую статью, а на 26-м, последнем, — ни на одну (энциклопедия по
        окончании 26-го хода считается завершённой).

        :return:
        """
        if self.random_letter:
            letter = random.choice(self.LETTERS)
        else:
            letter = self.LETTERS[self.letter_id]

        print("Буква \"{}\"".format(letter))
        print("Придумайте название статьи и напишите 100—200 слов на заданную тему.")
        print("В конце статьи поставьте ссылки на другие статьи той же энциклопедии.")
        print("Например:")
        for link in self.prev_links():
            print("{}...(существующая)".format(link))
        for link in self.new_links(letter):
            print("{}...(новая)".format(link))


def main(players_count=4, turns=None, random_letter=False):
    players = [Game(random_letter) for _ in range(players_count)]
    turns = turns or len(Game.LETTERS)
    for _ in range(turns - 1):
        for player in players:
            player.next()


"""


Варианты
========

Существует много модификаций правил этой игры, часть из них концептуальна, остальные просто вытекают из возможностей
используемого в каком-то конкретном случае вики-движка:

*   Игроки могут начинать писать с разных букв, после чего всё равно идут последовательно, возвращаясь к началу по
    достижении конца.
*   На каждом ходу игроки выбирают любую букву, на которую ещё ничего не написали.
*   Нельзя начинать статью с произвольным названием, можно только выбирать среди названий на нужную букву, на которые
    уже есть ссылки.
*   На каждом ходу надо ссылаться на одну уже готовую статью, на одну ненаписанную, но уже «использованную» как
    источник в другой статье, и на одну новую.
*   По завершении игры весь цикл повторяется снова, либо циклы вообще не считаются (получается бесконечный процесс как
    в реальной википедии).
*   «Телефонный» вариант заканчивает игру за восемь ходов, группируя буквы как на мобильных телефонах: ABC, DEF, GHI,
    JKL, MNO, PQRS, TUV, WXYZ.
*   «Правило X» объявляет одну из букв (например, икс) «козырной» — когда до неё доходит дело, можно начинать новую
    статью с любой буквы. Это может быть особенно актуальным в случае русского алфавита, где придумать слово на букву
    Щ — трудно, а на букву Ь — вообще невозможно.
*   Некоторые хоумрулы позволяют ограниченно редактировать уже написанные статьи.
*   Ссылки на другие статьи можно ставить не в конце, как принято в реальных академических кругах, а в любом месте
    статьи, что больше отвечает вики-стилю.
*   Можно индексировать Лексикон не по буквам, а по чему-то другому: по дате, рунам, элементам, волшебным двеомерам,
    дыныдышным мировоззрениям и т. п.
*   Ссылки расставляются не непосредственными авторами статей, а другими игроками (можно заставлять ссылаться на себя
    и свои будущие статьи).
"""

if __name__ == "__main__":
    main(1, 1, True)
