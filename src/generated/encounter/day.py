from models.history.events import Events
from models.history.time import Time


class Day(Events):
    def __init__(
        self,
        day_id,
        *events,
    ):
        super().__init__(*events)
        self.day_id = day_id

    @property
    def daily(self):
        return self.find(lambda e: e.time_of_day == Time.DAY).events

    @property
    def nightly(self):
        return self.find(lambda e: e.time_of_day == Time.NIGHT).events

    @property
    def events(self):
        yield from self.daily
        yield from self.nightly

    def __str__(self):
        return str(self.day_id)
