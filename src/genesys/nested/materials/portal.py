from factories.thing.nested_factory import NestedFactory
from models.v5 import materials


class PortalFactory(NestedFactory):
    model = materials.Portal

    def children(self):
        from ..universe import UniverseFactory

        yield UniverseFactory.one()
