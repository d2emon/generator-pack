from .complex_model import ComplexModel


class DbModel(ComplexModel):
    database = None

    def save(self):
        """
        Save serialized model to database
        """
        self.database.update(self.serialize())
        self.database.save()

    # Get data
    @classmethod
    def all(cls, query=lambda item: True):
        """
        Get all models from db

        :param query: Db query
        :return: Deserialized model
        """
        return map(cls.deserialize, cls.database.all(query))

    @classmethod
    def first(cls, query=lambda item: True):
        """
        Get first model from db

        :param query: Db query
        :return: Deserialized model
        """
        return cls.deserialize(cls.database.first(query))

    @classmethod
    def get(cls, item_id):
        """
        Get model by item id

        :param item_id: Model uuid
        :return: Deserialized model
        """
        return cls.deserialize(cls.database.get(item_id))

    @classmethod
    def random(cls):
        """
        Get random model from db

        :return: Model
        """
        return cls.deserialize(cls.database.random())
