import unittest
from v3.models.complex import ComplexModel


class TestComplexModel(unittest.TestCase):
    def setUp(self):
        self.model = ComplexModel()

    def test_complex_model(self):
        self.assertIsInstance(ComplexModel.field_names, list)
        self.assertIsInstance(ComplexModel.children, dict)

    def test_fill(self):
        model = ComplexModel(value="old value")

        model.fill(value="new value")
        self.assertEqual(model.value, "new value")

    def test_serialize(self):
        serialized = self.model.serialize()

        for field in self.model.field_names:
            value = self.model[field]
            if isinstance(value, ComplexModel):
                self.assertEqual(serialized[field], value.uuid)
            else:
                self.assertEqual(serialized[field], value)

        for field in self.model.children.keys():
            value = self.model[field]
            if isinstance(value, ComplexModel):
                self.assertEqual(serialized[field], value.uuid)
            else:
                self.assertEqual(serialized[field], value)

    def test_deserialize(self):
        model1 = ComplexModel.deserialize({
            "key": "value",
        })
        model2 = ComplexModel(key="value")
        self.assertEqual(model1.data, model2.data)

    def test_with_children(self):
        model = self.model.with_children()

        self.assertEqual(model, self.model)

        for k in model.children.keys():
            self.assertIsNotNone(model.data.get(k))

    def test_random(self):
        model = ComplexModel.random()

        self.assertIsInstance(model, ComplexModel)

        for k in model.children.keys():
            self.assertIsNotNone(model.data.get(k))


if __name__ == "__main__":
    unittest.main()
