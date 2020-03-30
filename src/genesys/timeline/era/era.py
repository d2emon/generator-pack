from dice.dice import Dice
from factories.random_factory import RandomFactory, DiceFactory
from models.data_manager import DataManager
from models.timeline.event import Event


class Era(DataManager):
    count_dice = Dice(max_value=4)
    years_dice = Dice(max_value=10)
    events_data = []

    def __init__(self):
        super().__init__()
        self.__count = DiceFactory(self.count_dice)
        self.__year = DiceFactory(self.years_dice)
        self.__event_generators = RandomFactory(self.events_data)

    @property
    def count(self):
        return self.__count

    @property
    def year(self):
        return self.__year

    @property
    def event_generators(self):
        return self.__event_generators

    def events(self):
        for _ in range(next(self.count)):
            year = next(self.year)
            event_generator = next(self.event_generators)
            yield Event(year, event_generator())