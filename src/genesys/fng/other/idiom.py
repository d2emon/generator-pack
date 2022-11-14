from factories.list_factory import ListFactory
from models.fng.names.name import Name

from data.fixtures.fixtures.other.idiom import idiom


class Idiom(Name):
    provider = ListFactory(idiom)
