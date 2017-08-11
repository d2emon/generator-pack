import random
from . import Generated, DataGenerator
from .data.artConcept import names1, names2, names3, names4


class ArtConcept(Generated):
    def __repr__(self):
        return "ArtConcept: \"%s\"" % (self.generated_text)


class ArtConceptGenerator(DataGenerator):
    generated_class = ArtConcept
    art_names1 = names1
    art_names2 = names2
    art_names3 = names3
    art_names4 = names4

    @classmethod
    def generate_place(cls):
        return " ".join([
            random.choice(cls.art_names3),
            random.choice(cls.art_names4),
        ])

    @classmethod
    def generate_being(cls):
        return " ".join([
            random.choice(cls.art_names1),
            random.choice(cls.art_names2),
        ])

    @classmethod
    def generate_text(cls, being):
        if being:
            return cls.generate_being()
        else:
            return cls.generate_place()

    @classmethod
    def generate(cls, being=True):
        generated = cls.generated_class()
        generated.generated_text = cls.generate_text(being)
        return generated
