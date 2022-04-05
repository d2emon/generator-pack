from v3.models import Model


class Encounter(Model):
    pass


class Item(Model):
    description = property(lambda self: self.data.get('description', ''))

    def __repr__(self):
        return f"<{self.__class__.__name__} \"{self}\": \"{self.description}\">"
