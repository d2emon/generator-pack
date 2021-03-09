from v1.models.fng.names.name import Name


class AnimatronicName(Name):
    @property
    def value(self):
        return f"{self.items[0]} {self.items[1]}"
