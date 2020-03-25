class Day:
    def __init__(self, day_id, events=()):
        self.day_id = day_id
        self.events = list(events)

    @classmethod
    def _sorted_events(cls, events):
        return sorted(events, key=lambda event: event.minutes)

    def _filtered_events(self, event_filter=lambda: True):
        return self._sorted_events(filter(event_filter, self.events))

    def add_event(self, event):
        self.events.append(event)
