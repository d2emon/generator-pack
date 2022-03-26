import unittest
from uuid import uuid4
from models.model import Model
from models.complex_model import ComplexModel as BaseComplexModel
from database.serializer import serialize


class ComplexModel(BaseComplexModel):
    children = {
        "child_model_field": BaseComplexModel(value="value1"),
        "child_value_field": "VALUE",
        "pregenerated_child": "OLD_PREGENERATED",
    }
    static_field_names = [
        "value"
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__child_model = None

    @property
    def child_model_field(self):
        if self.__child_model is None:
            self.__child_model = BaseComplexModel(value="value2")
            self.__child_model.uuid = uuid4()

        return self.__child_model

    @property
    def child_value_field(self):
        return "VALUE"


class TestComplexModel(unittest.TestCase):

    def setUp(self):
        self.model = ComplexModel(pregenerated_child="PREGENERATED")

    def test_complex_model(self):
        self.assertIsInstance(ComplexModel.children, dict)

    def test_fill(self):
        model = ComplexModel(value="old value")

        model.fill(value="new value")
        self.assertEqual(model.value, "new value")

    def test_serialize(self):
        serialized = serialize(self.model, self.model.field_names)

        for field in self.model.children.keys():
            if not hasattr(self.model, field):
                self.assertEqual(serialized[field], self.model[field])
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


if __name__ == "__main__":
    unittest.main()
