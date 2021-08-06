from v3.models import Model


class Eyes(Model):
    style = property(lambda self: self.items.get('style'))
    color = property(lambda self: self.items.get('color'))
    sockets = property(lambda self: self.items.get('sockets'))
    sight = property(lambda self: self.items.get('sight'))

    @property
    def value(self) -> str:
        return f"{self.style} {self.color} eyes, set {self.sockets} within their sockets"

    def describe(self, target):
        return f"{self}, watch {self.sight} over the {target}."
