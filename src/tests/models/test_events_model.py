import random
import unittest
from models.history.time import Time
from models.history.with_events import WithEvents
from models.encounters.distance import Distance
from models.encounters.event import Event, DailyEvent, NightlyEvent


class TestEventsModel(unittest.TestCase):
    def setUp(self):
        self.time = Time(minutes=random.randrange(0, 100))
        self.times = [Time(minutes=random.randrange(0, 100)) for _ in range(10)]
        self.values = [Event(time) for time in self.times]

    def test_event_model(self):
        encounter = random.uniform(0, 100)
        model = Event(self.time, encounter)
        self.assertIsNone(model.time_of_day)
        self.assertEqual(model.time, self.time)
        self.assertEqual(model.encounter, encounter)
        self.assertEqual(model.minutes, self.time.minutes)
        self.assertEqual(model.distance, self.time.distance)
 
        model.distance = None
        self.assertEqual(model.distance, self.time.distance)
 
        model.distance = 1000
        self.assertEqual(model.minutes, 6000)

    def test_daily_event_model(self):
        encounter = random.uniform(0, 100)
        encounter_type = random.uniform(0, 100)
        max_time = random.randrange(self.time.minutes + 1, 100)
        text = '\n'.join([
            f"Столкновение в пути ({self.time} / {Distance.km(self.time.distance)} км)",
            str(encounter),
        ])
        model = DailyEvent(self.time, encounter, encounter_type, max_time)

        self.assertEqual(model.time_of_day, Time.DAY)
        self.assertEqual(str(model), text)

    def test_nightly_event_model(self):
        encounter = random.uniform(0, 100)
        encounter_type = random.uniform(0, 100)
        max_time = random.randrange(self.time.minutes + 1, 100)
        text = '\n'.join([
            f"Столкновение во время отдыха ({self.time})",
            str(encounter),
        ])
        model = NightlyEvent(self.time, encounter, encounter_type, max_time)

        self.assertEqual(model.time_of_day, Time.NIGHT)
        self.assertEqual(str(model), text)

    def test_events_model(self):
        model = WithEvents(*self.values)
        events_before = list(model.filtered_events())
        for event in events_before:
            self.assertIn(event, self.values)

        new_item = Event(self.time)
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
