import random
from . import Generated, ParamGenerator
from .data.artConcept import names1, names2, names3, names4


class ArtConcept(Generated):
    def __repr__(self):
        return "ArtConcept: \"%s\"" % (self.generated_text)


class ArtConceptGenerator(ParamGenerator):
    generated_class = ArtConcept
    art_names1 = [names1, names2]
    art_names2 = [names3, names4]

    @classmethod
    def generate_place(cls):
        return GeneratorTemplate.generate(
            "data/art-concept/place1.txt",
            "data/art-concept/place2.txt",
        )

    @classmethod
    def generate_being(cls):
        return GeneratorTemplate.generate(
            "data/art-concept/being1.txt",
            "data/art-concept/being2.txt",
        )

    @classmethod
    def generate_text(cls, being):
        if being:
            return cls.generate_being()
        else:
            return cls.generate_place()
