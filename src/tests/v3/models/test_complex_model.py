import unittest
from uuid import uuid4
from v3.models.model import Model
from v3.models.complex_model import ComplexModel


class TestModel(ComplexModel):
    children = {
        "child_model_field": ComplexModel(value="value1"),
        "child_value_field": "VALUE",
        "pregenerated_child": "OLD_PREGENERATED",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__child_model = None

    @property
    def child_model_field(self):
        if self.__child_model is None:
            self.__child_model = ComplexModel(value="value2")
            self.__child_model.uuid = uuid4()

        return self.__child_model

    @property
    def child_value_field(self):
        return "VALUE"


class TestComplexModel(unittest.TestCase):
    def setUp(self):
        self.model = TestModel(pregenerated_child="PREGENERATED")

    def test_complex_model(self):
        self.assertIsInstance(TestModel.children, dict)

    def test_serialize_fields(self):
        self.assertIsInstance(self.model.serialize_fields, list)

    def test_fill(self):
        model = TestModel(value="old value")

        model.fill(value="new value")
        self.assertEqual(model.value, "new value")

    def test_serialize(self):
        serialized = self.model.serialize()

        for field in self.model.children.keys():
            if not hasattr(self.model, field):
                self.assertEqual(serialized[field], None)
                continue

            value = self.model.__getattribute__(field) if hasattr(self.model, field) else None
            if isinstance(value, Model):
                self.assertEqual(serialized[field], value.uuid)
            else:
                self.assertEqual(serialized[field], value)

    def test_with_children(self):
        model = self.model.with_children()

        self.assertEqual(model, self.model)

        for k in model.children.keys():
            self.assertIsNotNone(model.data.get(k))

    def test_random(self):
        model = TestModel.random()

        self.assertIsInstance(model, TestModel)

        for k in model.children.keys():
            self.assertIsNotNone(model.data.get(k))


if __name__ == "__main__":
    unittest.main()
