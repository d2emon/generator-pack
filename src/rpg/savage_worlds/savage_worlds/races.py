from src.rpg.savage_worlds.savage_worlds import dices


class Race:
    pass


class Human(Race):
    additional_trait = 1
    movement = 6
    run = dices.D6
