"""Slotted model classes."""
from typing import Any, Collection
from models.model import Model


class SlotItem(Model):
    """Model to fill slots.

    Attributes:
        slots (Collection): Item slots.
    """

    slots = ()

    @classmethod
    def by_slot(cls, slot: Any, items: Collection) -> Collection:
        """Filter items by slot.

        Args:
            slot (Any): Slot to filter items.
            items (Collections): Items to filter.

        Returns:
            Collection: Filtered items.
        """
        return (item for item in items if slot in item.slots)


class Slotted(Model):
    """Model with slots to fill."""

    def __init__(self, **fields):
        """Initialize slotted model."""
        super().__init__(**fields)
        self.slots = {}

    def __get_slot(self, slot: Any) -> Model:
        """Get slot contents.

        Args:
            slot (Any): Model slot.

        Returns:
            Model: Slot contents.
        """
        return self.slots.get(slot)

    def __set_slot(self, slot: Any, item: Model) -> None:
        """Put item in slot.

        Args:
            slot (Any): Model slot.
            item (Model): Slot contents.
        """
        self.slots[slot] = item

    def __fill_slots(self, slots: Collection, value: Model) -> None:
        """Fill slots with item.

        Args:
            slots (Collection): Model slots.
            value (Model): Slot contents.
        """
        for slot in slots:
            self.__set_slot(slot, value)

    def in_slot(self, slot: Any) -> Model:
        """Get slot contents.

        Args:
            slot (Any): Model slot.

        Returns:
            Model: Slot contents.
        """
        return self.__get_slot(slot)

    def pop(self, item: Model) -> None:
        """Remove all from item slots.

        Args:
            item (Model): Slot item.
        """
        if item is not None:
            self.__fill_slots(item.slots, None)

    def push(self, item: Model) -> None:
        """Fill item slots.

        Args:
            item (Model): Slot item.
        """
        if item is not None:
            self.__fill_slots(item.slots, item)

    def release(self, *slots) -> None:
        """Clear slots."""
        for slot in slots:
            self.pop(self.__get_slot(slot))
