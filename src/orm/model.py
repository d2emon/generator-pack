class Model:
    database = None
    fields = []
    children = {}

    def __init__(self, **fields):
        self.uuid = None
        for k, v in fields.items():
            self.__setattr__(k, v)

    def __serialize(self):
        """
        Serialize model fields

        :return: Dict with model data
        """
        result = {}
        for field in (self.fields + list(self.children.keys())):
            value = self.__getattribute__(field)
            result[field] = value if not isinstance(value, Model) else value.uuid
        return result

    @classmethod
    def __deserialize(cls, data=None):
        """
        Deserizlize model from dict

        :param data: Dict with model data
        :return: Deserialized model
        """
        return cls(**data) if data is not None else None

    def save(self):
        """
        Save serialized model to database
        """
        self.database.update(self.__serialize())
        self.database.save()

    def fill_children(self):
        """
        Fill model with random children

        :return:
        """
        for k, v in self.children.items():
            if self.__getattribute__(k) is None:
                self.__setattr__(k, v.random())

    # Get data
    @classmethod
    def all(cls, query=lambda item: True):
        """
        Get all models from db

        :param query: Db query
        :return: Deserialized model
        """
        return map(cls.__deserialize, cls.database.all(query))

    @classmethod
    def first(cls, query=lambda item: True):
        """
        Get first model from db

        :param query: Db query
        :return: Deserialized model
        """
        return cls.__deserialize(cls.database.first())

    @classmethod
    def get(cls, item_id):
        """
        Get model by item id

        :param item_id: Model uuid
        :return: Deserialized model
        """
        return cls.__deserialize(cls.database.get(item_id))

    @classmethod
    def random(cls):
        """
        Get random model from db with random children

        :return: Model
        """
        record = cls.__deserialize(cls.database.random())
        if not record:
            return None

        record.fill_children()

        return record
