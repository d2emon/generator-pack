"""Deck model class."""
import random
from typing import Any, Collection
from .model import Model


class Deck(Model):
    """Deck model."""

    def __init__(self, cards: Collection):
        """Initialize deck.

        Args:
            cards (Collection): Cards of the deck.
        """
        super().__init__()

        for card in cards:
            self.add_card(card)

    @property
    def cards(self) -> Collection:
        """Get deck cards.

        Returns:
            Collection: Deck cards.
        """
        return self.values

    @cards.setter
    def cards(self, value: Collection) -> None:
        """Set deck cards.

        Args:
            value (Collection): Deck cards.
        """
        self.values = value

    def add_card(self, card: Any) -> None:
        """Add card to deck.

        Args:
            card (Any): Card to add.
        """
        self.cards += [card] * card.weight

    def shuffle(self) -> Model:
        """Shuffle deck.

        Returns:
            Model: Shuffled deck.
        """
        random.shuffle(self.values)
        return self

    def __len__(self) -> int:
        """Get deck size.

        Returns:
            int: Deck size.
        """
        return len(self.cards)
