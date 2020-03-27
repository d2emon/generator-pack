from factories.generator import Generated, ListGenerator


class Material(Generated):
    def __init__(self, name="leather", description=None):
        self.name = name
        if description is None:
            self.description = self.name
        else:
            self.description = description
        self.rarity = "rare"

    def __repr__(self):
        return self.name


class MaterialGenerator(ListGenerator):
    generated_class = Material
    materials = [
        ("leather", ),
        ("hide", ),
        ("furred", ),
        ("leather", "soft leather"),
        ("leather", "hard leather"),
        ("cloth", "bound cloth"),
    ]
    rarities = [
        "rare",
        "very rare",
        "fairly rare",
        "fairly uncommon",
        "very uncommon",
        "pretty uncommon",
        "pretty rare",
        "pretty unusual",
        "pretty unique",
    ]

    @classmethod
    def fill_generated(cls, generated):
        material = cls.generate_value(cls.materials)
        name = material[0]
        if len(material) > 1:
            description = material[1]
        else:
            description = material[0]
        generated.name = name
        generated.description = description
        generated.rarity = cls.generate_value(cls.rarities)
        return generated
