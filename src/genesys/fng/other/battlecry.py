from data.fixtures.fixtures.other.battlecry import battlecry
from factories.list_factory import ListFactory
from models.fng.names.name import Name



class BattleCry(Name):
    provider = ListFactory(battlecry)

    def __str__(self):
        return "{}!".format(self.value)
