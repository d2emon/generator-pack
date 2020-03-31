from .. import dices
from .race import Race


class Human(Race):
    additional_trait = 1
    movement = 6
    run = dices.D6
