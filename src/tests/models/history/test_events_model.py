import random
import unittest
from models.history.time import Time
from models.history.events import Events
from models.encounters.events.event import Event


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
        for event in self.model.find().events:
            self.assertIn(event, self.values)

    def test_filter_events(self):
        for event in self.model.find(lambda item: random.uniform(0, 100) < 50).events:
            self.assertIn(event, self.values)


if __name__ == "__main__":
    unittest.main()
