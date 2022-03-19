from .clothing_model import ClothingModel


class Fabric(ClothingModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.description = "comfortable"
        self.fabric = "buttoned up fabric"

    def __str__(self):
        return ", ".join([
            self.description,
            self.fabric
        ])


class Dress(ClothingModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
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

    def __str__(self):
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
