import unittest
from models.model import Model
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
    


class TestSerializableModel(unittest.TestCase):
    def setUp(self):
        self.model = SerializableModel(field1=Model())

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


if __name__ == "__main__":
    unittest.main()
