from orm.models.models import Model


class Material(Model):
    def __init__(self, name="leather", description=None):
        self.name = name
        if description is None:
            self.description = self.name
        else:
            self.description = description
        self.rarity = "rare"

    def __repr__(self):
        return self.name
