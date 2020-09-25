from dice.dice import Dice as OldDice


class Dice(OldDice):
    def __init__(self, *args, modifier=0, multiplier=1, **kwargs):
        super().__init__(*args, **kwargs)
        self.result_modifier = modifier
        self.result_multiplier = multiplier

    def total(self):
        return (sum(self.roll()) + self.result_modifier) * self.result_multiplier
