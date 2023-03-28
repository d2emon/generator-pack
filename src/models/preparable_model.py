"""Preparable model class."""
from .model import Model


class PreparableModel(Model):
    """Model with prepare data."""

    @classmethod
    def check_swear(cls, value: str) -> str:
        """Check name for bad words.

        Args:
            value (str): Name to test.

        Returns:
            str: Name without bad words.
        """
        return value

    @classmethod
    def prepare(cls, value: str) -> str:
        """Prepare value for model.

        Args:
            value (str): Unprepared value.

        Returns:
            str: Prepared model.
        """
        return cls.check_swear(str(value))

    @property
    def value(self) -> str:
        """Get model value.

        Returns:
            str: Model value.
        """
        return self.prepare(self['value'] or '')
