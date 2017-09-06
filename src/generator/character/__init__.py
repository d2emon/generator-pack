from generator import Generated, DataGenerator
# from .special import SpecialSignGenerator, ScarGenerator, TattooGenerator
from . import special as s
from .frame import FrameGenerator
from .strange import StrangeGenerator
from .race import Race, Human, Vampire, Werewolf
from .race.elf import Elf, NightElf, BloodElf, HighElf, WoodElf, DarkElf
from .race.gnome import Gnome
from .race.goblin import Troll, Orc, Goblin
from .race.dwarf import Dwarf, Giant, Halfling
import random


races = [
    Human,
    Human,
    Human,
    Human,
    Elf,
    NightElf,
    BloodElf,
    HighElf,
    WoodElf,
    DarkElf,
    Gnome,
    Troll,
    Orc,
    Goblin,
    Dwarf,
    Giant,
    Halfling,
    Vampire,
    Werewolf,
]
male_specials = [
    s.ScarGenerator,
    s.ScarsGenerator,
    s.SwordMarkGenerator,
    s.GunshotMarkGenerator,
    s.DebryMarkGenerator,
    s.FireMarkGenerator,
    s.BirthmarkGenerator,
    s.MaleOldTattooGenerator,
    s.MaleTattooGenerator,
    s.TribalMarkGenerator,
    s.MolesGenerator,
    s.FrecklesGenerator,
    s.SmoothSkinGenerator,
    s.SoftSkinGenerator,
    s.FairSkinGenerator,
    s.BeardGenerator,
    s.LargeBeardGenerator,
    s.DarkStubbleGenerator,
    s.MoustacheGenerator,
    s.GoateeGenerator,
    s.MoustacheAndGoateeGenerator,
]
female_specials = [
    s.ScarGenerator,
    s.ScarsGenerator,
    s.SwordMarkGenerator,
    s.GunshotMarkGenerator,
    s.DebryMarkGenerator,
    s.FireMarkGenerator,
    s.BirthmarkGenerator,
    s.FemaleOldTattooGenerator,
    s.FemaleTattooGenerator,
    s.TribalMarkGenerator,
    s.MolesGenerator,
    s.FrecklesGenerator,
    s.SmoothSkinGenerator,
    s.SoftSkinGenerator,
    s.FairSkinGenerator,
]


class Character(Generated):
    frame_generator = FrameGenerator
    strange_generator = StrangeGenerator

    def __init__(self, race=None, sex=0):
        if race is None:
            race = Race
        self.sex = sex
        self.race = race
        self.generate()

    def generate(self):
        if self.sex == 1:
            specials = female_specials
        else:
            specials = male_specials
        special_generator = random.choice(specials)

        g = self.race.generators(self.sex)
        self.hair = g.hair.generate()
        self.face = g.face.generate()
        self.eyes = g.eyes.generate()
        self.promise = g.promise.generate()
        self.special = special_generator.generate()
        self.name = g.name.generate()
        self.frame = self.frame_generator.generate()
        self.strange = self.strange_generator.generate()
        self.attitude = g.attitude.generate()

    @property
    def description(self):
        head = "%s a %s. %s over %s" % (
            self.hair,
            self.face,
            self.eyes,
            self.promise,
        )
        title = "This is the face of %s among %s. %s" % (
            self.name,
            self.race.plural,
            self.frame,
        )
        personality = "%s But nonetheless, %s." % (
            self.strange,
            self.attitude,
        )

        description = "\n".join([
            head,
            str(self.special),
            title,
            personality,
        ])

        replaces = {
            "{{He}}": "He",
            "{{he}}": "he",
            "{{him}}": "him",
            "{{his}}": "his",
        }
        if self.sex == 1:
            replaces["{{He}}"] = "She"
            replaces["{{he}}"] = "she"
            replaces["{{him}}"] = "her"
            replaces["{{his}}"] = "her"

        for k, v in replaces.items():
            description = description.replace(k, v)
        return description


class CharacterGenerator(DataGenerator):
    generated_class = Character
    races = races
    male_specials = male_specials
    female_specials = female_specials

    @classmethod
    def generate(cls, races=None, sex=None):
        if races is None:
            races = cls.races
        if sex is None:
            sex = random.choice([0, 1])
        generated = cls.generated(race=random.choice(races), sex=sex)
        return cls.fill_generated(generated)

    @classmethod
    def fill_generated(cls, generated):
        generated.generate()
        return generated
