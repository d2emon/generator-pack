import unittest
from models.encounters.distance import Distance


class DistanceGroup:
    def __init__(self) -> None:
        self.description = 'DESCRIPTION'


class TestDistanceModel(unittest.TestCase):
    def setUp(self) -> None:
        self.distance_group = DistanceGroup()
        self.distance = 1000
        self.model = Distance(
            distance=self.distance,
            distance_group=self.distance_group,
        )

        return super().setUp()

    def test_distance_translation(self):
        self.assertEqual(Distance.m_to_ft(1000), 3281)
        self.assertEqual(Distance.ft_to_m(1000), 305)
        self.assertEqual(Distance.km_to_miles(1000), 621)
        self.assertEqual(Distance.miles_to_km(1000), 1609)

    def test_distance_model(self):
        self.assertEqual(self.model.distance_group, self.distance_group)
        self.assertEqual(self.model.distance, self.distance)
        self.assertEqual(str(self.model), f"Расстояние:\t305 м\tDESCRIPTION")

    def test_feet(self):
        self.assertEqual(self.model.feet, 1000)

        self.model.feet = 500

        self.assertEqual(self.model.feet, 500)

    def test_meters(self):
        self.assertEqual(self.model.meters, 305)

        self.model.meters = 500

        self.assertEqual(self.model.meters, 500)

    def test_value(self):
        self.assertEqual(self.model.value, 305)

        self.model.value = 500

        self.assertEqual(self.model.value, 500)


if __name__ == "__main__":
    unittest.main()
