import random
import unittest
from v3.models.model import Model


class TestModel(unittest.TestCase):
    def setUp(self):
        self.data = {
            "value": random.uniform(0, 100),
            "value1": random.uniform(0, 100),
        }
        self.model = Model(**self.data)

    def test_uuid(self):
        self.assertIsNone(self.model.uuid)

    def test_data(self):
        self.assertEqual(self.model.data, self.data)
        self.assertEqual(self.model.items, self.data)

    def test_raw_value(self):
        self.assertEqual(self.model.raw_value, self.data['value'])

    def test_value(self):
        self.assertEqual(self.model.value, self.data['value'])

    def test_fill(self):
        model = Model(value="old value")

        model.fill(value="new value")
        self.assertEqual(model.value, "new value")

    def test_model_item(self):
        model = Model(value1="old value")

        self.assertEqual(model['value1'], "old value")

        model['value1'] = "new value"

        self.assertEqual(model['value1'], "new value")

    def test_str(self):
        text = str(self.model.value)

        self.assertEqual(str(self.model), text)
        self.assertEqual(repr(self.model), f"<Model: \"{text}\">")
        self.assertEqual(len(self.model), len(text))


if __name__ == "__main__":
    unittest.main()
