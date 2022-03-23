import random
import unittest
from v3.models.generated_model import GeneratedModel


class TestGeneratedModel(unittest.TestCase):
    def setUp(self):
        self.data = {
            "value": random.uniform(0, 100),
            "value1": random.uniform(0, 100),
        }
        self.factory = lambda model: self.data

    def test_model(self):
        model = GeneratedModel(generated=True, factory=self.factory)

        self.assertTrue(model.generated)
        self.assertEqual(model.factory, self.factory)

    def test_data_no_factory(self):
        kwargs = {
            "no_factory": random.uniform(0, 100),
        }

        model = GeneratedModel(generated=False, **kwargs)

        self.assertEqual(model.data, kwargs)
        self.assertFalse(model.generated)

    def test_data_generated(self):
        kwargs = {
            "no_factory": random.uniform(0, 100),
        }

        model = GeneratedModel(factory=self.factory, **kwargs)

        self.assertTrue(model.generated)
        self.assertNotEqual(model.data, self.data)
        self.assertEqual(model.data, kwargs)
        self.assertTrue(model.generated)

    def test_data_not_generated(self):
        model = GeneratedModel(factory=self.factory, generated=False)

        self.assertFalse(model.generated)
        self.assertEqual(model.data, self.data)
        self.assertTrue(model.generated)

    def test_items(self):
        model = GeneratedModel(**self.data)

        self.assertEqual(model.items, self.data)

    def test_raw_value(self):
        model = GeneratedModel(**self.data)

        self.assertEqual(model.raw_value, self.data['value'])

    def test_value(self):
        model = GeneratedModel(**self.data)

        self.assertEqual(model.value, self.data['value'])

    def test_fill(self):
        model = GeneratedModel(value="old value")

        model.fill(value="new value")
        self.assertEqual(model.value, "new value")

    def test_model_item(self):
        model = GeneratedModel(value1="old value")

        self.assertEqual(model['value1'], "old value")

        model['value1'] = "new value"

        self.assertEqual(model['value1'], "new value")


if __name__ == "__main__":
    unittest.main()
