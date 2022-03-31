class WithEvents:
    def __init__(self, *events):
        self.__events = list(events)

    def add_event(self, event):
        self.__events.append(event)

    @classmethod
    def sort_events(cls, events):
        return sorted(events, key=lambda event: event.minutes)

    @classmethod
    def filter_events(cls, events, event_filter=lambda item: True):
        return cls.sort_events(filter(event_filter, events))

    def filtered_events(self, event_filter=lambda item: True):
        return self.filter_events(self.__events, event_filter)
