from database.helpers.serializer import serialize, deserialize, deserialize_decorator, deserialize_all_decorator


class ModelDatabase:
    def __init__(self, database):
        self.database = database

    def save(self, model, fields):
        """
        Save serialized model to database
        """
        data = serialize(self.model, fields)
        self.database.update(data)
        self.database.save()

    # Get data
    @deserialize_all_decorator
    def all(self, query=lambda item: True):
        """
        Get all models from db

        :param query: Db query
        :return: Deserialized model
        """
        return self.database.all(query)

    @deserialize_decorator
    def first(self, query=lambda item: True):
        """
        Get first model from db

        :param query: Db query
        :return: Deserialized model
        """
        return self.database.first(query)

    @deserialize_decorator
    def get(self, item_id):
        """
        Get model by item id

        :param item_id: Model uuid
        :return: Deserialized model
        """
        return self.database.get(item_id)

    @deserialize_decorator
    def random(self):
        """
        Get random model from db

        :return: Model
        """
        return self.database.random()
