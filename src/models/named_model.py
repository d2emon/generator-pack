"""Named model class."""
from .model import Model


class NamedModel(Model):
    """Model with name.

    Attribute:
        default_name (str): Default name for model.
    """

    default_name = None

    def __init__(self, name=None):
        """Initialize model.

        Args:
            name (str, optional): Initial name for model. Defaults to None.
        """
        super().__init__()
        self.__name = name

    @property
    def value(self) -> str:
        """Get model value.

        Returns:
            str: Model value.
        """
        if self.__name is None:
            self.__name = self.default_name or self.__class__.__name__
        
        return self.__name

    @value.setter
    def value(self, value: str):
        """Set model value.

        Args:
            value (str): Model value.
        """
        self.__name = value

    @property
    def name(self) -> str:
        """Get model name.

        Returns:
            str: Model name.
        """
        return self.value

    @name.setter
    def name(self, value: str):
        """Set model name.

        Args:
            value (str): Model name.
        """
        self.value = value
