from dice.dice import Dice
from factories import ListFactory, DiceFactory
from generated.history import Event
from providers.data_manager import DataManager


class Era(DataManager):
    count_dice = Dice(max_value=4)
    years_dice = Dice(max_value=10)
    events_data = []

    def __init__(self):
        super().__init__()
        self.__count_factory = DiceFactory(self.count_dice)
        self.__year_factory = DiceFactory(self.years_dice)
        self.__event_factories = ListFactory(self.events_data)

    @property
    def count(self):
        return self.__count_factory

    @property
    def year(self):
        return self.__year_factory

    @property
    def event_factories(self):
        return self.__event_factories

    def events(self):
        for _ in range(next(self.count)):
            year = next(self.year)
            event_factory = next(self.event_factories)
            yield Event(year, event_factory())
