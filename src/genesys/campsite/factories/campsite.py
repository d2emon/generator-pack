import random
from factories import ModelFactory
from ..models import Campsite


class BaseCampsiteFactory(ModelFactory):
    @property
    def data(self):
        raise NotImplementedError()

    @property
    def model_class(self):
        return Campsite

    @classmethod
    def build_resources(cls):
        """
        Next roll twice (once for each column) on Table 2 (When was the camp last
        used and what resources are available?)

        :return:
        """
        return []

    @classmethod
    def build_encounters(cls):
        """
        Finally roll for occurrences as often as you'd like. Table 3 is split into 3a, 3b,
        3c, and 3d. Roll a d12 to pick the column to use (this spans the 4 sub-tables),
        then roll again to pick the row.

        :return:
        """
        return []

    def build(self, *args, **kwargs):
        return self.model_class(
            description=random.choice(self.data),
            resources=self.build_resources(),
            encounters=self.build_encounters(),
        )
