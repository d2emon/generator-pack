import random
import unittest
from generated.history.with_events import WithEvents


class Event:
    @property
    def minutes(self):
        return random.uniform(0, 100)


class TestEventsModel(unittest.TestCase):
    def setUp(self):
        self.values = [Event() for _ in range(10)]

    def test_events_model(self):
        model = WithEvents(*self.values)
        events_before = list(model.filtered_events())
        for event in events_before:
            self.assertIn(event, self.values)

        new_item = Event()
        model.add_event(new_item)
        events_after = list(model.filtered_events())
        self.assertIn(new_item, events_after)

    def test_sort_events(self):
        # TODO: sorted(events, key=lambda event: event.minutes)
        for event in WithEvents.sort_events(self.values):
            self.assertIn(event, self.values)

    def test_filter_events(self):
        # TODO: cls.sort_events(filter(event_filter, events))
        for event in WithEvents.filter_events(self.values):
            self.assertIn(event, self.values)

        for event in WithEvents.filter_events(self.values, lambda item: random.uniform(0, 100) < 50):
            self.assertIn(event, self.values)


if __name__ == "__main__":
    unittest.main()
