from dice.dice import Dice
from models.model import Model


class Fraction:
    def __init__(
        self,
        surprised=False,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.surprised = surprised

    def check_surprise(self):
        self.surprised = next(Dice().roll()) < 2
        return self.surprised
