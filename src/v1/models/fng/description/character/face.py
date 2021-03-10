from v1.models.fng.model import Model


class Face(Model):
    shape = property(lambda self: self.items.get('shape'))
    style = property(lambda self: self.items.get('style'))

    @property
    def value(self) -> str:
        return f"{self.shape}, {self.style} face"
