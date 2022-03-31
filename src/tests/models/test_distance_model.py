import random
import unittest
from generated.encounter.day import Day
from models.history.time import Time
from models.encounters.distance import Distance


class DistanceGroup:
    def __init__(self) -> None:
        self.description = 'DESCRIPTION'


class TestDistanceModel(unittest.TestCase):
    def test_distance_model(self):
        distance_group = DistanceGroup()
        distance = 1000

        model = Distance(distance_group, distance)

        self.assertEqual(model.distance_group, distance_group)
        self.assertEqual(model.distance, distance)
        self.assertEqual(model.meters, 304)
        self.assertEqual(Distance.km(1000), 1609)
        self.assertEqual(str(model), f"Расстояние:\t304 м\tDESCRIPTION")



if __name__ == "__main__":
    unittest.main()
