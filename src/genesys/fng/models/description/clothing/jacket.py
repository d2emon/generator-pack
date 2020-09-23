from .clothing_model import ClothingModel
from .material import Material
from .sleeves import Sleeves


class Tie(ClothingModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__description = "tightly tied with string"
        self.position = "at the center"

    def __str__(self):
        return " ".join([
            self.__description,
            self.position
        ])


class Jacket(ClothingModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "jacket"
        self.sleeves = Sleeves()
        self.material = Material("leather")
        self.cover = "just below his waist"
        self.tie = Tie()
        self.neckline = "round neckline"

    def __str__(self):
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
