import random
import unittest
from models.preparable_model import PreparableModel


class TestPreparableModel(unittest.TestCase):
    def setUp(self):
        self.data = {
            "value": random.uniform(0, 100),
            "value1": random.uniform(0, 100),
        }

    def test_prepare(self):
        value = random.uniform(0, 100)

        self.assertEqual(PreparableModel.prepare(value), str(value))

    def test_check_swear(self):
        value = "NAME"

        self.assertEqual(PreparableModel.check_swear(value), value)

    def test_str(self):
        value = random.uniform(0, 100)
        model = PreparableModel(value=value)
        text = PreparableModel.prepare(value)

        self.assertEqual(str(model), text)
        self.assertEqual(repr(model), f"<PreparableModel: \"{text}\">")
        self.assertEqual(len(model), len(text))


if __name__ == "__main__":
    unittest.main()
