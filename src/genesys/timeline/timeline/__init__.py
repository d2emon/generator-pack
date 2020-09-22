class TimelineModel:
    def __init__(self, events):
        self.__events = list(events)

    @property
    def events(self):
        return sorted(self.__events, key=lambda e: e.year, reverse=True)

    @events.setter
    def events(self, value):
        self.events = value
