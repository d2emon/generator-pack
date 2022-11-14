from factories.list_factory import ListFactory
from models.fng.names.name import Name
from data.fixtures.fixtures.other.motivation import motivation


class CharacterGoal(Name):
    provider = ListFactory(motivation)
