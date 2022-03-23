from .model import Model


class SerializableModel(Model):
    field_names = []

    @property
    def serialize_fields(self):
        return self.field_names

    def serialize(self):
        """
        Serialize model fields

        :return: Dict with model data
        """
        result = {}
        for field in self.serialize_fields:
            value = self.__getattribute__(field)
            result[field] = value if not isinstance(value, self.__class__) else value.uuid
        return result

    @classmethod
    def deserialize(cls, data=None):
        """
        Deserialize model from dict

        :param data: Dict with model data
        :return: Deserialized model
        """
        return cls(**data) if data is not None else None
