import random
import unittest
from genesys.scales import compared, in_scale, metric


class TestScalesFactory(unittest.TestCase):
    def test_in_scale(self):
        scale = random.randrange(1, 10)
        for item in in_scale(scale):
            self.assertGreaterEqual(item.length.scale, scale - 1)
            self.assertLessEqual(item.length.scale, scale + 2)

        for item in in_scale(-40, 30):
            self.assertGreaterEqual(item.length.scale, -40)
            self.assertLessEqual(item.length.scale, 30)

    def test_metric(self):
        self.assertEqual(metric(-6), 'мкм')
        self.assertEqual(metric(-3), 'мм')
        self.assertEqual(metric(0), 'м')
        self.assertEqual(metric(3), 'км')
        self.assertEqual(metric(6), 'Мм')

    def test_compared(self):
        self.assertEqual(compared(-6), 'Бактерия')
        self.assertEqual(compared(-3), 'Насекомое')
        self.assertEqual(compared(0), 'Человек')
        self.assertEqual(compared(3), 'Город')
        self.assertEqual(compared(6), 'Планета')


if __name__ == "__main__":
    unittest.main()
