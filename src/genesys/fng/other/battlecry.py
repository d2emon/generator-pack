from factories.generator import Generated
from factories.list_factory import ListFactory

from data.fixtures.fixtures.other.battlecry import battlecry


class BattleCry(Generated):
    provider = ListFactory(battlecry)

    def __str__(self):
        return "{}!".format(self.value)
