from dice.dice import Dice
from data import timeline
from .age import Age


class Past(Age):
    """
    These events occurred after the setting’s ancient period but before the last living generation. About two-thirds of
    these events should provide general support for the setting’s background, while the remaining third forms the
    foundation for present-day adventure hooks. Depending on the setting’s age, this period can span a really long
    time; I recommend rolling 4d6 events, each spaced 1d10x10 years apart, but add as many more as you feel are
    necessary to represent sufficiently the era’s duration:

    :return:
    """
    count_dice = Dice(4, 6)
    years_dice = Dice(max_value=10, multiplier=10)
    events_data = timeline.PAST_EVENTS
