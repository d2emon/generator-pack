import random
import unittest
from generated.encounter.day import Day
from models.history.time import Time


class Event:
    def __init__(self, time_of_day) -> None:
        self.time_of_day = time_of_day
        self.minutes = random.uniform(0, 100)


class TestDayModel(unittest.TestCase):
    def setUp(self):
        self.day_id = random.uniform(0, 100)
        self.events = [Event(Time.DAY if random.uniform(0, 100) < 50 else Time.NIGHT) for _ in range(10)]
        self.model = Day(self.day_id, *self.events)

    def test_day_model(self):
        self.assertEqual(self.model.day_id, self.day_id)
        self.assertEqual(str(self.model), str(self.day_id))

        for event in self.model.filtered_events():
            self.assertIn(event, self.events)

        for event in self.model.events:
            self.assertIn(event, self.events)

        for event in self.model.daily:
            self.assertEqual(event.time_of_day, Time.DAY)

        for event in self.model.nightly:
            self.assertEqual(event.time_of_day, Time.NIGHT)


if __name__ == "__main__":
    unittest.main()
