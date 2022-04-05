from factories.generator import Generated
from factories.list_factory import ListFactory

from genesys.fixtures.fixtures.other.commandment import commandment


class ReligiousCommandment(Generated):
    provider = ListFactory(commandment)

    def __str__(self):
        return "You shall {}".format(self.value)
