import unittest
from v3.models.complex_model import ComplexModel


class TestComplexModel(unittest.TestCase):
    def setUp(self):
        self.model = ComplexModel()

    def test_complex_model(self):
        self.assertIsInstance(ComplexModel.children, dict)

    def test_serialize_fields(self):
        self.assertIsInstance(self.model.serialize_fields, list)

    def test_fill(self):
        model = ComplexModel(value="old value")

        model.fill(value="new value")
        self.assertEqual(model.value, "new value")

    def test_serialize(self):
        serialized = self.model.serialize()

        for field in self.model.children.keys():
            value = self.model[field]
            if isinstance(value, ComplexModel):
                self.assertEqual(serialized[field], value.uuid)
            else:
                self.assertEqual(serialized[field], value)

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
