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
        return "%s %s" % (
            random.choice(cls.art_names2[0]),
            random.choice(cls.art_names2[1]),
        )

    @classmethod
    def generate_being(cls):
        return "%s %s" % (
            random.choice(cls.art_names1[0]),
            random.choice(cls.art_names2[1]),
        )

    @classmethod
    def generate_text(cls, being):
        if being:
            return cls.generate_being()
        else:
            return cls.generate_place()
