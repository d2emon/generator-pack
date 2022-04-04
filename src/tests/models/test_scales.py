import random
import unittest
from models.scales import ScalableSize, Distance, Sized


class TestSizedModel(unittest.TestCase):
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

        self.assertEqual(str(model), "5.00*10^-6m")

    def test_sized_model(self):
        model = Sized(
            name='NAME',
            width=ScalableSize(5, 3),
            length=ScalableSize(10, 3),
            height=ScalableSize(15, 3),
        )
        self.assertEqual(str(model), "NAME (5.00*10^3m x 10.00*10^3m x 1.50*10^4m)")

    def test_distance_model(self):
        model = Distance(
            name='SCALABLE',
            distance=ScalableSize(5, 3),
        )

        self.assertEqual(str(model), "Расстояние SCALABLE - 5.00*10^3m")


if __name__ == "__main__":
    unittest.main()
