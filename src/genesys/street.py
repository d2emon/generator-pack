from factories import MarkovFactory
from orm.models import Model, MarkovChain
from providers import MarkovProvider
from sample_data.fixtures.streets import streets


class Street(Model):
    def __init__(self, name, **fields):
        super().__init__(**fields)
        self.name = name

    def __repr__(self):
        return "ул. {}".format(self.name)


class StreetChain(MarkovChain):
    def street(self):
        return Street(str(self))


class StreetUnitProvider(MarkovProvider):
    def __init__(self, data=None):
        super().__init__(
            data=data or streets,
            unit_length=3,
        )


class StreetFactory(MarkovFactory):
    def __init__(self, provider=None, max_length=32):
        super().__init__(provider or StreetUnitProvider(), max_length)

    @property
    def model_class(self):
        return StreetChain
