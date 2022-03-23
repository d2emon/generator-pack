from v3.models.model import Model


class Personality(Model):
    him_or_her = property(lambda self: self.items.get('him_or_her'))

    @property
    def value(self) -> str:
        return f"There's something {self.data[24]} about {self.him_or_her}, " \
            + f"perhaps it's {self.data[25]} or perhaps it's simply {self.data[26]}. " \
            + f"But nonetheless, people tend to {self.data[27]}, while {self.data[28]}."
