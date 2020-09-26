from providers import ListProvider
from factories.generator import Generated

from genesys.fixtures.fixtures.other import battlecry


class BattleCry(Generated):
    provider = ListProvider(battlecry)

    def __str__(self):
        return "{}!".format(self.value)
