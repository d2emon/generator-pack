from dice.dice import Dice


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


DISTANCES = [
    Distance(
        "Нос к носу (ближний бой возможен с ходу)",
        Dice(1, 6),
        1,
        True,
        True,
        True,
    ),
    Distance(
        "На расстоянии нескольких шагов (минимальный предел дистанционного боя без штрафов)",
        Dice(1, 6),
        3,
        True,
        True,
        True,
    ),
    Distance(
        "Среднее (1d6 х 30 футов, на дистанции прямого выстрела)",
        Dice(1, 6),
        30,
        False,
        True,
        True,
    ),
    Distance(
        "Дальнее (2d6+6 х 30 футов, вне прямой видимости)",
        Dice(2, 6, modifier=6),
        30,
        False,
        True,
        True,
    ),
    Distance(
        "Сверхдальнее (2d6+12 х 30 футов, вне прямой видимости)",
        Dice(2, 6, modifier=12),
        30,
        False,
        True,
        False,
    ),
    Distance(
        "На пределе видимости (10 минут бодрым шагом, вне прямой видимости)",
        Dice(1, 3),
        1200,
        False,
        True,
        False,
    ),
]
