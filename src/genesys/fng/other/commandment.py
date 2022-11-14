from data.fixtures.fixtures.other.commandment import commandment
from factories.list_factory import ListFactory
from models.fng.names.name import Name



class ReligiousCommandment(Name):
    provider = ListFactory(commandment)

    def __str__(self):
        return "You shall {}".format(self.value)
