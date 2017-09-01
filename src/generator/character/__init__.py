from generator import Generated, DataGenerator
from .special import SpecialSignGenerator
from .name import NameGenerator
from .frame import FrameGenerator
from .strange import StrangeGenerator
from .attitude import AttitudeGenerator
from . import race as r
import random


races = [
    r.Human,
    r.Human,
    r.Human,
    r.Human,
    r.Elf,
    r.NightElf,
    r.BloodElf,
    r.HighElf,
    r.WoodElf,
    r.DarkElf,
    r.Gnome,
    r.Troll,
    r.Orc,
    r.Goblin,
    r.Dwarf,
    r.Giant,
    r.Halfling,
    r.Vampire,
    r.Werewolf,
]


class Character(Generated):
    def __init__(self, race=None):
        if race is None:
            race = r.Race
        self.race = race
        self.hair = self.race.hair_generator.generate()
        self.face = self.race.face_generator.generate()
        self.eyes = self.race.eyes_generator.generate()
        self.promise = self.race.promise_generator.generate()
        self.special = SpecialSignGenerator.generate()
        self.name = NameGenerator.generate()
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
        generated.name = NameGenerator.generate()
        generated.frame = FrameGenerator.generate()
        generated.strange = StrangeGenerator.generate()
        generated.attitude = AttitudeGenerator.generate()
        return generated
