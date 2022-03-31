import unittest
from models.encounters.fraction import Fraction


class TestFractionModel(unittest.TestCase):
    def test_fraction(self):
        fraction = Fraction()
        check = fraction.check_surprise()
        self.assertEqual(check, fraction.surprised)


if __name__ == "__main__":
    unittest.main()
