from .events import Events
from .time import Time


class Day(Events):
    day_id = Events.field_property('day_id')
    value = Events.field_property('day_id')

    def __init__(
        self,
        day_id=None,
        *events,
    ):
        super().__init__(
            day_id=day_id,
            *events,
        )

    @property
    def field_names(self):
        yield 'day_id'
        yield 'events'

    @property
    def daily(self):
        return self.find(lambda e: e.time_of_day == Time.DAY).events

    @property
    def nightly(self):
        return self.find(lambda e: e.time_of_day == Time.NIGHT).events

    def get_events(self):
        yield from self.daily
        yield from self.nightly

    def __str__(self) -> str:
        return str(self.value)
