from dice.dice import Dice
from models.model import Model


class Fraction(Model):
    surprised = Model.field_property('surprised', False)

    @property
    def field_names(self):
        yield "surprised"

    def check_surprise(self):
        self.surprised = next(Dice().roll()) < 2
        return self.surprised
