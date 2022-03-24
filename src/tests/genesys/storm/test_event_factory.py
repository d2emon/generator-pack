import random
import unittest
from data.storm.data.encounter.distance import distances_by_time
from data.storm.data.encounter.encounter_types import encounter_by_time
from models.encounters.event import Event, DailyEvent, NightlyEvent
from generated.history.time import Time
from genesys.storm.encounter.factories.event import EventFactory, DailyEventFactory, NightlyEventFactory
from genesys.storm.encounter.factories.distance import DistanceFactory


class EmptyEventFactory(EventFactory):
    available_encounters = []


class TestEventFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [random.uniform(0, 100) for _ in range(10)]

    def test_event_factory_class(self):
        factory = EventFactory
        self.assertEqual(factory.default_model, Event)
        self.assertEqual(factory.available_encounters, encounter_by_time())
        self.assertEqual(factory.available_distances, distances_by_time())
        self.assertIn(factory.select(self.values), self.values)
        self.assertIn(factory.encounter_type(), factory.available_encounters)
        self.assertRaises(NotImplementedError, factory.time)

        distance_factory = factory.distance_factory()
        # distance = cls.select(cls.available_distances)
        # return distance and DistanceFactory(distance)
        self.assertIsInstance(distance_factory, DistanceFactory)

    def test_event_factory(self):
        factory = EventFactory()
        factory.time = lambda: "TIME"

        model_args = factory.model_args()
        self.assertEqual(model_args.get('time'), "TIME")

        # party = Fraction()
        # party.check_surprise()

        # enemies = Fraction()
        # enemies.check_surprise()

        # encounter_type = cls.encounter_type()
        # if not encounter_type:
        #     return None

        # distance_factory = cls.distance_factory()
        # distance = distance_factory and distance_factory()
        # return encounter_type(
        #     distance=distance,
        #     is_surprising=party.surprised,
        #     is_surprised=enemies.surprised,
        # )

        # self.assertEqual(model_args.get('encounter'), factory.encounter())

        model = factory(value1="VALUE1")
        self.assertIsInstance(model, Event)

    def test_no_event_factory(self):
        factory = EmptyEventFactory
        self.assertIsNone(factory.encounter())

    def test_daily_event_factory_class(self):
        factory = DailyEventFactory
        self.assertEqual(factory.default_model, DailyEvent)

        self.assertEqual(factory.available_encounters, encounter_by_time(Time.DAY))
        self.assertEqual(factory.available_distances, distances_by_time(Time.DAY))

        for _ in range(10):        
            distance = factory.distance()
            self.assertGreaterEqual(distance, 1)
            self.assertLessEqual(distance, 20)

        for _ in range(10):        
            time = factory.time()
            self.assertGreaterEqual(time.minutes, 2 * 1 * 15)
            self.assertLessEqual(time.minutes, 2 * 20 * 15)

    def test_nightly_event_factory_class(self):
        factory = NightlyEventFactory
        self.assertEqual(factory.default_model, NightlyEvent)

        self.assertEqual(factory.available_encounters, encounter_by_time(Time.NIGHT))
        self.assertEqual(factory.available_distances, distances_by_time(Time.NIGHT))

        for _ in range(10):        
            time = factory.time()
            self.assertGreaterEqual(time.hours, 1 - 1)
            self.assertLessEqual(time.hours, 6 - 1)


if __name__ == "__main__":
    unittest.main()
