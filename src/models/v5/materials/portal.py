from models.tree_model import TreeModel as Model


class Portal(Model):
    universe = property(lambda self: self.children[0] if len(self.children) else None)

    def enter(self):
        return self.universe
