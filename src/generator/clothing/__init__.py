from generator import Generated, DataGenerator
from ..character.sex import Male, Female
from .jacket import JacketGenerator
from .shirt import ShirtGenerator
from .belt import BeltGenerator
from .pants import PantsGenerator
from .shoes import ShoesGenerator
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


class ClothingGenerator(DataGenerator):
    generated_class = Clothing
    # male_specials = male_specials
    # female_specials = female_specials

    @classmethod
    def generate(cls, sex=None):
        if sex is None:
            sex = random.choice([Male, Female])
        generated = cls.generated(sex=sex)
        return cls.fill_generated(generated)

    @classmethod
    def fill_generated(cls, generated):
        generated.generate()
        return generated
