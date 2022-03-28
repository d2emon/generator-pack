from factories.factory import Factory


class StaticProvider(Factory):
    def __init__(self, value=None):
        self.value = value

    def __call__(self):
        return self.value
