from v1.models.fng.names.name import Name


class ApocalypseNickname(Name):
    @property
    def value(self):
        return f"{self.items[1]}"
