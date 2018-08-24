from generator import Generated, ListGenerator
from .sleeves import SleevesGenerator


class Shirt(Generated):
    def __init__(self):
        self.name = "shirt"
        self.style = "rough"
        self.sleeves = SleevesGenerator.generate()

    def __repr__(self):
        return "%s %s" % (
            self.style,
            self.name,
        )


class ShirtGenerator(ListGenerator):
    generated_class = Shirt
    styles = [
        "rough",
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

    @classmethod
    def fill_generated(cls, generated):
        generated.style = cls.generate_value(cls.styles)
        generated.sleeves = SleevesGenerator.generate()
        return generated
