from v1.factories.fng.name_factory import NameFactory
from models.fng.description import Face


class FaceFactory(NameFactory):
    child_class = Face
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
