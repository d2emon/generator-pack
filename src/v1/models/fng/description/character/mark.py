from v1.models.fng.model import Model, TextModel


class Mark(TextModel):
    def __init__(self, value):
        super().__init__(value)
        self.factories = None


class MarkDescription(Model):
    mark = property(lambda self: self.items.get('mark'))
    start = property(lambda self: self.items.get('start'))
    middle = property(lambda self: self.items.get('middle'))
    finish = property(lambda self: self.items.get('finish'))
    memory = property(lambda self: self.items.get('memory'))
    subject = property(lambda self: self.items.get('subject'))

    @property
    def value(self) -> str:
        return f"{self.mark} {self.start} {self.middle} {self.finish} and leaves {self.memory} of {self.subject}."
