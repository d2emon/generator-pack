from dice.dice import Dice
from generated.encounter.day import Day
from .event import DailyEventFactory, NightlyEventFactory


class EncounterFactory:
    def __init__(
        self,
        roll_on_double=True,
    ):
        self.roll_on_double = roll_on_double
        self.daily = DailyEventFactory()
        self.nightly = NightlyEventFactory()

    def __add_event(self):
        dice1, dice2 = Dice(count=2).roll()

        yield self.nightly() if dice1 % 2 else self.daily()

        if self.roll_on_double and (dice1 == dice2):
            yield from self.__add_event()

    def __events(self):
        yield self.daily()
        yield self.nightly()
        yield from self.__add_event()

    def __call__(self, day_id, *args, **kwargs):
        return Day(day_id, *self.__events())
