from dice.dice import Dice
from generated.encounter.day import Day
from .data import DEFAULT_EVENT_DATA_PROVIDER
from .event import DailyEventFactory, NightlyEventFactory


class EncounterFactory:
    def __init__(
        self,
        roll_on_double=True,
        provider=DEFAULT_EVENT_DATA_PROVIDER,
    ):
        self.roll_on_double = roll_on_double

        self.daily_event_factory = DailyEventFactory(provider=provider)
        self.nightly_event_factory = NightlyEventFactory(provider=provider)

    def __add_event(self):
        dice1, dice2 = Dice(count=2).roll()

        yield self.nightly_event_factory() if dice1 % 2 else self.daily_event_factory()

        if self.roll_on_double and (dice1 == dice2):
            yield from self.__add_event()

    def __events(self):
        yield self.daily_event_factory()
        yield self.nightly_event_factory()
        yield from self.__add_event()

    def __call__(self, day_id, *args, **kwargs):
        return Day(day_id, *self.__events())
