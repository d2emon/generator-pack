import random
import unittest
from models.history.time import Time
from models.history.events import Events
from models.events.event import Event


class TestEventsModel(unittest.TestCase):
    def setUp(self):
        self.time = Time(minutes=random.randrange(0, 100))
        self.times = [Time(minutes=random.randrange(0, 100)) for _ in range(10)]
        self.values = [Event(time) for time in self.times]
        self.model = Events(*self.values)

    def test_events_model(self):
        for event in self.model.events:
            self.assertIn(event, self.values)

    def test_sort_events(self):
        last_time = 0
        last_event_class = None
        for event in self.model.find().events:
            if last_event_class is None:
                last_event_class = event.__class__

            if not isinstance(event, last_event_class):
                last_time = 0
                last_event_class = event.__class__

            self.assertIn(event, self.values)
            self.assertGreaterEqual(event.time.minutes, last_time)
            self.assertIsInstance(event, Event)
            last_time = event.time.minutes

    def test_filter_events(self):
        for event in self.model.find(lambda item: random.uniform(0, 100) < 50).events:
            self.assertIn(event, self.values)


if __name__ == "__main__":
    unittest.main()
