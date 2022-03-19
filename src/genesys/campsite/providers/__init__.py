import random
from data.campsite import UNUSUAL_ROLL, SIMPLE, UNUSUAL


class CampsiteDataProvider:
    unusual_roll = UNUSUAL_ROLL
    simple = SIMPLE
    unusual = UNUSUAL

    @classmethod
    def roll(cls):
        return random.randrange(12)
