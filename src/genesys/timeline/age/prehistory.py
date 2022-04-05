from dice.dice import Dice
from v3.fixtures import timeline
from .age import Age


class Prehistory(Age):
    """
    Any event that occurred before recorded history. In most cases, this era is described in speculative terms,
    typically describing how the setting came to be peopled and serving as a precursory justification of the setting’s
    ancient period (see below). As a result, prehistory events may or may not have actually happened, but because
    they’re so broadly foundational and there is little evidence (or need) to dispute them, they are offered with the
    weight of scholarly truth or religious faith. Roll 1d4 events, each spaced 1d10x1000 years apart:

    :return:
    """
    count_dice = Dice(max_value=4)
    years_dice = Dice(max_value=10, multiplier=1000)
    events_data = timeline.PREHISTORY_EVENTS
