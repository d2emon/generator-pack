import random
import unittest
from genesys.storm.encounter.factories.encounter import EncounterFactory
from models.encounters.events.event import Event, DailyEvent, NightlyEvent
from models.history.day import Day


class TestEncounterFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.day_id = random.randint(1, 10)
        self.factory = EncounterFactory()

    def test_event_factory(self):
        for event in self.factory.event_factory():
            self.assertIsInstance(event, Event)

    def test_events(self):
        events = list(self.factory.events())
        self.assertGreaterEqual(len(events), 3)
        for event in events:
            self.assertIsInstance(event, Event)

    def test_encounter_factory_roll_on_double(self):
        factory = EncounterFactory(roll_on_double=True)
        day = factory(self.day_id)
        self.assertIsInstance(day, Day)
        self.assertEqual(day.day_id, self.day_id)
        self.assertGreaterEqual(len(day.events), 3)

    def test_encounter_factory_dont_roll_on_double(self):
        factory = EncounterFactory(roll_on_double=False)
        day = factory(self.day_id)
        self.assertIsInstance(day, Day)
        self.assertEqual(day.day_id, self.day_id)
        self.assertEqual(len(day.events), 3)


if __name__ == "__main__":
    unittest.main()
