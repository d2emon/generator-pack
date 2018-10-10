from generator.generator.generated import Generated
from generator.generator.data_provider import ListProvider

from fixtures.other.commandment import commandment


class ReligiousCommandment(Generated):
    provider = ListProvider(commandment)

    def __str__(self):
        return "You shall {}".format(self.value)
