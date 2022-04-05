from models.name.name import TextModel


class Race(TextModel):
    race_group_id = property(lambda self: self.items.get('race_group_id'))

    def __init__(self, value, **kwargs):
        super().__init__(value, **kwargs)
        self.factories = None
