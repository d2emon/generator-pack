from models.v4.model import Model


class Portal(Model):
    universe = property(lambda self: self.children[0] if len(self.children) else None)

    def enter(self):
        return self.universe
