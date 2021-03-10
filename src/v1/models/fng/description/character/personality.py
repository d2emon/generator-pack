from v1.models.fng.model import Model


class Personality(Model):
    him_or_her = property(lambda self: self.items.get('him_or_her'))

    @property
    def value(self) -> str:
        return f"There's something {self.items[24]} about {self.him_or_her}, " \
            + f"perhaps it's {self.items[25]} or perhaps it's simply {self.items[26]}. " \
            + f"But nonetheless, people tend to {self.items[27]}, while {self.items[28]}."
