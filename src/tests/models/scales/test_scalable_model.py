import random
import unittest
from models.scales.scalable import Scalable, ScalableSize, Distance


class TestScalableModel(unittest.TestCase):
    def setUp(self) -> None:
        self.size = random.uniform(1, 10)
        self.scale = random.randrange(-9, 9)

        return super().setUp()

    def test_negative_scalable_size(self):
        model = ScalableSize(
            size=self.size * -1,
            scale=self.scale,
        )

        self.assertAlmostEqual(model.size, -self.size)
        self.assertEqual(model.scale, self.scale)

    def test_less_scalable_size(self):
        model = ScalableSize(
            size=self.size * 0.001,
            scale=self.scale,
        )

        self.assertAlmostEqual(model.size, self.size)
        self.assertEqual(model.scale, self.scale - 3)

    def test_more_scalable_size(self):
        model = ScalableSize(
            size=self.size * 1000,
            scale=self.scale,
        )

        self.assertAlmostEqual(model.size, self.size)
        self.assertEqual(model.scale, self.scale + 3)

    def test_scalable_size_repr(self):
        model = ScalableSize(
            size=0.005,
            scale=-3,
        )

        self.assertEqual(repr(model), "5.00*10^-6m")

    def test_scalable_model_1d(self):
        model = Scalable(
            name='SCALABLE',
            width=5,
            scale=3,
        )

        self.assertEqual(repr(model), "SCALABLE (5.00*10^3m)")

    def test_scalable_model_2d(self):
        model = Scalable(
            name='SCALABLE',
            width=5,
            length=10,
            scale=3,
        )

        self.assertEqual(repr(model), "SCALABLE (5.00*10^3m x 10.00*10^3m)")

    def test_distance_model(self):
        model = Distance(
            name='SCALABLE',
            size=5,
            scale=3,
        )

        self.assertEqual(repr(model), "Расстояние SCALABLE - 5.00*10^3m")


if __name__ == "__main__":
    unittest.main()
