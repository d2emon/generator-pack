class Model:
    value = property(lambda self: self.data.get('value', ''))

    def __init__(self, *args, **kwargs):
        self.data = kwargs

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"<{self.__class__.__name__}: \"{self}\">"
