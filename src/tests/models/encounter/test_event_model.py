import random
import unittest
from models.encounters.distance import Distance
from models.history.time import Time
from models.encounters.events.event import Event, DailyEvent, NightlyEvent


class TestEventModel(unittest.TestCase):
    def setUp(self) -> None:
        self.minutes = random.randrange(0, 100)
        self.time = Time(minutes=self.minutes)
        return super().setUp()

    def test_minutes(self):
        event = Event(
            time=self.time,
        )

        self.assertEqual(event.minutes, self.minutes)

        new_minutes = random.randrange(0, 100)
        event.minutes = new_minutes

        self.assertEqual(event.minutes, new_minutes)

    def test_distance(self):
        event = Event(
            time=self.time,
        )

        self.assertEqual(event.distance, self.time.distance)

        new_distance = random.randrange(0, 100)
        event.distance = new_distance

        self.assertEqual(event.distance, new_distance)

    def test_max_time(self):
        max_time = random.randrange(0, 100)

        event = Event(
            time=self.time,
            max_time=max_time,
        )

        self.assertEqual(event.time.max_time, max_time)

    def test_no_time(self):
        event = Event()

        self.assertIsNone(event.minutes)
        self.assertIsNone(event.distance)

        new_minutes = random.randrange(0, 100)
        event.minutes = new_minutes

        self.assertIsNone(event.minutes)

        new_distance = random.randrange(0, 100)
        event.distance = new_distance

        self.assertIsNone(event.distance)

    def test_daily_event(self):
        event_text = '\n'.join([ 
            f"Столкновение в пути ({self.time} / {Distance.miles_to_km(self.time.distance)} км)", 
            'ENCOUNTER', 
        ])

        event = DailyEvent(
            time=self.time,
            encounter='ENCOUNTER',
        )

        self.assertEqual(str(event), event_text)

    def test_nightly_event(self):
        event_text = '\n'.join([ 
            f"Столкновение во время отдыха ({self.time})", 
            'ENCOUNTER', 
        ])

        event = NightlyEvent(
            time=self.time,
            encounter='ENCOUNTER',
        )

        self.assertEqual(str(event), event_text)


if __name__ == "__main__":
    unittest.main()
