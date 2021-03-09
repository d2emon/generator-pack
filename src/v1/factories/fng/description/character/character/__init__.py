import random
from factories import Factory
# from .special import SpecialSignGenerator, ScarGenerator, TattooGenerator
from genesys.generator_models.character import Character
from . import special as s
from genesys.generator_models.character import Male, Female
from .race import Race, Human, Vampire, Werewolf
from .race.elf import Elf, NightElf, BloodElf, HighElf, WoodElf, DarkElf
from .race.gnome import Gnome
from .race.goblin import Troll, Orc, Goblin
from .race.dwarf import Dwarf, Giant, Halfling
# from factories.generator import ClothingGenerator


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
    s.ScarFactory,
    s.ScarsFactory,
    s.SwordMarkFactory,
    s.GunshotMarkFactory,
    s.DebryMarkFactory,
    s.FireMarkFactory,
    s.BirthmarkFactory,
    s.MaleOldTattooFactory,
    s.MaleTattooFactory,
    s.TribalMarkFactory,
    s.MolesFactory,
    s.FrecklesFactory,
    s.SmoothSkinFactory,
    s.SoftSkinFactory,
    s.FairSkinFactory,
    s.BeardFactory,
    s.LargeBeardFactory,
    s.DarkStubbleFactory,
    s.MoustacheFactory,
    s.GoateeFactory,
    s.MoustacheAndGoateeFactory,
]
female_specials = [
    s.ScarFactory,
    s.ScarsFactory,
    s.SwordMarkFactory,
    s.GunshotMarkFactory,
    s.DebryMarkFactory,
    s.FireMarkFactory,
    s.BirthmarkFactory,
    s.FemaleOldTattooFactory,
    s.FemaleTattooFactory,
    s.TribalMarkFactory,
    s.MolesFactory,
    s.FrecklesFactory,
    s.SmoothSkinFactory,
    s.SoftSkinFactory,
    s.FairSkinFactory,
]


class CharacterGenerator(Factory):
    generated_class = Character
    races = races
    male_specials = male_specials
    female_specials = female_specials

    @classmethod
    def generate(cls, races=None, sex=None):
        if races is None:
            races = cls.races
        if sex is None:
            sex = random.choice([Male, Female])
        generated = cls.generated(race=random.choice(races), sex=sex)
        return cls.fill_generated(generated)

    @classmethod
    def fill_generated(cls, generated):
        generated.generate()
        return generated
