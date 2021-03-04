from v1.models.fng.names.name import Name


class AnimalSpeciesName(Name):
    @property
    def value(self):
        return f"{self.items[1]} {self.items[2]}"
