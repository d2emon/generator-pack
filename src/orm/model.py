import random


class Model:
    database = None
    fields = []
    children = {}

    def __init__(self, **fields):
        self.uuid = None
        for k, v in fields.items():
            self.__setattr__(k, v)

    # Serializing
    def __serialize(self):
        result = {}
        for field in (self.fields + list(self.children.keys())):
            value = self.__getattribute__(field)
            result[field] = value if not isinstance(value, Model) else value.uuid
        return result

    @classmethod
    def __deserialize(cls, data=None):
        return cls(**data) if data is not None else None

    # Save data
    def save(self):
        self.database.update(self.__serialize())
        self.database.save()

    # Get data
    @classmethod
    def __all(cls, query=lambda item: True):
        return filter(query, cls.database.data)

    @classmethod
    def all(cls, query=lambda item: True):
        return map(cls.__deserialize, cls.__all(query))

    @classmethod
    def first(cls, query=lambda item: True):
        return next(cls.all(query), None)

    @classmethod
    def get(cls, item_id):
        return cls.first(lambda item: item.get('uuid') == item_id)

    @classmethod
    def random(cls):
        records = list(cls.all())
        record = random.choice(records) if len(records) > 0 else cls()
        if not record:
            return None

        for k, v in cls.children.items():
            if record.__getattribute__(k) is None:
                record.__setattr__(k, v.random())

        return record
