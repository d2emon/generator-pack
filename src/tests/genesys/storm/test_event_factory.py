import random
import unittest
from genesys.storm.encounter.factories.event import EventFactory, DailyEventFactory, NightlyEventFactory
from genesys.storm.encounter.factories.distance import DistanceFactory
from models.encounters.distance import Distance
from models.encounters.encounter import Encounter
from models.encounters.events.event import Event, DailyEvent, NightlyEvent
from models.history.time import Time


class TestEventFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [random.uniform(0, 100) for _ in range(10)]

    def test_event_factory_class(self):
        factory = EventFactory()
        factory.time = lambda: "TIME"

        encounter_type = factory.encounter_type_factory()
        self.assertTrue(issubclass(encounter_type, Encounter))

        distance_factory = factory.distance_factory()
        self.assertIsInstance(distance_factory, DistanceFactory)

        distance = distance_factory()
        self.assertIsInstance(distance, Distance)

        model = factory()
        self.assertIsInstance(model, Event)

    def test_event_factory_encounter(self):
        factory = EventFactory()

        encounter = factory.encounter()
        self.assertIsInstance(encounter, Encounter)
        self.assertIsInstance(encounter.distance, Distance)
        self.assertIsInstance(encounter.is_surprised, bool)
        self.assertIsInstance(encounter.is_surprising, bool)

    def test_daily_event_factory_class(self):
        factory = DailyEventFactory()
        model = factory()
        self.assertIsInstance(model, DailyEvent)

        # self.assertEqual(factory.available_encounters, encounter_by_time(Time.DAY))
        # self.assertEqual(factory.available_distances, distances_by_time(Time.DAY))

        for _ in range(10):        
            distance = factory.distance()
            self.assertGreaterEqual(distance, 1)
            self.assertLessEqual(distance, 20)

        for _ in range(10):        
            time = factory.time()
            self.assertGreaterEqual(time.minutes, 2 * 1 * 15)
            self.assertLessEqual(time.minutes, 2 * 20 * 15)

    def test_nightly_event_factory_class(self):
        factory = NightlyEventFactory()
        model = factory()
        self.assertIsInstance(model, NightlyEvent)

        # self.assertEqual(factory.available_encounters, encounter_by_time(Time.NIGHT))
        # self.assertEqual(factory.available_distances, distances_by_time(Time.NIGHT))

        for _ in range(10):        
            time = factory.time()
            self.assertGreaterEqual(time.hours, 1 - 1)
            self.assertLessEqual(time.hours, 6 - 1)


if __name__ == "__main__":
    unittest.main()
