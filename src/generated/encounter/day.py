from generated.history.with_events import WithEvents
from generated.history.time import Time


class Day(WithEvents):
    def __init__(
        self,
        day_id,
        *events,
    ):
        super().__init__(*events)
        self.day_id = day_id

    @property
    def daily(self):
        return self.filtered_events(lambda e: e.time_of_day == Time.DAY)

    @property
    def nightly(self):
        return self.filtered_events(lambda e: e.time_of_day == Time.NIGHT)

    @property
    def events(self):
        yield from self.daily
        yield from self.nightly

    def __str__(self):
        return str(self.day_id)
