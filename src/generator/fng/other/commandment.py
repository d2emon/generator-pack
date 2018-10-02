from generator.generator.generated import ListGenerated
from generator.generator.generator_data import ListData

from fixtures.other.commandment import commandment


class ReligiousCommandment(ListGenerated):
    data = {'value': ListData(commandment)}

    def __str__(self):
        return "You shall {}".format(self.value)
