from . import dices


class Race:
    pass


class Human(Race):
    additional_trait = 1
    movement = 6
    run = dices.D6
