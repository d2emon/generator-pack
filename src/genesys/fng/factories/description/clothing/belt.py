from models.models import Model
from factories.factories.list_factory import ListFactory


class BeltGenerator(ListFactory):
    generated_class = Belt
    sizes = [
        "thin",
        "thick",
        "simple",
        "small",
        "big",
        "light",
        "dark",
        "large",
        "long",
        "wide",
        "small",
    ]
    names = [
        "leather belt",
        "cloth belt",
        "rope belt",
        "cloth band",
    ]
    buckles = [
        "a big belt buckle",
        "a simple knot",
        "a small belt buckle",
        "an intricate knot",
        "an ornate pin",
        "a decorative pin",
    ]
    decorations = [
        "purely decorative and a sign of wealth",
        "mostly decorative and a sign of wealth",
        "entirely decorative and a way to show off",
        "solely decorative and a status symbol",
        "mostly decorative, but does serve its purpose",
        "partially decorative, but mostly a purposeful addition",
        "slightly decorative, but mostly there to hang things from",
        "almost entirely a functional addition",
        "purely a functional addition",
        "a functional addition, but does have some decorative value",
    ]

    @classmethod
    def fill_generated(cls, generated):
        generated.size = cls.generate_value(cls.sizes)
        generated.name = cls.generate_value(cls.names)
        generated.buckle = cls.generate_value(cls.buckles)
        generated.decoration = cls.generate_value(cls.decorations)
        return generated


class FemaleBeltGenerator(BeltGenerator):
    generated_class = FemaleBelt
    sizes = [
        "thin",
        "thick",
        "simple",
        "slender",
        "light",
        "dark",
        "large",
        "long",
        "wide",
        "small",
    ]
    names = [
        "leather belt",
        "ribbon",
        "cloth belt",
        "rope belt",
        "cloth band",
    ]
    decorations = [
        "fairly high",
        "quite high",
        "low",
        "high",
        "fairly low",
        "quite low",
    ]


class SleeveBandGenerator(FemaleBeltGenerator):
    generated_class = SleeveBand
    names = [
        "bands",
    ]
    decorations = [
        "decorative",
        "elegant",
        "ornamental",
        "cosmetic",
        "embellishing",
        "ornate",
        "delicate",
        "graceful",
        "luxurious",
        "simple",
        "modest",
        "refined",
        "stylish",
    ]
