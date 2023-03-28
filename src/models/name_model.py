"""Base name model."""
from typing import Collection
from .model import Model


class Name(Model):
    """Name model class.

    Attributes:
        glue (str): String to glue name parts.
    """

    glue = ""

    @property
    def value(self) -> str:
        """Get model value.

        Returns:
            str: Model value.
        """
        return self.get_name(self.values)

    @classmethod
    def get_name(cls, items: Collection) -> str:
        """Create name from parts.

        Args:
            items (Collection): Name parts.

        Returns:
            str: Generated name.
        """
        return cls.glue.join(items).title()
