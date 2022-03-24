import random
import unittest
from generated.history.time import Time
from generated.history.with_events import WithEvents
from models.encounters.distance import Distance
from models.encounters.event import Event, DailyEvent, NightlyEvent


class TestEventsModel(unittest.TestCase):
    def setUp(self):
        self.times = [Time(minutes=random.uniform(0, 100)) for _ in range(10)]
        self.values = [Event(time) for time in self.times]

    def test_event_model(self):
        time = Time(minutes=random.uniform(0, 100))
        encounter = random.uniform(0, 100)
        model = Event(time, encounter)
        self.assertIsNone(model.time_of_day)
        self.assertEqual(model.time, time)
        self.assertEqual(model.encounter, encounter)
        self.assertEqual(model.minutes, time.minutes)
        self.assertEqual(model.distance, time.distance)
 
        model.distance = None
        self.assertEqual(model.distance, time.distance)
 
        model.distance = 1000
        self.assertEqual(model.minutes, 6000)

    def test_daily_event_model(self):
        time = Time(minutes=random.uniform(0, 100))
        encounter = random.uniform(0, 100)
        encounter_type = random.uniform(0, 100)
        max_time = random.uniform(0, 100)
        text = '\n'.join([
            f"Столкновение в пути ({time} / {Distance.km(time.distance)} км)",
            str(encounter),
        ])
        model = DailyEvent(time, encounter, encounter_type, max_time)

        self.assertEqual(model.time_of_day, Time.DAY)
        self.assertEqual(str(model), text)

    def test_nightly_event_model(self):
        time = Time(minutes=random.uniform(0, 100))
        encounter = random.uniform(0, 100)
        encounter_type = random.uniform(0, 100)
        max_time = random.uniform(0, 100)
        text = '\n'.join([
            f"Столкновение во время отдыха ({time})",
            str(encounter),
        ])
        model = NightlyEvent(time, encounter, encounter_type, max_time)

        self.assertEqual(model.time_of_day, Time.NIGHT)
        self.assertEqual(str(model), text)

    def test_events_model(self):
        model = WithEvents(*self.values)
        events_before = list(model.filtered_events())
        for event in events_before:
            self.assertIn(event, self.values)

        time = Time(minutes=random.uniform(0, 100))
        new_item = Event(time)
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
