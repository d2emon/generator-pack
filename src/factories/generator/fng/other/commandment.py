from factories.providers import ListProvider
from factories.generator import Generated

from sample_data.fixtures.other import commandment


class ReligiousCommandment(Generated):
    provider = ListProvider(commandment)

    def __str__(self):
        return "You shall {}".format(self.value)
