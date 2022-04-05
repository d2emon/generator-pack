from dice.dice import Dice
from models.distance.distance_group import DistanceGroup
from models.history.time import Time


DISTANCES = [
    DistanceGroup(
        "Нос к носу (ближний бой возможен с ходу)",
        dice=Dice(1, 6),
        avoidable=False,
        allowed_at=[Time.DAY, Time.NIGHT],
    ),
    DistanceGroup(
        "На расстоянии нескольких шагов (минимальный предел дистанционного боя без штрафов)",
        dice=Dice(1, 6, multiplier=3),
        avoidable=False,
        allowed_at=[Time.DAY, Time.NIGHT],
    ),
    DistanceGroup(
        "Среднее (1d6 х 30 футов, на дистанции прямого выстрела)",
        dice=Dice(1, 6, multiplier=30),
        avoidable=True,
        allowed_at=[Time.DAY, Time.NIGHT],
    ),
    DistanceGroup(
        "Дальнее (2d6+6 х 30 футов, вне прямой видимости)",
        dice=Dice(2, 6, modifier=6, multiplier=30),
        avoidable=True,
        allowed_at=[Time.DAY, Time.NIGHT],
    ),
    DistanceGroup(
        "Сверхдальнее (2d6+12 х 30 футов, вне прямой видимости)",
        dice=Dice(2, 6, modifier=12, multiplier=30),
        avoidable=True,
        allowed_at=[Time.DAY],
    ),
    DistanceGroup(
        "На пределе видимости (10 минут бодрым шагом, вне прямой видимости)",
        dice=Dice(1, 3, multiplier=1200),
        avoidable=True,
        allowed_at=[Time.DAY],
    ),
]


def distances_by_time(time=None):
    if time is None:
        return [*DISTANCES]
    else:
        return [distance for distance in DISTANCES if time in distance.allowed_at]