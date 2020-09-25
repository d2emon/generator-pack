from generated.history.with_events import WithEvents


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
        return self.filtered_events(lambda e: e.is_daily)

    @property
    def nightly(self):
        return self.filtered_events(lambda e: e.is_nightly)

    @property
    def events(self):
        yield from self.daily
        yield from self.nightly

    def __str__(self):
        return self.day_id
