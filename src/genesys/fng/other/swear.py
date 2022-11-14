from factories.list_factory import ListFactory
from models.fng.names.name import Name
from data.fixtures.fixtures import swears


class Curse(Name):
    provider = ListFactory(swears)
