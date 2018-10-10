from generator.generator.generated import Generated
from generator.generator.data_provider import ListProvider

from fixtures.other.battlecry import battlecry


class BattleCry(Generated):
    provider = ListProvider(battlecry)

    def __str__(self):
        return "{}!".format(self.value)
