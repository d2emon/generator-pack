from dice.dice import Dice
from models.storm.encounters.distance import Distance


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
