from genesys.model.models import Model


class Shoes(Model):
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
