from v1.fng.genesys.name_factory import NameFactory, GenderNameFactory
from v1.fng.genesys.name import Name
from v1.fng.genesys.data_block import load_data
from v1.fng.genesys.genders import NEUTRAL, MALE, FEMALE


namesFemale = ["Absent", "Adamance ", "Aide", "Angel", "Anomaly", "Ash", "Ashes", "Aurora", "Beak", "Bling", "Blinkey",
               "Blossom", "Bones", "Books", "Bookworm", "Box", "Boxey", "Bubblegum", "Bucks", "Bugs", "Butterfly",
               "Cascade", "Chance", "Cinders", "Clarity", "Cloak", "Cloud", "Clumsy", "Dancer", "Darling", "Daydream",
               "Desire", "Doc", "Doctor", "Dot", "Dragonfly", "Dust", "Elsewhere", "Ember", "Enigma", "Exo", "Facade",
               "Face", "Faith", "Feather", "Feathers", "Fiddles", "Fix", "Flower", "Fluque", "Fortune", "Foxy", "Freak",
               "Freakshow", "Freckles", "Gadget", "Gentle", "Ghost", "Gloom", "Grace", "Heat", "Hive", "Hog", "Honey",
               "Hope", "Huntress", "Hybrid", "Hydra", "Imp", "Ion", "Jams", "Jester", "Joy", "Longshot", "Lotus",
               "Magma", "Magpie", "Mask", "Mendy", "Minx", "Misty", "Moon", "Mopes", "Muse", "Naughty", "Needle",
               "Nemo", "Nightmare", "Nightowl", "Nocturne", "Oddity", "Patch", "Patches", "Penance", "Pepper", "Petal",
               "Pickle", "Piggy", "Pixy", "Plasma", "Prodigy", "Puzzle", "Puzzles", "Pygmy", "Raine", "Random",
               "Rascal", "Riddle", "Risque", "Rogue", "Rubble", "Saber", "Serpente", "Silence", "Silver", "Siren",
               "Skins", "Skit", "Skitters", "Sky", "Slime", "Slimey", "Sly", "Smokes", "Snail", "Snout", "Snow", "Soot",
               "Specter", "Spikes", "Spirit", "Spot", "Spots", "Sprite", "Starlight", "Sunshine", "Tadpole", "Tags",
               "Tattoo", "Tinder", "Tinkle", "Tooths", "Toothsey", "Toots", "Tootsey", "Trace", "Twinkle", "Utopia",
               "Vex", "Vipra", "Vyolet", "Weeds", "Whisper", "Wicked", "Wings", "Wink", "Wish", "Witch", "Wither",
               "Woe", "Zero"]
namesMale = ["Absent", "Adamance ", "Aide", "Angel", "Anomaly", "Ash", "Atlas", "Beak", "Beast", "Bishop", "Bling",
             "Blinkey", "Blob", "Blood", "Bolt", "Bones", "Books", "Bookworm", "Box", "Bravo", "Bucks", "Buffalo",
             "Bugs", "Bullet", "Bulletproof", "Cable", "Captain", "Chance", "Chaos", "Cinders", "Cloak", "Cloud",
             "Clumsy", "Cobalt", "Cyclops", "Dagger", "Dancer", "Daydream", "Doc", "Doctor", "Dragonfly", "Dust",
             "Elsewhere", "Exo", "Facade", "Face", "Fallen", "Feather", "Feathers", "Fiddles", "Fix", "Flood", "Fluke",
             "Freak", "Freakshow", "Frenzy", "Gadget", "Gentle", "Ghost", "Glob", "Gloom", "Gremlin", "Grub", "Hawk",
             "Heat", "Hermit", "Hijack", "Hive", "Hog", "Hunter", "Husk", "Hybrid", "Hydro", "Imp", "Inn", "Ion",
             "Jams", "Jester", "Jet", "Lance", "Leech", "Longshot", "Maggot", "Magma", "Marsh", "Mask", "Mercury",
             "Mime", "Mist", "Moon", "Moose", "Mopes", "Muzzle", "Naughty", "Needle", "Nemo", "Newman", "Nightmare",
             "Nightowl", "Nocturne", "Oaf", "Oak", "Omega", "Ooze", "Patch", "Patches", "Penance", "Phantom", "Pickle",
             "Piggy", "Plasma", "Prodigy", "Puzzle", "Puzzles", "Pygmy", "Pyro", "Rain", "Random", "Rascal", "Rat",
             "Riddle", "Rig", "Rigs", "Risk", "Roach", "Rogue", "Rubble", "Saber", "Scooter", "Serpent", "Silence",
             "Silver", "Skeleton", "Sketch", "Skins", "Skit", "Skitters", "Sky", "Slime", "Sly", "Smokes", "Snail",
             "Snout", "Snow", "Soot", "Specter", "Spike", "Spikes", "Spirit", "Spot", "Spots", "Sprite", "Stonewall",
             "Striker", "Tadpole", "Tags", "Tattoo", "Thorn", "Thunder", "Tinder", "Toad", "Tooth", "Triclops", "Viper",
             "Weeds", "Whisper", "Wicked", "Wings", "Wink", "Wither", "Worm", "Zero"]
namesNeutral = ["Absent", "Adamance ", "Aide", "Angel", "Anomaly", "Ash", "Beak", "Bling", "Blinkey", "Blob", "Bones",
                "Books", "Bookworm", "Box", "Bucks", "Bugs", "Chance", "Cinders", "Cloak", "Cloud", "Clumsy", "Cyclops",
                "Dancer", "Daydream", "Desire", "Doc", "Doctor", "Dragonfly", "Dust", "Elsewhere", "Exo", "Facade",
                "Face", "Feather", "Feathers", "Fiddles", "Fix", "Fluke", "Freak", "Freakshow", "Frenzy", "Gadget",
                "Gentle", "Ghost", "Gloom", "Heat", "Hive", "Hog", "Hybrid", "Imp", "Ion", "Jams", "Jester", "Leech",
                "Longshot", "Maggot", "Magma", "Mask", "Mime", "Moon", "Moonshine", "Moose", "Mopes", "Naughty",
                "Needle", "Nemo", "Nightmare", "Nightowl", "Nocturne", "Patch", "Penance", "Pickle", "Piggy", "Plasma",
                "Prodigy", "Puzzle", "Puzzles", "Pygmy", "Random", "Rascal", "Riddle", "Risk", "Rogue", "Rubble",
                "Saber", "Silence", "Silver", "Skins", "Skit", "Skitters", "Sky", "Slime", "Sly", "Smokes", "Smokey",
                "Snail", "Snout", "Snow", "Soot", "Specter", "Spikes", "Spirit", "Spot", "Spots", "Sprite", "Tadpole",
                "Tags", "Tattoo", "Tinder", "Tooth", "Triclops", "Weeds", "Whisper", "Wicked", "Wings", "Wink",
                "Wither", "Zero"]


# Models


class ApocalypseNickname(Name):
    @property
    def value(self):
        return f"{self.items[1]}"


# Factory

class ApocalypseNicknameFactory(GenderNameFactory):
    """Apocalypse Nickname Factory"""

    class MaleApocalypseNicknameFactory(NameFactory):
        name_class = ApocalypseNickname
        blocks_map = {
            1: MALE,
        }

    class FemaleApocalypseNicknameFactory(NameFactory):
        name_class = ApocalypseNickname
        blocks_map = {
            1: FEMALE,
        }

    class NeutralApocalypseNicknameFactory(NameFactory):
        name_class = ApocalypseNickname
        blocks_map = {
            1: NEUTRAL,
        }

    description = """Not all names will fit mutants, and not all names will fit normal people caught up in a broken
        world, but there's plenty of names for both.
        Many names will overlap as well, like 'Anomaly', 'Ashes', 'Imp', 'Leech', 'Pickle', and 'Slime' to name just a
        few. Each of these names could be used for mutants and nicknames, depending on the meaning you put behind it.
        
        The names were mainly created as descriptive or role fulfilling names. Like 'Doc', 'Silence', 'Beak', and
        'Feathers'.
        'Doc' is either a doctor or somebody who really wants to be one. Silence is either a quiet person or a mute.
        Beak is most likely a mutant with either a real beak or a deformed face making it look like a beak. Feathers
        could be a mutant with actual feathers or just somebody who dresses up using feathers they found.
        
        Note that while some names will fit X-Men themed mutants, many of the names were created with less fortunate
        mutants in mind. This is also where the post-apocalyptic theme comes into play. The mutants I had in mind for
        this generator are simply people who were transformed by some sort of apocalypse.
        
        Quite a few of the names, especially the apocalypse-themed ones, can often be used for duos, like 'Bullet' and
        'Bulletproof', 'Daydream' and 'Nightmare' or 'Ash' and 'Soot'."""
    factory_classes = {
        MALE: MaleApocalypseNicknameFactory,
        FEMALE: FemaleApocalypseNicknameFactory,
        NEUTRAL: NeutralApocalypseNicknameFactory,
    }
    default_blocks = load_data({
        MALE: namesMale,
        FEMALE: namesFemale,
        NEUTRAL: namesNeutral,
    })
