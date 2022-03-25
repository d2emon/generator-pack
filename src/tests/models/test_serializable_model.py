from dataclasses import field
from email import generator
import unittest
from models.model import Model
from models.serializable_model import SerializableModel as BaseSerializableModel


class SerializableModel(BaseSerializableModel):
    serialize_field_names = [
        "field1",
        "field2",
    ]

    @property
    def field_names(self):
        yield "field1"
        yield "field2"
    


class TestSerializableModel(unittest.TestCase):
    def setUp(self):
        self.model = SerializableModel(field1=Model())

    def test_serialize_fields(self):
        self.assertEqual(self.model.serialize_fields, list(self.model.field_names))

    def test_serialize(self):
        serialized = self.model.serialize()

        for field in self.model.field_names:
            value = self.model[field]
            if isinstance(value, Model):
                self.assertEqual(serialized[field], value.uuid)
            else:
                self.assertEqual(serialized[field], value)

    def test_deserialize(self):
        model1 = SerializableModel.deserialize({
            "key": "value",
        })
        model2 = SerializableModel(key="value")
        self.assertEqual(model1.data, model2.data)


if __name__ == "__main__":
    unittest.main()
