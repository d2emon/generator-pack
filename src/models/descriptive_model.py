"""Descriptive model classes."""
from .model import Model


class DescriptiveModel(Model):
    """Model with description."""

    def __init__(self, value=None, **kwargs):
        """Initialize descriptive model.

        Args:
            value (str, optional): Model description. Defaults to None.
        """
        super().__init__(**kwargs)

        self.value = value

    @property
    def description(self):
        """Get model description.

        Returns:
            str: Model description.
        """
        return str(self.value)

    @description.setter
    def description(self, value):
        """Set model description.

        Args:
            value (str): Model description.
        """
        self.value = value

    def __str__(self):
        """Get model as string.

        Returns:
            str: Model description.
        """
        return self.description


class ListDescriptiveModel(DescriptiveModel):
    """List descriptive model."""

    @property
    def description(self):
        """Get model description.

        Returns:
            str: Model description.
        """
        return " ".join(self.value)
