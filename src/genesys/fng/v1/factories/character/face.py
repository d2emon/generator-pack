from factories import DictFactory
from models.generator_models.character.face import Face


class FaceFactory(DictFactory):
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
