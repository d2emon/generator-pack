from v3.factories import ListModelFactory
from ..data.origins import ORIGINS
from ..models.origin import Origin


class OriginFactory(ListModelFactory):
    model = Origin

    def __init__(self, data=None):
        super().__init__(data or ORIGINS)
