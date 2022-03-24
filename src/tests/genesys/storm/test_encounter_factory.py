import random
import unittest
from dice.dice import Dice
from generated.encounter.day import Day
from genesys.storm.encounter.factories.distance import DistanceFactory
from genesys.storm.encounter.factories.encounter import EncounterFactory
from genesys.storm.encounter.factories.event import DailyEventFactory, NightlyEventFactory
from models.encounters.distance import Distance


"""
    def __add_event(self):
        dice1, dice2 = Dice(count=2).roll()

        yield self.nightly() if dice1 % 2 else self.daily()

        if self.roll_on_double and (dice1 == dice2):
            yield from self.__add_event()

    def __events(self):
        yield self.daily()
        yield self.nightly()
        yield from self.__add_event()

    def __call__(self, day_id, *args, **kwargs):
        return Day(day_id, *self.__events())
"""


class DistanceData:
    def __init__(self):
        self.dice = Dice()


class TestEncounterFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [random.uniform(0, 100) for _ in range(10)]

    def test_encounter_factory(self):
        day_id = random.randint(1, 10)

        factory_1 = EncounterFactory(roll_on_double=True)
        self.assertTrue(factory_1.roll_on_double)
        self.assertIsInstance(factory_1.daily, DailyEventFactory)
        self.assertIsInstance(factory_1.nightly, NightlyEventFactory)

        day_1 = factory_1(day_id)
        self.assertIsInstance(day_1, Day)
        self.assertEqual(day_1.day_id, day_id)

        factory_2 = EncounterFactory(roll_on_double=False)
        self.assertFalse(factory_2.roll_on_double)
        self.assertIsInstance(factory_2.daily, DailyEventFactory)
        self.assertIsInstance(factory_2.nightly, NightlyEventFactory)

        day_2 = factory_1(day_id)
        self.assertIsInstance(day_2, Day)
        self.assertEqual(day_2.day_id, day_id)

    def test_distance_factory(self):
        empty_factory = DistanceFactory(None)
        self.assertIsNone(empty_factory())

        data = DistanceData()
        factory = DistanceFactory(data)
        distance = factory()
        self.assertIsInstance(distance, Distance)
        # return Distance(
        #     self.distance,
        #     self.distance.dice.total(),
        # )


if __name__ == "__main__":
    unittest.main()
