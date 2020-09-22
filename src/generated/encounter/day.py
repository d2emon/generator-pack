from genesys.storm.storm import Day as DayModel


class Day(DayModel):
    @property
    def daily(self):
        return self._filtered_events(lambda e: e.is_daily)

    @property
    def nightly(self):
        return self._filtered_events(lambda e: e.is_nightly)

    def get_events(self, show_daily=True, show_nightly=True):
        if show_daily:
            yield from self.daily
        if show_nightly:
            yield from self.nightly

    def show(self, show_daily=True, show_nightly=True):
        dashes = '-' * 80 + '\n'
        encounters = []
        if show_daily:
            encounters += list(self.daily)
        if show_nightly:
            encounters += list(self.nightly)
        events = self.get_events(show_daily=show_daily, show_nightly=show_nightly)
        print(dashes.join(map(str, events)))
