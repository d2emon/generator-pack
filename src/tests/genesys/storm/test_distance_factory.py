import unittest
from dice.dice import Dice
from genesys.storm.encounter.distance import DistanceFactory
from models.distance.distance_group import DistanceGroup


class TestWorldFactory(unittest.TestCase):
    def test_no_distance_group(self):
        factory = DistanceFactory()
        model = factory()
        self.assertIsNone(model)

    def test_distance_group(self):
        distance_group = DistanceGroup(
            dice=Dice(1, 6),
        )
        factory = DistanceFactory(
            distance_group=distance_group,
        )
        model = factory()
        self.assertEqual(model.distance_group, distance_group)
        self.assertGreaterEqual(model.distance, 1)
        self.assertLessEqual(model.distance, 6)


if __name__ == "__main__":
    unittest.main()
