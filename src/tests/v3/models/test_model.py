import random
import unittest
from v3.models.model import Model


class TestModel(unittest.TestCase):
    def setUp(self):
        self.data = {
            "value": random.uniform(0, 100),
            "value1": random.uniform(0, 100),
        }
        self.factory = lambda model: self.data

    def test_model(self):
        model = Model(generated=True, factory=self.factory)

        self.assertIsNone(model.uuid)
        self.assertTrue(model.generated)
        self.assertEqual(model.factory, self.factory)

    def test_prepare(self):
        value = random.uniform(0, 100)

        self.assertEqual(Model.prepare(value), str(value))

    def test_check_swear(self):
        value = "NAME"

        self.assertEqual(Model.check_swear(value), value)

    def test_data_no_factory(self):
        kwargs = {
            "no_factory": random.uniform(0, 100),
        }

        model = Model(generated=False, **kwargs)

        self.assertEqual(model.data, kwargs)
        self.assertFalse(model.generated)

    def test_data_generated(self):
        kwargs = {
            "no_factory": random.uniform(0, 100),
        }

        model = Model(factory=self.factory, **kwargs)

        self.assertTrue(model.generated)
        self.assertNotEqual(model.data, self.data)
        self.assertEqual(model.data, kwargs)
        self.assertTrue(model.generated)

    def test_data_not_generated(self):
        model = Model(factory=self.factory, generated=False)

        self.assertFalse(model.generated)
        self.assertEqual(model.data, self.data)
        self.assertTrue(model.generated)

    def test_items(self):
        model = Model(**self.data)

        self.assertEqual(model.items, self.data)

    def test_raw_value(self):
        model = Model(**self.data)

        self.assertEqual(model.raw_value, self.data['value'])

    def test_value(self):
        model = Model(**self.data)

        self.assertEqual(model.value, self.data['value'])

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
        model = Model(factory=self.factory)

        self.assertEqual(str(model), Model.prepare(model.value))
        self.assertEqual(repr(model), f"<Model: \"{model}\">")
        self.assertEqual(len(model), len(Model.prepare(model.value)))


if __name__ == "__main__":
    unittest.main()
