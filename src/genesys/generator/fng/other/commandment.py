from genesys.generator import Generated
from genesys.generator import ListProvider

from fixtures.other import commandment


class ReligiousCommandment(Generated):
    provider = ListProvider(commandment)

    def __str__(self):
        return "You shall {}".format(self.value)
