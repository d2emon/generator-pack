from factories.factory import Factory


class DiceFactory(Factory):
    default_data = None

    def __init__(self, dices=None):
        super().__init__()
        self.data = dices

    def __next__(self):
        return sum(self.data.roll())
