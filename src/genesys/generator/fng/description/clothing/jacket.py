from genesys.generator import Generated, ListGenerator
from .sleeves import SleevesGenerator
from .material import Material


class Tie(Generated):
    def __init__(self):
        self.description = "tightly tied with string"
        self.position = "at the center"

    def __repr__(self):
        return " ".join([
            self.description,
            self.position
        ])


class TieGenerator(ListGenerator):
    generated_class = Tie
    descriptions = [
        "tightly tied with string",
        "loosely tied with string",
        "buttoned up completely",
        "almost completely buttoned up",
        "half buttoned up",
        "barely tied with string",
        "barely buttoned up",
        "bound",
    ]
    positions = [
        "at the center",
        "at the left side",
        "at the right side",
        "at the top left side",
        "at the top right side",
        "at the bottom left side",
        "at the bottom right side",
        "slightly off-center",
    ]

    @classmethod
    def fill_generated(cls, generated):
        generated.description = cls.generate_value(cls.descriptions)
        generated.position = cls.generate_value(cls.positions)
        return generated


class Jacket(Generated):
    def __init__(self):
        self.name = "jacket"
        self.sleeves = SleevesGenerator.generate()
        self.material = Material("leather")
        self.cover = "just below his waist"
        self.tie = TieGenerator.generate()
        self.neckline = "round neckline"

    def __repr__(self):
        return "%s sleeved, %s jacket" % (
            self.sleeves.length,
            self.material,
        )

    @property
    def description(self):
        return "His %s covers him to %s and is %s." % (
            str(self),
            self.cover,
            self.tie,
        )


class JacketGenerator(ListGenerator):
    generated_class = Jacket
    materials = [
        Material("leather"),
        Material("hide"),
        Material("furred"),
        Material("cloth"),
        Material("animal skin"),
        Material("silky"),
        Material("velvety"),
    ]
    covers = [
        "just below his waist",
        "well below his waist",
        "just below his groin",
        "well below his groin",
        "just below his knees",
        "well below his knees",
        "just above his waist",
        "well above his waist",
        "just above his groin",
        "well above his groin",
        "just above his knees",
        "well above his knees",
        "his waist",
        "his knees",
        "his groin",
    ]
    necklines = [
        "round neckline",
        "wide, round neckline",
        "narrow, round neckline",
        "deep, round neckline",
        "wide v-neck",
        "narrow v-neck",
        "deep v-neck",
        "rectangular neckline",
        "wide, rectangular neckline",
        "narrow, rectangular neckline",
        "deep, rectangular neckline",
    ]

    @classmethod
    def fill_generated(cls, generated):
        generated.sleeves = SleevesGenerator.generate()
        generated.material = cls.generate_value(cls.materials)
        generated.cover = cls.generate_value(cls.covers)
        generated.tie = TieGenerator.generate()
        generated.neckline = cls.generate_value(cls.necklines)
        return generated
