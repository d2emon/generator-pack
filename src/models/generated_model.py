"""Generated Model class."""
from .model import Model


class GeneratedModel(Model):
    """Model with factory."""

    def __init__(self, *args, generated=True, factory=None, **fields):
        """Initialize generated model.

        Args:
            generated (bool, optional): If model is generated. Defaults to True.
            factory (Factory, optional): Factory to generate model. Defaults to None.
        """
        super().__init__(**fields)

        self.generated = generated
        self.factory = factory

    @property
    def data(self) -> dict:
        """Get model fields.

        Returns:
            dict: Model field.
        """
        if not self.generated:
            self.__generate()
        return super().data

    def __generate(self):
        """Build model with factory."""
        if self.factory is None:
            return

        self.fill(**self.factory(self))

        self.generated = True
