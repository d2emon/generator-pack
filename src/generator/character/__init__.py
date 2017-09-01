from generator import Generated, DataGenerator
from .special import SpecialSignGenerator
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


class Character(Generated):
    def __init__(self, race=None):
        if race is None:
            race = Race
        self.race = race
        self.hair = self.race.hair_generator.generate()
        self.face = self.race.face_generator.generate()
        self.eyes = self.race.eyes_generator.generate()
        self.promise = self.race.promise_generator.generate()
        self.special = SpecialSignGenerator.generate()
        self.name = self.race.name_generator.generate()
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

        return "\n".join([
            head,
            str(self.special),
            title,
            personality,
        ])


class CharacterGenerator(DataGenerator):
    generated_class = Character
    races = races

    @classmethod
    def generate(cls, races=None):
        if races is None:
            races = cls.races
        generated = cls.generated(race=random.choice(races))
        return cls.fill_generated(generated)

    @classmethod
    def fill_generated(cls, generated):
        race = generated.race
        generated.hair = race.hair_generator.generate()
        generated.face = race.face_generator.generate()
        generated.eyes = race.eyes_generator.generate()
        generated.promise = race.promise_generator.generate()
        generated.special = SpecialSignGenerator.generate()
        generated.name = race.name_generator.generate()
        generated.frame = FrameGenerator.generate()
        generated.strange = StrangeGenerator.generate()
        generated.attitude = AttitudeGenerator.generate()
        return generated
