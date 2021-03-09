from v1.models.fng.model import TextModel


class Race(TextModel):
    def __init__(self, value):
        super().__init__(value)
        self.factories = None
