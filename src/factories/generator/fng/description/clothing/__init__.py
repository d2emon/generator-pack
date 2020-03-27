from factories.generator import Generated, DataGenerator
from factories._unknown.character import Male, Female
from .jacket import JacketGenerator
from .shirt import ShirtGenerator
from .belt import BeltGenerator, FemaleBeltGenerator
from .pants import PantsGenerator
from .shoes import ShoesGenerator
from .dress import DressGenerator
import random


class Clothing(Generated):
    # frame_generator = FrameGenerator
    # strange_generator = StrangeGenerator

    def __init__(self, sex=0):
        self.sex = sex
        self.generate()

    def generate(self):
        self.jacket = JacketGenerator.generate()
        self.shirt = ShirtGenerator.generate()
        self.belt = BeltGenerator.generate()
        self.pants = PantsGenerator.generate()
        self.shoes = ShoesGenerator.generate()
        # if self.sex == 1:
        #     specials = female_specials
        # else:
        #     specials = male_specials
        # special_generator = random.choice(specials)

        # g = self.race.generators(self.sex)
        # self.hair = g.hair.generate()
        # self.face = g.face.generate()
        # self.eyes = g.eyes.generate()
        # self.promise = g.promise.generate()
        # self.special = special_generator.generate()
        # self.name = g.name.generate()
        # self.frame = self.frame_generator.generate()
        # self.strange = self.strange_generator.generate()
        # self.attitude = g.attitude.generate()
        pass

    @property
    def description(self):
        if self.jacket.sleeves.length.is_long:
            c = self.jacket
        else:
            c = self.shirt

        sleeves = " The sleeves of his %s are %s." % (
            c.name,
            c.sleeves,
        )
        part1 = self.jacket.description + sleeves
        part2 = "The jacket has a %s which reveals part of the %s worn below it and is worn with a %s. The %s is %s." % (
            self.jacket.neckline,
            self.shirt,
            self.belt.description,
            self.belt,
            self.belt.decoration,
        )
        part3 = "His pants are simple and %s and reach down to his %s. %s" % (
            self.pants.width,
            self.shoes,
            self.shoes.description,
        )

        description = "\n".join([
            part1,
            part2,
            part3,
        ])

        for k, v in self.sex.replaces.items():
            description = description.replace(k, v)
        return description


class MaleClothing(Clothing):
    def __init__(self):
        self.sex = Male
        self.generate()

    def generate(self):
        self.jacket = JacketGenerator.generate()
        self.shirt = ShirtGenerator.generate()
        self.belt = BeltGenerator.generate()
        self.pants = PantsGenerator.generate()
        self.shoes = ShoesGenerator.generate()

    @property
    def description(self):
        if self.jacket.sleeves.length.is_long:
            c = self.jacket
        else:
            c = self.shirt

        sleeves = " The sleeves of his %s are %s." % (
            c.name,
            c.sleeves,
        )
        part1 = self.jacket.description + sleeves
        part2 = "The jacket has a %s which reveals part of the %s worn below it and is worn with a %s. The %s is %s." % (
            self.jacket.neckline,
            self.shirt,
            self.belt.description,
            self.belt,
            self.belt.decoration,
        )
        part3 = "His pants are simple and %s and reach down to his %s. %s" % (
            self.pants.width,
            self.shoes,
            self.shoes.description,
        )

        description = "\n".join([
            part1,
            part2,
            part3,
        ])

        for k, v in self.sex.replaces.items():
            description = description.replace(k, v)
        return description


class FemaleClothing(Clothing):
    def __init__(self):
        self.sex = Female
        self.generate()

    def generate(self):
        self.dress = DressGenerator.generate()
        self.underdress = DressGenerator.generate()
        # self.jacket = JacketGenerator.generate()
        # self.shirt = ShirtGenerator.generate()
        self.belt = FemaleBeltGenerator.generate()

        # self.pants = PantsGenerator.generate()
        # self.shoes = ShoesGenerator.generate()

    @property
    def description(self):
        stomach = "The %s of her dress covers her stomach where the continuous flow is broken up by a %s worn %s around her waist." % (
            self.dress.fabric,
            self.belt,
            self.belt.decoration,
        )
        part1 = "Her %s, which %s reveals the %s dress worn below it. %s" % (
            self.dress,
            self.dress.reveal,
            self.underdress.style,
            stomach,
        )
        part2 = "Below the %s the dress %s the dress below. %s" % (
            self.belt.name,
            self.dress.opening,
            self.dress.endings,
        )
        part3 = "Her sleeves are %s and %s, their flow is broken up %s where %sthey're divided by %s, these are the same fabric and color used to outline the %s of the dress." % (
            self.dress.sleeves.length,
            self.dress.sleeves.width,
            self.dress.sleeves.change_position,
            self.dress.sleeves.change_type,
            self.dress.sleeves.bands,
            self.dress.outline,
        )

        description = "\n".join([
            part1,
            part2,
            part3,
        ])

        for k, v in self.sex.replaces.items():
            description = description.replace(k, v)
        return description


class ClothingGenerator(DataGenerator):
    male_generated_class = MaleClothing
    female_generated_class = FemaleClothing

    @classmethod
    def generate(cls, sex=None):
        if sex is None:
            sex = random.choice([Male, Female])

        if sex is Female:
            generated = cls.female_generated_class()
        else:
            generated = cls.male_generated_class()

        return cls.fill_generated(generated)

    @classmethod
    def fill_generated(cls, generated):
        generated.generate()
        return generated
