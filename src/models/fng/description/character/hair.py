from models.model import Model


class Hair(Model):
    color = property(lambda self: self.items.get('color'))
    hair_type = property(lambda self: self.items.get('hair_type'))
    style = property(lambda self: self.items.get('style'))

    @property
    def value(self) -> str:
        return f"{self.color}, {self.hair_type} {self.style}"
