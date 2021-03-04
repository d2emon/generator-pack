from v1.models.fng.names.name import Name


class AnimeCharacterName(Name):
    @property
    def value(self):
        return f"{self.items[3]}{self.items[4]} {self.items[1]}{self.items[2]}"
