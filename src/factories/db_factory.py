from models.serializable_model import ModelSerializer


class DbFactory:
    def __init__(self, model, database):
        self.model = model
        self.database = database

    def get_data(self, **kwargs):
        data = {}
        data.update(kwargs)
        return data

    def save(self, model):
        """
        Save serialized model to database
        """
        self.database.update(model.serialize())
        self.database.save()

    # Get data
    @ModelSerializer.deserialize_all_decorator
    def all(self, query=lambda item: True):
        """
        Get all models from db

        :param query: Db query
        :return: Deserialized model
        """
        return self.database.find(query)

    @ModelSerializer.deserialize_decorator
    def first(self, query=lambda item: True):
        """
        Get first model from db

        :param query: Db query
        :return: Deserialized model
        """
        return self.database.first(query)

    @ModelSerializer.deserialize_decorator
    def get(self, item_id):
        """
        Get model by item id

        :param item_id: Model uuid
        :return: Deserialized model
        """
        return self.database.get(item_id)

    @ModelSerializer.deserialize_decorator
    def random(self):
        """
        Get random model from db

        :return: Model
        """
        return self.database.random()

    def __call__(self, *args, **kwargs):
        data = self.get_data(**kwargs)
        return self.model(*args, **data)
