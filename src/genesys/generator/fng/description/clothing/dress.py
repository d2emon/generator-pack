from genesys.generator import Generated, ListGenerator
from .sleeves import DressSleevesGenerator


class Fabric(Generated):
    def __init__(self):
        self.description = "comfortable"
        self.fabric = "buttoned up fabric"

    def __repr__(self):
        return ", ".join([
            self.description,
            self.fabric
        ])


class FabricGenerator(ListGenerator):
    generated_class = Fabric
    descriptions = [
        "comfortable",
        "delectable",
        "delicate",
        "exquisite",
        "fine",
        "flowing",
        "gentle",
        "ornate",
        "satiny",
        "silky",
        "smooth",
        "soft",
        "velvety",
    ]
    fabrics = [
        "buttoned up fabric",
        "loosely tied fabric",
        "tightly tied fabric",
        "corset-like tied fabric",
        "corset",
    ]

    @classmethod
    def fill_generated(cls, generated):
        generated.description = cls.generate_value(cls.descriptions)
        generated.fabric = cls.generate_value(cls.fabrics)
        return generated


class Dress(Generated):
    def __init__(self):
        self.name = "dress"
        self.style = "delicate"
        self.fabric = FabricGenerator.generate()

        self.sleeves = DressSleevesGenerator.generate()

        self.opening = "opens up slightly and reveals"
        self.front = "is shorter at the front and curves outwards"
        self.back = "fair"
        self.backend = "broad curve"

        self.neckline = "Queen Anne neckline"
        self.reveal = "charmingly"

        self.outline = "edges"

    def __repr__(self):
        return "%s dress flows from top to bottom and has a %s" % (
            self.style,
            self.neckline,
        )

    @property
    def endings(self):
        return "The front of the top dress %s, the back continues to flow a %s length behind her and ends in a %s." % (
            self.front,
            self.back,
            self.backend,
        )


class DressGenerator(ListGenerator):
    generated_class = Dress
    styles = [
        "delicate",
        "elegant",
        "fancy",
        "graceful",
        "luxurious",
        "relatively simple",
        "majestic",
        "modest",
        "noble",
        "ornate",
        "rather simple",
        "refined",
        "stylish",
        "traditional",
    ]
    necklines = [
        "Queen Anne neckline",
        "court neckline",
        "cowl neckline",
        "draped neckline",
        "halter neckline",
        "jewel neckline",
        "keyhole neckline",
        "round neckline",
        "scoop neckline",
        "semi-sweethear neckline",
        "square neckline",
        "sweetheart neckline",
        "v-neck",
    ]
    reveals = [
        "charmingly",
        "daintily",
        "delicately",
        "elegantly",
        "entrancingly",
        "gracefully",
        "graciously",
        "harmoniously",
        "lightly",
        "subtly",
        "tastefully",
        "wonderfully",
    ]
    openings = [
        "opens up slightly and reveals",
        "opens up to the right and reveals",
        "opens up to the left and reveals",
        "opens up and reveals",
        "opens up wide and reveals",
        "flows down and hides",
        "opens up left and right and reveals",
        "flows down wide and hides",
    ]
    fronts = [
        "is shorter at the front and curves outwards",
        "is much shorter at the front and curves outwards",
        "is shorter at the front and flows straight down",
        "reaches the ground generously",
        "easily reaches the ground in the front",
        "is longer than the bottom dress and flows straight down",
        "is longer than the bottom dress and curves outwards",
        "makes it just to the ground to cover her feet",
    ]
    backs = [
        "fair",
        "large",
        "good",
        "short",
        "decent",
        "long",
        "small",
    ]
    backends = [
        "broad curve",
        "narrow curve",
        "narrow tip",
        "broad tip",
        "narrow rectangle",
        "broad rectangle",
    ]
    outlines = [
        "edges",
        "sleeves",
        "sleeves and bottom",
        "bottom",
        "neckline",
        "bottom and neckline",
        "sleeves, bottom and neckline",
        "sleeves and neckline",
    ]

    @classmethod
    def fill_generated(cls, generated):
        generated.style = cls.generate_value(cls.styles)
        generated.sleeves = DressSleevesGenerator.generate()

        generated.fabric = FabricGenerator.generate()
        generated.opening = cls.generate_value(cls.openings)
        generated.front = cls.generate_value(cls.fronts)
        generated.back = cls.generate_value(cls.backs)
        generated.backend = cls.generate_value(cls.backends)

        generated.neckline = cls.generate_value(cls.necklines)
        generated.reveal = cls.generate_value(cls.reveals)

        generated.outline = cls.generate_value(cls.outlines)
        return generated
