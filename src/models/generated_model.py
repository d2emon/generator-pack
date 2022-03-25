from .model import Model


class GeneratedModel(Model):
    """
    Generate model
    """

    def __init__(self, *args, generated=True, factory=None, **fields):
        super().__init__(**fields)

        self.generated = generated
        self.factory = factory

    @property
    def data(self):
        if not self.generated:
            self.__generate()
        return super().data

    def __generate(self):
        if self.factory is None:
            return

        self.fill(**self.factory(self))

        self.generated = True
