from .clothing_model import ClothingModel


class Shirt(ClothingModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "shirt"
        self.style = "rough"
        self.sleeves = SleevesGenerator.generate()

    def __str__(self):
        return "%s %s" % (
            self.style,
            self.name,
        )
