from generator import Generated, DataGenerator
# from .special import SpecialSignGenerator, ScarGenerator, TattooGenerator
from . import special as s
from .frame import FrameGenerator
from .strange import StrangeGenerator
from .attitude import AttitudeGenerator
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
woman_signs = [
    s.ScarGenerator,
    s.ScarsGenerator,
    s.SwordMarkGenerator,
    s.GunshotMarkGenerator,
    s.DebryMarkGenerator,
    s.FireMarkGenerator,
    s.BirthmarkGenerator,
    s.OldTattooGenerator,
    s.TattooGenerator,
    s.TribalMarkGenerator,
    s.MolesGenerator,
    s.FrecklesGenerator,
    s.SmoothSkinGenerator,
    s.SoftSkinGenerator,
    s.FairSkinGenerator,
]
man_signs = woman_signs + [
    s.BeardGenerator,
    s.LargeBeardGenerator,
    s.DarkStubbleGenerator,
    s.MoustacheGenerator,
    s.GoateeGenerator,
    s.MoustacheAndGoateeGenerator,
]


class Character(Generated):
    def __init__(self, race=None, sex=0):
        if race is None:
            race = Race
        self.sex = sex
        self.race = race
        self.hair = self.race.hair_generator(sex).generate()
        self.face = self.race.face_generator.generate()
        self.eyes = self.race.eyes_generator.generate()
        self.promise = self.race.promise_generator.generate()
        self.special = None
        self.name = self.race.name_generator(sex).generate()
        self.frame = FrameGenerator.generate()
        self.strange = StrangeGenerator.generate()
        self.attitude = AttitudeGenerator.generate()

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
    specials = man_signs

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
        race = generated.race
        sex = generated.sex
        special_generator = random.choice(cls.specials)

        generated.hair = race.hair_generator(sex).generate()
        generated.face = race.face_generator.generate()
        generated.eyes = race.eyes_generator.generate()
        generated.promise = race.promise_generator.generate()
        generated.special = special_generator.generate()
        generated.name = race.name_generator(sex).generate()
        generated.frame = FrameGenerator.generate()
        generated.strange = StrangeGenerator.generate()
        generated.attitude = AttitudeGenerator.generate()
        return generated
