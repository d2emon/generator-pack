import random
import unittest
from genesys.storm.encounter import EncountersManager
from models.history.day import Day
from models.encounters.events.event import Event, NightlyEvent


class TestEncounterManager(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [random.uniform(0, 100) for _ in range(10)]

    def test_events_for_day(self):
        day = EncountersManager.events_for_day()
        self.assertIsInstance(day, Day)

    def test_encounters(self):
        count = random.randrange(10)

        encounters_manager = EncountersManager()
        result = encounters_manager.encounters(count)

        for day_id, day in enumerate(result):
            self.assertEqual(str(day), f"День {day_id + 1} из {count}")


if __name__ == "__main__":
    unittest.main()
