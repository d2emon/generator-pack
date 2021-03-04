from v1.models.fng.names.name import Name


class ArtificialIntelligenceName(Name):
    @property
    def value(self):
        return f"{self.items[1]}"
