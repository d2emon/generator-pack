from dice.dice import Dice
from data import timeline
from .age import Age


class Modern(Age):
    """
    These are events that have occurred within the lifespan of the last living generation; only those living under the
    setting’s rocks will not have some memory of these events, either as a participant, a live observer, or as a direct
    relation to same. Because people tend to have relatively short attention spans, and because the effects of these
    events may still be felt, these events have artificial prominence that the stuff of older histories do not. As a
    rule of thumb, each of these events should form the basis for a current adventure hook, either as stand-alone
    instance or as an extension of an event from a previous era. Roll 2d6 events, each spaced 1d10 years apart:

    :return:
    """
    count_dice = Dice(2, 6)
    years_dice = Dice(max_value=10)
    events_data = timeline.MODERN_EVENTS
