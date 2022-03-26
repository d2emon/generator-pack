from models.model import Model


def serialize(model, fields) -> dict:
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


def deserialize(model, data) -> Model:
    """
    Deserialize model from dict

    :param data: Dict with model data
    :return: Deserialized model
    """
    return model(**data) if data is not None else None


def deserialize_decorator(method):
    def wrapper(self, *args, **kwargs):
        data = method(self, *args, **kwargs)
        return deserialize(self.model, data)

    return wrapper


def deserialize_all_decorator(method):
    def wrapper(self, *args, **kwargs):
        data = method(self, *args, **kwargs)
        return [deserialize(self.model, item) for item in data]

    return wrapper
