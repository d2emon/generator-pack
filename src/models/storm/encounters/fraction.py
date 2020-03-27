from dice.dice import Dice


class Fraction:
    def __init__(self):
        self.surprised = False

    def check_surprise(self):
        self.surprised = next(Dice().roll()) < 2
        return self.surprised
