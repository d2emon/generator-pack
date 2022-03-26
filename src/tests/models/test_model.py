import random
import unittest
from models.model import Model


class NewModel(Model):
    value1 = Model.field_property('value1')
    value2 = Model.field_property('value2', 'DEFAULT')


class TestModel(unittest.TestCase):
    def setUp(self):
        self.data = {
            "value": random.uniform(0, 100),
            "value1": random.uniform(0, 100),
        }
        self.model = Model(**self.data)

    def test_field_properties(self):
        model = NewModel(**self.data)

        model.value1 = 'NEW VALUE'

        # self.assertIsNone(model.uuid)
        self.assertEqual(model.value1, model.data.get('value1'))
        self.assertEqual(model.value1, 'NEW VALUE')
        self.assertEqual(model.value2, 'DEFAULT')

        del model.value1

        self.assertIsNone(model.value1)

    def test_field_names(self):
        class FieldNamesModel(Model):
            @property
            def field_names(self):
                yield "field1"

        model = FieldNamesModel(
            field1="value1",
            field2="value2",
        )

        self.assertIn('field1', model.data)
        self.assertNotIn('field2', model.data)

    def test_fill(self):
        model = Model(value="old value")
        model.fill(value="new value")
        self.assertEqual(model.value, "new value")

    def test_data(self):
        model = Model(**self.data)

        self.assertEqual(model.data, self.data)
        self.assertEqual(model.value, self.data['value'])
        self.assertEqual(model['value1'], self.data['value1'])

        model['value1'] = "new value"

        self.assertEqual(model['value1'], "new value")


    def test_str(self):
        text = str(self.model.value)

        self.assertEqual(str(self.model), text)
        self.assertEqual(repr(self.model), f"<Model: \"{text}\">")
        self.assertEqual(len(self.model), len(text))


if __name__ == "__main__":
    unittest.main()
