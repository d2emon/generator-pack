from .clothing_model import ClothingModel


class Shoes(ClothingModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "shoes"
        self.material = MaterialGenerator.generate()
        self.design = ""

    def __str__(self):
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
