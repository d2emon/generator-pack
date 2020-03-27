from factories.generator import Generated, ListGenerator
from .material import MaterialGenerator


class Shoes(Generated):
    def __init__(self):
        self.name = "shoes"
        self.material = MaterialGenerator.generate()
        self.design = ""

    def __repr__(self):
        return "%s %s" % (
            self.material.description,
            self.name,
        )

    @property
    def description(self):
        return "The %s are made from a %s %s, but are otherwise %s." % (
            self.name,
            self.material.rarity,
            self.material.name,
            self.design,
        )


class ShoesGenerator(ListGenerator):
    generated_class = Shoes
    shoetypes = [
        "boots",
        "shoes",
    ]
    designs = [
        "quite simple",
        "a simple design",
        "an ordinary design",
        "a common design",
        "a common type",
        "not that special",
        "a design found commonly",
        "not any different from others",
    ]

    @classmethod
    def fill_generated(cls, generated):
        generated.material = MaterialGenerator.generate()
        generated.name = cls.generate_value(cls.shoetypes)
        generated.design = cls.generate_value(cls.designs)
        return generated
