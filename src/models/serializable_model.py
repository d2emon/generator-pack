from .model import Model


class ModelSerializer:
    @classmethod
    def serialize(cls, model, fields) -> dict:
        """
        Serialize model fields to dict

        :param data: Dict with model data
        :return: Dict with model data
        """
        result = {}
        for field in fields:
            value = model.__getattribute__(field) if hasattr(model, field) else model[field]
            result[field] = value.uuid if isinstance(value, Model) else value
        return result

    @classmethod
    def deserialize(cls, model, data) -> Model:
        """
        Deserialize model from dict

        :param data: Dict with model data
        :return: Deserialized model
        """
        return model(**data) if data is not None else None

    @classmethod
    def deserialize_decorator(cls, method):
        def wrapper(self, *args, **kwargs):
            data = method(self, *args, **kwargs)
            return cls.deserialize(self.model, data)

        return wrapper

    @classmethod
    def deserialize_all_decorator(cls, method):
        def wrapper(self, *args, **kwargs):
            data = method(self, *args, **kwargs)
            return [cls.deserialize(self.model, item) for item in data]

        return wrapper


class SerializableModel(Model):
    serialize_field_names = []

    @property
    def serialize_fields(self):
        return self.serialize_field_names

    def serialize(self):
        return ModelSerializer.serialize(self, self.serialize_fields)

    @classmethod
    def deserialize(cls, data):
        return ModelSerializer.deserialize(cls, data)
