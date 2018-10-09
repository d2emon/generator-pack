from generator.generator.generated import ListGenerated
from generator.generator.data_provider import ListProvider

from fixtures.other.battlecry import battlecry


class BattleCry(ListGenerated):
    provider = ListProvider(battlecry)

    def __str__(self):
        return "{}!".format(self.value)
