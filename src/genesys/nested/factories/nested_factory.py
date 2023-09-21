from factories.thing.nested_factory import NestedFactory as Factory
from .data_provider import PROVIDER


class NestedFactory(Factory):
    default_data = PROVIDER
