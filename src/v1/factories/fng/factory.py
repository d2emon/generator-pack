from v3.models import Model
from v1.factories.factory import Factory as __Factory


class Factory(__Factory):
    @property
    def model(self):
        return Model