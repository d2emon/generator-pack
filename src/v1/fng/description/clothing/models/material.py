from .clothing_model import ClothingModel


class Material(ClothingModel):
    def __init__(self, name="leather", description=None):
        super().__init__()
        self.name = name
        self.description = description or name
        self.rarity = "rare"

    def __str__(self):
        return self.name
