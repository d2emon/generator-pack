from generator import Generated, ListGenerator


class Face(Generated):
    def __init__(self):
        self.facetype = "thin"
        self.expreession = "time-worn"

    def __repr__(self):
        return "%s, %s face" % (self.facetype, self.expression)


class FaceGenerator(ListGenerator):
    generated_class = Face
    facetypes = [
        "thin",
        "chiseled",
        "craggy",
        "fine",
        "fresh",
        "full",
        "furrowed",
        "handsome",
        "sculpted",
        "weak",
        "strong",
        "long",
        "round",
        "bony",
        "lean",
        "skinny",
        "fat",
    ]
    expressions = [
        "time-worn",
        "cheerful",
        "friendly",
        "charming",
        "radiant",
        "warm",
        "anguished",
        "menacing",
        "lively",
        "tense",
        "wild",
        "gloomy",
        "frowning",
        "worried",
        "sad",
        "lived-in",
    ]

    @classmethod
    def fill_generated(cls, generated):
        generated.facetype = cls.generate_value(cls.facetypes)
        generated.expression = cls.generate_value(cls.expressions)
        return generated


class ElfFaceGenerator(FaceGenerator):
    facetypes = [
        "elf",
    ]


class GnomeFaceGenerator(FaceGenerator):
    facetypes = [
        "gnome",
    ]


class GoblinFaceGenerator(FaceGenerator):
    facetypes = [
        "goblin",
    ]


class GiantFaceGenerator(FaceGenerator):
    facetypes = [
        "giant",
    ]
