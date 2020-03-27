from dice.dice import Dice
from sample_data import timeline
from .era import Era


class Ancient(Era):
    """
    These events occurred during the setting’s distant past, typically describing the rise (and possible fall) of an
    ancestral race or explaining the remnants of a now-extinct culture. Like prehistory, ancient events are offered
    with a fair amount of speculation. However, unlike prehistory, there is more evidence of ancient culture (in the
    form of monuments, burial mounds and tombs, lost scrolls, et al.) to inspire scholarly debate and varied
    interpretation. As a result, there is usually enough doubt surrounding ancient events to prevent taking them at
    face value. Roll 2d6 events, each spaced 1d10x100 years apart:

    :return:
    """
    count_dice = Dice(2, 6)
    years_dice = Dice(max_value=10, multiplier=100)
    events_data = timeline.ANCIENT_EVENTS
