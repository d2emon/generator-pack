import random
import unittest
from dice.dice import Dice
from genesys.storm.encounter.factories.distance import DistanceFactory
from models.encounters.distance import Distance


class DistanceGroup:
    def __init__(self) -> None:
        self.description = 'DESCRIPTION'
        self.dice = Dice(1, 6)


class TestWorldFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [random.uniform(0, 100) for _ in range(10)]
        self.distance_group = DistanceGroup()

    def test_no_distance(self):
        factory = DistanceFactory()
        model = factory()
        self.assertIsNone(model)

    def test_distance(self):
        factory = DistanceFactory(
            distance_group=self.distance_group,
        )
        model = factory()
        self.assertIsInstance(model, Distance)


if __name__ == "__main__":
    unittest.main()
