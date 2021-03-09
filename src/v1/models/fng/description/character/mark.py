from v1.models.fng.model import TextModel


class Mark(TextModel):
    def __init__(self, value):
        super().__init__(value)
        self.factories = None
