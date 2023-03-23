import random


class Deck:
    def __init__(self, cards):
        self.cards = []
        for card in cards:
            self.add_card(card)

    def add_card(self, card):
        self.cards += [card] * card.weight

    def shuffle(self):
        random.shuffle(self.cards)
        return self
