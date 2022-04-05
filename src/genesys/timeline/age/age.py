from dice.dice import Dice
from ..models import Event
from v3.factories import Factory, DiceFactory, ListFactory


class Age(Factory):
    count_dice = Dice(max_value=4)
    years_dice = Dice(max_value=10)
    events_data = []

    def __init__(self):
        super().__init__()
        self.__count_factory = DiceFactory(self.count_dice)
        self.__year_factory = DiceFactory(self.years_dice)
        self.__event_factories = ListFactory([{"value": value} for value in self.events_data])

    def get_count(self):
        return self.__count_factory()

    def get_year(self):
        return self.__year_factory()

    def get_event_factory(self):
        item = self.__event_factories()
        if not item:
            return None
        return item.get('value')

    def generate(self):
        event_factory = self.get_event_factory()
        if not event_factory:
            return {}
        return {
            "year": self.get_year(),
            "title": event_factory(),
        }

    def __call__(self, *args, count=None, **kwargs):
        count = self.get_count() if count is None else count
        for _ in range(count):
            data = self.generate()
            yield Event(**data)
