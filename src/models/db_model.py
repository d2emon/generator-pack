from .serializable_model import ModelSerializer
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
    @ModelSerializer.deserialize_all_decorator
    def all(self, query=lambda item: True):
        """
        Get all models from db

        :param query: Db query
        :return: Deserialized model
        """
        return self.database.all(query)

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
