class Distance:
    def __init__(
        self,
        description=None,
        distance_dice=None,
        multiplier=30,
        can_run=True,
        is_daily=False,
        is_nightly=False,
    ):
        self.description = description
        self.distance_dice = distance_dice
        self.multiplier = multiplier
        self.can_run = can_run
        self.is_daily = is_daily
        self.is_nightly = is_nightly

    def generate(self):
        if self.distance_dice is None:
            return 0
        return next(self.distance_dice.roll()) * self.multiplier
