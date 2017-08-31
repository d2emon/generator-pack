from .special import SpecialSignGenerator
from .name import NameGenerator
import generator.character.race
import random


races = [
    race.Human,
    race.Human,
    race.Human,
    race.Human,
    race.Elf,
    race.NightElf,
    race.BloodElf,
    race.HighElf,
    race.WoodElf,
    race.DarkElf,
    race.Gnome,
    race.Troll,
    race.Orc,
    race.Goblin,
    race.Dwarf,
    race.Giant,
    race.Halfling,
    race.Vampire,
    race.Werewolf,
]


class Character():
    def __init__(self, race=None):
        if race is None:
            race = Race
        self.race = race

    def generate(self):
        self.hair = self.race.hair_generator.generate()
        self.face = self.race.face_generator.generate()
        self.eyes = self.race.eyes_generator.generate()
        self.promise = self.race.promise_generator.generate()
        self.special= SpecialSignGenerator.generate()
        self.name= NameGenerator.generate()

    @property
    def description(self):
        head = "%s a %s. %s over %s" % (
            self.hair,
            self.face,
            self.eyes,
            self.promise,
        )
        title = "This is the face of %s among %s. He stands %s others, despite his %s frame." % (
            self.name,
            self.race.plural,
            "random22",
            "random23",
        )
        # name4 = "There's something %s about him, perhaps it's %s or perhaps it's simply %s. But nonetheless, people tend to %s, while %s." % (
        #     random24,
        #     random25,
        #     random26,
        #
        #     random27,
        #     random28,
        # )

        return "\n".join([
            head,
            str(self.special),
            title,
            # name4,
        ])


def random_character(racelist=None):
    if racelist is None:
        racelist = races
    c = Character(race=random.choice(racelist))
    c.generate()
    return c

