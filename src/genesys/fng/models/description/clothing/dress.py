from orm.models.models import Model


class Fabric(Model):
    def __init__(self):
        self.description = "comfortable"
        self.fabric = "buttoned up fabric"

    def __repr__(self):
        return ", ".join([
            self.description,
            self.fabric
        ])


class Dress(Model):
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
