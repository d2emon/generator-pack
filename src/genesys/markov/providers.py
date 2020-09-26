from providers import MarkovProvider
from genesys.fixtures.fixtures.streets import streets


class StreetUnitProvider(MarkovProvider):
    def __init__(self, data=None):
        super().__init__(
            data=data or streets,
            unit_length=3,
        )
