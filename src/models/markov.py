"""Models for Markov chains. """
from typing import Any
from .model import Model


class MarkovUnit(Model):
    """Model for unit of chain.

    Attributes:
        field_names (Collection): Field names.
        prev: (Any): Previous unit value.
        value (Any): Unit value.
    """

    field_names = [
        'prev',
        'value',
    ]

    prev = Model.field_property('prev')
    value = Model.field_property('value')

    def __init__(self, prev, value):
        """Initialize model.

        Args:
            prev (Any): Previous unit value.
            value (Any): Unit value.
        """
        super().__init__(prev=prev, value=value)


class MarkovChain(Model):
    """Model for Markov chain."""

    def __init__(self, units=None):
        """Initialize Markov chain.

        Args:
            units (list, optional): List of MarkovUnit. Defaults to None.
        """
        super().__init__()
        self.values = units or []

    @property
    def last(self) -> MarkovUnit:
        """Get last unit of chain.

        Returns:
            MarkovUnit: Last unit of chain.
        """
        return self.values[-1] if len(self.values) else ''

    @property
    def value(self) -> str:
        """Get chain as str.

        Returns:
            str: Chain as str.
        """
        return ''.join(map(str, self.values)).strip()

    def __len__(self) -> int:
        """Get chain length.

        Returns:
            int: Chain units count.
        """
        return len(self.values)

    def __str__(self) -> str:
        """Get chain as str.

        Returns:
            str: Chain as str.
        """
        return self.value

    def reset(self) -> None:
        """Reset chain units."""
        self.values = []

    def append(self, unit: MarkovUnit) -> None:
        """Add unit to chain.

        Args:
            unit (MarkovUnit): Unit to add.
        """
        self.values.append(unit)
