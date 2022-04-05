from genesys.fng.factories.name_factory import NameFactory
from models.fng.description import Hair


class EyesFactory(NameFactory):
    child_class = Hair
    styles = [
        "Beady",
        "Big, round",
        "Bloodshot",
        "Bright",
        "Bulging",
        "Clear",
        "Dancing",
        "Darting",
        "Dead",
        "Expressive",
        "Gentle",
        "Glinting",
        "Glistening",
        "Glittering",
        "Heavy",
        "Hollow",
        "Hooded",
        "Lidded",
        "Narrow",
        "Piercing",
        "Round",
        "Shining",
        "Shuttered",
        "Small",
        "Smart",
        "Sparkling",
        "Squinting",
        "Wide",
        "Woeful",
    ]
    colors = [
        "blue",
        "brown",
        "hazel",
        "black",
        "green",
        "amber",
        "gray",
    ]
    depths = [
        "deep",
        "narrowly",
        "buried",
        "far",
        "rooted",
        "well",
        "low",
        "high",
        "sunken",
        "lightly",
        "thightly",
        "graciously",
        "concealed",
        "delicately",
        "elegantly",
        "handsomely",
        "a-symmetrically",
        "gracefully",
        "seductively",
        "appealingly",
        "charmingly",
        "dreadfully",
        "wickedly",
    ]
    sights = [
        "wearily",
        "delightfully",
        "cheerfully",
        "gratefully",
        "heartily",
        "warmly",
        "eagerly",
        "delightedly",
        "merrily",
        "lovingly",
        "enthusiastically",
        "readily",
        "hungrily",
        "intently",
        "energetically",
        "impatiently",
        "longingly",
        "vigorously",
        "rapidly",
        "admiringly",
        "affectionately",
        "fondly",
        "thoughtfully",
        "devotedly",
        "yearningly",
        "loyally",
        "cautiously",
        "slowly",
        "carefully",
        "guardedly",
        "discreetly",
        "anxiously",
        "attentively",
        "meticulously",
        "honorably",
        "vigilantly",
        "watchfully",
        "delicately",
        "faithfully",
    ]

    # def __init__(self, styles=None, colors=None, depths=None, sights=None):
    #     if styles is not None:
    #         self.__class__.styles = styles
    #     if colors is not None:
    #         self.__class__.colors = colors
    #     if depths is not None:
    #         self.__class__.colors = colors
    #     if sights is not None:
    #         self.__class__.colors = colors

    @classmethod
    def fill_generated(cls, generated):
        generated.style = cls.generate_value(cls.styles)
        generated.color = cls.generate_value(cls.colors)
        generated.depth = cls.generate_value(cls.depths)
        generated.sight = cls.generate_value(cls.sights)
        return generated
