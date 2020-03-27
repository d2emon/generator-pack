from factories.generator import Generated
from factories.generator import ListProvider

from sample_data.fixtures.other import commandment


class ReligiousCommandment(Generated):
    provider = ListProvider(commandment)

    def __str__(self):
        return "You shall {}".format(self.value)
