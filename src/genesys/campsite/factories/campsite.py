import random
from factories.model import ModelFactory
from ..models import Campsite


class BaseCampsiteFactory(ModelFactory):
    def __init__(self, data=()):
        super().__init__()
        self.__data = data

    @property
    def data(self):
        return self.__data

    @property
    def model_class(self):
        return Campsite

    def description_factory(self):
        """
        Select random description from descriptions

        :return:
        """
        return random.choice(self.data)

    @classmethod
    def resource_factory(cls):
        """
        Next roll twice (once for each column) on Table 2 (When was the camp last
        used and what resources are available?)

        :return:
        """
        return []

    @classmethod
    def encounter_factory(cls):
        """
        Finally roll for occurrences as often as you'd like. Table 3 is split into 3a, 3b,
        3c, and 3d. Roll a d12 to pick the column to use (this spans the 4 sub-tables),
        then roll again to pick the row.

        :return:
        """
        return []

    def __call__(self, *args, **kwargs):
        return self.model_class(
            description=self.description_factory(),
            resources=self.resource_factory(),
            encounters=self.encounter_factory(),
        )
