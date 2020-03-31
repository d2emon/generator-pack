from .collection import Collection


class Equipment(Collection):
    def __init__(self):
        super().__init__([])

    def set_values(self, items):
        self.items = items
