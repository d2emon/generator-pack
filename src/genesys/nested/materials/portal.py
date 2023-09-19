from factories.thing.nested_factory import NestedFactory as Factory
from models.v5 import materials


class PortalFactory(Factory):
    model = materials.Portal

    def children(self):
        from ..universe import UniverseFactory

        yield from UniverseFactory.one()
