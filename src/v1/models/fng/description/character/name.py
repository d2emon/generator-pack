from v3.models import Model


class Name(Model):
    name = property(lambda self: self.items.get('name'))
    surname = property(lambda self: self.items.get('surname'))

    @property
    def value(self) -> str:
        return f"{self.name} {self.surname}"
