import unittest
from uuid import uuid4
from models.model import Model
from models.complex_model import ComplexModel as BaseComplexModel
from database.serializer import serialize, deserialize


class SerializableModel(Model):
    serialize_field_names = [
        "field1",
        "field2",
    ]

    @property
    def field_names(self):
        yield "field1"
        yield "field2"


class ComplexModel(BaseComplexModel):
    children = {
        "child_model_field": BaseComplexModel(value="value1"),
        "child_value_field": "VALUE",
        "pregenerated_child": "OLD_PREGENERATED",
    }

    static_field_names = [
        "value",
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__child_model = BaseComplexModel(value="value2")
        self.__child_model.uuid = uuid4()

    @property
    def child_model_field(self):
        return self.__child_model

    @property
    def child_value_field(self):
        return "VALUE"


class TestSerialize(unittest.TestCase):
    def setUp(self):
        self.model = SerializableModel(field1=Model())
        self.complex_model = ComplexModel(pregenerated_child="PREGENERATED")

    def test_serialize(self):
        serialized = serialize(self.model, self.model.field_names)

        for field in self.model.field_names:
            value = self.model[field]
            if isinstance(value, Model):
                self.assertEqual(serialized[field], value.uuid)
            else:
                self.assertEqual(serialized[field], value)

    def test_deserialize(self):
        model1 = deserialize(SerializableModel, {
            "key": "value",
        })
        model2 = SerializableModel(key="value")
        self.assertEqual(model1.data, model2.data)

    def test_serialize_complex(self):
        serialized = serialize(self.complex_model, self.complex_model.field_names)

        for field in self.complex_model.children.keys():
            if not hasattr(self.complex_model, field):
                self.assertEqual(serialized[field], self.complex_model[field])
                continue

            value = self.complex_model.__getattribute__(field) if hasattr(self.complex_model, field) else None
            if isinstance(value, Model):
                self.assertEqual(serialized[field], value.uuid)
            else:
                self.assertEqual(serialized[field], value)


if __name__ == "__main__":
    unittest.main()
