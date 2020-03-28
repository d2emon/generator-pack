from models.models import Model


class Tie(Model):
    def __init__(self):
        self.description = "tightly tied with string"
        self.position = "at the center"

    def __repr__(self):
        return " ".join([
            self.description,
            self.position
        ])


class Jacket(Model):
    def __init__(self):
        self.name = "jacket"
        self.sleeves = SleevesGenerator.generate()
        self.material = Material("leather")
        self.cover = "just below his waist"
        self.tie = TieGenerator.generate()
        self.neckline = "round neckline"

    def __repr__(self):
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
