from models.nested_model import NestedModel


class Portal(NestedModel):
    @property
    def universe(self):
        if len(self.children):
            return self.children[0]

        return None

    def enter(self):
        return self.universe
