from v1.models.fng.names.name import Name


class BansheeName(Name):
    @property
    def value(self):
        return f"The {self.items[1]} {self.items[2]}"
