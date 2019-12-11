from genesys.generator import Generated
from genesys.generator import ListProvider

from fixtures.other import battlecry


class BattleCry(Generated):
    provider = ListProvider(battlecry)

    def __str__(self):
        return "{}!".format(self.value)
