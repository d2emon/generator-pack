from models.model import Model


class Events(Model):
    events = Model.field_property('events', [])

    def __init__(self, *events, **kwargs):
        super().__init__(
            events=list(events),
            **kwargs,
        )

    @property
    def field_names(self):
        yield 'events'

    def find(self, query=lambda item: True):
        events = filter(query, self.events)
        events = sorted(events, key=lambda event: event.minutes)
        return Events(*events)
